#!/usr/bin/env python3
"""
Check preview URL coverage for Spotify playlist tracks.
Uses spotipy library to get detailed track information including preview URLs.
"""

import json
import sys
from pathlib import Path

try:
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth
except ImportError:
    print("ERROR: spotipy not installed. Install with: pip3 install spotipy")
    sys.exit(1)

# Playlist ID for "Murder on the Dancefloor"
PLAYLIST_ID = "1LlTlKGKS1lsIR3CMsPk5a"

def get_spotify_client():
    """Initialize Spotify client with OAuth."""
    # Spotify will use SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI from env
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope="playlist-read-private playlist-read-collaborative",
        open_browser=False
    ))

def analyze_playlist(sp, playlist_id):
    """Get all tracks from playlist and analyze preview URL coverage."""

    print(f"Fetching playlist tracks...")
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']

    # Handle pagination
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    total_tracks = len(tracks)
    tracks_with_preview = 0
    tracks_without_preview = 0
    preview_urls = []

    print(f"\nAnalyzing {total_tracks} tracks...\n")

    for i, item in enumerate(tracks, 1):
        if item['track'] is None:
            continue

        track = item['track']
        track_name = track['name']
        artists = ', '.join([artist['name'] for artist in track['artists']])
        preview_url = track.get('preview_url')

        if preview_url:
            tracks_with_preview += 1
            preview_urls.append({
                'track_id': track['id'],
                'name': track_name,
                'artists': artists,
                'preview_url': preview_url
            })
            status = "✓"
        else:
            tracks_without_preview += 1
            status = "✗"

        print(f"{status} [{i:3d}/{total_tracks}] {track_name} - {artists}")

    # Calculate coverage
    coverage_pct = (tracks_with_preview / total_tracks * 100) if total_tracks > 0 else 0

    # Print summary
    print("\n" + "="*70)
    print("PREVIEW URL COVERAGE ANALYSIS")
    print("="*70)
    print(f"Total tracks:              {total_tracks}")
    print(f"Tracks WITH preview URLs:  {tracks_with_preview} ({coverage_pct:.1f}%)")
    print(f"Tracks WITHOUT previews:   {tracks_without_preview}")
    print("="*70)

    if coverage_pct >= 95:
        print("\n✅ COVERAGE SUFFICIENT (≥95%) - Client-side analysis viable")
    else:
        print(f"\n⚠️  COVERAGE INSUFFICIENT ({coverage_pct:.1f}% < 95%) - May need alternative approach")

    # Save detailed results
    output_file = Path(__file__).parent / "preview_coverage_analysis.json"
    output_data = {
        'playlist_id': playlist_id,
        'total_tracks': total_tracks,
        'tracks_with_preview': tracks_with_preview,
        'tracks_without_preview': tracks_without_preview,
        'coverage_percentage': coverage_pct,
        'preview_urls': preview_urls
    }

    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2)

    print(f"\n📄 Detailed results saved to: {output_file}")

    return output_data

if __name__ == "__main__":
    try:
        sp = get_spotify_client()
        results = analyze_playlist(sp, PLAYLIST_ID)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
