// Firebase Configuration and Initialization for "The List"
// This file handles Firebase setup and provides helper functions

// Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyA2yc4et1IdF879uff_TT508Ti6tmoNOFE",
  authDomain: "the-list-13e1c.firebaseapp.com",
  databaseURL: "https://the-list-13e1c-default-rtdb.firebaseio.com",
  projectId: "the-list-13e1c",
  storageBucket: "the-list-13e1c.firebasestorage.app",
  messagingSenderId: "971193044084",
  appId: "1:971193044084:web:af363f93be00cb59d79521"
};

// Global Firebase references (will be set once modules load)
let firebaseApp = null;
let database = null;
let auth = null;
let firebaseRef = null;
let firebaseSet = null;
let firebaseGet = null;
let firebaseOnValue = null;

// Initialize Firebase when modules are loaded
window.initializeFirebase = function() {
  return import('https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js')
    .then((firebaseModule) => {
      return Promise.all([
        import('https://www.gstatic.com/firebasejs/10.7.1/firebase-database.js'),
        import('https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js')
      ])
        .then(([databaseModule, authModule]) => {
          // Initialize Firebase app
          firebaseApp = firebaseModule.initializeApp(firebaseConfig);

          // Get database reference
          database = databaseModule.getDatabase(firebaseApp);

          // Get auth reference
          auth = authModule.getAuth(firebaseApp);

          // Store module functions globally
          firebaseRef = databaseModule.ref;
          firebaseSet = databaseModule.set;
          firebaseGet = databaseModule.get;
          firebaseOnValue = databaseModule.onValue;

          console.log("Firebase initialized successfully");

          // Sign in anonymously (required for security rules)
          return authModule.signInAnonymously(auth)
            .then(() => {
              console.log("✅ Signed in anonymously to Firebase");
              return true;
            })
            .catch((error) => {
              console.error("❌ Error signing in anonymously:", error);
              // Still return true - app can function without auth in emergency
              return true;
            });
        });
    })
    .catch((error) => {
      console.error("Error initializing Firebase:", error);
      return false;
    });
};

// Helper function to save rating to Firebase
window.saveRating = function(playlistId, trackId, username, rating) {
  if (!database || !firebaseRef || !firebaseSet) {
    console.error("Firebase not initialized");
    return Promise.reject("Firebase not initialized");
  }

  const ratingPath = `playlists/${playlistId}/tracks/${trackId}/ratings/${username}`;
  const ratingRef = firebaseRef(database, ratingPath);

  return firebaseSet(ratingRef, rating)
    .then(() => {
      // Calculate and save average
      return updateAverageRating(playlistId, trackId);
    });
};

// Helper function to save comment to Firebase
window.saveComment = function(playlistId, trackId, username, commentText) {
  if (!database || !firebaseRef || !firebaseSet) {
    console.error("Firebase not initialized");
    return Promise.reject("Firebase not initialized");
  }

  const commentsPath = `playlists/${playlistId}/tracks/${trackId}/comments`;
  const commentsRef = firebaseRef(database, commentsPath);

  return firebaseGet(commentsRef)
    .then((snapshot) => {
      const comments = snapshot.val() || [];
      const newComment = {
        username: username,
        text: commentText,
        timestamp: Date.now()
      };

      comments.push(newComment);
      return firebaseSet(commentsRef, comments);
    });
};

// Helper function to load ratings for a track
window.loadRatings = function(playlistId, trackId) {
  if (!database || !firebaseRef || !firebaseGet) {
    return Promise.resolve({ ratings: {}, average: 0 });
  }

  const ratingsPath = `playlists/${playlistId}/tracks/${trackId}/ratings`;
  const ratingsRef = firebaseRef(database, ratingsPath);

  return firebaseGet(ratingsRef)
    .then((snapshot) => {
      const ratings = snapshot.val() || {};
      const average = calculateAverage(Object.values(ratings));
      return { ratings, average };
    });
};

// Helper function to load comments for a track
window.loadComments = function(playlistId, trackId) {
  if (!database || !firebaseRef || !firebaseGet) {
    return Promise.resolve([]);
  }

  const commentsPath = `playlists/${playlistId}/tracks/${trackId}/comments`;
  const commentsRef = firebaseRef(database, commentsPath);

  return firebaseGet(commentsRef)
    .then((snapshot) => {
      return snapshot.val() || [];
    });
};

// Calculate average rating
function calculateAverage(ratings) {
  if (!ratings || ratings.length === 0) return 0;
  const sum = ratings.reduce((a, b) => a + b, 0);
  return (sum / ratings.length).toFixed(1);
}

// Update average rating in Firebase
function updateAverageRating(playlistId, trackId) {
  const ratingsPath = `playlists/${playlistId}/tracks/${trackId}/ratings`;
  const avgPath = `playlists/${playlistId}/tracks/${trackId}/average`;
  const ratingsRef = firebaseRef(database, ratingsPath);
  const avgRef = firebaseRef(database, avgPath);

  return firebaseGet(ratingsRef)
    .then((snapshot) => {
      const ratings = snapshot.val() || {};
      const average = calculateAverage(Object.values(ratings));
      return firebaseSet(avgRef, average);
    });
}
