import csv
from datetime import datetime

def selection_sort_by_date(csv_file, date_column_index):

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = list(reader)

    for row in data:
        row[date_column_index] = datetime.strptime(row[date_column_index])

    for i in range(len(data)):
        min_index = 1
        for j in range(i + 1, len(data)):
            if data[j] [date_column_index] < data[min_index] [date_column_index]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]

    for row in data:
        row[date_column_index] = row[date_column_index].strftime('%b-%d')

    return header, data

if __name__ == '__main2__':
    csv_file = '/Users/q.gaffney/Lab-4/Resources/budget_data.csv'
    date_column_index = 2

    header, sorted_data = selection_sort_by_date(csv_file, date_column_index)

    with open('select_sort_budget', w, newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(sorted_data)

