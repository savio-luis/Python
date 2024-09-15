def is_leap_year(ano):
  """Determines if a given year is a leap year.

  Args:
    year: The year to check.

  Returns:hvg
    True if the year is a leap year, False otherwise.
  """

  if ano % 4 == 0:
    if ano % 100 == 0:
      return ano % 400 == 0
    else:
      return True
  else:
    return False

# Get the year from the user
ano = int(input("Digite o ano: "))

# Check if the year is a leap year
if is_leap_year(ano):
  print(f"{ano} é um ano bissexto.")
else:
  print(f"{ano} não é ano bissexto.")
