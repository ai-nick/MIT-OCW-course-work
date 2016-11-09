variables=range(0,20)
n = 0
exams=range(6,61)
for total in exams:
    for a in variables:
        for b in variables:
            for c in variables:
                if total != ((6*a)+(9*b)+(20*c)):
                    n = n + total
                    print n
                if total == ((6*a)+(9*b)+(20**c)) and total > (n+6):
                    print total, n
