count = 0
with open("result.txt","r") as f:
    for i,line in enumerate(f):
        if i % 28 == 0:
            if line[0] == line[1]:
                count += 1
print(count/(i//29))
