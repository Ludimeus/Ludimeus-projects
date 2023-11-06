while True:
  inp = input('Your text here: ')
  x = 0
  for i in str(inp):
    if i == ' ':
      x += 1
  print(x+1)
