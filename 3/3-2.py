input = open('input', 'r')
Lines = input.readlines()


total = 0 
n=0

for line in Lines:
    n=n+1
    line = line.strip()

    items = [*line]
    if n==1:
        elf1=items
    if n==2:
        elf2 = items
    if n == 3:
        n=0
        elf3 = items
        for item in elf1 :
            if item in elf2 and item in elf3:
                print (item)
                inum = ord(item)
                if inum >= 97 :
                    priority = inum -96
                else :
                    priority = inum - 64 + 26
                total = total + priority
                break

print (total)
