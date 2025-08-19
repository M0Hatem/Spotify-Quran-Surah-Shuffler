# **Spotify Quran Surah Shuffler**

A simple Python script to help you listen to a random Surah from your favorite Quran podcast on Spotify. Since Spotify doesn't offer a shuffle feature for podcasts, this tool fetches all episodes (Surahs), picks one at random, and helps you play it.

It's optimized to be fast after the first run by caching the list of Surahs locally and only checking for new ones when you run it.

## **❓ Which Script Should I Use?**

This project includes two scripts. Choose the one that matches your Spotify account type.

* **QuranPicker.py (For Free Users):**  
  * Picks a random Surah and **opens it in your web browser**.  
  * You just need to press play in the new browser tab.  
  * Perfect for users with a **Free Spotify account**.  
* **QuranPicker\_Premium.py (For Premium Users):**  
  * Picks a random Surah and **plays it directly** on one of your active Spotify devices (your computer, phone, etc.).  
  * Requires a **Spotify Premium account** due to API limitations.

## **✨ Features**

* **True Random Shuffle:** Picks a truly random Surah from the entire podcast archive.  
* **Smart Caching:** After the first run, the script saves the episode list locally, making subsequent runs almost instant.  
* **Automatic Updates:** Automatically checks for and adds any newly released Surahs to your local list.  
* **Direct Playback (Premium):** Instantly plays the selected Surah on your active device.

## **🚀 Setup Guide**

Follow these steps to get the script up and running on your machine.

### **1\. Prerequisites**

* **Python 3:** Make sure you have Python 3 installed. You can check by opening your terminal and running python3 \--version. If you don't have it, you can download it from [python.org](https://www.python.org/downloads/).

### **2\. Installation**

First, download the script files to a folder on your computer. Then, install the required Python library, spotipy:

pip3 install spotipy

### **3\. Spotify API Credentials**

This script needs to talk to Spotify's API. You'll need to get your own free API keys.

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in.  
2. Click **"Create App"**.  
3. Give it a name (e.g., "Quran Shuffler") and a description. Check the boxes to agree to the terms.  
4. Once created, you will see your **Client ID**. Click **"Show client secret"** to see your **Client Secret**. Keep these safe\!  
5. Now, click **"Edit Settings"**.  
6. In the **"Redirect URIs"** field, add the following URL exactly as it is:  
   http://127.0.0.1:9090/callback

7. Click the **"Add"** button, then scroll down and **"Save"**.

### **4\. Set Environment Variables**

To use your API keys securely, you should save them as environment variables.

**On macOS & Linux:**

1. Open your terminal.  
2. Edit your shell's startup file. This is usually \~/.zshrc (for macOS) or \~/.bashrc (for many Linux distros).  
   \# For Zsh (default on modern macOS)  
   nano \~/.zshrc

   \# For Bash on Linux  
   nano \~/.bashrc

3. Add the following lines to the end of the file, replacing the placeholder text with your actual keys from the Spotify Dashboard.  
   export SPOTIPY\_CLIENT\_ID='Your\_Client\_ID\_Here'  
   export SPOTIPY\_CLIENT\_SECRET='Your\_Client\_Secret\_Here'  
   export SPOTIPY\_REDIRECT\_URI='http://127.0.0.1:9090/callback'

4. Save the file (Ctrl+O, then Enter) and exit (Ctrl+X).  
5. **Important:** Close and reopen your terminal for the changes to take effect.

**On Windows:**

1. Open the **Command Prompt** (not PowerShell for this command).  
2. Run the following commands one by one, replacing the placeholder text with your actual keys. Use double quotes.  
   setx SPOTIPY\_CLIENT\_ID "Your\_Client\_ID\_Here"  
   setx SPOTIPY\_CLIENT\_SECRET "Your\_Client\_Secret\_Here"  
   setx SPOTIPY\_REDIRECT\_URI "http://127.0.0.1:9090/callback"

3. You will see a "SUCCESS" message after each command.  
4. **Important:** You must close and reopen the Command Prompt window for these changes to take effect.

## **▶️ How to Use**

### **1\. Find the Podcast URI**

You need to tell the script which podcast to shuffle.

1. Open Spotify and go to the podcast you want (e.g., "المصحف المرتل").  
2. Click the **three dots (...)** menu.  
3. Go to **Share** \-\> **Copy Spotify URI**.  
4. It will look something like this: spotify:show:0vSL8N2M5W742y3a2gV0u9.

### **2\. Update the Script**

Open the script file you plan to use (QuranPicker.py or QuranPicker\_Premium.py) and paste your URI into the PODCAST\_URI variable at the top.

\# \--- Configuration \---  
\# The URI of the podcast you want to shuffle.  
PODCAST\_URI \= 'spotify:show:YOUR\_URI\_HERE'

### **3\. Run the Script**

Navigate to the script's folder in your terminal and run the appropriate file:

\# For Free users  
python3 QuranPicker.py

\# For Premium users  
python3 QuranPicker\_Premium.py

* **First time:** A browser window will open asking you to log in to Spotify and grant permission.  
* **Every time:** The script will pick a random Surah and either open it in your browser or play it directly, depending on which script you ran. Enjoy\!