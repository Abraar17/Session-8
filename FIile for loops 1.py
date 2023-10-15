print("Year, Balance, End Balance")
principal=int(input("Please enter principal amount"))
prince=principal
int=float(input("Please enter interest rate"))
year=1
while year<=5:
  Bmw = prince*int
  balance= prince+Bmw 
  year=year+1
  print(year, " ",prince, " " , balance)
  prince=balance 
print("Total interest earned ", prince-principal)