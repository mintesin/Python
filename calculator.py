3def add(n1,n2):
  return n1+n2
def multiply(n1,n2):
  return n1*n2
def devide(n1,n2):
  return n1/n2
def substract(n1,n2):
  return n1-n2

mat_operations={'+':add,'*':multiply,'-':substract,'/':devide}

num1=int(input("What is the first number: "))
num2=int(input("What is the second number: "))

for key,value in mat_operations.items():
  print(key)


should_continue=True
while should_continue:
  symbol=input("Enter the symbol you want to: ")
  operation=mat_operations[symbol]
  result=operation(num1,num2)
  print(result)
  conti=input("Enter Y to continue the operatioon: ")
  if conti=='Y':
    continue
  else:
    should_continue=False

