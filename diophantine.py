variables = range(0,20)
exams = range(6,57)
for total in exams:
    for a in variables:
        for b in variables:
            for c in variables:
                if total == ((6*a)+(9*b)+(20*c)):
                    print total, a, 'six pieces', b, 'nine pieces', c, 'twenty pieces'
