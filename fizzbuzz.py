i = 0
while(i < 65):
    
    
    if(i%3==0):
        if(i%5==0):
            print("FizzBuzz")
        else:
            print("Fizz")
    else:
        if(i%5==0):
            print("Buzz")
        else:
            print(i)
    i = i+1
    
