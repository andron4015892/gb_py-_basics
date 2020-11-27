from itertools import count
from itertools import cycle

for el in count(1):
    if el > 4:
        break
    else:
        print(el)

control = 0
for el in cycle(["one", 34, 52.3, "doubl"]):
    if control > 3:
        break
    else:
        print(el)
        control += 1
