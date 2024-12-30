from flask import Flask, render_template, request, redirect, url_for
import openpyxl
import os

app = Flask(__name__)

# Ensure the Excel file exists
DATA_FILE = "fitness_data.xlsx"
if not os.path.exists(DATA_FILE):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Fitness Log"
    sheet.append(["Name", "Date", "Week Number", "Exercise", "Set", "Reps", "Weight", "Total Weight"])
    workbook.save(DATA_FILE)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Gather data from the form
        name = request.form['name']
        date = request.form['date']
        week_number = request.form['week_number']
        exercises = int(request.form['exercises'])

        # Open the Excel workbook
        workbook = openpyxl.load_workbook(DATA_FILE)
        sheet = workbook["Fitness Log"]

        total_workout_weight = 0

        # Process exercises
        for i in range(1, exercises + 1):
            exercise_name = request.form[f'exercise_name_{i}']
            sets = int(request.form[f'sets_{i}'])
            
            for s in range(1, sets + 1):
                reps = int(request.form[f'reps_{i}_{s}'])
                weight = request.form.get(f'weight_{i}_{s}', 0)

                if weight:
                    weight = float(weight)
                    total_weight = reps * weight
                    total_workout_weight += total_weight
                else:
                    total_weight = 0

                # Append to Excel sheet
                sheet.append([name, date, week_number, exercise_name, s, reps, weight, total_weight])

        # Save the workbook
        workbook.save(DATA_FILE)

        return redirect(url_for('success', total_workout_weight=total_workout_weight))

    return render_template('index.html')

@app.route('/success')
def success():
    total_workout_weight = request.args.get('total_workout_weight', 0)
    return f"Workout logged successfully! Total weight moved: {total_workout_weight} lbs."

if __name__ == '__main__':
    app.run(debug=True)
