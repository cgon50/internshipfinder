from csv import *
CnL={}
holder=[]
with open("links.csv",mode="r") as f:
    freader= reader(f,delimiter=",")
    for row in freader:
        holder.append(row)
CnL={row[0]:row[1] for row in holder}
#print(CnL)  
for k,v in CnL.items():
    print(f"Company:{k} link{v} ")
        

