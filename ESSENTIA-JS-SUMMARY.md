---
tags: #spotify #essentia-js #summary #the-list
created: 14-12-2025
---

# Essentia.js Quick Summary

## The Verdict: ❌ NOT VIABLE

### Why?

**Spotify killed preview URLs on 27 Nov 2024**

- Your playlist: 167 tracks
- Tracks with previews: **0** (0%)
- Even "Blinding Lights", "Shape of You" have NO previews

### What is Essentia.js Capable Of?

**200+ audio analysis algorithms including:**

✅ BPM/Tempo Detection (25+ algorithms)
✅ Key Detection (18+ algorithms)
✅ Energy & Loudness (14+ algorithms)
✅ Danceability Detection
✅ Spectral Analysis (30+ algorithms)

**Essentia.js is EXCELLENT... if you have audio to analyze**

### The Problem

```
Spotify API → No preview URLs
    ↓
No audio access → Can't analyze anything
    ↓
Essentia.js is useless without audio input
```

### Workaround?

**GitHub scraper exists:** https://github.com/rexdotsh/spotify-preview-url-workaround

**BUT:**
- Violates Spotify ToS
- Could break anytime
- Unknown reliability
- Legal risk

### What Now?

**Option 1: Web Playback SDK** (RECOMMENDED)
- Official Spotify solution
- Requires Premium users
- Full track access, not just 30s clips
- More complex integration

**Option 2: Give Up Client-Side Analysis**
- Use Spotify's existing Audio Features API
- Limited features (no energy, danceability)
- See: [[AUDIO-FEATURES-ALTERNATIVES-RESEARCH.md]]

**Option 3: Wait for Spotify Policy Change**
- Monitor developer blog
- Unlikely to revert decision

---

**Full Report:** [[ESSENTIA-JS-FEASIBILITY-REPORT.md]]
