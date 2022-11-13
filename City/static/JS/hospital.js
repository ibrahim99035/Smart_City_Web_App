let brainAction = document.getElementById('brain_span');
let brainTarget = document.getElementById('brainTarget');

let breastAction = document.getElementById('breast_span');
let breastTarget = document.getElementById('breastTarget');

let deafultDiv = document.getElementById('deafult');


brainAction.addEventListener('click', () => {
    breastTarget.style.display = 'none';
    deafultDiv.style.display = 'none';
    brainTarget.style.display = 'block'
});

breastAction.addEventListener('click', () => {
    breastTarget.style.display = 'block';
    deafultDiv.style.display = 'none';
    brainTarget.style.display = 'none'
});
