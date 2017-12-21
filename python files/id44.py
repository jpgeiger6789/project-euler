#id44.py

import itertools

def pentgenerator():
    n = 0
    while True:
        n += 1
        yield n * (3 * n - 1) // 2

def ID44(maxn):
    pentgen = pentgenerator()
    pentset = {next(pentgen) for i in range(maxn)}
    permutation_list = itertools.combinations(pentset, 2) #returns a list
    special_permlist = [w for w in permutation_list if abs(w[0] - w[1]) in pentset and (w[0] + w[1]) in pentset]
    while not special_permlist:
        nextpent = next(pentgen)
        perm_list_append = ([nextpent, w] for w in pentset)
        pentset.add(nextpent)
        special_permlist += [w for w in perm_list_append if abs(w[0] - w[1]) in pentset and (w[0] + w[1]) in pentset]
            
    D = [abs(w[0] - w[1]) for w in special_permlist]
    D.sort()
    return D[-1]

maxn = 10000
ans = ID44(maxn)
print('The answer is', ans)
