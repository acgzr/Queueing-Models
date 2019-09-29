A = float(eval(input('Enter Lambda = ')))
U = float(eval(input('Enter Mu = ')))
print("*** kmin = {0:d} ***".format(int(1+A//U)))
kmax = int(eval(input('Enter kmax (kmin?) = ')))
Pnmax = int(eval(input('Enter Pnmax (0?) = ')))
Cw = float(eval(input('Enter Cw (0?) = ')))
Cs = float(eval(input('Enter Cs (0?) = ')))
F = []; F = [1]+[F[-1] for n in range(1, kmax+1) if not F.append(F[-1]*n if F else 1)]
for k in range(int(1+A//U), kmax+1):
    print()
    print("k = {0:d}".format(k))
    sum1 = []; sum1 = [sum1[-1] for n in range(k) if not sum1.append(sum1[-1]+(A/U)**n/F[n] if sum1 else 1)]
    P = [1/(sum1[-1]+(A/U)**k*(k*U)/(F[k]*(k*U-A)))]
    print("P({0:d}) = {1:.4G}%".format(0, P[0]*100))
    for n in range(1, k+1):
        P += [P[0]*(A/U)**n/F[n]]
        print("P({0:d}) = {1:.4G}%".format(n, P[n]*100))
    for n in range(k+1, Pnmax+1):
        P += [P[0]*(A/U)**n/(F[k]*k**(n-k))]
        print("P({0:d}) = {1:.4G}%".format(n, P[n]*100))
    Lq = P[0]*(A/U)**k*A*U/((k*U-A)**2*F[k]/k)
    print("Lq = {0:.4G}".format(Lq))
    L = Lq+A/U
    print("L = {0:.4G}".format(L))
    Wq = Lq/A
    print("Wq = {0:.4G}".format(Wq))
    W = Wq+1/U
    print("W = {0:.4G}".format(W))
    Rho = A/(k*U)
    print("Rho (p) = {0:.4G}".format(Rho))
    Pw = P[0]*k*U*A**k/(F[k]*(k*U-A)*U**k)
    print("Pw = {0:.4G}%".format(Pw*100))
    if Cw != 0 or Cs != 0:
        CT = Cw*L+Cs*k
        print("CT = Cw*L + Cs*k =")
        print("   = {0:.2f} + {1:.2f} =".format(Cw*L, Cs*k))
        print("   = {0:.2f}".format(CT))
#190929
