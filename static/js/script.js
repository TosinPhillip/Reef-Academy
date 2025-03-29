// Get the pop-out button and container
const popOutBtn = document.getElementById('pop-out-btn');
const popOutContainer = document.getElementById('pop-out-container');

// Event Listener to the button
popOutBtn.addEventListener('click', () =>{
    //Toggle the display of the pop-out container
    popOutBtn.style.display = 'block';
});