def Bin(num):
    x = bin(num)[2:]
    return "0" * (SC - len(x)) + x


def Dec(num):
    return int(num, 2)


def twosComplimentInBinary(x):  # positive binary no
    temp_arr = []
    for i in x:
        if i == "0":
            temp_arr.append("1")
        else:
            temp_arr.append("0")
    temp = "".join(temp_arr)
    temp = Dec(temp) + 1
    return Bin(temp)


def Add(ac, br):
    out = Dec(ac) + Dec(br)
    out = Bin(out)
    return out[-SC:]


def ASHR(ac, qr, qnplusone):
    signbit = ac[0]
    t = ac + qr + qnplusone
    t = Dec(t) >> 1
    t = Bin(t)
    if signbit == "0":
        t = "0" * (2*SC + 1 - len(t)) + t
    else:
        t = "1" + t

    ac = t[:SC]
    qr = t[SC:-1]
    qnplusone = t[-1]
    return ac, qr, qnplusone


a, b = map(int, input("Enter two nos: ").split())
QR = a
BR = b
sc_temp = max(abs(QR), abs(BR))
SC = len(bin(sc_temp)) - 1
AC = "0" * SC

if QR < 0:
    QR *= -1
    QR_Bin = twosComplimentInBinary(Bin(QR))
else:
    QR_Bin = Bin(QR)

if BR < 0:
    BR *= -1
    BR_Bin = twosComplimentInBinary(Bin(BR))
else:
    BR_Bin = Bin(BR)

print(f"QR = {QR_Bin} , BR = {BR_Bin}")

BRbarplusone = twosComplimentInBinary(BR_Bin)

print("BRbarplus =", BRbarplusone)

Qn = QR_Bin[-1]
Qnplusone = "0"

print("Qn =", Qn, "Qnplusone =", Qnplusone)
print("SC =", SC)
print("AC =", AC)

for i in range(SC):

    print("Cycle:", i+1)
    print(f" {Qn}  {Qnplusone}      {AC} {QR_Bin} {Qnplusone}")

    if Qn == "1" and Qnplusone == "0":
        AC = Add(AC, BRbarplusone)
        print(f" Subtract +{BRbarplusone}")
        print("       AC ", AC, QR_Bin)

    elif Qn == "0" and Qnplusone == "1":
        AC = Add(AC, BR_Bin)
        print(f"      Add +{BR_Bin}")
        print("       AC ", AC, QR_Bin)

    AC, QR_Bin, Qnplusone = ASHR(AC, QR_Bin, Qnplusone)

    Qn = QR_Bin[-1]

    print(f"     ASHR: {AC} {QR_Bin} {Qnplusone}")

    print()
    print()


finalstring = AC + QR_Bin

if finalstring[0] == "1":
    finalstring = twosComplimentInBinary(finalstring)
    final = -Dec(finalstring)

else:
    final = Dec(finalstring)


print(f"{a} * {b} = {final}")