# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    n = int(input())
    #print(4%5)
    #print(4/5)
    for _ in range(n):
        cc = str(input())
        #print(cc)
        flag = 0
        count = 0
        patt = 0
        valid = 1
        #print(cc[0])
        if len(cc) <= 19:
            #print("Length is %i " % len(cc) )
            if cc[0] >= str(4) and cc[0] <= str(6):
                #print("First digit is valid")
                for i in range(len(cc)):
                    #print(cc[i])
                    if flag == 0:
                        patt = cc[i]
                        count = 0
                        flag = 1
                    if cc[i] == "-":
                        #print(i,float((i) % 5))
                        if float((i)%5) == float(0):
                            #print(i,float((i)%5))
                            print("Invalid")
                            valid = 0
                            break
                        else:
                            continue
                    if cc[i]>=str(0) or cc[i]<=str(9):
                        if patt == cc[i]:
                            count += 1
                        else: flag = 0
                        if count == 4:
                            print("Invalid")
                            #print("Count is 4")
                            valid = 0
                            break
                if valid == 1:
                    print("Valid")
            else :
                #print("Loop exited")
                print("Invalid")

        else:
            # print("Loop exited")
            print("Invalid")







# 61234-567-8912-3456
#
# 1111-2222-3333-4444
# My Out : Valid
# Ex Out : Invalid




