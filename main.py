import random
karakterler=("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
sfuzunlugu=int(input("Şifre ne kadar uzun olsun?"))
sifre=""

for i in range(sfuzunlugu):
    sifre+=random.choice(karakterler)

print(sifre)
