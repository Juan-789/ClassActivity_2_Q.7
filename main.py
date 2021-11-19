
"""
7. A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes. A program asks the user for three numbers three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.
"""
A = int(input("What is the cost of a cupcake in dollars? "))
B = int(input("What is the cost of a cupcake in cents? "))
N = int(input("How many cupcakes are you buying? "))
pricedollar = A *N
pricecents = B*N
while pricecents>=100:
  pricedollar += 1
  pricecents -= 100
print (f"The cupcakes cost {pricedollar} dollars and {pricecents} cents")

