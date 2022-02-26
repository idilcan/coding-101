# f(x) = (x+5)^2
# f(x) = (x+5)^2
# y = (x+5)^
# f --> function name
# f(x) --> x --> function's input
# (x+5)^2 --> function's output, the insturctions that is
# required for y
def f(x):
   return (x+5)**2
 
for  x in range(100):
   if x % 5 == 0 and x != 0:
       print()
   print(f(x), end=", ")
print()
