#returns the nth prime number so primeNth(1) = 2 and primeNth(5) = 11

def primeNth(requested):
    if(requested <2 ):
        return 2
    x = 2 #this is our starting point
    lastPrime = 2
    count = 1
    while(count != requested):
        x += 1
        divisors = 2
        for i in range(2,x):
            if (x%i == 0):
                divisors +=1
        if divisors == 2:
            lastPrime = x
            count +=1
    print (lastPrime)
primeNth(100)
