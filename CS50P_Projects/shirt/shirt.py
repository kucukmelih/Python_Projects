import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")

    extensions = [".jpg", ".jpeg", ".png"]
    ext1 = os.path.splitext(sys.argv[1])[1]
    ext2 = os.path.splitext(sys.argv[2])[1]

    if ext1 == ext2 and ext1 in extensions:
        try:
            user_image = Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("Input file not found")

        try:
            shirt = Image.open("shirt.png")
        except FileNotFoundError:
            sys.exit("Shirt image not found")

        size = shirt.size
        user_image = ImageOps.fit(user_image, size)
        user_image.paste(shirt, (0, 0), shirt)
        user_image.save(sys.argv[2])
    else:
        sys.exit("Input and output have different extensions")

if __name__ == "__main__":
    main()
