input = open('input', 'r')
Lines = input.readlines()


count=0
n=0

for line in Lines:
    n=n+1
    line = line.strip()
    elfs = line.split(",")
    elf1 = elfs[0].split("-")
    elf2 = elfs[1].split("-")
    if int(elf1[1]) < int(elf2[0]) or  int(elf2[1]) < int(elf1[0]) :
        #print( elf1, elf2)
        count = count + 1
    


print ( n-count )
