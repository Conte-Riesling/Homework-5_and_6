# Використання функції zip для створення словника
keys = ["a", "b", "c"]
values = [10, 20, 30]
dict = {key:value for key, value in zip(keys, values)}
print(dict)