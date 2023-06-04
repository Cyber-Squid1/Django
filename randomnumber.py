import random
# randomNum1=random.randint(1000,9999)
# randomNum2=random.randint(100,999)
# randomNum3=random.randint(10,99)
# randomOtp=randomNum1*randomNum2/randomNum3
# print("1: ",randomNum1)
# print("2: ",randomNum2)
# print("3: ",randomNum3)
# print(int(randomOtp))

def generate():
    otp=''
    for _ in range(6):
        otp+=str(random.randint(0,9))
    return otp

print(generate())