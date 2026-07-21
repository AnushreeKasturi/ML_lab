def max(s):
    max_char=""
    max_count=0
    for ch in s:
        if ch.isalpha():
            count=s.lower().count(ch.lower())
            if count>max_count:
                max_count=count
                max_char=ch.lower()
    return max_count,max_char
def main():
    text=input("enter a string")
    character,count=max(text)
    print("highest occuring character",character)
    print("max count is",count)
main()
