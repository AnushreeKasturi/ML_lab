def calc_range(lst):
    if len(lst)<3:
        print("Range determination not possible")
    return max(lst)-min(lst)
def main():
    l=[5,3,8,1,0,4]
    range=calc_range(l)
    print("the range of the list is",range)
main()