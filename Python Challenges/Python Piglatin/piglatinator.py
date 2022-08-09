def main():
    words = input("What would you like to translate into Pig-Latin? \n")

    words = words.split()

    for each_word in range(len(words)):
        word = words[each_word]

        if word[0] in [ 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            words[each_word] = word +'ay'    
        else:
            words[each_word] = word[1:]+word[0]+'ay'

    return ' '.join(words)

piglatin = main()
print(piglatin)