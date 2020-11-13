import csv
from math import cos, sin, radians
input_file="wheelData.csv"
anglist = []
distlist=[]
xlist=[]
ylist=[]
prevx=0
prevy=0
totangle=0
with open(input_file,"rb") as pos_input:
	csv_reader = csv.reader(pos_input)
	csv_reader.next()
	for row in csv_reader:
         angle=float(row[0])
         #print angle
         distance=float(row[1])
         #print distance
         anglist.append(angle)
         distlist.append(distance)


for i in range(len(distlist)):
    ang=anglist[i]
    dist=distlist[i]
    ang  = -ang
    tempx=dist*(sin(radians(ang)))
    tempy=dist*cos(radians(ang))    
    #print str(tempx) + "     " + str(tempy)
    x=tempx*cos(radians(totangle))+tempy*sin(radians(totangle))
    y=-tempx*sin(radians(totangle))+tempy*cos(radians(totangle))
    x = x + prevx
    y = y + prevy
    totangle = totangle - ang
    prevx = x
    prevy = y
    #print ("Total Angle: ", totangle)
    xlist.append(y)
    ylist.append(x)
    #print "X: ",x
    #print "Y: ",y

filehandle=open("generatedXY.csv","w")
writer = csv.writer(filehandle)
writer.writerow(["x","y"])
for i in range(len(xlist)):
    x=xlist[i]
    y=ylist[i]
    writer.writerow([x,y])
filehandle.close()    
'''
    if(totangle>360):
        totangle=totangle-360
    if(totangle>=0 and totangle<90):
        x=x
        y=y
    if(totangle==90):
        x=prevx+x
        y=prevyy
    if(totangle>90 and totangle<180):
        x=prevx-x
        y=prevy+y
    if(totangle==180):
        x=x
        y=prevy-y
    if(totangle>180 and totangle<270):
        x=prevx+x
        y=prevy+y
    if(totangle==270):
        x=prevx-x
        y=y
    if(totangle>270 and totangle<360):
        x=prevx-x
        y=prevy+y
        
    prevx=x
    prevy=y
'''    
    
   
