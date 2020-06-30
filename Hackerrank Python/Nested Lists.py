
list = []
least = []
def nested():
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([name,score])
    findleast()
    print(list)
    #print(list[0][1])

def findleast():
    flag = 0
    low = 0
    l = len(list)
    for i in range(l):
        print(i)
        print(list[i][1])
        if i != l:
         if list[i][1] < list[i+1][1]:
             if low == 0:
                 least[0] = list[i][1]
                 low = 1
             else:
                 least[1] = list[i][1]





nested()