import csv
from datetime import datetime, timedelta

def analyze_file(file_path):
    # Assuming CSV format with headers: Name, Position, Date, Hours_Worked
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Sort data by Name and then by Date
    data.sort(key=lambda x: (x['Name'], datetime.strptime(x['Date'], '%Y-%m-%d')))

    # Analyze the data
    for i in range(len(data)-1):
        current_employee = data[i]
        next_employee = data[i+1]

        # Check for employees who worked for 7 consecutive days
        if current_employee['Name'] == next_employee['Name']:
            current_date = datetime.strptime(current_employee['Date'], '%Y-%m-%d')
            next_date = datetime.strptime(next_employee['Date'], '%Y-%m-%d')
            if (next_date - current_date).days == 6:
                print(f"{current_employee['Name']} worked for 7 consecutive days, Position: {current_employee['Position']}")

        # Check for employees with less than 10 hours between shifts (greater than 1 hour)
        current_hours = float(current_employee['Hours_Worked'])
        next_hours = float(next_employee['Hours_Worked'])
        time_between_shifts = (datetime.strptime(next_employee['Date'], '%Y-%m-%d') -
                               datetime.strptime(current_employee['Date'], '%Y-%m-%d')).total_seconds() / 3600
        if (current_employee['Name'] == next_employee['Name']) and (1 < time_between_shifts < 10):
            print(f"{current_employee['Name']} has less than 10 hours between shifts (greater than 1 hour), Position: {current_employee['Position']}")

        # Check for employees who worked for more than 14 hours in a single shift
        if current_hours > 14:
            print(f"{current_employee['Name']} worked for more than 14 hours in a single shift, Position: {current_employee['Position']}")

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    analyze_file(file_path)
