---
tags: #spotify #essentia-js #audio-analysis #feasibility-study #the-list #client-side #research
created: 14-12-2025
status: completed
---

# Essentia.js Client-Side Audio Analysis - Feasibility Report

## Executive Summary

**Recommendation: NOT VIABLE for 95%+ coverage goal**

Essentia.js is technically capable of extracting rich audio features from 30-second preview clips, **BUT** Spotify deprecated preview URLs from their Web API as of 27 November 2024. While workarounds exist, this introduces significant complexity and reliability concerns that make client-side analysis impractical for production use.

**Critical Finding:** 0% of tracks in "Murder on the Dancefloor" playlist (167 tracks) have preview URLs available through Spotify's official API.

---

## Table of Contents

- [Spotify Preview URL Crisis](#spotify-preview-url-crisis)
- [Essentia.js Technical Capabilities](#essentiajs-technical-capabilities)
- [Coverage Analysis](#coverage-analysis)
- [Workaround Assessment](#workaround-assessment)
- [Implementation Complexity](#implementation-complexity)
- [Final Recommendation](#final-recommendation)
- [Alternative Approaches](#alternative-approaches)

---

## Spotify Preview URL Crisis

### What Happened

On **27 November 2024**, Spotify officially removed 30-second preview URLs from their Web API for:
- All new applications registered on or after 27 November 2024
- Existing apps still in development mode without extension requests

### Impact on "Murder on the Dancefloor" Playlist

**Testing Results:**
- Total tracks: 167
- Tracks WITH preview URLs: **0**
- Tracks WITHOUT preview URLs: **167**
- Coverage: **0.0%**

### Verification with Popular Tracks

Tested well-known tracks to rule out playlist-specific issues:
- "Blinding Lights" by The Weeknd - NO preview
- "Shape of You" by Ed Sheeran - NO preview
- "Bad Guy" by Billie Eilish - NO preview
- "Bohemian Rhapsody" by Queen - NO preview

**Result:** Preview URLs are completely unavailable through official API for our application.

### Official Spotify Statement

> "30-second preview URLs, in multi-get responses (SimpleTrack object) are intentionally being removed for new API applications."

Source: https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api

---

## Essentia.js Technical Capabilities

### Overview

Essentia.js is a comprehensive JavaScript library from the Music Technology Group (Barcelona) providing **200+ audio analysis algorithms** via WebAssembly.

**Official Site:** https://mtg.github.io/essentia.js/

### Key Features for Spotify Alternative

#### 1. Rhythm & Tempo Analysis (25+ algorithms)

**BPM Detection:**
- `BeatTrackerDegara` - Beat position estimation
- `BeatTrackerMultiFeature` - Multi-feature beat tracking
- `PercivalBpmEstimator` - Tempo estimation in BPM
- `TempoCNN` - Deep learning tempo estimation
- `BpmHistogram` - Predominant periodicities

**Onset & Beat Features:**
- `OnsetDetection` / `OnsetDetectionGlobal`
- `SuperFluxExtractor` - Advanced onset detection
- `RhythmExtractor2013` - Comprehensive rhythm analysis

#### 2. Tonal & Key Analysis (18+ algorithms)

**Key Detection:**
- `HPCP` - Harmonic pitch class profiles
- `Key` / `KeyExtractor` - Key detection
- `ChordsDetection` - Chord analysis
- `Chromagram` - Chromatic analysis

**Harmonic Features:**
- `TuningFrequency` - Tuning estimation
- `Dissonance` / `Inharmonicity`
- `NNLSChroma` - Non-negative least squares chroma

#### 3. Energy & Loudness (14+ algorithms)

**Loudness Measurement:**
- `LoudnessEBUR128` - ITU-R BS.1770 standard
- `LoudnessVickers` / `Loudness` (Stevens' power law)
- `DynamicComplexity` - Loudness deviation

**Intensity & Dynamics:**
- `Intensity` - Aggressiveness classification
- `ReplayGain` - Loudness normalisation
- `Leq` - Equivalent sound level

#### 4. Spectral Analysis (30+ algorithms)

**Spectral Features:**
- `SpectralCentroid` / `SpectralPeaks`
- `SpectralContrast` / `SpectralComplexity`
- `MFCC` / `BFCC` / `GFCC` - Cepstral coefficients
- `RollOff` / `Flatness` / `HFC`

**Frequency Bands:**
- `MelBands` / `BarkBands` / `ERBBands`

#### 5. Perceptual Features

**Danceability:**
- `Danceability` - Direct danceability estimation

**Pitch & Melody:**
- `PitchMelodia` / `PitchYin` / `PitchCREPE` (deep learning)

---

## Coverage Analysis

### Official API Results

**Playlist:** "Murder on the Dancefloor" (167 tracks)

| Metric | Value |
|--------|-------|
| Total tracks | 167 |
| Tracks with preview URLs | 0 |
| Tracks without preview URLs | 167 |
| **Coverage** | **0.0%** |

### Sample Tracks WITHOUT Previews

1. "Run" by MPH, EV, Chris Lorenzo
2. "NOW" by Oppidan
3. "ABC's" by MPH, AntsLive
4. "one2three (feat. Leven Kali)" by Disclosure, Chris Lake, Leven Kali
5. "Expand" by Nitepunk, Harrison Clayton

**All 167 tracks returned `preview_url: null`**

---

## Workaround Assessment

### GitHub Workaround: spotify-preview-url-workaround

**Repository:** https://github.com/rexdotsh/spotify-preview-url-workaround

#### How It Works

- Scrapes Spotify's public embed player HTML
- Extracts preview URL from embed page source
- No API key or authentication required
- Available in Python and TypeScript

#### Example Usage

```python
from spotify_preview import get_spotify_preview_url
preview_url = get_spotify_preview_url('1301WleyT98MSxVHPZCA6M')
```

```typescript
const previewUrl = await getSpotifyPreviewUrl("1301WleyT98MSxVHPZCA6M");
```

#### Pros

- Works around API limitation
- No authentication needed
- Simple implementation
- Client-side capable

#### Cons

- **Violates Spotify ToS** - Scraping is not permitted
- **No reliability guarantees** - Could break at any time
- **Unknown success rate** - No documented coverage metrics
- **Legal risk** - Not using official API
- **Maintenance burden** - Requires updates when Spotify changes embed player
- **Rate limiting unclear** - Could trigger anti-scraping measures

---

## Implementation Complexity

### Client-Side Analysis Workflow

**Required Steps:**

1. **Get Track IDs** from Spotify API (works fine)
2. **Extract Preview URLs** via workaround scraper (HIGH RISK)
3. **Download/Stream Audio** to Web Audio API
4. **Initialize Essentia.js** WebAssembly modules
5. **Process Audio** through feature extractors
6. **Cache Results** to avoid re-processing

### Technical Challenges

#### 1. WebAssembly Bundle Size
- Essentia.js WebAssembly module is **several MB**
- Initial page load impact
- CDN/caching strategy required

#### 2. Browser Compatibility
- Requires WebAssembly support (all modern browsers)
- Web Audio API required
- Potential CORS issues with preview URLs

#### 3. Processing Performance
- 30-second preview × 167 tracks = **83.5 minutes of audio**
- Client-side CPU/memory intensive
- Battery drain on mobile devices
- Progress tracking/UI responsiveness challenges

#### 4. Reliability Concerns
- Scraper workaround could fail silently
- No error handling guarantees
- Embed player format could change
- Anti-scraping measures possible

#### 5. Caching Strategy
- IndexedDB for computed features
- Cache invalidation logic
- Storage quota management

### Complexity Rating: **HARD**

**Estimated Development Time:** 2-3 weeks for MVP
**Risk Level:** HIGH (legal, technical, reliability)

---

## Final Recommendation

### ❌ NOT RECOMMENDED

**Reasons:**

1. **0% Official API Coverage** - Spotify removed preview URLs entirely
2. **Legal Risk** - Workaround violates Spotify ToS
3. **Reliability Concerns** - Scraper could break at any time
4. **High Complexity** - Multiple integration points with failure modes
5. **Performance Issues** - Client-side processing 167 tracks is intensive
6. **Maintenance Burden** - Requires ongoing workaround updates

### Critical Blocker

**Spotify's API deprecation makes client-side audio analysis fundamentally incompatible with their platform for new applications.**

Even if Essentia.js is technically capable, the lack of reliable audio access makes it impractical for production use.

---

## Alternative Approaches

### 1. Web Playback SDK (RECOMMENDED)

**Approach:** Use Spotify's official Web Playback SDK to stream full tracks

**Pros:**
- Official API - no ToS violations
- Full track access, not just 30-second previews
- Better audio quality for analysis
- More reliable than scraping

**Cons:**
- Requires Spotify Premium subscription for users
- More complex integration than preview URLs
- User must authenticate

**Recommendation:** This is the **only viable official path forward** for audio analysis.

### 2. Server-Side Analysis

**Approach:** Use backend service to analyse audio and cache results

**Pros:**
- More processing power
- Can use full Essentia C++ library (faster)
- Better error handling
- Centralized caching

**Cons:**
- Infrastructure costs
- Still requires audio access (same preview URL problem)
- Latency for users

### 3. Hybrid: Use Spotify's Audio Features API

**Approach:** Leverage Spotify's existing audio analysis

**Pros:**
- Official API
- No audio processing needed
- Instant results
- Covers all tracks

**Cons:**
- Limited to Spotify's feature set
- Cannot customise analysis
- Deprecated features (energy, danceability) may not return

**Status:** Already explored in [[AUDIO-FEATURES-ALTERNATIVES-RESEARCH.md]]

### 4. Meyda.js (Client-Side Alternative)

**Approach:** Use Meyda.js instead of Essentia.js

**Pros:**
- Lighter weight than Essentia.js
- Simpler API
- Good for basic spectral features

**Cons:**
- **SAME PREVIEW URL PROBLEM** - Still blocked by Spotify API deprecation
- Fewer features than Essentia.js
- Less sophisticated algorithms

**Verdict:** Does not solve the core issue.

---

## Conclusion

Essentia.js is an **excellent library with powerful capabilities**, but **Spotify's API changes make client-side audio analysis non-viable** for new applications.

**The preview URL deprecation is a deal-breaker.**

### Recommended Path Forward

**Option 1: Web Playback SDK (Best)**
- Build feature using Spotify's official playback SDK
- Requires Premium users
- Full track analysis possible
- Officially supported

**Option 2: Abandon Client-Side Audio Analysis**
- Rely entirely on Spotify's Audio Features API
- Accept limited feature set
- Focus on features that still work (valence, acousticness, instrumentalness)
- See [[AUDIO-FEATURES-ALTERNATIVES-RESEARCH.md]] for details

**Option 3: Wait for Policy Change**
- Monitor Spotify Developer Blog
- Re-evaluate if preview URLs are restored
- Use alternative features in the meantime

---

## References

### Documentation
- Essentia.js: https://mtg.github.io/essentia.js/
- Essentia Algorithms: https://essentia.upf.edu/algorithms_reference.html
- Spotify API Changes: https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api

### Community Discussions
- Preview URLs Deprecated: https://community.spotify.com/t5/Spotify-for-Developers/Preview-URLs-Deprecated/td-p/6791368
- Preview URLs Missing: https://community.spotify.com/t5/Spotify-for-Developers/Preview-URLs-MP3-no-longer-exist-all-tracks/td-p/6685031

### Workarounds
- GitHub Workaround: https://github.com/rexdotsh/spotify-preview-url-workaround

### Related Research
- [[AUDIO-FEATURES-ALTERNATIVES-RESEARCH.md]]
- [[CLIENT-SIDE-AUDIO-ANALYSIS-LIBRARIES-RESEARCH.md]]
- [[SESSION-HANDOFF-13-12-2025.md]]

---

## Test Data

### Analysis Script
**Location:** `/Users/alastairpreacher/Documents/Obsidian/Master-Knowledge-Base/Personal/Personal-Spotify/the-list/check_preview_urls.py`

### Results
**Location:** `/Users/alastairpreacher/Documents/Obsidian/Master-Knowledge-Base/Personal/Personal-Spotify/the-list/playlist_preview_analysis.json`

**Summary:**
```json
{
  "summary": {
    "total_tracks": 167,
    "tracks_with_preview": 0,
    "tracks_without_preview": 167,
    "coverage_percentage": 0.0
  }
}
```

---

*Report generated: 14-12-2025*
*Researcher: Claude Code*
*Session: Essentia.js Spotify Analysis Testing*
