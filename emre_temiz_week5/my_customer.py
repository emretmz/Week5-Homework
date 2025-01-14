class Customer():
    discount=0
    def __init__(self,cust_fname,cust_lname,cust_id):
        self.cust_fname=cust_fname
        self.cust_lname=cust_lname
        self.cust_id=cust_id
    @classmethod
    def get_cust_info(cls):
        #Get Customer informations from the user
        cust_fname=str(input("Enter the customer first name:"))
        cust_lname=str(input("Enter the customer last name:"))
        cust_id=str(input("Enter the id:"))     
           
        return cls(cust_fname,cust_lname,cust_id)
        
    def my_str(self):
        #Print Customer informations
        return print( f"customer first name:{self.cust_fname} cust last name:{self.cust_lname} customer id: {self.cust_id}")
    
    def get_cust_id(self):
        #Send the customer id
        return self.cust_id

class Items(Customer):
    def __init__(self,item_name,item_price,item_qty,item_discount):   
        self.item_name=item_name     
        self.item_price=item_price
        self.item_qty=item_qty
        self.item_discount=int(item_discount)
    
    @classmethod
    def shopping_cart(cls):
        #Get item informations by this method
        item_code=int(input("Enter the item code:"))
        item_name=str(input("Enter the item name:"))
        price=int(input("Enter the price:"))
        qty=int(input("Enter the qty:")) 

        return cls(item_code,item_name,price,qty)

    def calculate_discount(self):
        #Calculate total paid amount by this method
        total_price=int(self.item_price)*int(self.item_qty)
        if total_price>=4000:self.item_discount=0.25
        elif 4000<total_price<=2000:self.item_discount=0.15
        else:self.item_discount=0.10

        price_tobe_paid=float(total_price)-(float(self.item_price)*self.item_discount)
        return_my_list=[total_price,price_tobe_paid]
        return return_my_list

    def __str__(self):
   
        #Print Item's informations
        return print(f"customer id:{Customer.get_cust_id()} item name:{self.item_name} item total price:{Items.calculate_discount()[0]} item qty: {self.item_qty} item discount:{self.item_discount} price tobe paid: {self.calculate_discount()[1]}")        

customer1=Customer.get_cust_info()
customer1.my_str()

item1=Items.shopping_cart()
item1.calculate_discount()
item1.__str__()
