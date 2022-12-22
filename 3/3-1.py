input = open('input', 'r')
Lines = input.readlines()


total = 0 

for line in Lines:
    line = line.strip()

    items = [*line]
    half_local= int(len(items)/2)
    comp1 = items[0:half_local]
    comp2 = items[half_local:]

    for item in comp1:
        if item in comp2:
            print (item)
            inum = ord(item)
            if inum >= 97 :
                priority = inum -96
            else :
                priority = inum - 64 + 26
            total = total + priority
            break


print (total)
