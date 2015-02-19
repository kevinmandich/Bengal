points= []

def isGoodPoint(x,y):
	xs=str(abs(x))
	ys=str(abs(y))
	xsum=0
	ysum=0
	for c in xs:
		xsum=xsum+int(c)
	for c in ys:
		ysum=ysum+int(c)
	if xsum+ysum <=19:
		return True

def addGoodNeighbors(x,y):
	if isGoodPoint(x+1,y) and [x+1,y] not in points: points.append([x+1,y])
	if isGoodPoint(x-1,y) and [x-1,y] not in points: points.append([x-1,y])
	if isGoodPoint(x,y+1) and [x,y+1] not in points: points.append([x,y+1])
	if isGoodPoint(x,y-1) and [x,y-1] not in points: points.append([x,y-1])

points.append([0,0]) # the starting point

i=0
while True:
	addGoodNeighbors(points[i][0],points[i][1])
	i=i+1
	print len(points)
	if i>=len(points): break


print len(points)
