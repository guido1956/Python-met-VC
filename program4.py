aantal_stappen = [2300, 4500,7056,3403]
telop =0 
aantal = 0
max = 0
min = 100000 
for stap in aantal_stappen:
    print(stap)
    telop += stap
    aantal = aantal + 1
    if stap > max:
        max = stap
    if stap < min:
        min = stap
        
print("Gemiddeld gelopen: " + str(telop/aantal))
print("minst aantal     :" + str(min))
print("max aantal       :"  + str(max))