# Spotify Quran Surah Shuffler (Premium Version)
# This script is for Spotify Premium users. It fetches all episodes,
# caches them locally, picks a random one, and plays it directly on an
# active Spotify device.

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import os
import json

# --- Configuration ---
PODCAST_URI = 'spotify:show:2LLRRGmC6yuXZoyyd8JCq2' # إيه المشكلة؟ - محمد الغليظ
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
        return []
    try:
        with open(CACHE_FILENAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
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
    Main function to authenticate, fetch/update episodes, and play a random one.
    """
    print("--- Spotify Quran Shuffler (Premium Version) ---")

    # --- Authentication (with playback scope) ---
    scope = "user-modify-playback-state user-read-playback-state"
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        user_info = sp.current_user()
        print(f"Authenticated as: {user_info['display_name']}")
    except Exception as e:
        print(f"\n--- Authentication Error --- \nDetails: {e}")
        return

    # --- Load/Update Episodes (same as the other script) ---
    all_episodes = load_episodes_from_cache()
    if all_episodes:
        print(f"\nLoaded {len(all_episodes)} episodes from local cache.")
        existing_ids = {ep['id'] for ep in all_episodes}
    else:
        print("\nNo local cache found. Performing a full fetch of all episodes.")
        existing_ids = set()

    print("Checking for new episodes...")
    newly_fetched_episodes = []
    offset = 0
    limit = 50
    found_existing_episode = False

    while not found_existing_episode:
        try:
            results = sp.show_episodes(PODCAST_URI, limit=limit, offset=offset)
            episodes_page = results['items']
            if not episodes_page: break
            for ep in episodes_page:
                if ep['id'] in existing_ids:
                    found_existing_episode = True
                    break
                else:
                    newly_fetched_episodes.append(ep)
            if found_existing_episode: break
            offset += len(episodes_page)
        except Exception as e:
            print(f"An error occurred while fetching new episodes: {e}")
            break

    if newly_fetched_episodes:
        print(f"Found {len(newly_fetched_episodes)} new episodes. Updating cache...")
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
    episode_uri = random_episode['uri']
    print(f"\nSelected random episode: '{episode_name}'")

    # --- Find an Active Device and Play ---
    try:
        devices = sp.devices()
        active_devices = [d for d in devices['devices'] if d['is_active']]

        if not devices['devices']:
             print("\n--- No Spotify Device Found ---")
             print("Please open Spotify on one of your devices (phone, computer, etc.) and try again.")
             return

        # If no device is active, we'll use the first one available.
        target_device = active_devices[0] if active_devices else devices['devices'][0]
        device_id = target_device['id']
        device_name = target_device['name']

        print(f"Playing on device: '{device_name}'")

        # Play the episode
        sp.start_playback(device_id=device_id, uris=[episode_uri])
        print("\nPlayback started! Enjoy.")

    except IndexError:
        print("\n--- No Active Spotify Device Found ---")
        print("Please make sure Spotify is open and active on one of your devices.")
    except Exception as e:
        print(f"\nAn error occurred during playback: {e}")


if __name__ == '__main__':
    main()
