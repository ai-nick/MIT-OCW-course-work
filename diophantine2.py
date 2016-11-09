n = 0
x = 0
variables = range(0,20)
exams = range(20,70)
for total in exams:
    for a in variables:
        for b in variables:
            for c in variables:
                if total == ((6*a)+(9*b)+(20*c)):
                    if total == n + 2:
                        n = (n + 1)
                        x = n
                    if total == x + 7:
                        print x,'is the greatest number that cannot be be bought'
                        x = 0
                    n = total

                    
                            

                    
