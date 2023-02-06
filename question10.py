#10). create a class BANK and with two function simple interest and compound interest
# and need to create instance for pnb, icici and hdfc banks with corresponding input.
class Bank:
    def __init__(self,bank_name,P,R,T):
      self.bank_name= bank_name
      self.principle = P
      self.rate = R
      self.time = T


    def __str__(self):
      return f"{self.bank_name}"
     def s_Interest(self):
      X = (self.principle*self.rate*self.time)/100
      return f"Simple Interest: {X}"
    def c_Interest(self):
      Amount = self.principle * (pow((1 + self.rate/ 100), self.time))
      Y = Amount - self.principle
      return f"Compund Interest: {Y}"
      


Bank1=Bank("PNB",50000,9,10) 
Bank2=Bank("ICICI",100000,20,5)
Bank3=Bank("HDFC",30000,12,2)
#for pnb bank
print(Bank1) 
print(Bank1.s_Interest()) 
print(Bank1.c_Interest()) 

#for icici bank
print(Bank2)
print(Bank2.s_Interest())
print(Bank2.c_Interest())
#for hdfc bank
print(Bank3)
print(Bank3.s_Interest())
print(Bank3.c_Interest())