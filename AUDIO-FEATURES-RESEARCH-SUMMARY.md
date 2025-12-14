# Audio Features Research Summary - "The List" Playlist App

**Date:** 14 December 2025
**Objective:** Find API solution to provide audio features (BPM, Energy, Danceability, etc.) for 168 tracks in "Murder on the Dancefloor" playlist
**Required Coverage:** 95%+ to be viable
**Playlist Characteristics:** Underground/esoteric electronic music (UK Bass, Tech House, Techno, Garage)

---

## Executive Summary

**RESULT: No viable solution found for 95%+ coverage**

After comprehensive testing of 5 different approaches, none can provide the required coverage for this esoteric playlist. The best option (ReccoBeats) only covers 25% of tracks.

**DECISION: Proceed without automated audio features. Focus on collaborative rating system (already working).**

---

## Options Tested

### 1. ReccoBeats API ⚠️ PARTIAL COVERAGE

**Coverage:** 25% (25 out of 100 tracks tested)

**Available Features (10):**
- ✅ Tempo (BPM)
- ✅ Energy (0.0-1.0)
- ✅ Danceability (0.0-1.0)
- ✅ Valence (mood: 0=sad, 1=happy)
- ✅ Key (pitch class 0-11)
- ✅ Mode (major/minor)
- ✅ Acousticness (0.0-1.0)
- ✅ Speechiness (0.0-1.0)
- ✅ Instrumentalness (0.0-1.0)
- ✅ Loudness (dB)

**Access:** Free API, no authentication required

**Why Coverage is Low:**
- Database favours mainstream/major label releases
- Underground artists (MPH, Oppidan, bullet tooth, etc.) not included
- Missing 75% of tracks including some established artists (Charlotte de Witte, Kelly Lee Owens, The Dare)

**Verdict:** Could use for 25% of tracks, but 75% gap unacceptable

**Test Report:** `reccobeats_api_coverage_report.md`

---

### 2. Beatport API ❌ ACCESS BLOCKED

**Coverage:** Unable to test (API access unavailable)

**Available Features (if accessible):**
- BPM (accurate to 0.1 BPM, professional DJ standard)
- Musical Key
- Genre/Sub-genre

**Missing Features:**
- Energy, Valence, Loudness, Instrumentalness, Speechiness, Liveness

**Access Issues:**
- Official API exists (v4) but requires approval
- Developer portal shows "No Access - You don't have permission to view this portal"
- Multiple developers report 12+ month wait times with no response
- Registration URL redirects to main Beatport site

**Estimated Coverage (if accessible):** 60-75%
- Good genre match for electronic/dance music
- Underground/emerging artists likely missing
- Bootlegs, edits, VIP mixes not included

**Verdict:** Not viable - cannot obtain API credentials

**Test Report:** `Beatport API Research Report` (in agent output)

---

### 3. GetSongBPM API ❌ CLOUDFLARE BLOCKS AUTOMATION

**Coverage:** 0% (cannot test - Cloudflare bot protection)

**Available Features (6 only):**
- ✅ Tempo (BPM)
- ✅ Time Signature
- ✅ Key
- ✅ Camelot Notation
- ✅ Danceability (0-100)
- ✅ Acousticness (0-100)

**Missing Features:**
- ❌ Energy (critical for workout/high-energy playlists)
- ❌ Valence
- ❌ Loudness
- ❌ Instrumentalness
- ❌ Speechiness
- ❌ Liveness

**Access:**
- Free with mandatory backlink requirement
- ✅ Backlink added to app footer: https://alastairpreacher.github.io/the-list/
- ✅ API key obtained: `f5dfad7e75c4b716e0ce0d62ad05562d`

**CRITICAL BLOCKER:**
- API protected by Cloudflare "Enable JavaScript and cookies" challenge
- Cannot be accessed from server-side Python/Node scripts
- Only works from browser JavaScript with user session
- **Impossible to batch test tracks or automate lookups**

**Rate Limits:** 3000 requests/hour (would be sufficient if API was accessible)

**Verdict:** Not viable - automation blocked, missing 50% of features

**Test Results:** All 100 tracks returned Cloudflare challenge page

---

### 4. MCP Audio Analysis (Hugo How-Choong's Servers) ❌ NO AUDIO SOURCE

**Coverage:** 0% (Spotify preview URLs deprecated November 2024)

**Available Features (if audio existed):**
- BPM/tempo detection (librosa)
- Energy/loudness (RMS)
- Spectral characteristics
- Beat locations
- MFCC (timbre)
- Basic key detection (chroma features)

**Missing Features (require ML models):**
- Danceability
- Valence
- Speechiness
- Acousticness
- Instrumentalness

**CRITICAL BLOCKER:**
- Spotify deprecated `preview_url` field on 27 November 2024
- 0% of tracks have preview URLs (all return null)
- Cannot analyze audio without source files

**Installation Complexity:** Medium-Hard (requires uvx, librosa, ffmpeg)

**Verdict:** Not viable - no audio source to analyze

**Test Report:** `MCP_AUDIO_ANALYSIS_RESEARCH_REPORT.md`

---

### 5. Essentia.js (Client-Side Analysis) ❌ NO AUDIO SOURCE

**Coverage:** 0% (Spotify preview URLs deprecated November 2024)

**Available Features (if audio existed):**
- BPM/tempo detection (multiple algorithms including neural network)
- Key detection
- Energy & loudness (multiple algorithms)
- **Direct danceability algorithm** (exactly what's needed!)
- Rhythm extraction
- Spectral features

**Technical Specs:**
- WebAssembly-based
- Runs in browser and Node.js
- Pre-trained TensorFlow.js models

**SAME BLOCKER AS MCP:**
- Spotify preview URLs deprecated 27 November 2024
- 0% of tracks have preview URLs
- Cannot analyze without audio source

**Implementation Complexity:** Medium (would have been straightforward)

**Verdict:** Not viable - no audio source to analyze

**Test Report:** `ESSENTIA-JS-ANALYSIS-SUMMARY.md`

---

## Coverage Comparison Table

| Solution | Coverage | Features Available | Cost | Setup | Automation | Verdict |
|----------|----------|-------------------|------|-------|------------|---------|
| **ReccoBeats** | 25% | 10 features (full set) | Free | Easy | ✅ Yes | ⚠️ Low coverage |
| **Beatport** | Unable to test | 3 features (BPM, Key, Genre) | Free (non-commercial) | HARD (blocked) | N/A | ❌ No access |
| **GetSongBPM** | 0% (blocked) | 6 features (missing Energy) | Free* (*backlink) | Medium | ❌ Cloudflare blocks | ❌ Not viable |
| **MCP Analysis** | 0% (no audio) | 5 features (basic only) | Free | Medium-Hard | ✅ Yes | ❌ No source |
| **Essentia.js** | 0% (no audio) | 10+ features (comprehensive) | Free | Medium | ✅ Yes | ❌ No source |

---

## Why 95%+ Coverage Impossible for This Playlist

**Playlist Characteristics:**
- **Underground/esoteric** electronic music
- **Emerging artists** (MPH, Oppidan, bullet tooth, Prozak, fia)
- **Independent labels** and self-releases
- **Edits, VIP mixes, bootlegs** (not in commercial databases)
- **Recent releases** (less time for database ingestion)
- **Crossover artists** (Baxter Dury, Mura Masa, The Dare - not primarily electronic)

**Database Coverage Patterns:**
- Mainstream music databases favour **major label releases**
- Underground/niche artists **underrepresented**
- **Spotify's own audio features** (deprecated) were the only source with 100% coverage

---

## Alternative Approaches Considered

### ❌ Web Scraping Beatport
- Violates Terms of Service
- Fragile (breaks when HTML changes)
- Could result in IP ban
- Requires ongoing maintenance
- **Rejected:** Legal and technical risks

### ❌ Self-Hosted Audio Analysis
- Requires downloading full tracks (copyright issues)
- Processing time: 3-7 seconds per track
- Need ML models for Danceability/Valence
- Spotify preview URLs deprecated (no legal audio source)
- **Rejected:** No audio source available

### ❌ Manual Data Entry
- 168 tracks × 10 features = 1,680 data points
- Time-consuming and error-prone
- Subjective ratings for Energy/Danceability
- **Rejected:** Not scalable

---

## Recommendation: Focus on Collaborative Rating

### What's Already Working ✅

1. **Star Ratings (1-5 stars)**
   - User can rate tracks
   - See other users' ratings
   - Calculate average ratings
   - Saves to Firebase in real-time

2. **Comments System**
   - Users can comment on tracks
   - See all comments chronologically
   - Identify own comments vs others
   - Real-time collaboration

3. **User Management**
   - Username picker modal
   - Multiple users supported
   - Persistent username storage

4. **Playlist Integration**
   - Load any Spotify playlist
   - Display album artwork
   - Show track metadata
   - User-resizable columns

### What This Means

**The VALUE of your app is already there:**
- Collaborative rating between you and Neil
- Comments for context and recommendations
- Album artwork for visual recognition
- Real-time Firebase sync

**Audio features would be "nice to have" but NOT essential:**
- 25% coverage (ReccoBeats) doesn't justify complexity
- Manual ratings provide MORE value (your personal taste)
- Focus energy on high-priority features instead

---

## Next Steps: Remaining Features

Instead of chasing audio features APIs, focus on:

### HIGH PRIORITY
1. **'Currently Playing' indicator** - Show what you're listening to in real-time
   - Uses Spotify Web Playback SDK
   - Updates automatically when track changes
   - User said: "definitely high priority"

### MEDIUM PRIORITY
2. **Track playback in browser** - Play full tracks (Premium users)
3. **CSV export** - Download ratings + comments as spreadsheet
4. **Playlist recommendations** - Suggest tracks based on ratings

### LOWER PRIORITY
5. **Firebase security rules** - Secure the database (currently in test mode)
6. **Testing with Neil** - Verify collaborative features work

---

## Files Created During Research

1. **ReccoBeats Coverage Report:** `reccobeats_api_coverage_report.md`
2. **Beatport Research:** Included in agent outputs
3. **GetSongBPM Test Script:** `test_getsongbpm_coverage.py`
4. **MCP Audio Analysis Report:** `MCP_AUDIO_ANALYSIS_RESEARCH_REPORT.md`
5. **Essentia.js Summary:** `ESSENTIA-JS-ANALYSIS-SUMMARY.md`
6. **This Summary:** `AUDIO-FEATURES-RESEARCH-SUMMARY.md`

---

## Conclusion

**After comprehensive testing of 5 different approaches:**
- ❌ None provide 95%+ coverage for esoteric playlists
- ❌ Spotify's deprecation of preview URLs killed client-side analysis
- ❌ Commercial databases focus on mainstream music
- ✅ Collaborative rating system already provides core value

**DECISION: Proceed without automated audio features. Focus on "Currently Playing" indicator and other high-priority features.**

---

**Research completed:** 14 December 2025
**Time invested:** ~2 hours
**Conclusion:** Skip audio features, move forward with collaborative rating focus
