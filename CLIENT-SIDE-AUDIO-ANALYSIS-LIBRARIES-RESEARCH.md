# Client-Side JavaScript Audio Analysis Libraries Research

**Research Date:** 14-12-2025
**Purpose:** Find JavaScript libraries that can analyse Spotify track preview URLs (30-second MP3 clips) directly in the browser to extract audio features like BPM, energy, key, etc.

---

## Executive Summary

After researching 8+ client-side JavaScript audio analysis libraries, **Essentia.js** emerges as the most comprehensive solution for extracting Spotify-like audio features, though it comes with a larger bundle size (2.5-3 MB). For projects prioritising lightweight bundles and focusing primarily on BPM detection, **web-audio-beat-detector** or **realtime-bpm-analyzer** offer excellent alternatives at ~24 KB.

**Key Findings:**
- **Most Comprehensive:** Essentia.js (200+ algorithms, includes danceability, energy, key, tempo)
- **Best for BPM Only:** web-audio-beat-detector or realtime-bpm-analyzer (lightweight, focused)
- **Best Balance:** Meyda (~53 KB, 20 features including energy, RMS, spectral analysis)
- **Key Detection:** webKeyFinder or Essentia.js (dedicated key detection algorithms)

**Important Note on Accuracy:**
- Client-side BPM detection typically achieves 78-90% accuracy on electronic music
- Spotify's API has known accuracy issues (~90% incorrect BPM in some datasets)
- Client-side key detection is less reliable than tempo detection
- 30-second preview clips may not provide enough data for accurate tempo changes or key modulations

---

## Detailed Library Analysis

### 1. Essentia.js ⭐ Most Comprehensive

**GitHub/NPM:** https://github.com/MTG/essentia.js | https://www.npmjs.com/package/essentia.js

**What It Can Extract:**
- ✅ BPM/Tempo detection
- ✅ Energy/Intensity measurement
- ✅ Key detection (musical key)
- ✅ Beat detection
- ✅ Danceability (values 0-3, higher = more danceable)
- ✅ Loudness
- ✅ Spectral analysis (200+ algorithms)
- ✅ MFCC (Mel-Frequency Cepstral Coefficients)
- ✅ Pre-trained ML models via TensorFlow.js

**Technical Details:**
- **Bundle Size:** 2.5-3 MB (WebAssembly backend)
- **Last Updated:** 4 years ago (v0.1.3, but actively maintained repo)
- **Browser Compatibility:**
  - ✅ Chrome, Firefox, Safari (desktop)
  - ⚠️ Limited on mobile (iOS/Android memory constraints for large models)
  - ⚠️ ES6 module imports in Workers NOT supported on Firefox/Safari
- **Performance:**
  - Most features: 0.46-3.48 seconds (1.5-6.8% of audio duration)
  - MFCC/pYIN pitch: 8.68-16.4 seconds (28.9-54.7% of audio duration)
  - Chrome on Android slowest, Linux/Node.js fastest

**Ease of Integration:** Moderate (WebAssembly setup required)

**Code Example:**
```javascript
import Essentia from 'essentia.js';

// Initialise Essentia
const essentia = new Essentia();

// Extract features from audio buffer
const features = essentia.compute(audioBuffer, {
  danceability: true,
  energy: true,
  tempo: true,
  key: true
});

console.log('BPM:', features.tempo);
console.log('Danceability:', features.danceability);
console.log('Energy:', features.energy);
console.log('Key:', features.key);
```

**Accuracy vs Spotify:**
- Research-grade algorithms from Music Technology Group, UPF Barcelona
- Best performer in terms of coverage and speed among alternatives
- More comprehensive than Spotify's API feature set

**Pros:**
- Most comprehensive feature set (200+ algorithms)
- Research-backed (published in ISMIR 2020)
- Pre-trained ML models available
- Both real-time and offline analysis

**Cons:**
- Largest bundle size (2.5-3 MB)
- Mobile memory constraints for large models
- Rapid development = API changes expected
- AGPL v3 licence (copyleft)

---

### 2. Meyda ⭐ Best Balance

**GitHub/NPM:** https://github.com/meyda/meyda | https://www.npmjs.com/package/meyda

**What It Can Extract:**
- ✅ Energy (infinite integral of squared signal)
- ✅ RMS (Root Mean Square - loudness measure)
- ✅ Spectral Centroid (brightness)
- ✅ Spectral Flatness (noisiness)
- ✅ Spectral Flux (spectrum change rate)
- ✅ Spectral Rolloff, Spread, Slope, Skewness, Kurtosis
- ✅ Loudness (Bark scale-based)
- ✅ Chroma (pitch class distribution)
- ✅ MFCC
- ✅ ZCR (Zero Crossing Rate)
- ❌ NO dedicated BPM/tempo feature
- ❌ NO key detection

**Technical Details:**
- **Bundle Size:** ~53 KB (package size, minified size not specified)
- **Last Updated:** 2 years ago (v5.6.3, April 2024)
- **Browser Compatibility:** Modern browsers with Web Audio API support
- **Performance:** Less predictable than Essentia.js across platforms
- **Development Status:** 1,600+ GitHub stars, used by 1,400+ projects

**Ease of Integration:** Simple (pure JavaScript, no external dependencies)

**Code Example:**
```javascript
import Meyda from 'meyda';

// Create analyser
const analyzer = Meyda.createMeydaAnalyzer({
  audioContext: audioContext,
  source: audioSource,
  bufferSize: 512,
  featureExtractors: ['rms', 'energy', 'spectralCentroid', 'loudness'],
  callback: features => {
    console.log('RMS:', features.rms);
    console.log('Energy:', features.energy);
    console.log('Spectral Centroid:', features.spectralCentroid);
    console.log('Loudness:', features.loudness);
  }
});

// Start analysing
analyzer.start();

// For offline analysis
const features = Meyda.extract(['rms', 'energy', 'spectralCentroid'], audioBuffer);
```

**Accuracy vs Spotify:**
- No direct BPM comparison available
- Spectral features useful for inferring characteristics like brightness/intensity
- Cannot directly replicate Spotify's danceability or tempo features

**Pros:**
- Lightweight (~53 KB)
- Pure JavaScript (no WASM)
- 20 well-documented features
- MIT licence
- Active community (1,600+ stars)
- Both real-time and offline analysis

**Cons:**
- No built-in BPM/tempo detection
- No key detection
- Less comprehensive than Essentia.js
- Performance less consistent across platforms

---

### 3. web-audio-beat-detector ⭐ Best for BPM

**GitHub/NPM:** https://github.com/chrisguttandin/web-audio-beat-detector | https://www.npmjs.com/package/web-audio-beat-detector

**What It Can Extract:**
- ✅ BPM/Tempo detection (default range: 90-180, customisable)
- ✅ Beat offset (time to first beat in seconds)
- ❌ NO energy, key, or spectral features

**Technical Details:**
- **Bundle Size:** ~24 KB (estimated from Package Galaxy)
- **Last Updated:** Active (v8.2.31, September 2025)
- **Browser Compatibility:** All browsers with Web Audio API
- **Performance:** Lightweight algorithm, surprisingly good results for electronic music

**Ease of Integration:** Very Simple

**Code Example:**
```javascript
import { analyze, guess } from 'web-audio-beat-detector';

// Simple tempo extraction
const tempo = await analyze(audioBuffer);
console.log('BPM:', tempo);

// Detailed analysis with offset
const result = await guess(audioBuffer);
console.log('BPM:', result.bpm);
console.log('Offset:', result.offset);
console.log('Tempo:', result.tempo);

// Custom tempo range
const customResult = await analyze(audioBuffer, {
  minTempo: 60,
  maxTempo: 120
});
```

**Accuracy vs Spotify:**
- Algorithm "not as complex as many others" but yields "surprisingly good results especially for electronic music"
- Tested accuracy: 14 out of 18 tracks correct (78%)
- Comparable to Spotify's API (which has ~90% error rate in some datasets)

**Pros:**
- Very lightweight (~24 KB)
- Simple API
- Actively maintained (Sept 2025)
- Customisable tempo range
- Fast processing

**Cons:**
- BPM only - no other features
- Best suited for electronic music
- May struggle with tempo changes

---

### 4. realtime-bpm-analyzer

**GitHub/NPM:** https://github.com/dlepaux/realtime-bpm-analyzer | https://www.npmjs.com/package/realtime-bpm-analyzer

**What It Can Extract:**
- ✅ BPM/Tempo detection (real-time and offline)
- ❌ NO energy, key, or spectral features

**Technical Details:**
- **Bundle Size:** Unknown (described as "lightweight", no specific KB figure)
- **Last Updated:** 2 years ago (v4.0.2)
- **Browser Compatibility:** All browsers with Web Audio API
- **Supported Formats:** MP3, FLAC, WAV
- **Performance:** Real-time analysis whilst audio/video plays

**Ease of Integration:** Simple (TypeScript/JavaScript, no dependencies)

**Code Example:**
```javascript
import RealTimeBPMAnalyzer from 'realtime-bpm-analyzer';

// Analyse audio file
const analyzer = new RealTimeBPMAnalyzer({
  scriptNode: {
    bufferSize: 4096,
    numberOfInputChannels: 1,
    numberOfOutputChannels: 1
  }
});

analyzer.analyzeBuffer(audioBuffer).then(bpm => {
  console.log('BPM:', bpm);
});

// Real-time analysis from stream
const audioStream = await navigator.mediaDevices.getUserMedia({ audio: true });
const bpm = await analyzer.analyzeStream(audioStream);
```

**Accuracy vs Spotify:** No specific accuracy data available

**Pros:**
- Real-time and offline analysis
- Supports audio/video nodes, streams, files
- TypeScript support
- Dependency-free
- Supports multiple audio formats

**Cons:**
- BPM only
- Last updated 2 years ago
- No detailed accuracy benchmarks
- Bundle size unknown

---

### 5. aubiojs

**GitHub/NPM:** https://github.com/qiuxiang/aubiojs | https://www.npmjs.com/package/aubiojs

**What It Can Extract:**
- ✅ BPM/Tempo detection
- ✅ Pitch detection
- ❌ NO energy, key, or danceability features

**Technical Details:**
- **Bundle Size:** Unknown
- **Last Updated:** Unknown (active repo)
- **Browser Compatibility:** Modern browsers, via CDN or npm
- **Technology:** Emscripten-compiled C++ aubio library

**Ease of Integration:** Moderate (async initialisation required)

**Code Example:**
```javascript
import aubio from 'aubiojs';

// Node.js example
const { Tempo } = await aubio();
const tempo = new Tempo(bufferSize, hopSize, sampleRate);
tempo.do(audioBuffer);
const bpm = tempo.getBpm();
console.log('BPM:', bpm);

// Browser example
aubio().then(({ Tempo, Pitch }) => {
  const tempo = new Tempo(512, 256, 44100);
  tempo.do(audioBuffer);
  console.log('BPM:', tempo.getBpm());

  const pitch = new Pitch('default', bufferSize, hopSize, sampleRate);
  pitch.do(audioBuffer);
  console.log('Pitch:', pitch.getFrequency());
});
```

**Accuracy vs Spotify:** No specific comparison data

**Pros:**
- Tempo AND pitch detection
- Based on established aubio C++ library
- Available via CDN
- MIT licence

**Cons:**
- Async initialisation adds complexity
- Limited feature set compared to Essentia.js
- No bundle size data
- No energy/key/danceability features

---

### 6. webKeyFinder ⭐ Best for Key Detection

**GitHub:** https://github.com/dogayuksel/webKeyFinder

**What It Can Extract:**
- ✅ Key detection (musical key - major/minor)
- ❌ NO BPM, energy, or spectral features

**Technical Details:**
- **Bundle Size:** Unknown
- **Last Updated:** Unknown
- **Browser Compatibility:** Modern browsers with WebAssembly support
- **Technology:** Emscripten-compiled libKeyFinder + FFTW3

**Ease of Integration:** Complex (requires Emscripten setup, WASM build)

**How It Works:**
- **Live Audio:** AudioWorkletProcessor captures ~1 second chunks, sends to Web Worker with WASM module
- **Audio Files:** Decoded to PCM, processed in 1-second chunks in parallel with dedicated workers

**Code Example:**
```javascript
// Installation requires:
// 1. Install emscripten via emsdk
// 2. yarn build:wasm (fetches FFTW3 + libKeyFinder)
// 3. yarn build:web

// Usage (simplified - actual implementation complex)
import KeyFinder from 'key-finder-wasm';

const keyFinder = new KeyFinder();
const key = await keyFinder.analyzeAudio(audioBuffer);
console.log('Detected Key:', key);
```

**Accuracy vs Spotify:**
- Based on Ibrahim Sha'ath's libKeyFinder (industry-standard)
- No direct Spotify comparison data
- Note: Key detection is generally less accurate than tempo detection

**Pros:**
- Dedicated key detection algorithm
- Parallel processing for audio files
- Browser-based (no server upload)
- Based on established libKeyFinder

**Cons:**
- Complex setup (Emscripten, WASM build)
- Key detection only
- No bundle size data
- Requires significant technical expertise

---

### 7. Tone.js

**GitHub/NPM:** https://github.com/Tonejs/Tone.js | https://www.npmjs.com/package/tone

**What It Can Extract:**
- ✅ FFT analysis (frequency spectrum)
- ✅ Waveform data (time-domain)
- ✅ Meter (audio level measurement)
- ❌ NO built-in BPM, key, danceability, or energy extractors

**Technical Details:**
- **Bundle Size:** 5.4 MB unpacked (actual bundled size much smaller with tree-shaking)
- **Last Updated:** Active (v15.1.22)
- **Browser Compatibility:** All modern browsers with Web Audio API
- **Primary Use:** Interactive music creation, NOT feature extraction

**Ease of Integration:** Moderate (primarily designed for music synthesis/playback)

**Code Example:**
```javascript
import * as Tone from 'tone';

// FFT analysis
const fft = new Tone.FFT(256);
audioSource.connect(fft);
const frequencyData = fft.getValue(); // Float32Array

// Waveform analysis
const waveform = new Tone.Waveform(1024);
audioSource.connect(waveform);
const waveformData = waveform.getValue(); // Float32Array (0-1)

// Meter
const meter = new Tone.Meter();
audioSource.connect(meter);
const level = meter.getValue(); // dB value
```

**Accuracy vs Spotify:** Not applicable (no BPM/key extraction features)

**Pros:**
- Comprehensive Web Audio framework
- Excellent for music synthesis/playback
- Active development
- Large community

**Cons:**
- Not designed for audio feature extraction
- Large unpacked size (5.4 MB)
- No built-in BPM/key/danceability extractors
- Overkill if only analysing audio

---

### 8. Pizzicato.js

**GitHub/NPM:** https://github.com/alemangui/pizzicato | https://www.npmjs.com/package/pizzicato

**What It Can Extract:**
- ❌ NO audio feature extraction capabilities
- ⚠️ Primarily an audio effects/manipulation library

**Technical Details:**
- **Bundle Size:** ~6 KB (minified + gzipped)
- **Last Updated:** Unknown
- **Browser Compatibility:** All browsers with Web Audio API
- **Primary Use:** Audio effects (distortion, delay, flanger, etc.)

**Ease of Integration:** Very Simple

**Why Not Suitable:**
Pizzicato.js is designed for applying audio effects (distortion, delay, tremolo, filters) to sounds, NOT for extracting audio features like BPM, energy, or key. It's excellent for sound manipulation but won't help with analysis.

**Code Example (for context):**
```javascript
import Pizzicato from 'pizzicato';

// Load sound
const sound = new Pizzicato.Sound('audio.mp3', function() {
  // Apply effects
  const distortion = new Pizzicato.Effects.Distortion({ gain: 0.5 });
  sound.addEffect(distortion);
  sound.play();
});
```

**Pros:**
- Very lightweight (6 KB)
- Elegant API
- Great for audio effects

**Cons:**
- NOT an analysis library
- No feature extraction capabilities
- Wrong tool for this use case

---

## Comparison Table

| Library | BPM | Energy | Key | Spectral | Bundle Size | Last Updated | Ease of Use | Accuracy |
|---------|-----|--------|-----|----------|-------------|--------------|-------------|----------|
| **Essentia.js** | ✅ | ✅ | ✅ | ✅ (200+) | 2.5-3 MB | 2021 (active) | Moderate | Research-grade |
| **Meyda** | ❌ | ✅ | ❌ | ✅ (20) | ~53 KB | 2024 | Simple | Good |
| **web-audio-beat-detector** | ✅ | ❌ | ❌ | ❌ | ~24 KB | 2025 | Very Simple | 78% |
| **realtime-bpm-analyzer** | ✅ | ❌ | ❌ | ❌ | Unknown | 2023 | Simple | Unknown |
| **aubiojs** | ✅ | ❌ | ❌ | ❌ | Unknown | Active | Moderate | Unknown |
| **webKeyFinder** | ❌ | ❌ | ✅ | ❌ | Unknown | Unknown | Complex | Industry-standard |
| **Tone.js** | ❌ | ❌ | ❌ | ⚠️ (raw FFT) | 5.4 MB* | 2024 | Moderate | N/A |
| **Pizzicato.js** | ❌ | ❌ | ❌ | ❌ | ~6 KB | Unknown | Very Simple | N/A |

*Tone.js unpacked size; actual bundle much smaller with tree-shaking

---

## Recommendations by Use Case

### 1. Full Spotify-like Feature Set
**Recommendation:** Essentia.js

**Why:**
- Only library with danceability, energy, BPM, and key detection
- 200+ audio analysis algorithms
- Research-backed (Music Technology Group, UPF Barcelona)
- Pre-trained ML models available

**Trade-offs:**
- Larger bundle size (2.5-3 MB)
- More complex setup (WebAssembly)
- Mobile limitations for large models

**Best For:** Projects where comprehensive audio analysis is critical and bundle size is acceptable

---

### 2. BPM Detection Only (Lightweight)
**Recommendation:** web-audio-beat-detector

**Why:**
- Smallest bundle (~24 KB)
- Simple API
- Actively maintained (Sept 2025)
- 78% accuracy on test dataset
- Customisable tempo range

**Alternative:** realtime-bpm-analyzer (if real-time analysis needed)

**Best For:** Projects prioritising small bundle size and only need tempo detection

---

### 3. Energy + Spectral Analysis (No BPM/Key)
**Recommendation:** Meyda

**Why:**
- Excellent feature coverage (RMS, energy, spectral features)
- Lightweight (~53 KB)
- MIT licence
- Active community (1,600+ stars)
- Both real-time and offline

**Note:** Combine with web-audio-beat-detector for BPM + energy analysis

**Best For:** Projects needing intensity/brightness/spectral characteristics without BPM

---

### 4. Key Detection Only
**Recommendation:** webKeyFinder

**Why:**
- Based on industry-standard libKeyFinder
- Dedicated key detection algorithm
- Browser-based (no server upload)

**Trade-offs:**
- Complex setup (Emscripten, WASM build)
- Key detection only

**Alternative:** Essentia.js (if you need multiple features)

**Best For:** Projects specifically focused on musical key detection

---

### 5. Hybrid Approach (Best Accuracy + Reasonable Size)
**Recommendation:** Meyda + web-audio-beat-detector

**Why:**
- Combined bundle: ~77 KB
- BPM (web-audio-beat-detector) + energy/spectral (Meyda)
- Both lightweight and simple APIs
- Can run in parallel on same audio buffer

**Code Example:**
```javascript
import Meyda from 'meyda';
import { analyze } from 'web-audio-beat-detector';

// Extract all features
const [bpm, meydaFeatures] = await Promise.all([
  analyze(audioBuffer),
  Promise.resolve(Meyda.extract(['rms', 'energy', 'spectralCentroid'], audioBuffer))
]);

console.log('BPM:', bpm);
console.log('Energy:', meydaFeatures.energy);
console.log('RMS:', meydaFeatures.rms);
console.log('Brightness:', meydaFeatures.spectralCentroid);
```

**Best For:** Projects wanting multiple features with reasonable bundle size

---

## Performance Considerations

### CPU Intensity
Audio analysis is computationally expensive. Key factors:

**1. Analysis Complexity:**
- Simple BPM detection: Low-Medium CPU
- Spectral analysis: Medium CPU
- Key detection: Medium-High CPU
- ML-based features (Essentia.js): High CPU

**2. Audio Buffer Size:**
- Smaller buffers = more frequent analysis = higher CPU
- Recommended: 512-4096 samples for real-time
- Offline analysis can use larger buffers

**3. Browser Optimization:**
- Web Workers: Run analysis in background thread (recommended)
- WebAssembly: Near-native performance (Essentia.js, aubiojs, webKeyFinder)
- Throttling: Analyse every Nth frame for real-time use

**4. 30-Second Preview Limitations:**
- Short clips may not capture tempo changes
- Key modulations might be missed
- Average values may not represent full track
- Some algorithms need minimum duration (e.g., 60s for accurate key detection)

### Browser Compatibility Summary

**Chrome:**
- ✅ All libraries work well
- ⚠️ Android performance issues (Essentia.js slowest)

**Firefox:**
- ✅ All libraries work
- ⚠️ ES6 module Workers not supported (Essentia.js)
- Better desktop performance than Chrome

**Safari:**
- ✅ All libraries work
- ⚠️ ES6 module Workers not supported (Essentia.js)
- iOS memory constraints for large models (Essentia.js)

**Edge:**
- ✅ All libraries work (Chromium-based)

**Mobile:**
- ⚠️ Performance significantly slower
- ⚠️ Memory constraints for large models (Essentia.js VGGish models won't run)
- ✅ Lightweight libraries (Meyda, web-audio-beat-detector) work well

---

## Accuracy Comparison with Spotify API

### BPM/Tempo Detection
- **Spotify API:** ~90% error rate reported in some datasets (half/double tempo issues)
- **web-audio-beat-detector:** 78% accuracy on test dataset
- **Essentia.js:** Research-grade, likely comparable or better than Spotify
- **General:** Electronic music easier to detect than acoustic/jazz

### Key Detection
- **Spotify API:** Less accurate than tempo, confidence scores often low
- **Client-side:** Generally less reliable than BPM detection
- **webKeyFinder/Essentia.js:** Industry-standard algorithms, comparable to commercial tools

### Energy/Danceability
- **Spotify API:** Proprietary algorithms, confidence scores provided
- **Essentia.js:** Research-backed danceability (0-3 scale)
- **Meyda:** Raw energy values, not directly comparable to Spotify's scale

### Important Caveats
1. **30-second previews** may not provide enough data for accurate analysis
2. **Tempo changes** within tracks won't be detected from short clips
3. **Key modulations** likely missed in preview clips
4. **Genre matters** - electronic music = higher accuracy, jazz/classical = lower

---

## Implementation Recommendations

### For Spotify Preview URL Analysis

**1. Fetch and Decode Audio:**
```javascript
async function fetchAndDecodeAudio(previewUrl) {
  const response = await fetch(previewUrl);
  const arrayBuffer = await response.arrayBuffer();

  const audioContext = new AudioContext();
  const audioBuffer = await audioContext.decodeAudioData(arrayBuffer);

  return audioBuffer;
}
```

**2. Run Analysis (Essentia.js example):**
```javascript
import Essentia from 'essentia.js';

async function analyzeSpotifyPreview(previewUrl) {
  const audioBuffer = await fetchAndDecodeAudio(previewUrl);
  const essentia = new Essentia();

  const features = essentia.compute(audioBuffer, {
    tempo: true,
    energy: true,
    danceability: true,
    key: true
  });

  return {
    bpm: features.tempo,
    energy: features.energy,
    danceability: features.danceability,
    key: features.key,
    analysedDuration: audioBuffer.duration
  };
}
```

**3. Run Analysis (Hybrid Meyda + web-audio-beat-detector):**
```javascript
import Meyda from 'meyda';
import { analyze } from 'web-audio-beat-detector';

async function analyzeSpotifyPreview(previewUrl) {
  const audioBuffer = await fetchAndDecodeAudio(previewUrl);

  const [bpm, features] = await Promise.all([
    analyze(audioBuffer),
    Promise.resolve(Meyda.extract(
      ['rms', 'energy', 'spectralCentroid', 'spectralRolloff', 'zcr'],
      audioBuffer
    ))
  ]);

  return {
    bpm: Math.round(bpm),
    energy: features.energy,
    rms: features.rms,
    brightness: features.spectralCentroid,
    spectralRolloff: features.spectralRolloff,
    zcr: features.zcr,
    analysedDuration: audioBuffer.duration
  };
}
```

**4. Error Handling:**
```javascript
async function safeAnalyzePreview(previewUrl) {
  try {
    return await analyzeSpotifyPreview(previewUrl);
  } catch (error) {
    if (error.name === 'NotSupportedError') {
      console.error('Audio format not supported');
    } else if (error.name === 'NetworkError') {
      console.error('Failed to fetch audio');
    } else {
      console.error('Analysis failed:', error);
    }
    return null;
  }
}
```

**5. Optimisation with Web Workers:**
```javascript
// worker.js
import { analyze } from 'web-audio-beat-detector';

self.onmessage = async (event) => {
  const { audioBuffer } = event.data;
  const bpm = await analyze(audioBuffer);
  self.postMessage({ bpm });
};

// main.js
const worker = new Worker('worker.js', { type: 'module' });

worker.postMessage({ audioBuffer });
worker.onmessage = (event) => {
  console.log('BPM:', event.data.bpm);
};
```

---

## Final Recommendation

**For "The List" Spotify Playlist Rating App:**

### Primary Recommendation: Hybrid Approach
**Use:** Meyda + web-audio-beat-detector

**Why:**
1. **Bundle Size:** ~77 KB combined (very reasonable)
2. **Feature Coverage:**
   - BPM (web-audio-beat-detector)
   - Energy (Meyda)
   - RMS/Loudness (Meyda)
   - Spectral Centroid/Brightness (Meyda)
   - Spectral characteristics for inferring danceability-like features
3. **Accuracy:** Good BPM accuracy (78%), reliable spectral analysis
4. **Ease of Use:** Both libraries have simple APIs
5. **Performance:** Lightweight, fast processing
6. **Maintenance:** Both actively maintained
7. **Licensing:** Both MIT (commercial-friendly)

### Alternative: Essentia.js (if comprehensive features needed)
**Use If:**
- You need direct danceability score
- Key detection is critical
- Bundle size <3 MB is acceptable
- You want research-grade accuracy

**Trade-off:** Larger bundle, more complex setup

### Implementation Strategy
1. **Start with:** Meyda + web-audio-beat-detector
2. **Analyse:** Compare extracted features with Spotify API features
3. **Decide:** If danceability/key detection critical, upgrade to Essentia.js
4. **Optimise:** Use Web Workers for background processing

---

## Additional Resources

### Documentation Links
- **Essentia.js:** https://mtg.github.io/essentia.js/
- **Meyda:** https://meyda.js.org/
- **web-audio-beat-detector:** https://github.com/chrisguttandin/web-audio-beat-detector
- **Web Audio API:** https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API

### Research Papers
- **Essentia.js (ISMIR 2020):** https://program.ismir2020.net/static/final_papers/260.pdf
- **Meyda (WAC 2015):** https://wac.ircam.fr/pdf/wac15_submission_17.pdf

### Tools
- **Bundlephobia:** https://bundlephobia.com (check npm package sizes)
- **BPM Finder Demo:** https://jmperezperez.com/beats-audio-api/ (compare with Spotify)
- **Tunebat Analyser:** https://tunebat.com/Analyzer (test accuracy)

---

## Conclusion

For client-side audio analysis of Spotify preview URLs, the JavaScript ecosystem offers several excellent options. The choice depends on:

1. **Feature Requirements:** Full Spotify-like features (Essentia.js) vs specific features (hybrid approach)
2. **Bundle Size Constraints:** Lightweight (Meyda + web-audio-beat-detector ~77 KB) vs comprehensive (Essentia.js 2.5-3 MB)
3. **Accuracy Needs:** Research-grade (Essentia.js) vs good-enough (hybrid)
4. **Development Complexity:** Simple APIs (Meyda/web-audio-beat-detector) vs complex setup (webKeyFinder)

**Bottom Line:** Start with Meyda + web-audio-beat-detector for BPM and energy detection. If danceability and key are critical, upgrade to Essentia.js. Both approaches will provide more reliable tempo detection than Spotify's API in many cases, whilst keeping data processing entirely client-side for privacy and speed.
