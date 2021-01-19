import subprocess

names = []
passwords = []
validchars = ["y", "n", "Y", "N"]

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if 'All User Profile' in i]
for i in profiles:
	results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, 'key=clear']).decode('utf-8').split('\n')
	results = [b.split(":")[1][1:-1] for b in results if 'Key Content' in b]
	try:
		print("{:<30}| {:<}".format(i, results[0]))
		names.append(i)
		passwords.append(results[0])
	except  IndexError:
		print("{:<30}| {:<}".format(i, ""))
		names.append(i)
		passwords.append("")

op = input("do you want to save the passwords? [y/n]: ")

while not isinstance(op, str) or op not in validchars:
	print("invalid input")
	op = input("do you want to save the passwords? [y/n]:")

if op == "y" or op == "Y":
	f = open("passwords.txt", "wt")
    
	for j in range(len(i)):
		f.write(f"{names[j]} - {passwords[j]}")
		f.write("\n")

	f.close()
	print("Names and passwords saved.")
	input("Press any key to exit...")
   
   
