from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from autoMeditationsWallpaper.stringBreaker import stringBreaker


def word_to_number(i):
    if i == 1:
        return "The First Book"
    elif i == 2:
        return "The Second Book"
    elif i == 3:
        return "The Third Book"
    elif i == 4:
        return "The Forth Book"
    elif i == 5:
        return "The Fifth Book"
    elif i == 6:
        return "The Sixth Book"
    elif i == 7:
        return "The Seventh Book"
    elif i == 8:
        return "The Eight Book"
    elif i == 9:
        return "The Ninth Book"
    elif i == 10:
        return "The Eleventh Book"
    elif i == 11:
        return "The Eleventh Book"
    elif i == 12:
        return "The Twelfth Book"
    else:

        print("wrong input in word_to_number")
        return "ERROR: Book does not exist!"


def textToImage(text, book):
    img = Image.open("C:\\Users\\Lord of Eight peaks\\PycharmProjects\\wallpaperChanger\\autoMeditationsWallpaper\\MarcusAureliusWallpaper.png")
    draw = ImageDraw.Draw(img)
    draw.text((65, 700), (word_to_number(book)), (233, 67, 115), ImageFont.truetype("timesbd.ttf", 50))

    number_of_lines = 0
    font_size = 40 - float(len(text)) * 0.4
    if font_size < 20:
        font_size = 20

    font = ImageFont.truetype("timesi.ttf", int(font_size))
    text = stringBreaker(220 - font_size * 4, 1, text)

    x = 530 + font_size * 0.5
    y = 60
    for line in text:

        draw.text((x, y), line, (233, 67, 115), font=font)
        if number_of_lines * 2 + font_size * 1.2 < 72:
            x += font_size * 0.55

        else:
            x -= font_size * 0.4

        y += 4 + font_size

        number_of_lines += 1

    img.save("sample-out.png")
