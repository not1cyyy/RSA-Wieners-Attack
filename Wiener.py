from owiener import attack 

e = int(input("Enter the public exponent e: "))
n = int(input("Enter the modulus n: "))
c = int(input("Enter the ciphertext c: "))

d = attack(e, n)

if d == None:
	print("cannot retrieve the private key")
else:
	m = pow(c, d, n)
	print(bytearray.fromhex(hex(m)[2:]).decode())