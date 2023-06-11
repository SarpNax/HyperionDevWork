menu = {"hash browns", "eggs", "english breakfast", "mushroom breakfast", "omelette"}
stock_price = [20, 20, 15, 10, 5]
stock_value = [10, 5, 12, 12, 6]
stock = 0
price = 0
while True:
    stock_check = input("Please enter Stock item\n hash browns,eggs,english breakfast,mushroom breakfast,omelette\n>")
    if stock_check == "hash browns":
        stock = (stock_price[1])
        price = (stock_price[1])
        stock_value_total = stock * price
        print(stock_value_total)

    elif stock_check == "eggs":
        stock = (stock_price[2])
        price = (stock_price[2])
        stock_value_total = stock * price
        print(stock_value_total)

    elif stock_check == "english breakfast":
        stock = (stock_price[3])
        price = (stock_price[3])
        stock_value_total = stock * price
        print(stock_value_total)

    elif stock_check == "mushroom breakfast":
        stock = (stock_price[4])
        price = (stock_price[4])
        stock_value_total = stock * price
        print(stock_value_total)

    elif stock_check == "omelette":
        stock = (stock_price[1])
        price = (stock_price[1])
        stock_value_total = stock * price
        print(stock_value_total)

    end_prog = input("would you like to continue? Y/N").upper()
    if end_prog == "N":
        break
