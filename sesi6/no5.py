for i in range(2,7):
    for j in range(1,6):
        if(i == 2 and j == 4 or i == 2 and j == 5):
            print(j+2, end=' ')
        elif((i == 5 and j == 3)or(i == 5 and j == 4)or(i == 5 and j == 5)):
            print((i-1)*j+1,end=' ')
        elif(i == 6 and j == 3):
            print((i-1)*j,end=' ')
        elif((i == 6 and j == 4)or(i == 6 and j == 5)):
            print((i-2)*j+3,end=' ')
        else:
            print(j*i-1, end=' ') 
    print()

