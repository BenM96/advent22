input = open('input', 'r')
Lines = input.readlines()


count=0

for line in Lines:
    line = line.strip()
    elfs = line.split(",")
    elf1 = elfs[0].split("-")
    elf2 = elfs[1].split("-")
    if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]) :
        #print( elf1, elf2)
        count = count + 1
    elif int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1]):
        #print( elf1, elf2)
        count = count + 1
    
    #if elf1[0] == elf2[0] and elf1[1] == elf2[1] :
    #    count = count - 1


print ( count )
