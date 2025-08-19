## How the Script Works

The script addresses the lack of a shuffle feature for podcasts on Spotify. It works by fetching all episodes of a specified podcast, picking one at random, and then either opening it in your web browser (for free accounts) or playing it directly on a device (for premium accounts). It also includes caching and auto-update features to make subsequent runs faster.

-----

## 🚀 Setup Guide

### 1\. Prerequisites

You need to have **Python 3** installed on your computer. You can check your version by running `python3 --version` in your terminal. If you don't have it, download it from [python.org](https://www.python.org/downloads/).

### 2\. Installation

First, download the script files, then install the required `spotipy` Python library by running this command in your terminal:

```bash
pip3 install spotipy
```

### 3\. Spotify API Credentials

The script needs to access the Spotify API. You'll need to create your own app to get the credentials.

1.  Go to the **Spotify Developer Dashboard** and log in.
2.  Click **"Create App,"** give it a name and description, and agree to the terms.
3.  Once created, you'll see your **Client ID**. Click **"Show client secret"** to see your **Client Secret**.
4.  Click **"Edit Settings"** and add `http://127.0.0.1:9090/callback` to the **"Redirect URIs"** field.
5.  Click **"Add,"** then **"Save."**

### 4\. Set Environment Variables

You should set your API keys as environment variables for security.

#### **On macOS & Linux:**

1.  Open your terminal.
2.  Edit your shell's startup file, like `~/.zshrc` (for macOS) or `~/.bashrc` (for Linux) using a text editor like `nano`. For example: `nano ~/.zshrc`.
3.  Add the following lines to the end of the file, replacing the placeholders with your actual keys:
    ```bash
    export SPOTIPY_CLIENT_ID='Your_Client_ID_Here'
    export SPOTIPY_CLIENT_SECRET='Your_Client_Secret_Here'
    export SPOTIPY_REDIRECT_URI='http://127.0.0.1:9090/callback'
    ```
4.  Save and exit the file. **Close and reopen your terminal** for the changes to take effect.

#### **On Windows:**

1.  Open the **Command Prompt** (not PowerShell).
2.  Run these commands one by one, replacing the placeholders with your keys. Use double quotes.
    ```cmd
    setx SPOTIPY_CLIENT_ID "Your_Client_ID_Here"
    setx SPOTIPY_CLIENT_SECRET "Your_Client_Secret_Here"
    setx SPOTIPY_REDIRECT_URI "http://127.0.0.1:9090/callback"
    ```
3.  After a "SUCCESS" message, **close and reopen the Command Prompt** for the changes to take effect.

-----

## ▶️ How to Use

### 1\. Find the Podcast URI

1.  Open Spotify and go to the podcast you want to shuffle.
2.  Click the **three dots (...)** menu, then go to **Share** \> **Copy Spotify URI**.
3.  The URI will look like `spotify:show:0vSL8N2M5W742y3a2gV0u9`.

### 2\. Update the Script

Open the script you want to use (`QuranPicker.py` or `QuranPicker_Premium.py`) and replace the placeholder in the `PODCAST_URI` variable with the URI you just copied.

```python
# --- Configuration ---
# The URI of the podcast you want to shuffle.
PODCAST_URI = 'spotify:show:YOUR_URI_HERE'
```

### 3\. Run the Script

Navigate to the script's folder in your terminal and run the appropriate file:

  * **For Free users:** `python3 QuranPicker.py`
  * **For Premium users:** `python3 QuranPicker_Premium.py`

The first time you run it, a browser window will open asking you to log in and grant permission. After that, the script will instantly pick a random Surah and either open it in your browser or play it directly.
