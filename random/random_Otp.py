import secrets

secretsGenerator = secrets.SystemRandom()

otp = secretsGenerator.randrange(100000, 999999)
print(f'Secure random OTP is {otp}')

