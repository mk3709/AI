
total=int(input('Total bananas: ')) #taking inputs A, B, C
distance=int(input('Distance to cover: '))
load_capacity=int(input('Max Load capacity: '))
lost=0 #bananas lost in (calculated incrementally for each mile)
rem = total # essentially bananas rem (at starting point) - after camel consumes
for i in range(distance):
while rem>0: #base condition
rem=rem-load_capacity
if rem==1:
lost=lost-1 #Loss is decreased - covering up and down for that one banana
lost=lost+2 #normal condition : losing 2 bananas per mile
lost=lost-1 #last round
rem=total-lost
if rem==0:
print("Not a single banana can be transferred to the market")
break
print("Ans: " + str(rem)
