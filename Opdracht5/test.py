import math
from Vector import Vector

u =Vector ( 3, [1,2,3])
v = Vector (3,3.5)
w = u.lincomb(v,10,1)
print(math.sqrt(u.inner(u)))
print(u.norm())

print(w)