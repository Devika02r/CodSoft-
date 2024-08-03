import random
import string

class password():
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    numbers=string.digits
    symbols=string.punctuation
    
    coll = lower+upper+numbers+symbols
    
    def generate(self):
        while True:
            try:
                len=int(input("enter length for password "))
                if len<=0:
                    print("error.. Please enter a valid integer")
                else:
                    res=""
                    for i in range(0,len):
                        res+=random.choice(self.coll)
                    print("password is : ",res)
                    p=input("another password ?(y/n):").lower()
                    if p not in ["yes","y"]:
                        exit()
            except ValueError:
                print("error")
                
if __name__ == "__main__":
    a=password()
    a.generate()