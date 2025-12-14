#!/usr/bin/env python3
"""
Test script to check Spotify preview URL availability and audio analysis feasibility
"""

import requests
import json
import librosa
import numpy as np
from io import BytesIO

# Sample track IDs from the "Murder on the Dancefloor" playlist
test_tracks = [
    "16iHE1uKRvAKd1Mt13udlV",  # Run - MPH
    "2957N2fOpFu3HhAAyrzzoz",  # NOW - Oppidan
    "5VEhGGpGA38ZiQRXhWgOTG",  # ABC's - MPH
    "7irbhODkTYtv3aTOze7ts1",  # Just Like - MPH
    "24caY3L0inVduxmvqNfrzj",  # DARWIN - Oppidan
]

def analyze_preview_audio(preview_url):
    """
    Download and analyze audio from a preview URL using librosa
    """
    try:
        # Download audio
        print(f"Downloading audio from {preview_url[:50]}...")
        response = requests.get(preview_url, timeout=30)
        response.raise_for_status()

        audio_data = BytesIO(response.content)

        # Load with librosa
        print("Loading audio with librosa...")
        y, sr = librosa.load(audio_data, sr=22050, mono=True)

        # Extract features
        print("Extracting audio features...")

        # Tempo/BPM
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

        # Spectral centroid (brightness)
        spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]

        # RMS Energy
        rms = librosa.feature.rms(y=y)[0]

        features = {
            "tempo_bpm": float(tempo),
            "duration_seconds": float(len(y) / sr),
            "spectral_centroid_mean": float(np.mean(spectral_centroids)),
            "rms_energy_mean": float(np.mean(rms)),
            "beat_count": len(beat_frames)
        }

        return {"success": True, "features": features}

    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    print("Test script created. Use with Spotify API to test preview URLs.")
