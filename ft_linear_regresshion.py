
#! C:\Users\andri\AppData\Local\Microsoft\Windows\python.exe

# Windows - ~\AppData\Local\Microsoft\Windows\python.exe
# Mac - /usr/bin/env python

import os
import matplotlib.pyplot as plt

class Theta:
    def __init__(self, zero = 0, one = 0):
        self.zero = float(zero)
        self.one = float(one)


def estimated_price(mileage, theta0, theta1):
    result = float(theta0 + (theta1 * mileage))
    return result


def J_theta0(theta0, theta1, mileage, price):
    result = 0
    for i in range(len(mileage)):
        result += (estimated_price(mileage[i], theta0, theta1) - float(price[i]))
    return float(result)


def J_theta1(theta0, theta1, mileage, price):
    result = 0
    for i in range(len(mileage)):
        result += (estimated_price(mileage[i], theta0, theta1) - float(price[i])) * float(mileage[i])
    return float(result)

def derivee(theta0, theta1, mileage, price):
    tmpt0 = 0
    tmpt1 = 0
    m = len(mileage)
    learningrate = 0.1
    derivee0 = J_theta0(theta0, theta1, mileage, price)
    derivee1 = J_theta1(theta0, theta1, mileage, price)
    tmpt0 = theta0 - (learningrate * ((1.0/m) * derivee0))
    tmpt1 = theta1 - (learningrate * ((1.0/m) * derivee1))
    return (tmpt0, tmpt1)

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

def gradient_descent(mileage, price):
    derive_prev = 0
    theta0 = 0
    theta1 = 0    
    while (derive_prev != J_theta0(theta0, theta1, mileage, price)):
        derive_prev = J_theta0(theta0, theta1, mileage, price)
        [new_theta0, new_theta1] = derivee(theta0, theta1, mileage, price)
        theta0 = new_theta0
        theta1 = new_theta1    
    return(theta0, theta1)

def get_data_from_training_set():
    mileage = []
    price = []
    with open("data.csv", 'r') as f:
        for index, line in enumerate(f):
            if index != 0:
                table = line.rstrip('\n').split(',')
                try:
                    mileage.append(float(table[0]))
                    price.append(float(table[1]))
                except ValueError:
                    print("Dataset is wrong.")
                    return (0, 0)
    return (mileage, price)

def mean_normalization(liste):
    liste2 = []
    for x in range(len(liste)):
        liste2.append(liste[x] / max(liste))
    return liste2

def main():
    [mileage, price] = get_data_from_training_set()
    if mileage == 0 and price == 0:
        return 0
    mileage2 = mean_normalization(mileage)
    price2 = mean_normalization(price)

    t = gradient_descent(mileage2, price2)
    theta = Theta( t[0], t[1] )
    theta.zero *= max(price)
    theta.one *= (max(price) / max(mileage))
    
    predicted_price = [ estimated_price(km, theta.zero, theta.one) for km in list(mileage) ]
    show_plot(mileage, predicted_price, price)
    keep_thetas_in_csv(theta.zero, theta.one)


if __name__ == "__main__":
    main()

