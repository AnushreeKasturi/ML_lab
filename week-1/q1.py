def count(l):
    count=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==10:
                print(l[i],l[j])
                count=count+1
            
    return count
def main():
    lst=[2,7,4,1,3,6]
    total=count(lst)
    print("the total no of pairs is ",total)
main()