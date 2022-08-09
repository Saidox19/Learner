from audioop import avg
from gettext import install


weight = [60.2, 48.4, 63.1, 79.2, 71.5]

print(max(weight))
print(min(weight))

#Define a function
def average(a):
    av = sum(a)
    lt = len(a)
    cd = av / lt
    return cd


print(average(weight))
