T = int(eval(input('How many types of objects? = ')))
Ask = int(eval(input('Enter 1 to specify occurence per type (else:global) = ')))
if Ask == 1:
    n = [int(input('How many objects of type {0:d}? = '.format(i+1))) for i in range(T)]
    O = [n.count(i+1) for i in range(max(n))]
    N = []; N = [N[-1] for i in range(max(n)) if not N.append(N[-1]+O[i]*(i+1) if N else O[0])]
else:
    n = [int(input('How many objects of each type? = '))]*T
    O = [0]*(n[0]-1)+[T]
    N = [n[0]*T]

Ask = 1#int(eval(input('Enter 1 to show a list of sets (else:END) = ')))
if Ask == 1:
    def gen(N, aset):
        if n[0] == N:
            global c
            c += 1
            print(c,list(reversed([i+1 for i in aset])))
        else:
            for i in range(0, T):
                if n[i] > 0:
                    aset[N-1] = i
                    n[i] = n[i]-1
                    gen(N-1, aset)
                    n[i] = n[i]+1
                    aset[N-1] = 0
    c = 0
    aset = [0]*N[-1]
    print()
    print("Results show numbers referring to each object's type:")
    gen(N[-1], aset)

#Ruskey, F. (2003). Combinatorial generation. University of Victoria, Victoria, BC, Canada.

#AC
#191002
