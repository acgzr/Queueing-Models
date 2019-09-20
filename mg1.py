import array
A = float(eval(input('Enter Lambda = ')))
U = float(eval(input('Enter Mu = ')))
D = float(eval(input('Enter Sigma (0?) = ')))
Cw = float(eval(input('Enter Cw (0?) = ')))
Cs = float(eval(input('Enter Cs (0?) = ')))
P = array.array('f', [1-A/U])
print("P(0) = {0:.4G}%".format(P[0]*100))
P.append(A/U)
print("P(1+2+...) = Pw = Rho = {0:.4G}%".format(P[1]*100))
Lq = (A**2*D**2+(A/U)**2)/(2*(1-A/U))
print("Lq = {0:.4G}".format(Lq))
L = Lq+A/U
print("L = {0:.4G}".format(L))
Wq = Lq/A
print("Wq = {0:.4G}".format(Wq))
W = Wq+1/U
print("W = {0:.4G}".format(W))
if Cw != 0 or Cs != 0:
    CT = Cw*L+Cs
    print("CT = Cw*L + Cs =")
    print("   = {0:.2f}*{1:.4G} + {2:.2f} =".format(Cw,L,Cs))
    print("   = {0:.2f} + {1:.2f} =".format(Cw*L,Cs))
    print("   = {0:.2f}".format(CT))
#190920
