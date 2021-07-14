import csv
import math
with open("numbers",newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)
data=filedata.pop(0)
def mean(data):
    m=len(data)
    total=0
    for i in data:
        total=total+i
    mean=total/m
    return mean
l=[]
for j in data:
    f=int(j)-mean(data)
    f=f**2
    l.append(f)
sum=0
for h in l:
    sum=sum+h
result=sum/(len(data)-1)
standarddeviation=math.sqrt(result)
print(standarddeviation)

