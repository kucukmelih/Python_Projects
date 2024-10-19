def main():
    word = str(input("Input: ")).strip()
    result = shorten(word)
    print(result)

def shorten(word):
    x = ['A','a','E','e','I','i','O','o','U','u']
    result = ""
    for i in word:
        if i not in x:
            result += i
    return result

if __name__ == "__main__":
    main()

