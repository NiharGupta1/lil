
document.addEventListener('DOMContentLoaded', function() {
    const calculateButton = document.getElementById('calculate-button');
    calculateButton.addEventListener('click', calculateCalories);
});

function calculateCalories() {
    const age = parseFloat(document.getElementById('age').value);
    const height = parseFloat(document.getElementById('height').value);
    const weight = parseFloat(document.getElementById('weight').value);
    const gender = document.getElementById('gender').value;
    const activityLevel = document.getElementById('activity-level').value;

    // Send a POST request to the backend for calorie calculation
    fetch('/calculate_calories', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `age=${age}&height=${height}&weight=${weight}&gender=${gender}&activity_level=${activityLevel}`,
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `Your daily calorie maintenance is: ${data.daily_calories.toFixed(2)} calories`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}