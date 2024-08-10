def hollow_pyramid(r):
  for n in range(1, r + 1):
    for p in range(n,r):
      print(" ",end="")
    for m in range(2 * n - 1):
      if m == 0 or m == 2 * n - 2:
        print("*",end="")
      else:
        print(" ",end="")
    print("")

  for n in range(2 * r - 1):
    print("*",end="")
  print("")
r=8
hollow_pyramid(r)
  
    
      
    
  