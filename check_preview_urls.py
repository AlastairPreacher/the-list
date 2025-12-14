#!/usr/bin/env python3
"""
Check preview URL coverage for Spotify playlist tracks.
Uses Spotify Web API directly to get full track details including preview URLs.
"""

import json
import subprocess
import sys

def get_spotify_access_token():
    """Get Spotify access token from MCP server's stored credentials."""
    try:
        import spotipy
        from spotipy.oauth2 import SpotifyOAuth
    except ImportError:
        print("Error: spotipy library not installed. Install with: pip3 install spotipy")
        sys.exit(1)

    import os
    from pathlib import Path

    # Load credentials from the same location MCP server uses
    creds_path = Path.home() / ".claude-worktrees/Master-Knowledge-Base/pedantic-torvalds/Systems/.credentials/spotify-oauth.json"

    with open(creds_path) as f:
        creds = json.load(f)

    # Set up cache in the script directory
    cache_path = Path(__file__).parent / ".spotify_cache"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=creds['client_id'],
        client_secret=creds['client_secret'],
        redirect_uri=creds['redirect_uri'],
        scope="user-library-read,playlist-read-private,playlist-read-collaborative",
        cache_path=str(cache_path),
        open_browser=True  # Will open browser for first-time auth
    ))
    return sp

def get_playlist_tracks_with_previews(sp, playlist_id):
    """Get all tracks from a playlist with preview URL information."""
    results = sp.playlist_tracks(playlist_id)
    tracks_data = []

    while results:
        for item in results['items']:
            if item['track'] is None:
                continue

            track = item['track']
            track_info = {
                'name': track['name'],
                'id': track['id'],
                'artists': [artist['name'] for artist in track['artists']],
                'preview_url': track.get('preview_url'),
                'has_preview': track.get('preview_url') is not None,
                'duration_ms': track.get('duration_ms'),
                'album': track['album']['name'] if track.get('album') else None
            }
            tracks_data.append(track_info)

        # Get next batch if available
        results = sp.next(results) if results['next'] else None

    return tracks_data

def main():
    # Murder on the Dancefloor playlist ID
    playlist_id = '1LlTlKGKS1lsIR3CMsPk5a'

    print("Authenticating with Spotify...")
    sp = get_spotify_access_token()

    print(f"Fetching playlist tracks...")
    tracks = get_playlist_tracks_with_previews(sp, playlist_id)

    # Calculate statistics
    total_tracks = len(tracks)
    tracks_with_preview = sum(1 for t in tracks if t['has_preview'])
    tracks_without_preview = total_tracks - tracks_with_preview
    coverage_percentage = (tracks_with_preview / total_tracks * 100) if total_tracks > 0 else 0

    # Print summary
    print("\n" + "="*60)
    print("PREVIEW URL COVERAGE ANALYSIS")
    print("="*60)
    print(f"Total tracks: {total_tracks}")
    print(f"Tracks WITH preview URLs: {tracks_with_preview}")
    print(f"Tracks WITHOUT preview URLs: {tracks_without_preview}")
    print(f"Coverage: {coverage_percentage:.1f}%")
    print("="*60)

    # Save detailed results
    output_file = 'playlist_preview_analysis.json'
    output_data = {
        'summary': {
            'total_tracks': total_tracks,
            'tracks_with_preview': tracks_with_preview,
            'tracks_without_preview': tracks_without_preview,
            'coverage_percentage': round(coverage_percentage, 2)
        },
        'tracks': tracks
    }

    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2)

    print(f"\nDetailed results saved to: {output_file}")

    # Show sample of tracks without previews
    tracks_no_preview = [t for t in tracks if not t['has_preview']]
    if tracks_no_preview:
        print(f"\nSample tracks WITHOUT preview URLs (first 10):")
        for track in tracks_no_preview[:10]:
            artists_str = ', '.join(track['artists'])
            print(f"  - {track['name']} by {artists_str}")

if __name__ == '__main__':
    main()
