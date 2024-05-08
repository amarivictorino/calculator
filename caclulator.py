def calculate(num1, num2):
  """
  This function performs division and provides the reciprocal or negative reciprocal
  depending on the user's choice.

  Args:
    num1: The first number entered by the user.
    num2: The first number entered by the user.
  
  Returns:
    The result of the calculation.
   """
  result = num1 / num2
  operation = input("Enter 'r' for reciprocal or 'n' for negative reciprocal: ")
  if operation == 'r':
    return result * -1 
  elif operation == 'n':
    return result / -1 
  else:
    print("Invalid operation. Please enter 'r' or 'n'.")
    return None
  
while True:
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = calculate(num1, num2)
    if result:
      print("The result is::", result)
  except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
  choice = input("Do you want to try again? (yes/no): ")
  if choice.lower() != 'yes':
    break
  
print("Thank you for using the calculator!")
