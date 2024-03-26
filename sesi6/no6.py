for i in range(1,6):
    for j in range(1,6):
        if((i == 1 and j == 1)or(i == 1 and j == 2)or(i == 1 and j == 3)or(i == 1 and j == 4)):
            print("+"*1,end=' ')
        elif((i == 2 and j == 1)or(i == 2 and j == 2)or(i == 2 and j == 3)):
            print("+"*1,end=' ')
        elif((i == 3 and j == 1)or(i == 3 and j == 2)):
            print("+"*1,end=' ')
        elif((i == 4 and j == 1)):
            print("+"*1,end=' ')
        else:
            print(j,end=' ')
    print()