# Spotify Podcast Shuffler (Optimized with Caching)
# This script fetches all episodes from a specific podcast, caches them locally,
# picks a random one, and opens it in your web browser to be played.
# Subsequent runs are much faster as it only checks for new episodes.

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import os
import webbrowser
import json # <-- To handle the cache file

# --- Configuration ---
# The URI of the podcast you want to shuffle.
PODCAST_URI = 'spotify:show:2LLRRGmC6yuXZoyyd8JCq2' 
# The file where the episode list will be stored.
CACHE_FILENAME = 'episodes_cache.json'

# --- Step 1: Spotify API Credentials ---
# (This section remains the same)
# It's best practice to set these as environment variables.
# os.environ['SPOTIPY_CLIENT_ID'] = 'YOUR_CLIENT_ID_HERE'
# os.environ['SPOTIPY_CLIENT_SECRET'] = 'YOUR_CLIENT_SECRET_HERE'
# os.environ['SPOTIPY_REDIRECT_URI'] = 'http://127.0.0.1:9090/callback'

def load_episodes_from_cache():
    """Loads the list of episodes from the local JSON cache file."""
    if not os.path.exists(CACHE_FILENAME):
        return [] # Return an empty list if the cache file doesn't exist
    try:
        with open(CACHE_FILENAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        # If the file is corrupted or can't be read, start fresh
        return []

def save_episodes_to_cache(episodes):
    """Saves the list of episodes to the local JSON cache file."""
    try:
        with open(CACHE_FILENAME, 'w', encoding='utf-8') as f:
            json.dump(episodes, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Error: Could not save cache file. {e}")

def main():
    """
    Main function to authenticate, fetch/update episodes, and open a random one.
    """
    print("--- Spotify Podcast Shuffler (Optimized) ---")

    # --- Authentication ---
    scope = "user-read-playback-state"
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        user_info = sp.current_user()
        print(f"Authenticated as: {user_info['display_name']}")
    except Exception as e:
        print(f"\n--- Authentication Error --- \nDetails: {e}")
        return

    # --- Load Episodes from Cache ---
    all_episodes = load_episodes_from_cache()
    if all_episodes:
        print(f"\nLoaded {len(all_episodes)} episodes from local cache.")
        # Create a set of existing episode IDs for quick lookups
        existing_ids = {ep['id'] for ep in all_episodes}
    else:
        print("\nNo local cache found. Performing a full fetch of all episodes.")
        existing_ids = set()

    # --- Check for New Episodes (Smart Update) ---
    print("Checking for new episodes...")
    newly_fetched_episodes = []
    offset = 0
    limit = 50
    found_existing_episode = False

    while not found_existing_episode:
        try:
            results = sp.show_episodes(PODCAST_URI, limit=limit, offset=offset)
            episodes_page = results['items']

            if not episodes_page:
                break # No more episodes on Spotify

            # Check if any episode on this page already exists in our cache
            for ep in episodes_page:
                if ep['id'] in existing_ids:
                    found_existing_episode = True
                    break # Stop checking this page
                else:
                    newly_fetched_episodes.append(ep)

            if found_existing_episode:
                break # Stop fetching more pages

            offset += len(episodes_page)

        except Exception as e:
            print(f"An error occurred while fetching new episodes: {e}")
            break

    # --- Update and Save Cache if Necessary ---
    if newly_fetched_episodes:
        print(f"Found {len(newly_fetched_episodes)} new episodes. Updating cache...")
        # Add the new episodes to the beginning of our master list
        all_episodes = newly_fetched_episodes + all_episodes
        save_episodes_to_cache(all_episodes)
    else:
        print("Your local list is already up-to-date.")


    if not all_episodes:
        print("Could not find any episodes for this podcast.")
        return

    # --- Select a Random Episode ---
    random_episode = random.choice(all_episodes)
    episode_name = random_episode['name']
    episode_url = random_episode['external_urls']['spotify']
    print(f"\nSelected random episode: '{episode_name}'")

    # --- Open Episode in Web Browser ---
    try:
        print(f"Opening in your browser...")
        webbrowser.open(episode_url)
        print("\nDone! Just press play in your browser. Enjoy.")
    except Exception as e:
        print(f"\nCould not open the episode in your browser. Error: {e}")
        print(f"You can open it manually here: {episode_url}")


if __name__ == '__main__':
    main()
