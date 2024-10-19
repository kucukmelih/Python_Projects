import random

def main():
    level = get_level()
    generate_integer(level)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except ValueError:
            continue
    return level

def generate_integer(level):
    score = 0
    for i in range(10):
        trials = 0  
        if level == 1:
            n1 = random.randint(0,9)
            n2 = random.randint(0,9)
        elif level == 2:
            n1 = random.randint(10,99)
            n2 = random.randint(10,99)
        else:
            n1 = random.randint(100,999)
            n2 = random.randint(100,999)

        while trials < 3:
            print(f"{n1} + {n2} = ", end = "")
            try:
                user_answer = int(input())
            except ValueError:
                print('EEE')
                trials += 1
                continue

            answer = n1 + n2

            if user_answer == answer:
                score += 1
                break
            else:
                print('EEE')
                trials += 1

        if trials == 3:
            print(f"{n1} + {n2} = {answer}")

    print(f"Score: {score}")

if __name__ == "__main__":
    main()
