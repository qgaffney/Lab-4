import csv

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def sort_csv(filename, sort_function, column_index):
    data = read_csv(filename)
    header = data[0]
    data = data[1:]

    data.sort(key=lambda row: row[column_index])

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

if __name__ == "__main__":
    filename = "/Users/q.gaffney/Lab-4/Lab 4/Resources/budget_data.csv"
    column_index = 1

    sort_csv(filename, selection_sort, column_index)

    sort_csv(filename, insertion_sort, column_index)