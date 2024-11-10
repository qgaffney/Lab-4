import csv
from datetime import datetime

def selection_sort(data, key):
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j][key] < data[min_index][key]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]

def insertion_sort(data, key):
    for i in range(1, len(data)):
        key_item = data[i][key]
        j = i - 1
        while j >= 0 and data[j][key] > key_item:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = data[i]

def sort_csv_date(csv_file, date_field, sort_method = 'selection'):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

        for row in data:
            row[date_field] = datetime.strptime(row[date_field], '%b-%d')

        if sort_method == 'selection':
            selection_sort(data, date_field)
        elif sort_method == 'insertion':
            insertion_sort(data, date_field)
        else:
            raise ValueError("Invalid. Select 'selection' or 'insertion'.")
        
        for row in data:
            row[date_field] = row[date_field].strftime('%b-%d')

    with open('sorted_' + csv_file, 'w', newline = '') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__':
    csv_file = '/Users/q.gaffney/Lab-4/Resources/budget_data.csv'
    date_field = 'Date'
    sort_csv_date(csv_file, date_field, 'insertion')