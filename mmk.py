import array
A = float(eval(input('Enter Lambda = ')))
U = float(eval(input('Enter Mu = ')))
print("*** kmin = {0:d} ***".format(int(1+A//U)))
kmax = int(eval(input('Enter kmax (kmin?) = ')))
Pnmax = int(eval(input('Enter Pnmax (0?) = ')))
Cw = float(eval(input('Enter Cw (0?) = ')))
Cs = float(eval(input('Enter Cs (0?) = ')))
for k in range(int(1+A//U), kmax+1):
    print()
    print("k = {0:d} ################".format(k))
    sum1 = 1; nf = 1
    for n in range(1, k):
        nf *= n
        sum1 += ((A/U)**n)/nf
    kf = nf * k
    P = array.array('f', [1/(sum1+((A/U)**k)*(k*U)/(kf*(k*U-A)))])
    nf = 1
    for n in range(1, k+1):
        nf *= n
        P.append(P[0]*((A/U)**n)/nf)
    for n in range(k+1, Pnmax+1):
        P.append(P[0]*((A/U)**n)/(kf*k**(n-k)))
    for n in range(Pnmax+1):
        print("P({0:d}) = {1:.4G}%".format(n,P[n]*100))
    Lq = P[0]*(((A/U)**k)*A*U)/((k*U-A)**2*kf/k)
    print("Lq = {0:.4G}".format(Lq))
    L = Lq+A/U
    print("L = {0:.4G}".format(L))
    Wq = Lq/A
    print("Wq = {0:.4G}".format(Wq))
    W = Wq+1/U
    print("W = {0:.4G}".format(W))
    Rho = A/(k*U)
    print("Rho (p) = {0:.4G}".format(Rho))
    Pw = P[0]*k*U*A**k/(kf*(k*U-A)*U**k)
    print("Pw = {0:.4G}%".format(Pw*100))
    if Cw != 0 or Cs != 0:
        CT = Cw*L+Cs*k
        print("CT = Cw*L + Cs*k =")
        print("   = {0:.2f}*{1:.4G} + {2:.2f}*{3:.4G} =".format(Cw,L,Cs,k))
        print("   = {0:.2f} + {1:.2f} =".format(Cw*L,Cs*k))
        print("   = {0:.2f}".format(CT))
print()
#190920
