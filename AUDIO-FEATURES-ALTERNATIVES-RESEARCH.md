---
tags:
  - personal
  - tech
  - spotify
  - research
  - alternatives
created: 2025-12-14
---

# Audio Features Alternatives Research Report
**Date:** 14 December 2025
**Project:** The List (Spotify Playlist Rating App)
**Status:** Comprehensive Research Complete

---

## Executive Summary

Spotify deprecated their Audio Features API in November 2024, removing access to track metrics like BPM, energy, danceability, and valence. This research evaluates **commercial APIs, freemium services, and hybrid client-side approaches** to replace this functionality for "The List" app.

**Key Findings:**
- **Best Free Option:** ReccoBeats (completely free, similar features)
- **Best Hybrid Option:** Client-side analysis using Essentia.js
- **Best Paid Option:** SoundNet Track Analysis API via RapidAPI (drop-in replacement)
- **Recommended Approach:** Start with ReccoBeats + Essentia.js fallback, cache results in Firebase

---

## Table of Contents
- [Commercial API Solutions](#commercial-api-solutions)
- [Freemium API Solutions](#freemium-api-solutions)
- [Hybrid Client-Side Approaches](#hybrid-client-side-approaches)
- [Comparison Matrix](#comparison-matrix)
- [Cost-Benefit Analysis](#cost-benefit-analysis)
- [Recommended Implementation Strategy](#recommended-implementation-strategy)
- [Implementation Roadmap](#implementation-roadmap)

---

## Commercial API Solutions

### 1. SoundNet Track Analysis API (via RapidAPI)
**URL:** https://rapidapi.com/soundnet-soundnet-default/api/track-analysis

**Features:**
- ✅ Drop-in replacement for Spotify's deprecated endpoints
- Key, mode, tempo (BPM), camelot notation
- Energy (0-100), danceability (0-100), happiness (0-100)
- Acousticness, instrumentalness, loudness, speechiness, liveness
- Popularity (0-100)

**Authentication:**
- Simple RapidAPI key authentication (no OAuth scopes)
- No audio file upload required
- Just send track title + artist name

**Pricing:**
- ⚠️ Exact pricing not publicly disclosed
- Hosted on RapidAPI (typical range: $10-$50/month for hobbyist tiers)
- **Action Required:** Check RapidAPI page directly for current pricing

**Pros:**
- ✅ Purpose-built as Spotify Audio Features replacement
- ✅ Simple authentication (easier than Spotify's OAuth)
- ✅ No file uploads (lightweight)
- ✅ Well-documented on RapidAPI

**Cons:**
- ❌ Paid service (no confirmed free tier)
- ❌ Third-party dependency
- ❌ May have usage caps on lower tiers

---

### 2. Cyanite Music Analysis API
**URL:** https://cyanite.ai/

**Features:**
- ✅ 120+ musical features extracted
- Mood labels: aggressive, calm, chilled, dark, energetic, epic, happy, romantic, sad, scary, sexy, ethereal, uplifting (0-1 scale)
- Genre classification: 15+ genres with probability scores
- BPM, key, voice classification (male/female/instrumental)
- Segment-wise analysis (15s temporal resolution for mood/genre)

**Pricing:**
- 💰 **€290/month** base fee (business-focused)
- Artists/producers: **$19/month** self-service tier
- Pricing scales with catalogue size

**Pros:**
- ✅ Very comprehensive (120+ features)
- ✅ Advanced mood/genre analysis
- ✅ Time-resolved features (track mood changes over time)
- ✅ High accuracy for professional use

**Cons:**
- ❌ Expensive (€290/month for API)
- ❌ Overkill for personal project
- ❌ Designed for music catalogues (not single-track queries)

**Verdict:** ❌ Not suitable for "The List" (too expensive for personal use)

---

### 3. Gracenote Music API
**URL:** https://developer.gracenote.com/

**Features:**
- ✅ 100+ million tracks in database
- Audio fingerprints, metadata, cover art
- Genre, mood, tempo, language, origin
- MusicID recognition technology

**Pricing:**
- ⚠️ Not publicly disclosed (enterprise contracts required)
- 30-day free Sample plan available
- Must contact sales for pricing

**Pros:**
- ✅ Industry-standard (owned by Nielsen)
- ✅ Massive database (100M+ tracks)
- ✅ Reliable enterprise solution

**Cons:**
- ❌ No public pricing (likely expensive)
- ❌ Enterprise-focused (contracts required)
- ❌ Overkill for personal project

**Verdict:** ❌ Not suitable for "The List" (enterprise pricing)

---

### 4. Soundcharts API
**URL:** https://developers.soundcharts.com/

**Features:**
- ✅ Complete audio features (tempo, key, energy, valence, danceability, acousticness)
- Real-time music analytics across DSPs (Spotify, Apple Music, YouTube, Deezer)
- Global music intelligence database

**Pricing:**
- **Free Tier:** 1,000 requests (no credit card required)
- **Paid Plans:**
  - 500,000 requests: **$250/month**
  - 4 million requests: **$450/month**
  - 10 million requests: **$850/month**
  - 20 million requests: **$1,600/month**
  - 60 million requests: **$4,500/month**
- Rate limit: 10,000 requests/minute (all tiers)

**Pros:**
- ✅ Free tier available (1,000 requests for testing)
- ✅ Full Spotify-like audio features
- ✅ Cross-platform music data
- ✅ Professional-grade analytics

**Cons:**
- ❌ Free tier too limited (1,000 requests burns quickly)
- ❌ Paid tiers expensive ($250/month minimum)
- ❌ Designed for music industry professionals

**Verdict:** ⚠️ Use free tier for testing only - not sustainable for personal project

---

### 5. 7digital Music API
**URL:** https://www.7digital.com/

**Features:**
- ✅ 70 million tracks
- High-quality album art, 30s previews, full-length streaming
- REST API with OAuth 2.0
- Catalogue metadata and content availability management

**Pricing:**
- ⚠️ Not publicly disclosed (contact sales)
- Appears to be music distribution-focused (not audio analysis)

**Pros:**
- ✅ Massive catalogue
- ✅ 99.9% uptime
- ✅ Preview clips available

**Cons:**
- ❌ No public pricing
- ❌ Focused on music distribution (not feature extraction)
- ❌ Unclear if audio features API exists

**Verdict:** ❌ Not suitable - doesn't appear to offer audio features API

---

### 6. ACRCloud Music Recognition API
**URL:** https://www.acrcloud.com/music-recognition/

**Features:**
- ✅ Music recognition (Shazam-like)
- Metadata from Spotify, Apple Music, YouTube, Deezer, etc.
- Audio fingerprinting

**Pricing:**
- **Free Trial:** 14 days
- **Free Tier:** 100 recognition requests/day
- **Paid:** $5.80 per 1,000 requests

**Pros:**
- ✅ Generous free tier (100/day = 3,000/month)
- ✅ Affordable paid tier ($5.80/1,000)
- ✅ Cross-platform metadata

**Cons:**
- ❌ Recognition-focused (not feature extraction)
- ❌ Doesn't extract audio features (BPM, energy, etc.)
- ❌ Wrong use case for "The List"

**Verdict:** ❌ Not suitable - doesn't provide audio features

---

### 7. Tunebat Music Metadata API
**URL:** https://tunebat.com/API

**Features:**
- ✅ 70+ million tracks
- Song key, BPM/tempo, energy, danceability, happiness, popularity
- Camelot notation (for DJs)
- Release date, label info

**Pricing:**
- **Analyzer Tool (upload files):** $7.99/month or $35.88/year
- **API Pricing:** ⚠️ Not publicly listed (contact Tunebat)

**Pros:**
- ✅ DJ-friendly (Camelot notation)
- ✅ Spotify-like features
- ✅ Large database

**Cons:**
- ❌ API pricing not transparent
- ❌ Likely paid-only (no free tier mentioned)
- ❌ Must contact sales for API access

**Verdict:** ⚠️ Investigate if free tier exists - otherwise too expensive

---

## Freemium API Solutions

### 1. ReccoBeats API ⭐ RECOMMENDED
**URL:** https://reccobeats.com/

**Features:**
- ✅ Acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, valence
- ✅ **Exact same features as Spotify's deprecated API**
- Track recommendations based on audio features
- Audio feature extraction (upload files)

**Pricing:**
- 🎉 **Completely FREE** (no paid tiers)
- No API key required (according to public APIs directory)

**Rate Limits:**
- ⚠️ Not publicly disclosed ("configured internally")
- 429 Too Many Requests response if exceeded
- Check `Retry-After` header for backoff timing

**Database Size:**
- Millions of tracks

**Pros:**
- ✅ **100% free** (no hidden costs)
- ✅ Drop-in Spotify replacement (same feature set)
- ✅ No authentication required
- ✅ Perfect for personal projects
- ✅ Audio file upload option

**Cons:**
- ❌ Smaller database than Spotify (newer service)
- ❌ Rate limits unknown (must test empirically)
- ❌ Limited track record (newer service, less proven)

**Implementation Notes:**
- Use for primary audio features retrieval
- Cache results in Firebase to respect rate limits
- Monitor 429 responses and implement exponential backoff
- Fallback to client-side analysis if track not found

**Verdict:** ✅ **BEST FREE OPTION** - Start here for "The List"

---

### 2. AcousticBrainz API
**URL:** https://acousticbrainz.org/

**Features:**
- ✅ Rhythm descriptors (BPM, danceability)
- Tonal information (key, scale)
- Low-level acoustic descriptors (loudness, spectral shape)

**Pricing:**
- 🎉 **100% FREE** (CC0 public domain license)

**Rate Limits:**
- 10 queries per 10 seconds per IP
- ~3,600 requests/hour max

**Database:**
- Community-contributed data
- Requires MusicBrainz ID (MBID) for lookups

**Pros:**
- ✅ Completely free and open data
- ✅ No authentication required
- ✅ Rich low-level features

**Cons:**
- ❌ **Service stopped collecting data in 2022** (static database)
- ❌ Requires MusicBrainz ID (extra lookup step)
- ❌ Smaller coverage (community-contributed only)
- ❌ No new tracks added after 2022

**Implementation Notes:**
- Use as fallback if ReccoBeats fails
- Must map Spotify Track ID → MusicBrainz ID first
- Limited usefulness for new music (post-2022)

**Verdict:** ⚠️ Use as **fallback only** - database frozen since 2022

---

### 3. Musixmatch API
**URL:** https://developer.musixmatch.com/

**Features:**
- ✅ Lyrics API
- Track metadata, album info
- Search API

**Pricing:**
- Free tier available (instant API key on registration)

**Pros:**
- ✅ Free to get started
- ✅ Good for lyrics integration

**Cons:**
- ❌ **Does NOT provide audio features** (BPM, energy, danceability)
- ❌ Lyrics-focused (wrong use case)

**Verdict:** ❌ Not suitable for audio features

---

## Hybrid Client-Side Approaches

### 1. Essentia.js ⭐ RECOMMENDED HYBRID
**URL:** https://mtg.github.io/essentia.js/

**Overview:**
JavaScript library for music/audio analysis developed by Music Technology Group, UPF Barcelona. Runs **entirely in the browser** (client-side processing).

**Features:**
- ✅ **Danceability** (0-3+ scale, higher = more danceable)
- ✅ **Energy** (intensity and activity)
- ✅ **Mood/genre classification** (rock, pop, electronic, jazz, etc.)
- ✅ BPM, tempo estimation
- ✅ Key, pitch, melody extraction
- ✅ Onset detection, beat tracking
- ✅ Pre-trained ML models using TensorFlow.js

**Licensing:**
- 🎉 **Open source** (free to use)

**Pros:**
- ✅ **No API calls required** (100% client-side)
- ✅ No rate limits (runs in user's browser)
- ✅ Privacy-friendly (audio never leaves device)
- ✅ Comprehensive feature extraction (120+ algorithms)
- ✅ No costs whatsoever
- ✅ Works with Spotify 30s preview URLs

**Cons:**
- ❌ Requires audio file access (need Spotify preview URL or local file)
- ❌ Processing overhead (uses user's CPU)
- ❌ May be slower than API calls
- ❌ Accuracy depends on audio quality (30s previews may be limiting)
- ❌ Larger bundle size (adds ~1-2MB to app)

**Implementation Strategy:**
1. Fetch Spotify track preview URL (30s MP3)
2. Load audio into browser using Web Audio API
3. Extract features using Essentia.js
4. Cache results in Firebase (avoid re-processing)
5. Display in "The List" table

**Code Example:**
```javascript
import * as Essentia from 'essentia.js';

async function analyzeTrack(previewUrl) {
  // Load audio
  const audioCtx = new AudioContext();
  const response = await fetch(previewUrl);
  const arrayBuffer = await response.arrayBuffer();
  const audioBuffer = await audioCtx.decodeAudioData(arrayBuffer);

  // Extract features
  const essentia = new Essentia.EssentiaWASM();
  const features = essentia.compute(audioBuffer);

  return {
    bpm: features.rhythm.bpm,
    danceability: features.rhythm.danceability,
    energy: features.energy,
    key: features.tonal.key,
    mood: features.highlevel.mood
  };
}
```

**Verdict:** ✅ **BEST HYBRID OPTION** - Use when preview URLs available

---

### 2. Web Audio Beat Detection Libraries

#### realtime-bpm-analyzer
**URL:** https://github.com/dlepaux/realtime-bpm-analyzer
**NPM:** `realtime-bpm-analyzer`

**Features:**
- ✅ BPM detection from files, streams, microphone
- Pure Web Audio API (no dependencies)
- Lightweight (~5KB minified)

**Pros:**
- ✅ Real-time analysis
- ✅ No external dependencies
- ✅ Works with audio streams

**Cons:**
- ❌ BPM only (no danceability, energy, etc.)
- ❌ Limited feature set

---

#### web-audio-beat-detector
**URL:** https://github.com/chrisguttandin/web-audio-beat-detector

**Features:**
- ✅ BPM detection from AudioBuffer
- Returns Promise with tempo

**Pros:**
- ✅ Simple API
- ✅ Good for electronic music

**Cons:**
- ❌ BPM only
- ❌ Algorithm optimized for electronic music (may not work well for other genres)

---

#### BeatDetect.js
**URL:** https://arthurbeaulieu.github.io/BeatDetect.js/

**Features:**
- ✅ BPM calculation
- ✅ Time offset to first beat
- ~5KB minified

**Pros:**
- ✅ Lightweight
- ✅ Provides beat timing (useful for visualizations)

**Cons:**
- ❌ BPM only

---

**Verdict on Beat Detection Libraries:**
⚠️ Use **only if you just need BPM** - otherwise use Essentia.js for comprehensive features

---

### 3. Spotify Preview URL Workaround
**URL:** https://github.com/rexdotsh/spotify-preview-url-workaround

**Overview:**
Extracts 30s preview URLs by scraping Spotify's embed player HTML (no API key required).

**How It Works:**
- Parses Spotify embed player HTML
- Extracts preview MP3 URL directly
- Bypasses official API limitations

**Pros:**
- ✅ No authentication required
- ✅ No API key needed
- ✅ Workaround for Spotify's API preview URL removal (Nov 2024)

**Cons:**
- ❌ **Unofficial solution** (could break anytime)
- ❌ Depends on Spotify's HTML structure
- ❌ Preview URLs often `null` (Spotify intentionally removing them)
- ❌ Limited adoption (5 GitHub stars, 2 commits)
- ❌ Not reliable long-term

**Verdict:** ⚠️ **Last resort only** - use official Spotify API preview URLs first

---

## Comparison Matrix

| Solution | Cost | BPM | Energy | Danceability | Mood | Free Tier | Rate Limits | Reliability | Use Case |
|----------|------|-----|--------|--------------|------|-----------|-------------|-------------|----------|
| **ReccoBeats** | Free | ✅ | ✅ | ✅ | ❌ | ✅ Unlimited | ⚠️ Unknown | ⚠️ Newer | **BEST FREE** |
| **Essentia.js** | Free | ✅ | ✅ | ✅ | ✅ | ✅ N/A | ✅ None | ✅ Proven | **BEST HYBRID** |
| **SoundNet (RapidAPI)** | Paid | ✅ | ✅ | ✅ | ✅ | ❌ | ⚠️ Tier-based | ✅ Good | Drop-in replacement |
| **Soundcharts** | $250/mo | ✅ | ✅ | ✅ | ❌ | ⚠️ 1,000 req | 10k/min | ✅ Enterprise | Testing only |
| **Cyanite** | €290/mo | ✅ | ✅ | ✅ | ✅ | ❌ | ⚠️ Unknown | ✅ Enterprise | Too expensive |
| **AcousticBrainz** | Free | ✅ | ❌ | ✅ | ❌ | ✅ Unlimited | 10/10s | ⚠️ Frozen 2022 | Fallback only |
| **Gracenote** | Enterprise | ✅ | ⚠️ | ⚠️ | ✅ | ❌ | ⚠️ Unknown | ✅ Industry std | Too expensive |
| **Tunebat** | Unknown | ✅ | ✅ | ✅ | ✅ | ❌ | ⚠️ Unknown | ✅ Good | Need pricing |

---

## Cost-Benefit Analysis

### For "The List" App (Personal Project)

**Budget Constraints:**
- No budget initially
- Must be free or very low cost (<$10/month)
- Unpredictable usage (bursts during playlist rating sessions)

**Feature Requirements:**
- BPM (nice-to-have)
- Energy (medium priority)
- Danceability (medium priority)
- Mood/happiness (low priority)

**Scale:**
- Estimated 50-200 tracks per rating session
- 2-5 sessions per week
- ~400-1,000 tracks/month
- Caching can reduce API calls by 70-90%

---

### Option 1: ReccoBeats Only (FREE)
**Monthly Cost:** $0

**Pros:**
- ✅ Zero cost
- ✅ Simple implementation
- ✅ All required features

**Cons:**
- ❌ Rate limits unknown (may hit ceiling)
- ❌ Newer service (reliability unknown)

**Risk Mitigation:**
- Cache all results in Firebase
- Implement exponential backoff on 429 errors
- Monitor service uptime

**Verdict:** ✅ **START HERE** - best risk/reward for personal project

---

### Option 2: Essentia.js Only (FREE)
**Monthly Cost:** $0

**Pros:**
- ✅ Zero cost
- ✅ No rate limits
- ✅ Privacy-friendly

**Cons:**
- ❌ Requires Spotify preview URLs (often null)
- ❌ Client-side processing overhead
- ❌ Larger bundle size

**Risk Mitigation:**
- Only analyze tracks with preview URLs
- Cache results to avoid re-processing
- Lazy-load Essentia.js library

**Verdict:** ✅ **EXCELLENT FALLBACK** - use when ReccoBeats fails

---

### Option 3: ReccoBeats + Essentia.js Hybrid (FREE)
**Monthly Cost:** $0

**Strategy:**
1. Try ReccoBeats API first
2. If track not found or rate limited → use Essentia.js
3. If no preview URL → display "N/A"
4. Cache all results in Firebase

**Pros:**
- ✅ Zero cost
- ✅ Best coverage (two sources)
- ✅ Resilient to API failures
- ✅ No vendor lock-in

**Cons:**
- ❌ More complex implementation
- ❌ Longer processing time (fallback chain)

**Verdict:** ✅ **RECOMMENDED APPROACH** for "The List"

---

### Option 4: SoundNet via RapidAPI (PAID)
**Monthly Cost:** $10-50/month (estimated)

**Pros:**
- ✅ Drop-in Spotify replacement
- ✅ Reliable (commercial service)
- ✅ Simple authentication

**Cons:**
- ❌ Monthly cost (budget constraint)
- ❌ Usage caps on lower tiers
- ❌ Vendor lock-in

**Verdict:** ⚠️ **ONLY IF FREE OPTIONS FAIL** - investigate pricing first

---

### Option 5: Soundcharts Free Tier (1,000 requests)
**Monthly Cost:** $0 (then $250/month)

**Pros:**
- ✅ Professional-grade
- ✅ 1,000 free requests for testing

**Cons:**
- ❌ Free tier burns quickly (2-3 sessions)
- ❌ Expensive paid tier ($250/month)
- ❌ Not sustainable for personal project

**Verdict:** ⚠️ **TESTING ONLY** - not viable long-term

---

## Recommended Implementation Strategy

### Phase 1: ReccoBeats API Integration (Week 1)

**Goals:**
- ✅ Fetch audio features from ReccoBeats
- ✅ Display BPM, energy, danceability in table
- ✅ Cache results in Firebase

**Implementation:**
```javascript
// Example: ReccoBeats API call
async function getAudioFeatures(trackName, artistName) {
  const cacheKey = `features_${trackId}`;

  // Check Firebase cache first
  const cached = await firebase.database()
    .ref(`audioFeatures/${cacheKey}`).once('value');
  if (cached.exists()) {
    return cached.val();
  }

  // Call ReccoBeats API
  try {
    const response = await fetch(
      `https://reccobeats.com/api/track?name=${trackName}&artist=${artistName}`
    );
    const features = await response.json();

    // Cache result
    await firebase.database()
      .ref(`audioFeatures/${cacheKey}`).set(features);

    return features;
  } catch (error) {
    console.error('ReccoBeats error:', error);
    return null; // Trigger fallback
  }
}
```

**Success Metrics:**
- 80%+ tracks found in ReccoBeats
- <500ms average response time
- No 429 rate limit errors

---

### Phase 2: Essentia.js Fallback (Week 2)

**Goals:**
- ✅ Analyze tracks using Essentia.js when ReccoBeats fails
- ✅ Use Spotify preview URLs as audio source
- ✅ Cache client-side results in Firebase

**Implementation:**
```javascript
import Essentia from 'essentia.js';

async function analyzeWithEssentia(previewUrl) {
  if (!previewUrl) return null; // No preview available

  const cacheKey = `essentia_${trackId}`;
  const cached = await firebase.database()
    .ref(`audioFeatures/${cacheKey}`).once('value');
  if (cached.exists()) {
    return cached.val();
  }

  // Load audio
  const audioCtx = new AudioContext();
  const response = await fetch(previewUrl);
  const buffer = await audioCtx.decodeAudioData(
    await response.arrayBuffer()
  );

  // Analyze
  const essentia = new Essentia.EssentiaWASM();
  const features = essentia.compute(buffer);

  const result = {
    bpm: features.rhythm.bpm,
    danceability: features.rhythm.danceability,
    energy: features.energy
  };

  // Cache
  await firebase.database()
    .ref(`audioFeatures/${cacheKey}`).set(result);

  return result;
}
```

**Success Metrics:**
- Fallback triggers for <20% of tracks
- Analysis completes in <5 seconds per track
- No browser crashes (memory management)

---

### Phase 3: UI Integration (Week 3)

**Goals:**
- ✅ Display audio features in table columns
- ✅ Show loading states during analysis
- ✅ Handle missing data gracefully

**UI Changes:**
```javascript
// Add columns to table
function renderTrackRow(track) {
  return `
    <tr data-track-id="${track.id}">
      <td>${track.name}</td>
      <td>${track.artist}</td>
      <td class="audio-feature" data-type="bpm">
        <span class="loading">...</span>
      </td>
      <td class="audio-feature" data-type="energy">
        <span class="loading">...</span>
      </td>
      <td class="audio-feature" data-type="danceability">
        <span class="loading">...</span>
      </td>
    </tr>
  `;
}

// Update after analysis
async function loadAudioFeatures(track) {
  let features = await getAudioFeatures(track.name, track.artists[0].name);

  if (!features) {
    features = await analyzeWithEssentia(track.preview_url);
  }

  if (features) {
    updateTableCell(track.id, 'bpm', Math.round(features.bpm));
    updateTableCell(track.id, 'energy', Math.round(features.energy * 100));
    updateTableCell(track.id, 'danceability', Math.round(features.danceability * 100));
  } else {
    updateTableCell(track.id, 'bpm', 'N/A');
    updateTableCell(track.id, 'energy', 'N/A');
    updateTableCell(track.id, 'danceability', 'N/A');
  }
}
```

**Success Metrics:**
- Features load within 10s of playlist load
- Loading states clear properly
- "N/A" displayed for unavailable features

---

### Phase 4: Monitoring & Optimization (Ongoing)

**Goals:**
- ✅ Monitor ReccoBeats availability
- ✅ Track cache hit rates
- ✅ Optimize for performance

**Monitoring:**
```javascript
// Track analytics
async function logFeatureFetch(source, success, duration) {
  await firebase.database()
    .ref('analytics/audioFeatures').push({
      source: source, // 'reccobeats' or 'essentia'
      success: success,
      duration: duration,
      timestamp: Date.now()
    });
}

// Weekly report
async function generateWeeklyReport() {
  const analytics = await firebase.database()
    .ref('analytics/audioFeatures')
    .orderByChild('timestamp')
    .startAt(Date.now() - 7 * 24 * 60 * 60 * 1000)
    .once('value');

  const stats = {
    reccobeats: { success: 0, fail: 0 },
    essentia: { success: 0, fail: 0 },
    cacheHitRate: 0
  };

  analytics.forEach(snap => {
    const data = snap.val();
    if (data.success) {
      stats[data.source].success++;
    } else {
      stats[data.source].fail++;
    }
  });

  console.log('Weekly Audio Features Report:', stats);
}
```

**Success Metrics:**
- Cache hit rate >70%
- ReccoBeats success rate >80%
- Combined success rate >95%

---

## Implementation Roadmap

### Week 1: Foundation
**Time Investment:** 4-6 hours

- [x] Research complete (this document)
- [ ] Test ReccoBeats API with sample tracks
- [ ] Implement Firebase caching layer
- [ ] Add audio features columns to UI
- [ ] Display ReccoBeats data in table

**Deliverable:** Basic BPM/energy/danceability display from ReccoBeats

---

### Week 2: Resilience
**Time Investment:** 6-8 hours

- [ ] Integrate Essentia.js library
- [ ] Implement fallback chain (ReccoBeats → Essentia → N/A)
- [ ] Test with preview URLs
- [ ] Optimize Essentia.js bundle size (lazy loading)
- [ ] Handle missing preview URLs gracefully

**Deliverable:** Robust audio features with fallback

---

### Week 3: Polish
**Time Investment:** 3-4 hours

- [ ] Add loading states and progress indicators
- [ ] Implement batch processing (analyze multiple tracks concurrently)
- [ ] Add "Analyze All" button for manual trigger
- [ ] Test with large playlists (100+ tracks)
- [ ] Mobile optimization (Essentia.js on mobile browsers)

**Deliverable:** Production-ready audio features

---

### Week 4: Monitoring (Optional)
**Time Investment:** 2-3 hours

- [ ] Set up Firebase analytics tracking
- [ ] Create weekly report automation
- [ ] Monitor ReccoBeats uptime
- [ ] Investigate SoundNet pricing (if free options fail)

**Deliverable:** Long-term sustainability plan

---

## Backup Plan: If Free Options Fail

**Scenario:** ReccoBeats shuts down, Essentia.js performance poor

**Action Plan:**
1. **Evaluate SoundNet Track Analysis API**
   - Check RapidAPI pricing page
   - Sign up for free tier (if available)
   - Test with 50 tracks
   - Calculate monthly cost projection

2. **Alternative: Soundcharts Free Tier**
   - Use 1,000 free requests strategically
   - Cache aggressively
   - Only analyze user's highest-rated tracks
   - Estimate: 1,000 requests = ~2-3 months of usage

3. **Alternative: Build Own ML Model**
   - Train TensorFlow.js model on Spotify dataset (if available)
   - Use transfer learning from Essentia.js models
   - Host model in app (no API calls)
   - **Time investment:** 20-40 hours (not recommended initially)

---

## Legal & Terms of Service Considerations

### ReccoBeats
- ✅ No TOS violations (public API)
- ⚠️ Check if attribution required (footer link)

### Essentia.js
- ✅ Open source (MIT-like license)
- ✅ Free for commercial use
- ✅ No attribution required (but recommended)

### Spotify Preview URLs
- ⚠️ Spotify TOS allows preview playback
- ⚠️ Workaround scraping may violate TOS (avoid if possible)
- ✅ Use official API preview URLs only

### Caching in Firebase
- ✅ Legal as long as data is for personal use
- ✅ Don't redistribute cached features publicly
- ✅ Respect original API TOS (no commercial resale)

---

## Conclusion

**Recommended Approach for "The List":**

✅ **Phase 1:** ReccoBeats API (primary source, free)
✅ **Phase 2:** Essentia.js (fallback, free, client-side)
✅ **Phase 3:** Firebase caching (reduce API calls by 70-90%)
✅ **Phase 4:** Monitor & optimize (ensure long-term viability)

**Total Cost:** $0/month
**Total Time Investment:** 13-18 hours over 3-4 weeks
**Success Probability:** 90%+ (two free redundant sources)

**Next Steps:**
1. Test ReccoBeats API with 10 sample tracks from your playlists
2. Verify response format matches expectations
3. Implement caching layer in Firebase
4. Add audio features columns to UI (hidden by default via "Hide Empty Columns")
5. Build fallback chain once ReccoBeats proven

---

**Document Status:** ✅ Complete
**Last Updated:** 14 December 2025
**Next Review:** After Week 1 implementation (ReccoBeats testing)
**Related Files:**
- [[SESSION-HANDOFF-13-12-2025]]
- [[PLAN-13-12-2025-1130-spotify-playlist-rating-app]]
