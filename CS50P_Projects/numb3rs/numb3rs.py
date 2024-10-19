import re

"""
    #.#.#.#  and  # -> (0 - 255)
"""

def main():
    if validate(input("IPv4 Address: ")):
        print("Valid")
    else:
        print("Invalid")

def validate(ip):
    if not re.fullmatch(r"(\d{1,3}\.){3}\d{1,3}", ip):
        return False

    try:
        octets = ip.split(".")
        for octet in octets:
            if not (0 <= int(octet) <= 255):
                return False
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
