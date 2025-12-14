---
tags:
  - spotify
  - essentia-js
  - audio-analysis
  - research
  - 14-12-2025
created: 2025-12-14
status: completed
---

# Essentia.js Client-Side Audio Analysis - Summary Report

## Executive Summary

❌ **Client-side audio analysis using Essentia.js is NOT VIABLE** for Spotify playlists.

**Reason**: Spotify officially deprecated preview URLs on November 27, 2024, resulting in 0% coverage across all tracks.

## Critical Finding

### Preview URL Deprecation

- **Deprecation Date**: November 27, 2024
- **Coverage**: 0% (all tracks return null for preview_url)
- **Scope**: Entire Spotify catalog, all markets
- **Alternatives**: None provided by Spotify
- **Status**: Permanent, no workarounds
- **Source**: [Spotify Developer Blog](https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api)

### Impact on "Murder on the Dancefloor" Playlist

- Total tracks: 167
- Tracks with preview URLs: 0
- Coverage percentage: 0%
- **Required threshold**: 95%+
- **Gap**: 95 percentage points below viable threshold

## Essentia.js Capabilities (Technical Reference)

### What Essentia.js Can Do

Essentia.js is a comprehensive WebAssembly-based audio analysis library that provides:

#### 1. Tempo/BPM Detection
- **BpmHistogram**: Analyzes predominant periodicities in signal
- **PercivalBpmEstimator**: Estimates tempo in BPM
- **TempoCNN**: Neural network-based tempo prediction
- **TempoTap**: Estimates periods and phases of periodic signals

#### 2. Key Detection
- **Key**: Computes key estimate from pitch class profile
- **KeyExtractor**: Extracts key/scale for audio signal
- **HPCP**: Generates harmonic pitch class profiles

#### 3. Energy & Loudness Analysis
- **Loudness**: Steven's power law implementation
- **LoudnessEBUR128**: EBU R128 standard loudness
- **Energy**: Total signal energy calculation
- **Intensity**: Classifies as relaxed/moderate/aggressive

#### 4. Rhythm & Danceability
- **BeatTrackerDegara/MultiFeature**: Beat position estimation
- **RhythmExtractor**: Tempo and beat positions
- **Danceability**: Direct danceability estimation algorithm

#### 5. Spectral Features
- **SpectralCentroid**: Frequency content brightness
- **RollOff**: Spectral roll-off frequency
- **Flux**: Spectral change over time
- **MelBands/MFCC**: Perceptual frequency representations

### Technical Specifications

**Platform:**
- WebAssembly-based, runs in browser and Node.js
- All Essentia C++ standard mode algorithms available
- Pre-trained TensorFlow.js ML models included
- Real-time and offline analysis support

**Browser Compatibility:**
- Requires WebAssembly support (all modern browsers)
- Multiple build formats: IIFE, UMD, ES6
- No browser version restrictions documented

**Development Status:**
- Under rapid development
- APIs may change (backwards compatibility not guaranteed)
- Active project from Music Technology Group, UPF Barcelona

**Bundle Size & Performance:**
- Not officially documented
- WebAssembly overhead considerations
- Performance varies by selected extractors
- Would require testing for specific use case

## Why This Approach Fails

### The Fatal Blocker

**No audio source to analyze**

1. Preview URLs deprecated (0% coverage)
2. Spotify Web Playback SDK requires user authentication
3. No unauthenticated audio access method exists
4. Cannot download/cache tracks (licensing restrictions)

### What Would Have Been Required

If preview URLs were still available (pre-November 2024):

1. **Client-side Processing**
   - WebAssembly-based analysis for all 167 tracks
   - Browser-based execution (no server needed)
   - 30-second preview per track

2. **Caching Strategy**
   - Store analyzed audio features locally
   - Avoid re-processing on playlist load
   - IndexedDB or localStorage

3. **Fallback Handling**
   - Manual feature selection for missing previews
   - User preference overrides
   - Hybrid approach with API data

4. **Performance Optimization**
   - Batch processing with progress indication
   - Web Workers for non-blocking analysis
   - Progressive enhancement

**Implementation Complexity**: Medium (if audio source existed)

## Alternative Approaches

### 1. Spotify Audio Features API (Recommended)

**Status**: Unknown if deprecated alongside preview URLs

**Approach:**
- Use `/audio-features/{id}` endpoint
- Provides: danceability, energy, key, tempo, valence, acousticness, instrumentalness, liveness, speechiness
- No audio file needed, just track IDs
- Server-side API call

**Advantages:**
- Direct replacement for deprecated audio features
- No client-side processing overhead
- Official Spotify data (high accuracy)
- Instant response (no analysis delay)

**Disadvantages:**
- May also be deprecated (needs verification)
- Requires API quota management
- Rate limiting considerations

**Next Steps:**
1. Test if `/audio-features` endpoint still works
2. Verify with sample tracks from playlist
3. Check rate limits and quotas

### 2. Third-Party Audio Analysis APIs

**Options:**
- AcousticBrainz (check if still active)
- MusicBrainz Picard
- Last.fm API (limited features)
- TheAudioDB (basic metadata)

**Advantages:**
- Independent of Spotify API changes
- May have audio feature data
- Open-source options available

**Disadvantages:**
- Coverage may be incomplete
- Accuracy varies by service
- May require track matching/lookup
- Additional API keys needed

### 3. User-Authenticated Playback Analysis

**Approach:**
- Spotify Web Playback SDK with user login
- Analyze audio during actual playback
- Real-time feature extraction

**Advantages:**
- Access to full track audio
- Most accurate analysis possible
- Could use Essentia.js for custom features

**Disadvantages:**
- Requires user authentication (OAuth flow)
- Complex implementation
- Not suitable for bulk/background analysis
- User must play entire playlist
- Performance impact during playback

### 4. Manual Rating System (Fallback)

**Approach:**
- User provides ratings/preferences
- No automated audio analysis
- Simple preference-based sorting

**Advantages:**
- Simplest implementation
- No API dependencies
- Works regardless of Spotify changes
- Truly personalized ratings

**Disadvantages:**
- No objective audio feature data
- Requires manual user input for all tracks
- Subjective ratings only
- Time-consuming for large playlists

## Recommendation

### Immediate Action

✅ **Test Spotify Audio Features API**

1. Verify `/audio-features/{id}` endpoint status
2. Test with sample tracks from "Murder on the Dancefloor" (167 tracks)
3. Check feature completeness:
   - Danceability
   - Energy
   - Key
   - Tempo
   - Valence
   - Acousticness
   - Instrumentalness
   - Liveness
   - Speechiness

### Decision Tree

```
Is Audio Features API available?
├─ YES → Use it (best option)
│  └─ Provides all needed features
│     └─ No client-side processing needed
│
└─ NO → Implement hybrid approach
   ├─ Third-party APIs for features (where available)
   ├─ Manual user ratings (primary method)
   └─ Accept reduced feature set
```

### Long-term Strategy

If Audio Features API is also deprecated:

1. **Phase 1**: Manual user ratings (MVP)
   - Simple, works immediately
   - No API dependencies
   - User provides all ratings

2. **Phase 2**: Enhance with metadata
   - Genre classification
   - Artist similarity
   - Playlist context
   - Release date/popularity

3. **Phase 3**: ML-based predictions (optional)
   - Train model on user ratings
   - Predict ratings for unrated tracks
   - Use Spotify metadata as features
   - Improve over time with more data

## Technical Details Reference

### Spotify API Endpoints

**Preview URLs (DEPRECATED):**
```
GET /tracks/{id}
Response: { preview_url: null }  // Always null as of Nov 27, 2024
```

**Audio Features (TO VERIFY):**
```
GET /audio-features/{id}
Response: {
  danceability: 0.808,
  energy: 0.626,
  key: 7,
  tempo: 125.927,
  valence: 0.544,
  ...
}
```

### Essentia.js Installation

**NPM:**
```bash
npm install essentia.js
```

**CDN:**
```html
<script src="https://cdn.jsdelivr.net/npm/essentia.js@latest/dist/essentia-wasm.web.js"></script>
```

**Example Usage (if audio source existed):**
```javascript
import Essentia from 'essentia.js';

const essentia = new Essentia();

// Load audio buffer
const audioBuffer = await fetch(previewUrl)
  .then(r => r.arrayBuffer());

// Extract features
const tempo = essentia.BpmHistogram(audioBuffer);
const key = essentia.KeyExtractor(audioBuffer);
const danceability = essentia.Danceability(audioBuffer);
```

## Conclusions

1. **Essentia.js is technically excellent** - has all needed features
2. **Preview URL deprecation is fatal** - no audio source to analyze
3. **Client-side analysis is impossible** - regardless of library quality
4. **Alternative approach required** - use Spotify Audio Features API or manual ratings
5. **Audio Features API verification is critical next step** - determines entire project architecture

## References

- [Essentia.js Official Documentation](https://mtg.github.io/essentia.js/)
- [Essentia Algorithms Reference](https://essentia.upf.edu/algorithms_reference.html)
- [Spotify Developer Blog - Preview URL Deprecation](https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api)
- [Spotify Community Discussion - Preview URLs Deprecated](https://community.spotify.com/t5/Spotify-for-Developers/Preview-URLs-MP3-no-longer-exist-all-tracks/td-p/6685031)

## Project Context

**Parent Project**: [[the-list]] - Spotify playlist rating application

**Related Documents**:
- [[PLAN-14-12-2025-1430-essentia-js-spotify-preview-analysis]] - Full research plan
- `check_preview_coverage.py` - Preview URL coverage analysis script (not executed)

**Date Completed**: 2025-12-14
