from tony_classexp2 import frac

rf = frac(2,7)
uf = frac(8,6)

rf.setNumerator(3)

rf.setDenominator(17)

rf.fprint()

print(rf)

if rf.equal(uf):
	print("are equal")
else:
	print("not equal")

if rf==uf:
	print("equal")
else:
	print("not equal")

result = rf+uf
print (result)

if rf!=uf:
	print("not equal")
else:
	print("equal")

if rf < uf:
	print ("small")
else:
	print ("not greater or equal")

rf = frac(-2,15)
af = abs(rf)
print(af)














