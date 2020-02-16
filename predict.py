import os
import csv
from learn import estimated_price
from learn import Theta


def get_thetas_in_csv():
    with open('thetas.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        rows = [row for row in csv_reader]
        row = rows[0]
        return Theta(float(row[0]), float(row[1]))

    return None


def main():
    try:
        theta = get_thetas_in_csv()
        mileage = int(input("Enter mileage : "))
        if (mileage < 0):
            print("Mileage must be bigger than 0")
        else:
            print(f"Estimated price {int(estimated_price(mileage, theta))}$")
    except:
        print("Error with thetas.csv or entered mileage")

if __name__ == "__main__":
    main()