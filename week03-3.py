for i in range(1,10):
  for j in range(1,10):
    print(i, "x", j, "=", i*j, sep="", end="  ")
    if i*j<10:
      print(" ", end="")
  print("\n")