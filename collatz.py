num = int(input("Enter Number, fool: "))

def collatzFunction(num):
  while num != 1:
    if (num % 2) == 0:
      num = num/2
      print(num)
    else:
      num = (num*3)+1
      print(num)

collatzFunction(num)
print("Loop found!")
