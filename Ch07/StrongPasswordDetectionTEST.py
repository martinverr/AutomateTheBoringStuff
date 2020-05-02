import StrongPasswordDetection as SPD

password1 = "questanonva1000"
password2 = "QUESTANONVA1000"
password3 = "questaNonVa"
password4 = "N3Anch3"
password5 = "questaVA1000"

print(SPD.isStrongPw(password1)) #False
print(SPD.isStrongPw(password2)) #False
print(SPD.isStrongPw(password3)) #False
print(SPD.isStrongPw(password4)) #False
print(SPD.isStrongPw(password5)) #True
