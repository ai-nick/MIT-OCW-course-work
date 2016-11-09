#this is a code to produce the fibonacci sequence numbers(way easier than primes)
a = 0
b = 1
count = 0
max_count = 20
while count < max_count:
    count = count + 1 # start of loop, needed to close the loop
    old_a = a # this is the variable we are printing it will be 0 in the first loop
    old_b = b # this is also now a value of 1
    a = old_b # this is so that old a next loop is equal to old b in the previous loop
    b = old_a + old_b #b = 0 + 1 so its 1
    print (old_a)
