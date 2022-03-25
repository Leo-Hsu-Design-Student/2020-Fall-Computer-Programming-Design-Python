def profit(dict):
    benefit=round((dict["price"]-dict["cost"])*dict["inventory"])
    return benefit
if __name__=="__main__":
    print(profit({"cost": 32.67,"price": 45.00,"inventory": 1200}))
    print(profit({"cost": 225.89,"price": 550.00,"inventory": 100}))
    print(profit({"cost": 2.77,"price": 7.95,"inventory": 8500}))
