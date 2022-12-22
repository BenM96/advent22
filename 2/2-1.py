input = open('input', 'r')
Lines = input.readlines()

score=0

for line in Lines:
    line = line.strip()
    hands = line.split()
    print(hands)
    if hands[1] == "X":
        score = score + 1
        if hands[0] == "C" :
            score = score + 6
        if hands[0] == "A":
            score = score + 3
    if hands[1] == "Y" :
        score = score + 2
        if hands[0] == "A":
            score = score + 6
        if hands[0] == "B":
            score = score + 3
    if hands[1] == "Z":
        score = score + 3
        if hands[0] == "B":
            score =  score + 6
        if hands[0] == "C":
            score = score + 3



print (score)

