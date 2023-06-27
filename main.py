import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

int_rates = []
rps = []
ep_int_rates = []

def calculate_rate(years):
    int_rate = 0
    counter = 0
    for rate in int_rates:
        int_rate += rate
        counter += 1
        if counter == years:
            break
    int_rate = float(int_rate/years)
    int_rate += rps[years-1]
    return int_rate

def read_input():
    years = int(input("Enter the number of years for the yield curve model: "))
    count = 0
    while count < years:
        if count == 0:
            rate = float(input("One-year interest rate for year 1: "))
            rp = float(input("Risk premium for year 1: "))
            int_rates.append(rate)
            rps.append(rp)
        else:
            rate = float(input(("Expected one-year interest rate for year ") + str(count+1) + ": "))
            rp = float(input(("Risk premium for year ") + str(count+1) + ": "))
            int_rates.append(rate)
            rps.append(rp)
        count += 1

def plot_rates():
    read_input()
    years = len(rps)
    x_axis = []
    for i in range(years):
        ep_int_rates.append(calculate_rate(i+1))
        x_axis.append(i+1)

    plt.plot(x_axis,ep_int_rates)
    plt.xlabel('Years')
    plt.xlim([0,years+1])
    plt.ylim([0,max(ep_int_rates)+1])
    plt.ylabel('Expected interest rate')
    plt.title('Expected interest rate for each year under the Expectations Hypothesis')
    plt.show()

plot_rates()






