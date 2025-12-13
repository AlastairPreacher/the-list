# The List - Collaborative Spotify Playlist Rating & Commenting

A collaborative playlist curation tool that extends the functionality of SortYourMusic with real-time ratings and comments synced via Firebase.

## Features

✅ **Sort Spotify Playlists** - Sort by BPM, energy, danceability, and more
✅ **5-Star Ratings** - Rate tracks individually, see your friend's ratings and averages
✅ **Comments** - Leave comments on tracks with username attribution
✅ **Real-Time Sync** - All ratings and comments sync via Firebase cloud
✅ **Simple Username System** - No passwords needed, just pick a username
✅ **Collaborative** - Share the app URL with a friend and rate playlists together

## How to Use (Local Testing)

1. **Open the app:**
   - Open `index.html` in your web browser (Chrome, Firefox, Safari, etc.)

2. **Set your username:**
   - On first visit, you'll see a modal asking for your username
   - Enter any username (2-20 characters)
   - Click "Get Started"

3. **Login with Spotify:**
   - Click "Login with Spotify"
   - Authorize the app to access your playlists

4. **Select a playlist:**
   - Choose any of your Spotify playlists

5. **Rate and comment:**
   - Click stars to rate tracks (1-5 stars)
   - Type comments and press Enter or click the 💬 button
   - All data saves automatically to Firebase

6. **Share with a friend:**
   - Your friend opens the same `index.html` file
   - They choose a different username
   - You both see each other's ratings and comments in real-time!

## Project Structure

```
the-list/
├── index.html                 # Main app (modified from SortYourMusic)
├── firebase-init.js           # Firebase configuration and helpers
├── username-manager.js        # Username picker and localStorage
├── ratings-comments.js        # Rating and comment UI/logic
├── the-list-styles.css        # Styles for new features
├── config.js                  # Spotify API configuration
├── styles.css                 # Original SortYourMusic styles
├── lib/                       # JavaScript libraries (jQuery, etc.)
├── dist/                      # Bootstrap CSS
└── images/                    # Image assets
```

## Technical Details

**Frontend:**
- HTML/JavaScript (no build process needed)
- jQuery for DOM manipulation
- DataTables for sortable table
- Bootstrap for styling

**Backend:**
- Firebase Realtime Database (free tier)
- Cloud-synced ratings and comments
- No server required!

**Authentication:**
- Simple localStorage-based username system
- Spotify OAuth for playlist access

## Firebase Data Structure

```json
{
  "playlists": {
    "{spotify-playlist-id}": {
      "tracks": {
        "{spotify-track-id}": {
          "ratings": {
            "username1": 4,
            "username2": 5
          },
          "average": 4.5,
          "comments": [
            {
              "username": "username1",
              "text": "Great track!",
              "timestamp": 1702468800000
            }
          ]
        }
      }
    }
  }
}
```

## Next Steps

### Deploy to GitHub Pages

1. Create a GitHub repository named "the-list"
2. Push this folder to the repository
3. Enable GitHub Pages in repository settings
4. Share the GitHub Pages URL with your friend!

### Configure Firebase Security Rules (Optional but Recommended)

Currently using test mode (anyone can read/write). For production:

1. Go to Firebase Console → Realtime Database → Rules
2. Update rules to restrict access:

```json
{
  "rules": {
    "playlists": {
      "$playlistId": {
        ".read": true,
        ".write": true
      }
    }
  }
}
```

## Credits

- **Original App:** SortYourMusic by [@plamere](http://twitter.com/plamere)
- **Enhancements:** The List - collaborative rating & commenting
- **Powered by:** Spotify API, Firebase

## License

Based on SortYourMusic (check original repository for license)
Enhancements for The List created for personal use

---

**Built:** 13-12-2025
**Firebase Project:** the-list-13e1c
**Status:** Ready for local testing and GitHub Pages deployment
