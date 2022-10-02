class BikeShop:
    def __init__(self,stock):
        self.stock=stock
    def displaybike(self):
        print("Total Bike available:----",self.stock) 
    def rentforbike(self,q):
        if q<=0:
            print("-----:Please enter the positive Value or greater than zero:-----")
        elif q>self.stock:
            print("----:Please sufficient value:----")    
        else:
            self.stock=self.stock-q
            print("Total price:--",q*100) 
            print("Available total bike:--",self.stock)   
 
while True:
    obj=BikeShop(100)
    uin=int(input('''
    1.Display Stocks
    2.Rent a Bike
    3.exit
    '''))
    if uin==1:
          obj.displaybike()
    elif uin==2:
          n=int(input("Enter the Qty:---"))
          obj.rentforbike(n) 
    else:
        break       
