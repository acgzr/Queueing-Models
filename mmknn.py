A = float(eval(input('Enter Lambda = ')))
U = float(eval(input('Enter Mu = ')))
N = int(eval(input('Enter N = ')))
k = int(eval(input('Enter k = ')))
Cw = float(eval(input('Enter Cw (0?) = ')))
Cs = float(eval(input('Enter Cs (0?) = ')))
F = []; F = [1]+[F[-1] for n in range(1, max([N, k])+1) if not F.append(F[-1]*n if F else 1)]
sum1 = []; sum1 = [sum1[-1] for n in range(k) if not sum1.append(sum1[-1]+F[N]*(A/U)**n/(F[N-n]*F[n]) if sum1 else 1)]
sum2 = []; sum2 = [sum2[-1] for n in range(k-1, N+1) if not sum2.append(sum2[-1]+F[N]*(A/U)**n/(F[N-n]*F[k]*k**(n-k)) if sum2 else 0)]
P = [1/(sum1[-1]+sum2[-1])]
print("P({0:d}) = {1:.4G}%".format(0, P[0]*100))
for n in range(1, k):
    P += [F[N]*(A/U)**n*P[0]/(F[N-n]*F[n])]
    print("P({0:d}) = {1:.4G}%".format(n, P[n]*100))
for n in range(k, N+1):
    P += [F[N]*(A/U)**n*P[0]/(F[N-n]*F[k]*k**(n-k))]
    print("P({0:d}) = {1:.4G}%".format(n, P[n]*100))
L = []; L = [L[-1] for n in range(N+1) if not L.append(L[-1]+n*P[n] if L else 0)]
print("L = {0:.4G}".format(L[-1]))
Ae = []; Ae = [Ae[-1] for n in range(N+1) if not Ae.append(Ae[-1]+(N-n)*A*P[n] if Ae else N*A*P[0])]
print("Ae = {0:.4G}".format(Ae[-1]))
W = L[-1]/Ae[-1]
print("W = {0:.4G}".format(W))
Rho = Ae[-1]/(k*U)
print("Rho (p) = {0:.4G}".format(Rho))
Wq = W-1/U
print("Wq = {0:.4G}".format(Wq))
Lq = Wq*Ae[-1]
print("Lq = {0:.4G}".format(Lq))
sum3 = []; sum3 = [sum3[-1] for n in range(k) if not sum3.append(sum3[-1]+P[n] if sum3 else P[0])]
Pw = 1-sum3[-1]
print("Pw = {0:.4G}%".format(Pw*100))
if Cw != 0 or Cs != 0:
    CT = Cw*L[-1]+Cs*k
    print("CT = Cw*L + Cs*k =")
    print("   = {0:.2f} + {1:.2f} =".format(Cw*L[-1], Cs*k))
    print("   = {0:.2f}".format(CT))
#190929
