# Результатом должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты
# площадь пи а б Б а и б длины полуосей эллипса
import math
orbits=[(1,3),(3,10),(7,2),(6,6),(4,3)]
max=0
result=0
for i in range(len(orbits)):
    if sum(orbits[i])>max:
        max=sum(orbits[i])
        result=orbits[i]
print(result)

#sort_orbit = [sum(x) for x in range(len(orbits)) if sum(x)>max ]
#mult=list([sum(x)*math.pi() for x in range(len(orbits))])
#Sort_orbit=[x for x in range(len(mult))]
