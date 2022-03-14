from asyncio.windows_events import NULL
class Iteminfo:
    def __init__(self,item_name=None,item_code=0,price=NULL,qty=NULL,net_price=NULL,discount=NULL):
        self.item_name=item_name
        self.item_code=item_code
        self.price=price
        self.qty=qty
        self.net_price=net_price   
        self.discount=discount

    @classmethod    
    def buy(cls):#To read information from members
        item_name=str(input("Enter the item name:"))
        item_code=int(input("Enter the item code:"))
        price=int(input("Enter the price:"))
        qty=int(input("Enter the qty:")) 
   
        return cls(item_name,item_code,price,qty)
      
    def calculate_discount(self):
        
        total_price=self.price*self.qty
        
        if self.qty <=10:
            self.discount=0
        elif 10<self.qty <20: 
            self.discount=15
        else: 
            self.discount=20
        
        self.net_price=self.price*self.qty-self.discount
        price_tobe_paid=total_price-self.discount
        return price_tobe_paid

    def show_all(self):
         
        return print( f"item name:{self.item_name} item code:{self.item_code} price: {self.price} qty:{self.qty} discount:{self.discount} price tobe paid:  {self.calculate_discount()}" )

item1=Iteminfo().buy()
item1.calculate_discount()
item1.show_all()

