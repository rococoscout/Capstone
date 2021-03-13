
def tokenize(text):

    removables = (".", ",", "?", ";", ":", "-", "_", "#", "!", "=", "+", "*", "^", "%", "$", "@", "~", "`", "|", "'", "{", "}", "/", "\"", "\\", "(", ")", "[", "]", "&", "<", ">", "  ", "   ")
    text = text.lower()
    for r in removables:
        text = text.replace(r, "")
    tokens = text.strip().split()

    return tokens

if __name__ == '__main__':

    import sys
    text = input("Enter input: ")
    clean = tokenize(text)
    print(clean)
