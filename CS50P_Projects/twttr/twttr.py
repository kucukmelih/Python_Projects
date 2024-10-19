def main():
    word = str(input("Input: ")).strip()
    shorten(word)

def shorten(word):
    x = ['A','a','E','e','I','i','O','o','U','u']
    for i in word:
        if i in x:
            print("",end="")
        else: print(i,end="")
    print()

if __name__ == "__main__":
    main()

