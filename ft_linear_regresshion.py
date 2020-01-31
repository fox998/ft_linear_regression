import csv
import matplotlib.pyplot as plt

def get_data(file: str) -> list:
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return [row for row in csv_reader]


if __name__ == "__main__":
    rows = get_data('data.csv')
    x = [2, 4, 6]
    y = [1, 3, 5]
    plt.plot(x, y)
    plt.show()
    #print(*rows)

