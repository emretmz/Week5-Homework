class Product:
    def __init__(self,product_name,product_id,product_purchase_price,product_sale_price):
        self.product_name=product_name
        self.product_id=product_id   
        self.product_purchase_price=product_purchase_price
        self.product_sale_price=product_sale_price
        
    def SetRemarks(self):
        print("Set remarks works {self.item_name}")
    
    def set_remarks(self):        
        if self.product_sale_price - self.product_purchase_price <0:
            return "Loss"
        else :
            return "Profit"

    @classmethod
    def set_details(cls):
        product_name=str(input("Enter the product name:"))
        product_id=int(input("Enter the product id:"))      
        product_purchase_price=float(input("Enter the product purchase price:"))       
        product_sale_price=float(input("Enter the product sale price:"))       
        Product.SetRemarks( )
        return cls(product_name,product_id,product_purchase_price,product_sale_price)

    def get_details(self):
        return print(f"product_name:{self.product_name} product id:{self.product_id} product purchase price: {self.product_purchase_price} product sale price:{self.product_sale_price} remark:{Product.set_remarks()} ")
 
product1=Product.set_details()
#product1.set_details()
product1.get_details()