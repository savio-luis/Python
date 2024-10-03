def celsius_to_fahrenheit(celsius):
  """Converts a temperature from Celsius to Fahrenheit.

  Args:
      celsius: The temperature in Celsius.

  Returns:
      The temperature in Fahrenheit.
  """

  fahrenheit = (celsius * 9 / 5) + 32
  return fahrenheit

# Get user input for the temperature in Celsius
celsius = float(input("Enter a temperature in Celsius: "))

# Convert the temperature to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Print the result
print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")