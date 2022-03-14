class Society:
    def __init__(self,society_name,house_no_of_man,income,flat="missing"): 
        self.society_name=society_name,
        self.house_no_of_man=house_no_of_man,
        self.flat=flat,
        self.income=income
                
    @classmethod
    def input_data(cls):#To read information from members
        society_name=str(input("Enter the society name:"))
        house_no_of_man=int(input("Enter the house no of man:"))
        income=int(input("Enter the income:"))
        return cls(society_name,house_no_of_man,income)

    def allocate_flat(self):#To allocate flat according to income using the below table.
        if self.income>=25000:self.flat="A Type" 
        elif 20000<=self.income<25000:self.flat="B Type"
        elif 15000<=self.income<20000:self.flat="C Type"
        else: self.flat="D Type"       
        return self.flat

    def show_data(self):#to display the details of the entire class
        return print(f"society name:{self.society_name} house no of man:{self.house_no_of_man} flat: {self.flat} income:{self.income}")

society1=Society.input_data()
society1.allocate_flat()
society1.show_data()
