import string

french_words = ["bonjour",  "oui", "non", "merci", "fille", "garçon"]

def check_line(line):
    word_count = 0
    words = line.split(" ")
    for word in words:
        word = word.strip(string.punctuation).lower()
        if word in french_words:
            word_count += 1
            print(f"Found this French word: {word}")

    return word_count

def check_file(filename):
    with open(filename) as myfile:
        word_count = 0
        for line in myfile:
            word_count += check_line(line)

        
    if word_count == 0:
        print("Now you're an English Pro!")

if __name__ == '__main__':
    check_file("doc.txt")
    check_line("Hello I am Frenchie, a fille, and my friend is James a Garçon.")
