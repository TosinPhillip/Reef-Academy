function openSignInPopup(url) {
  // Define popup window features (width, height, position, etc.)
  const popupWidth = 500;
  const popupHeight = 600;
  const left = (screen.width / 2) - (popupWidth / 2);
  const top = (screen.height / 2) - (popupHeight / 2);

  // Open the window
  window.open(
    url,
    'signInPopup',
    `width=<span class="math-inline">\{popupWidth\},height\=</span>{popupHeight},top=<span class="math-inline">\{top\},left\=</span>{left},resizable=yes,scrollbars=yes`
  );
}


// Get modal elements
const signInModal = document.getElementById('signInModal');
const signInOverlay = document.getElementById('signInOverlay');
// Find your Sign In link/button - *** YOU NEED TO ADD id="signInTrigger" to it ***
const signInTrigger = document.getElementById('signInTrigger'); 
const closeModalBtn = document.querySelector('#signInModal .modal-close-btn'); // Assumes only one modal for simplicity

// Function to open the modal
function openSignInModal() {
  if (signInModal && signInOverlay) {
    signInOverlay.style.display = 'block';
    signInModal.style.display = 'block';
    document.body.classList.add('modal-open'); // Add class for background effects/scroll lock
  }
}

// Function to close the modal
function closeSignInModal() {
  if (signInModal && signInOverlay) {
    signInOverlay.style.display = 'none';
    signInModal.style.display = 'none';
    document.body.classList.remove('modal-open'); // Remove background effect class
  }
}

// --- Event Listeners ---

// Listener for the Sign In link/button
if (signInTrigger) {
  signInTrigger.addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default link behavior
    openSignInModal();
  });
} else {
    console.error("Sign-in trigger element with ID 'signInTrigger' not found.");
}


// Listener for the close button inside the modal
// (We added onclick="closeSignInModal()" directly to the button in HTML,
// but adding a listener here is another way)
// if (closeModalBtn) {
//   closeModalBtn.addEventListener('click', closeSignInModal);
// }

// Listener for clicks on the overlay (to close the modal)
if (signInOverlay) {
  signInOverlay.addEventListener('click', closeSignInModal);
}

// Optional: Close modal on pressing the Escape key
document.addEventListener('keydown', function(event) {
    if (event.key === "Escape" && signInModal.style.display === 'block') {
        closeSignInModal();
    }
});