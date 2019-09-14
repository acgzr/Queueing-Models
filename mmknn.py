import array
A = float(input('Enter Lambda = '))
U = float(input('Enter Mu = '))
N = int(input('Enter N = '))
k = int(input('Enter k = '))
Cw = float(input('Enter Cw (0?) = '))
Cs = float(input('Enter Cs (0?) = '))
Nf = 1
for i in range(1, N+1):
    Nf = Nf*i
kf = 1; i = 0
for i in range(1, k+1):
    kf = kf*i
sum1 = float(0)
for n in range(0, k):
    Nnf = 1; i = 0
    for i in range(1, N-n+1):
       Nnf = Nnf*i
    nf = 1; i = 0
    for i in range(1, n+1):
       nf = nf*i
    sum1 += Nf*(A/U)**n/(Nnf*nf)
sum2 = float(0); n = 0
for n in range(k, N+1):
    Nnf = 1; i = 0
    for i in range(1, N-n+1):
       Nnf = Nnf*i
    sum2 += Nf*(A/U)**n/(Nnf*kf*k**(n-k))
P = array.array('f', [(sum1+sum2)**-1])
n = 0; sum3 = P[0]
for n in range(1, k):
    Nnf = 1; i = 0
    for i in range(1, N-n+1):
       Nnf = Nnf*i
    nf = 1; i = 0
    for i in range(1, n+1):
       nf = nf*i
    P.append(Nf*(A/U)**n*P[0]/(Nnf*nf))
    sum3 += P[n]
n = 0
for n in range(k, N+1):
    Nnf = 1; i = 0
    for i in range(1, N-n+1):
       Nnf = Nnf*i
    P.append(Nf*(A/U)**n*P[0]/(Nnf*kf*k**(n-k)))
n = 0; L = 0; Ae = 0
for n in range(0, N+1):
    print("P({0:d}) = {1:.4G}%".format(n,P[n]*100))
    L += n*P[n]
    Ae += (N-n)*A*P[n]
print("L = {0:.4G}".format(L))
print("Ae = {0:.4G}".format(Ae))
W = L/Ae
print("W = {0:.4G}".format(W))
Rho = Ae/(k*U)
print("Rho (p) = {0:.4G}".format(Rho))
Wq = W-U**-1
print("Wq = {0:.4G}".format(Wq))
Lq = Wq*Ae
print("Lq = {0:.4G}".format(Lq))
Pw = 1-sum3
print("Pw = {0:.4G}%".format(Pw*100))
if Cw != 0 or Cs != 0:
    CT = Cw*L+Cs*k
    print("CT = Cw*L + Cs*k =")
    print("   = {0:.2f}*{1:.4G} + {2:.2f}*{3:.4G} =".format(Cw,L,Cs,k))
    print("   = {0:.2f} + {1:.2f} =".format(Cw*L,Cs*k))
    print("   = {0:.2f}".format(CT))
