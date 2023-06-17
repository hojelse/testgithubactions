f = open("data.txt", "r")
for line in f:
  n = int(line.strip())
  print(n*10)
