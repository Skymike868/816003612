from execute.invest import begin
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab


def simulation(runs, x, y):
    Stock_A = []
    Stock_B = []
    total = []
    for _ in range (runs):
        results = begin(5000,x,y,20000)
        Stock_A.append(results['stock a'])
        Stock_B.append(results['stock b'])
        total.append(results['total'])

    return total


def portfolio(runs):
    expectedA =[]
    riskA = []
    expectedB = []
    riskB = []
    for x in range(1, 100):
        sim_results = simulation(runs, x, 100-x)
        expectedA.append(np.mean(sim_results))
        riskA.append(np.std(sim_results))

    return [expectedA, riskA]


get_sim = simulation(1000, 50 ,50)
stockAmean=np.mean(get_sim)
print("The mean for Stock A and Stock B at at  y= 50 x =50 ", "$", stockAmean)
print("The Standard Deviation for Stock and Stock B at y= 50 x =50 $", np.std(get_sim))
