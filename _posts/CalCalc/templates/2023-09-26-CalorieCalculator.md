---
permalink: /caloriecalculator
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calorie Calculator</title>
    <script src="{{ url_for('static', filename='CalCalcscript.js') }}"></script>
</head>
<body>
    <h1>Calorie Calculator</h1>
    <form id="calorie-form">
        <label for="age">Age (years):</label>
        <input type="number" id="age" name="age" required><br><br>
        <label for="height">Height (cm):</label>
        <input type="number" id="height" name="height" required><br><br>
        <label for="weight">Weight (kg):</label>
        <input type="number" id="weight" name="weight" required><br><br>
        <label for="gender">Gender:</label>
        <select id="gender" name="gender">
            <option value="male">Male</option>
            <option value="female">Female</option>
        </select><br><br>
        <label for="activity-level">Activity Level:</label>
        <select id="activity-level" name="activity-level">
            <option value="sedentary">Sedentary</option>
            <option value="lightly_active">Lightly Active</option>
            <option value="moderately_active">Moderately Active</option>
            <option value="very_active">Very Active</option>
            <option value="super_active">Super Active</option>
        </select><br><br>
        <button type="button" id="calculate-button">Calculate</button>
    </form>
    <div id="result"></div>
</body>
</html>
