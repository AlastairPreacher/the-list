// Ratings and Comments System for "The List"
// Handles rendering and interaction for track ratings and comments

(function() {
  'use strict';

  // Render 5-star rating display with clickable stars
  window.renderStarRating = function(playlistId, trackId, currentRating, username) {
    const stars = [];
    for (let i = 1; i <= 5; i++) {
      const filled = i <= currentRating;
      const starClass = filled ? 'star-filled' : 'star-empty';
      stars.push(`<span class="star ${starClass}" data-rating="${i}" data-playlist="${playlistId}" data-track="${trackId}">★</span>`);
    }
    return `<div class="star-rating" data-username="${username}">${stars.join('')}</div>`;
  };

  // Render rating display with user ratings and average
  window.renderRatingCell = function(playlistId, trackId, ratingsData) {
    const username = getCurrentUsername();
    if (!username) return '<span class="no-user">Set username first</span>';

    const { ratings, average } = ratingsData;
    const myRating = ratings[username] || 0;

    // Get all other users' ratings
    const otherUsers = Object.keys(ratings).filter(u => u !== username);
    const otherRatingsHTML = otherUsers.map(u => {
      return `<div class="user-rating"><span class="username-label">${u}:</span> ${renderStarRating(playlistId, trackId, ratings[u], u)}</div>`;
    }).join('');

    // My rating (editable)
    const myRatingHTML = `
      <div class="user-rating my-rating">
        <span class="username-label">You:</span>
        ${renderStarRating(playlistId, trackId, myRating, username)}
      </div>
    `;

    // Average rating
    const avgHTML = average > 0 ? `<div class="avg-rating"><strong>Avg: ${average}⭐</strong></div>` : '';

    return `
      <div class="rating-container">
        ${myRatingHTML}
        ${otherRatingsHTML}
        ${avgHTML}
      </div>
    `;
  };

  // Render comments cell
  window.renderCommentsCell = function(playlistId, trackId, comments) {
    const username = getCurrentUsername();
    if (!username) return '<span class="no-user">Set username first</span>';

    // Render existing comments
    const commentsHTML = comments.map(comment => {
      const date = new Date(comment.timestamp).toLocaleDateString();
      const isMyComment = comment.username === username;
      const commentClass = isMyComment ? 'comment my-comment' : 'comment';

      return `
        <div class="${commentClass}">
          <span class="comment-username">${comment.username}:</span>
          <span class="comment-text">${escapeHtml(comment.text)}</span>
          <span class="comment-date">${date}</span>
        </div>
      `;
    }).join('');

    // Add comment input
    const inputHTML = `
      <div class="comment-input-container">
        <input type="text"
               class="comment-input"
               placeholder="Add a comment..."
               data-playlist="${playlistId}"
               data-track="${trackId}" />
        <button class="comment-submit-btn"
                data-playlist="${playlistId}"
                data-track="${trackId}">
          💬
        </button>
      </div>
    `;

    return `
      <div class="comments-container">
        ${commentsHTML}
        ${inputHTML}
      </div>
    `;
  };

  // Handle star click
  window.handleStarClick = function(starElement) {
    const rating = parseInt(starElement.getAttribute('data-rating'));
    const playlistId = starElement.getAttribute('data-playlist');
    const trackId = starElement.getAttribute('data-track');
    const username = getCurrentUsername();

    if (!username) {
      alert('Please set your username first');
      showUsernamePicker();
      return;
    }

    // Save rating to Firebase
    saveRating(playlistId, trackId, username, rating)
      .then(() => {
        // Reload ratings for this track
        return loadRatings(playlistId, trackId);
      })
      .then((ratingsData) => {
        // Update the cell
        const cell = starElement.closest('td');
        if (cell) {
          cell.innerHTML = renderRatingCell(playlistId, trackId, ratingsData);
          attachRatingEventListeners(cell);
        }
      })
      .catch((error) => {
        console.error('Error saving rating:', error);
        alert('Failed to save rating. Please try again.');
      });
  };

  // Handle comment submission
  window.handleCommentSubmit = function(submitBtn) {
    const playlistId = submitBtn.getAttribute('data-playlist');
    const trackId = submitBtn.getAttribute('data-track');
    const username = getCurrentUsername();

    if (!username) {
      alert('Please set your username first');
      showUsernamePicker();
      return;
    }

    const input = submitBtn.previousElementSibling;
    if (!input) return;

    const commentText = input.value.trim();
    if (commentText.length === 0) {
      alert('Please enter a comment');
      return;
    }

    // Save comment to Firebase
    saveComment(playlistId, trackId, username, commentText)
      .then(() => {
        // Clear input
        input.value = '';
        // Reload comments for this track
        return loadComments(playlistId, trackId);
      })
      .then((comments) => {
        // Update the cell
        const cell = submitBtn.closest('td');
        if (cell) {
          cell.innerHTML = renderCommentsCell(playlistId, trackId, comments);
          attachCommentEventListeners(cell);
        }
      })
      .catch((error) => {
        console.error('Error saving comment:', error);
        alert('Failed to save comment. Please try again.');
      });
  };

  // Attach event listeners to rating stars in a container (legacy - kept for compatibility)
  window.attachRatingEventListeners = function(container) {
    // No longer needed - event delegation handles this
    // Kept as empty function to avoid breaking existing code
  };

  // Attach event listeners to comment inputs in a container (legacy - kept for compatibility)
  window.attachCommentEventListeners = function(container) {
    // No longer needed - event delegation handles this
    // Kept as empty function to avoid breaking existing code
  };

  // Escape HTML to prevent XSS
  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Initialize ratings and comments system with event delegation
  window.initializeRatingsCommentsSystem = function() {
    console.log('Initializing ratings and comments system with event delegation...');

    // Use event delegation - attach ONE listener to document that catches all star clicks
    // This works even when DataTables dynamically updates cells
    document.addEventListener('click', function(e) {
      // Check if clicked element is a star
      if (e.target.classList.contains('star')) {
        console.log('Star clicked:', e.target);
        handleStarClick(e.target);
      }

      // Check if clicked element is a comment submit button
      if (e.target.classList.contains('comment-submit-btn')) {
        console.log('Comment button clicked:', e.target);
        handleCommentSubmit(e.target);
      }
    });

    // Handle Enter key in comment inputs
    document.addEventListener('keypress', function(e) {
      if (e.key === 'Enter' && e.target.classList.contains('comment-input')) {
        e.preventDefault();
        const submitBtn = e.target.nextElementSibling;
        if (submitBtn && submitBtn.classList.contains('comment-submit-btn')) {
          console.log('Comment submitted via Enter key');
          handleCommentSubmit(submitBtn);
        }
      }
    });

    console.log('Ratings and comments system initialized with event delegation');
  };

})();
