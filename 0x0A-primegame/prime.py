def prime_Number(n: int) -> bool:
   if n == 1:
      return False
   elif n == 2:
      return True
   elif n == 3:
      return True
   elif n % 2 != 0 and n % 3 != 0:
      return True
   else:
      return False
   
print(prime_Number(3))