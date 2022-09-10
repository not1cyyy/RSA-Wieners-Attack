from owiener import attack 
import os
from time import * 

sleep(1)
e = int(input("Enter the public exponent e: "))
n = int(input("Enter the modulus n: "))
d = attack(e, n)

if d == None:
	sleep(1)
	print("cannot retrieve the private key, exiting...")
	sleep(1)
	os._exit(1)
else:
	choice = input("Do you want to decrypt a ciphertext ? y/n : ")
match choice:
	case "y":
		c = int(input("Enter the ciphertext c: "))
		m = pow(c, d, n)
		plain = bytearray.fromhex(hex(m)[2:]).decode()
		sleep(1)
		print(f'Here is the plain text: {plain}')
		sleep(1)
		os._exit(0)

	case "n":
		sleep(1)
		print(f'Here is the private key: {d}, exiting....')
		os._exit(0)

