x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x) # Local E Local

myfunc()

print("Python is " + x) # Global E Global



#Using Global Keyword In Function ****

x = "awesome"

def myfunc():
  global x    #Global
  x = "fantastic"
  
print(x)
myfunc()

print("Python is " + x)