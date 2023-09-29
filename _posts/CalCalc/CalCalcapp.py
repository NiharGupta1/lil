from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('2023-09-26-CalorieCalculator.html')

@app.route('/calculate_calories', methods=['POST'])
def calculate_calories():
    try:
        age = int(request.form['age'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        gender = request.form['gender']
        activity_level = request.form['activity_level']

        # Perform your calorie calculation here based on the provided formulas
        # Replace this line with your actual calorie calculation
        def daily_calories(age, height_cm, weight_kg, gender, activity_level):
            if gender == 'male':
                bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
            elif gender == 'female':
                bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
            else:
                raise ValueError("Invalid gender")
            activity_factors = {
                'sedentary': 1.2,
                'lightly_active': 1.375,
                'moderately_active': 1.55,
                'very_active': 1.725,
                'super_active': 1.9
            }

            if activity_level not in activity_factors:
                raise ValueError("Invalid activity level")
            
            daily_calories = bmr * activity_factors[activity_level]
            return daily_calories

        result = {'daily_calories': daily_calories}
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
