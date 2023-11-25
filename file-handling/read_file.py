# read file

file = open("names.txt", "r")
data = file.read()
file.close()

print(data)