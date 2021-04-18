class Bank:
    def acCreate(self,acno,name,bname):
        self.bname=bname
        self.acno=acno#INSTANCE VARIABLES IE VARIABLS USING SELF
        self.name=name
        self.minimumbal=5000
        self.balance=self.minimumbal
    def deposit(self,amt):
        self.balance+=amt
        print("account created with amount",amt)
        print("your current balance",self.balance)
    def withdraw(self,amt):
        if amt > self.balance:
            print("insuff balance")
        else:
            print("amount debited",amt)
            self.balance-=amt
            print("availiable balance",self.balance)
obj=Bank()
obj.acCreate(123,'abc','sbi')
obj.deposit(25000)
obj.withdraw(3000)
#two types of variables
#instance variables andstatic variables
#static variables are accessed using  classname

