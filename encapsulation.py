class Computer:

    def __init__ (self):
        self.__maxprice = 2000

    def sell (self):
        print(f"Selling Price: {self.__maxprice}") 

    def setmaxprice(self, price):
        self.__maxprice = price

com = Computer()
com.sell()

com.__maxprice=3000
com.sell()

com.setmaxprice(4000)
com.sell()
