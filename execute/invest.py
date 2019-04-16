import numpy as np

print("Simulation Start")
stocks = {
    'stock a': 0,
    'stock b': 0


}

Investment = {
    'stock a': 0,
    'stock b': 0,
    'total': 0
}

stocka = []
stockb = []



def stock_a(money):  # the x amount of money already inputted into stock a
    # returns the total amount of money  including percentage
    aroi = 10
    std =4
    percentage = (np.random.normal(aroi, std)) /100
    returns = money*(percentage+1)  # 1 in order to multiply % and add to itself
    return returns


def stock_b(money):
    aroi = 8
    std = 1
    percentage = (np.random.normal(aroi, std)) / 100
    returns = money * (percentage + 1)  # 1 in order to multiply % and add to itself
    return returns



# aa = annual addition
# x and y are inserted as full percentages such as (10,15)


def begin(aa, x, y,money):
    x = x / 100  # stock a
    y = y / 100  # stock b
    if x+y != 1:
        return " x+y not equal to one"
    form = 1

    stocka_total = []
    stockb_total = []
    stocka_total.append(money*x)
    stockb_total.append(money*y)


    while form < 7:

        latest_money_stocka = stocka_total.pop()  # gets the latest money to use
        stocka_total.append(latest_money_stocka)
        latest_money_stockb = stockb_total.pop()
        stockb_total.append(latest_money_stockb)


        if form > 2:
            # annual_addition = aa
            latest_money_stocka = latest_money_stocka + (aa * x)  # this adds the 5000 to existing
            stocka_total.append(stock_a(latest_money_stocka))

            latest_money_stockb = latest_money_stockb + (aa * y)  # this adds the 5000 to existing
            stockb_total.append(stock_b(latest_money_stockb))

        else: #form 1
            stocka_total.append(stock_a(latest_money_stocka))
            stockb_total.append(stock_b(latest_money_stockb))



        form = form + 1
    stocks['stock a']= stocka_total
    stocks['stock b'] = stockb_total
    Investment['stock a'] = stocka_total.pop()  # stocka_total no longer up to date
    Investment['stock b'] = stockb_total.pop()  # stockb_total no longer up to date
    Investment['total'] = Investment['stock a'] + Investment['stock b']
    # stocks contains the yearly breakdown of incremental increase


    return Investment



#print (stock_a(3000))
