# Open the file
# Hocam soruyu yanlis anlayip dosyayi okutarak yaptim, emek verdigim icin silesim gelmedi.
# Istenilen sekilde tek eklemem gereken kisim array e_words = [word for word in words if word.startswith("e")] bu sekilde kolay sekilde istenilen cozumu yapabilirdim.
with open('1000words.txt', 'r') as file:
    contents = file.read()
    start = contents.index('[')
    end = contents.rindex(']')

    word_str = contents[start:end]

    words = [word.strip('"') for word in word_str.split(',')]
    print("Words starting with 'e':")
    for word in words:
        if word.startswith('e'):
            print(word)

    print("\nWords starting with 'ha':")
    for word in words:
        if word.startswith('ha'):
            print(word)


a = int(input("Please enter a number between 3 and 9: "))

if a < 3 or a > 9:
    print(" Number must be between 3 and 9.")
else:
    for i in range(1, a + 1):
        print('*' * i)
        if i == a:
            for j in range(a - 1, 0, -1):
                print('*' * j)
