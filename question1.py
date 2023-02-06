#print all number in between 1500 and 2701 which are divisible by 7 bt not
#a multiple of 5
sl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5!=0):
        sl.append(str(x))
print (',','\n'.join(nl))