import itertools
l1 = [5,2,12,18]
l2 = [56,42,99,14]
for a,b in itertools.product(l1,l2):
    print(a*b)

l3 = ["Leila","Sara","Zeinab"]
for subset in itertools.combinations(l3,2):
    print(subset)