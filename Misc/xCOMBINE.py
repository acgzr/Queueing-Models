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
a = [1]; ysize = 1
for i in range(len(O)):
    b = [1]*(i+2)
    for j in range(O[i]):
        ysize += i+1
        y = [0] * ysize
        for k in range(len(y)):
            for l in range(i+2):
                if 0 <= k-l <= ysize-(i+2):
                    y[k] += a[k-l]*b[l]
        a = y
[print("C(pick ", ("{0:d} or ".format(i) if i != len(y)-i-1 else ""), "{0:d}) = {1:d}".format(len(y)-i-1, y[i]), sep = "") for i in range(int((len(y)+1)//2))]
Ask = int(eval(input('Enter 1 to show a list of sets (else:END) = ')))
if Ask == 1:
    def gen(k, t, N, cond):
        if cond == True:
            opt = [0, 0]
        else:
            opt = [N, n[t]]
        if k == opt[0]:
            global c
            c += 1
            print(c,aset)
        else:
            for i in range(max(0, k-N+n[t]), min(n[t], k)+1):
                aset[t] = i
                gen(k-i, t-1, N-n[t], cond)
                aset[t] = opt[1]
    c = 0
    k = int(eval(input('How many picked objects per set? = ')))
    if k <= N[-1]/2:
        aset = [0]*T
    else:
        aset = n[:]
    print()
    print("Results show quatity per object type:")
    gen(k, T-1, N[-1], k <= N[-1]/2)

#Ruskey, F. (2003). Combinatorial generation. University of Victoria, Victoria, BC, Canada.
#Thein, M. M. (2012). One Dimensional Convolution.

#AC
#191002
