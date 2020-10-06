from random import randrange

from autoMeditationsWallpaper.wallpaperMaker import textToImage


def findLines2():
    excerpts = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12],
                [1, 13], [1, 14], [1, 15], [1, 16], [1, 17], [2, 1], [2, 2], [2, 3], [2, 4], [2, 6], [2, 7], [2, 8],
                [2, 9], [2, 10], [2, 11], [2, 12], [2, 13], [2, 14], [2, 15], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5],
                [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12], [3, 13], [3, 14], [3, 15], [3, 16], [3, 17],
                [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [4, 11], [4, 12],
                [4, 13], [4, 14], [4, 15], [4, 16], [4, 17], [4, 18], [4, 19], [4, 20], [4, 21], [4, 22], [4, 23],
                [4, 24], [4, 25], [4, 26], [4, 27], [4, 28], [4, 29], [4, 30], [4, 31], [4, 32], [4, 33], [4, 34],
                [4, 35], [4, 36], [4, 37], [4, 38], [4, 39], [4, 40], [4, 41], [4, 42], [4, 43], [5, 1], [5, 2], [5, 3],
                [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [5, 12], [5, 13], [5, 14], [5, 15],
                [5, 16], [5, 17], [5, 18], [5, 19], [5, 20], [5, 21], [5, 22], [5, 23], [5, 24], [5, 25], [5, 26],
                [5, 27], [5, 28], [5, 29], [5, 30], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8],
                [6, 9], [6, 10], [6, 11], [6, 12], [6, 13], [6, 14], [6, 15], [6, 16], [6, 17], [6, 18], [6, 19],
                [6, 20], [6, 21], [6, 22], [6, 24], [6, 25], [6, 26], [6, 27], [6, 28], [6, 29], [6, 30], [6, 31],
                [6, 32], [6, 33], [6, 35], [6, 36], [6, 37], [6, 39], [6, 40], [6, 41], [6, 42], [6, 43], [6, 44],
                [6, 45], [6, 46], [6, 47], [6, 48], [6, 49], [6, 50], [6, 51], [6, 52], [6, 53], [6, 54], [7, 1],
                [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9], [7, 10], [7, 11], [7, 12], [7, 13],
                [7, 14], [7, 15], [7, 16], [7, 17], [7, 18], [7, 19], [7, 20], [7, 21], [7, 22], [7, 23], [7, 24],
                [7, 25], [7, 26], [7, 27], [7, 28], [7, 29], [7, 30], [7, 31], [7, 32], [7, 33], [7, 34], [7, 35],
                [7, 36], [7, 37], [7, 38], [7, 39], [7, 40], [7, 41], [7, 42], [7, 43], [7, 44], [8, 1], [8, 2], [8, 3],
                [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9], [8, 10], [8, 11], [8, 12], [8, 13], [8, 14], [8, 15],
                [8, 16], [8, 17], [8, 18], [8, 19], [8, 20], [8, 21], [8, 22], [8, 23], [8, 24], [8, 25], [8, 26],
                [8, 27], [8, 28], [8, 29], [8, 30], [8, 31], [8, 32], [8, 33], [8, 34], [8, 35], [8, 36], [8, 37],
                [8, 38], [8, 39], [8, 40], [8, 41], [8, 42], [8, 43], [8, 44], [8, 45], [8, 46], [8, 47], [8, 48],
                [8, 49], [8, 50], [8, 51], [8, 52], [8, 53], [8, 54], [8, 55], [8, 56], [8, 57], [8, 58], [9, 1],
                [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9], [9, 10], [9, 11], [9, 12], [9, 13],
                [9, 14], [9, 15], [9, 16], [9, 17], [9, 18], [9, 19], [9, 20], [9, 21], [9, 22], [9, 23], [9, 24],
                [9, 25], [9, 26], [9, 27], [9, 28], [9, 29], [9, 30], [9, 31], [9, 32], [9, 33], [9, 34], [9, 35],
                [9, 36], [9, 37], [9, 38], [9, 39], [9, 40], [9, 41], [9, 42], [9, 43], [10, 1], [10, 2], [10, 3],
                [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10], [10, 11], [10, 12], [10, 13], [10, 14],
                [10, 15], [10, 16], [10, 17], [10, 18], [10, 19], [10, 20], [10, 21], [10, 22], [10, 23], [10, 25],
                [10, 26], [10, 27], [10, 28], [10, 29], [10, 30], [10, 31], [10, 32], [10, 33], [10, 34], [10, 35],
                [10, 36], [10, 37], [10, 38], [11, 1], [11, 2], [11, 3], [11, 4], [11, 5], [11, 6], [11, 7], [11, 8],
                [11, 9], [11, 10], [11, 11], [11, 12], [11, 13], [11, 14], [11, 15], [11, 16], [11, 17], [11, 18],
                [11, 19], [11, 20], [11, 21], [11, 22], [11, 23], [11, 24], [11, 25], [11, 26], [11, 27], [11, 28],
                [11, 29], [11, 30], [11, 31], [12, 1], [12, 2], [12, 3], [12, 4], [12, 5], [12, 6], [12, 7], [12, 8],
                [12, 9], [12, 10], [12, 11], [12, 12], [12, 13], [12, 14], [12, 15], [12, 16], [12, 17], [12, 18],
                [12, 19], [12, 20], [12, 21], [12, 22], [12, 23], [12, 24], [12, 25], [12, 26], [12, 27]]

    randomExcerpt = randrange(1, len(excerpts))
    print(excerpts[randomExcerpt])
    print(excerpts[randomExcerpt])
    print(randomExcerpt)



    start_string = excerpts[randomExcerpt][1]
    end_string = start_string + 1
    text = []
    #with open('C:\\Users\\Lord of Eight peaks\\PycharmProjects\wallpaperChanger\\autoMeditationsWallpaper\\meditations\\book' + str(1) + '.txt', 'rt') as myfile:
    with open('C:\\Users\\Lord of Eight peaks\\PycharmProjects\wallpaperChanger\\autoMeditationsWallpaper\\meditations\\book' + str(excerpts[randomExcerpt][0]) + '.txt', 'rt') as myfile:

        for line in myfile:

            if len(line) > 1:
                first_word = line.split()[0]
                if first_word == int_to_Roman(end_string) + ".":

                    break
                elif first_word == int_to_Roman(start_string) + ".":

                    text.append(line.rstrip('\n'))
                elif len(text) != 0:

                    text.append(line.rstrip('\n'))


    textToImage(text, excerpts[randomExcerpt][0])


def int_to_Roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

