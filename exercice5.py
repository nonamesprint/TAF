#  progrmme FizzBuzz
intervalle=range(1,51)
for t in intervalle:
        if t%3==0 and t%5==0:
           print(" FizzBuzz")
        elif t%3==0:
           print("Fizz") 
        elif t%5==0:
         print("Buzz")
        else:
          print(t)