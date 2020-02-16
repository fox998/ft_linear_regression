
#! C:\Users\andri\AppData\Local\Microsoft\Windows\python.exe

# Windows - ~\AppData\Local\Microsoft\Windows\python.exe
# Mac - /usr/bin/env python

import os
import csv
import matplotlib.pyplot as plt

class Theta:
    def __init__(self, zero = 0, one = 0):
        self.zero = float(zero)
        self.one = float(one)


class Data:
    def __init__(self, mileage  = [], price = []):
        self.mileage = mileage
        self.price = price

    def is_valid(self) -> bool:
        return self.mileage != 0 and self.price != 0


def estimated_price(mileage, theta : Theta):
    result = float(theta.zero + (theta.one * mileage))
    return result


def compute_theta0_sum(theta : Theta, data : Data):
    result = 0
    for mileage, price in zip(data.mileage, data.price):
        result += (estimated_price(mileage, theta) - float(price))
    return float(result)


def compute_theta1_sum(theta : Theta, data : Data):
    result = 0
    for mileage, price in zip(data.mileage, data.price):
        result += (estimated_price(mileage, theta) - float(price)) * float(mileage)
    return float(result)


def compute_theta(theta : Theta, data: Data):
    theta0_sum = compute_theta0_sum(theta, data)
    theta1_sum = compute_theta1_sum(theta, data)

    learningrate = 0.1
    m = len(data.mileage)
    tmp_t0 = theta.zero - (learningrate * (1.0/m) * theta0_sum)
    tmp_t1 = theta.one - (learningrate * (1.0/m) * theta1_sum)
    
    return Theta(tmp_t0, tmp_t1)

def show_plot(mileage, mse, price):
    plt.plot(mileage, mse)
    plt.scatter(mileage, price, s=10)
    plt.xlabel("mileage")
    plt.ylabel("price")
    plt.show()

def keep_thetas_in_csv(theta: Theta) -> None:
    file = open("thetas.csv", "w")
    file.write(str(theta.zero) + "," + str(theta.one))
    file.close()

def gradient_descent(data : Data):
    theta = Theta(0, 0)
    prev_theta0_sum = 0
    cur_theta0_sum = compute_theta0_sum(theta, data)

    while prev_theta0_sum != cur_theta0_sum:
        prev_theta0_sum = cur_theta0_sum
        theta = compute_theta(theta, data)
        cur_theta0_sum = compute_theta0_sum(theta, data)

    return theta


def get_data_from_training_set():
    mileage = []
    price = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        rows = [row for row in csv_reader][1:] # cip coloms names
        for row in rows:
            mileage.append(float(row[0]))
            price.append(float(row[1]))

    return Data(mileage, price)


def normalize_values(in_list):
    max_in_value = max(in_list)
    out_list = [ value / max_in_value for value in in_list]
    return out_list


def normalize_data(data: Data) -> Data:
    mileage = normalize_values(data.mileage)
    price = normalize_values(data.price)
    return Data(mileage, price)

def main():
    data = get_data_from_training_set()
    if not data.is_valid():
        return 0

    theta = gradient_descent(normalize_data(data))
    theta.zero *= max(data.price)
    theta.one *= (max(data.price) / max(data.mileage))

    keep_thetas_in_csv(theta)

    predicted_price = [ estimated_price(km, theta) for km in data.mileage]
    show_plot(data.mileage, predicted_price, data.price)


if __name__ == "__main__":
    try:
        main()
    except expression as ex:
        print('Wrong input data')

