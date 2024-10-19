import emoji

string = input("Input: ")

emojized = emoji.emojize(string, language='alias')

print(f"Output: {emojized}")
