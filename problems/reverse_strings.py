#Based on the string below, generate a function that reverses it.

original = "prueba ejemplo"


def reverse(original):
	newString = ""

	i = len(original)-1

	while i >= 0:
		i-=1
		newString = newString + original[i]

	return newString

result = reverse(original);


print("Reverse strings: \nFrom:")
print(original)
print("-----------\nTo:")
print(result)
