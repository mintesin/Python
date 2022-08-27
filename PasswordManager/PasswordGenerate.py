def generate_password():
  import random
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


  nr_letters = random.choice(range(8,10))
  nr_symbols = random.choice(range(8,10))
  nr_numbers = random.choice(range(9,10))

  #Eazy Level
  # password = ""

  # for char in range(1, nr_letters + 1):
  #   password += random.choice(letters)

  # for char in range(1, nr_symbols + 1):
  #   password += random.choice(symbols)

  # for char in range(1, nr_numbers + 1):
  #   password += random.choice(numbers)

  # print(password)

  #Hard Level
  password_list = []

  for char in range(1, nr_letters + 1):

    password_list=[m for m in random.choice(letters)]

  for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

  for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

  # print(password_list)
  random.shuffle(password_list)
  # print(password_list)

  password = ""
  for char in password_list:
    password += char
  return password
