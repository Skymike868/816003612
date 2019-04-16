from execute.InvestmentSimulation import portfolio
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab


def execute():
    getresults = portfolio(1000)
    ExpectedA = getresults[0]
    RiskA = getresults[1]
    plt.scatter(RiskA,ExpectedA,  edgecolors='r')
    plt.xlabel('Expected Risk(Standard Deviation)')
    plt.ylabel('Expected Return (Mean)')
    plt.title('Portfolio Theory of Stock A and Stock B')
    plt.show()

execute()

