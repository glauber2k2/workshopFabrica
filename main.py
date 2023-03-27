def max (num1, num2):
  
  if num1 > num2:
    print("dentre ", num1, "e ", num2, "o maior é ", num1)
  else:
    print("dentre ", num1, "e ", num2, "o maior é ", num2)

def mult (num1, num2):
  if num1 % num2 == 0:
    print(num1, " é multiplo de ",num2)
    return True
  else:
    print(num1, " não é multiplo de ", num2)
    return False

def area (num1):
  print("area do quadrado com lado ", num1, "é ", num1 ** 2)

max(7,5)
mult(9,3)
area(2)