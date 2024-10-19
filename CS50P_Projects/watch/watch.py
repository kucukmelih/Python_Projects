import re

def main():
    html_input = input("HTML: ")
    print(parse(html_input))

def parse(s):
    match = re.search(r'<iframe[^>]*src="([^"]*)"', s)
    if not match:
        return None

    src = match.group(1)

    match = re.search(r'youtube\.com/embed/([^"?]*)', src)
    if not match:
        return None

    video_id = match.group(1)

    return f'https://youtu.be/{video_id}'

if __name__ == "__main__":
    main()
