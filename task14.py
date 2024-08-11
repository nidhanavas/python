t_keys = ["Rash", "Kil", "Varsha"]
t_values = [1, 4, 5]
print("Original key list is : " + str(t_keys))
print("Original value list is : " + str(t_values))
res = {}
for key in t_keys:
    for value in t_values:
        res[key] = value
        t_values.remove(value)
        break
print("Resultant dictionary is : " + str(res))