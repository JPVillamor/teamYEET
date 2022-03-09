
const btnViewAll = document.querySelector('#view_all');
const btnForce = document.querySelector('#force');
const btnSound = document.querySelector('#sound');
const btnTemperature = document.querySelector('#temperature');
const btnLight = document.querySelector('#light');
const btnVibration = document.querySelector('#vibration');

// Change color of button when clicked on
// NEED TO SOMEHOW SAVE IF BUTTON HAS BEEN CLICKED ON TO DETERMINE WHAT GRAPHS ARE DISPLAYED!!!


btnViewAll.addEventListener('click', function onClick(event) {
    const backgroundColor = btnViewAll.style.backgroundColor;

    if (backgroundColor === 'green') {
        btnViewAll.style.backgroundColor = 'gray';
    }
    else {
        btnViewAll.style.backgroundColor = 'green'
    }
});


btnForce.addEventListener('click', function onClick(event) {
    const backgroundColor = btnForce.style.backgroundColor;
    if (backgroundColor === 'green') {
        btnForce.style.backgroundColor = 'gray';
    }
    else {
        btnForce.style.backgroundColor = 'green'
    }
});

btnSound.addEventListener('click', function onClick(event) {
    const backgroundColor = btnSound.style.backgroundColor;
    if (backgroundColor === 'green') {
        btnSound.style.backgroundColor = 'gray';
    }
    else {
        btnSound.style.backgroundColor = 'green'
    }
});

btnTemperature.addEventListener('click', function onClick(event) {
    const backgroundColor = btnTemperature.style.backgroundColor;
    if (backgroundColor === 'green') {
        btnTemperature.style.backgroundColor = 'gray';
    }
    else {
        btnTemperature.style.backgroundColor = 'green'
    }
});

btnLight.addEventListener('click', function onClick(event) {
    const backgroundColor = btnLight.style.backgroundColor;
    if (backgroundColor === 'green') {
        btnLight.style.backgroundColor = 'gray';
    }
    else {
        btnLight.style.backgroundColor = 'green'
    }
});

btnVibration.addEventListener('click', function onClick(event) {
    const backgroundColor = btnVibration.style.backgroundColor;
    if (backgroundColor === 'green') {
        btnVibration.style.backgroundColor = 'gray';
    }
    else {
        btnVibration.style.backgroundColor = 'green'
    }
});


//btnForce.addEventListener('click', () => btnForce.style.backgroundColor = '#50b733')
//btnSound.addEventListener('click', () => btnSound.style.backgroundColor = '#337ab7')
//btnTemperature.addEventListener('click', () => btnTemperature.style.backgroundColor = '#337ab7')
//btnLight.addEventListener('click', () => btnLight.style.backgroundColor = '#337ab7')
//btnVibration.addEventListener('click', () => btnVibration.style.backgroundColor = '#337ab7')
