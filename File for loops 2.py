num=1
num2=1
print(num)
print (num2)
next=num+num2
print (next)
count=1
while count<20:
  num=num2
  num2=next  
  next=num+num2
  print(next)
  count=count+1