// Username Management for "The List"
// Handles username selection, storage, and switching

(function() {
  'use strict';

  // Get current username from localStorage
  window.getCurrentUsername = function() {
    return localStorage.getItem('the-list-username') || null;
  };

  // Set username in localStorage
  window.setUsername = function(username) {
    localStorage.setItem('the-list-username', username);
    updateUsernameDisplay();
  };

  // Clear username (logout)
  window.clearUsername = function() {
    localStorage.removeItem('the-list-username');
  };

  // Update username display in UI
  function updateUsernameDisplay() {
    const username = getCurrentUsername();
    const displayElement = document.getElementById('current-user-display');
    if (displayElement && username) {
      displayElement.textContent = username;
      displayElement.style.display = 'inline';
    }
  }

  // Show username picker modal
  window.showUsernamePicker = function() {
    const modal = document.getElementById('username-modal');
    if (modal) {
      modal.style.display = 'flex';
      const input = document.getElementById('username-input');
      if (input) {
        input.focus();
      }
    }
  };

  // Hide username picker modal
  window.hideUsernamePicker = function() {
    const modal = document.getElementById('username-modal');
    if (modal) {
      modal.style.display = 'none';
    }
  };

  // Handle username submission
  window.submitUsername = function() {
    const input = document.getElementById('username-input');
    const error = document.getElementById('username-error');

    if (!input) return;

    const username = input.value.trim();

    // Validate username
    if (username.length === 0) {
      if (error) {
        error.textContent = 'Please enter a username';
        error.style.display = 'block';
      }
      return;
    }

    if (username.length < 2) {
      if (error) {
        error.textContent = 'Username must be at least 2 characters';
        error.style.display = 'block';
      }
      return;
    }

    if (username.length > 20) {
      if (error) {
        error.textContent = 'Username must be less than 20 characters';
        error.style.display = 'block';
      }
      return;
    }

    // Save username
    setUsername(username);
    hideUsernamePicker();

    // Trigger any callback if set
    if (window.onUsernameSet) {
      window.onUsernameSet(username);
    }
  };

  // Initialize username system on page load
  window.initializeUsernameSystem = function() {
    // Add event listener for username form
    const form = document.getElementById('username-form');
    if (form) {
      form.addEventListener('submit', function(e) {
        e.preventDefault();
        submitUsername();
      });
    }

    // Add event listener for switch user button
    const switchBtn = document.getElementById('switch-user-btn');
    if (switchBtn) {
      switchBtn.addEventListener('click', function(e) {
        e.preventDefault();
        showUsernamePicker();
      });
    }

    // Check if username exists, if not show picker
    const username = getCurrentUsername();
    if (!username) {
      // Show picker after a short delay to let page load
      setTimeout(showUsernamePicker, 500);
    } else {
      updateUsernameDisplay();
    }
  };

  // Handle Enter key in username input
  document.addEventListener('DOMContentLoaded', function() {
    const input = document.getElementById('username-input');
    if (input) {
      input.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
          e.preventDefault();
          submitUsername();
        }
      });
    }
  });

})();
