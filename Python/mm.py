
def smaller_num(x, y): ## Can be rephrased to  def smaller_num(x, y):
    if x > y:          ##                          if x > y:
        number = y     ##                              return y
    else:              ##                          else:
        number = x     ##                              return x
        return number

x = input("Enter first number:-")
y = input("Enter second number:-")
result = smaller_num(x, y)
print("The smaller number between " +  str(x) + " and " + str(y) + " is " + str(result))


