d = {i: (i-1)*i for i in range(1, 31)}
print(d)


for key, value in d.items():
    print(key, value)



total = 0
for value in d.values():
    total += value
print(total)


user_input = input("Enter a key to remove from the dictionary: ")
if user_input.isdigit() and int(user_input) in d:
    d.pop(int(user_input))
print(d)


divided = {'Tony': 41, 'Rhodey': 43, 'Nat': 35}
we_fall = {'Steve': 39, 'Clint': 35, 'Wanda': 28}
united_we_stand = {**divided, **we_fall}
print("{:<10} {:<10}".format('Name', 'Age'))
for key, value in united_we_stand.items():
    print("{:<10} {:<10}".format(key, value))


united_we_stand.pop('Nat', None)
print(united_we_stand)


for key in sorted(united_we_stand):
    print(key, united_we_stand[key])


values = united_we_stand.values()
print("Maximum value:", max(values))
print("Minimum value:", min(values))
