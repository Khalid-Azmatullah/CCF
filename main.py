from pyscript import document


def get_float(prompt):
  while True:
    user_input = prompt
    try:
      # Attempt to convert the input to an integer
      value = float(user_input)
      return value
    except ValueError:
      # Handle the case where conversion fails
      output_div = document.querySelector("#output")
      output_div.innerText = ("Error: Invalid Argument Given")


def calculate(event):
  # Define six variables to store the integers
  f1x = document.getElementById('f1x').value
  f1y = document.getElementById('f1y').value
  f2x = document.getElementById('f2x').value
  f2y = document.getElementById('f2y').value
  f3x = document.getElementById('f3x').value
  f3y = document.getElementById('f3y').value

  f1x = get_float(f1x)
  #print('')
  f1y = get_float(f1y)
  #print('')
  f2x = get_float(f2x)
  #print('')
  f2y = get_float(f2y)
  #print('')
  f3x = get_float(f3x)
  #print('')
  f3y = get_float(f3y)
  #print('')

  # Print the values of the variables
  #print(Fore.WHITE)
  # Numerator of x
  xn1111 = f1x * f1x
  xn1112 = f1y * f1y
  xn1121 = f2x * f2x
  xn1122 = f2y * f2y
  xn1211 = f2y - f3y

  xn2111 = f2x * f2x
  xn2112 = f2y * f2y
  xn2121 = f3x * f3x
  xn2122 = f3y * f3y
  xn2211 = f1y - f2y

  # Brewing this shit
  xn111 = xn1111 + xn1112
  xn112 = xn1121 + xn1122
  xn121 = xn1211 * 2

  xn211 = xn2111 + xn2112
  xn212 = xn2121 + xn2122
  xn221 = xn2211 * 2

  # Lets Burn this Shit
  xn11 = xn111 - xn112
  xn12 = xn121

  xn21 = xn211 - xn212
  xn22 = xn221

  # You GO Boy!
  xn1 = xn11 * xn12
  xn2 = xn21 * xn22

  # Yay we got 'xn'
  xn0 = xn1 - xn2

  # Denominator for x
  xd11 = f1x - f2x
  xd12 = f2y - f3y

  xd21 = f2x - f3x
  xd22 = f1y - f2y

  #Brew the shit
  xd1 = xd11 * xd12 * 4
  xd2 = xd21 * xd22 * 4

  # Done the tough work
  xd0 = xd1 - xd2

  # We got 'x' bro!
  xkivalue = xn0 / xd0


  # NOW WE DO Y
  # Numerator of y
  yn1111 = f2x * f2x
  yn1112 = f2y * f2y
  yn1121 = f3x * f3x
  yn1122 = f3y * f3y
  yn1211 = f1x - f2x

  yn2111 = f1x * f1x
  yn2112 = f1y * f1y
  yn2121 = f2x * f2x
  yn2122 = f2y * f2y
  yn2211 = f2x - f3x

  # Brewing this shit
  yn111 = yn1111 + yn1112
  yn112 = yn1121 + yn1122
  yn121 = yn1211 * 2

  yn211 = yn2111 + yn2112
  yn212 = yn2121 + yn2122
  yn221 = yn2211 * 2

  # Lets Burn this Shit
  yn11 = yn111 - yn112
  yn12 = yn121
  yn21 = yn211 - yn212
  yn22 = yn221

  # You GO Boy!
  yn1 = yn11 * yn12
  yn2 = yn21 * yn22

  # Yay we got 'yn'
  yn0 = yn1 - yn2

  # Denominator for y too ezy

  yd0 = xd0

  # We got 'y' bro!
  ykivalue = yn0 / yd0

  #print(Style.BRIGHT + 'Co-ordinates of the centre are: (' + 
  #Fore.GREEN + str(x) + Fore.WHITE +',' + 
  #Fore.GREEN + str(y) + Fore.WHITE + ')')
  #print(Style.DIM + Fore.LIGHTRED_EX + 'NOTE: Value may not be exact due to rounding errors.')
  output_div = document.querySelector("#output")
  output_div.innerText = ('Co-ordinates of centre are: (' + str(xkivalue) + ',' + str(ykivalue) + ')')
