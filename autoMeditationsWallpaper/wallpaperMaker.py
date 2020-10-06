from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from autoMeditationsWallpaper.textFormatter import TextFormatter


def number_to_word(i):
    if i == 1:
        return "First"
    elif i == 2:
        return "Second"
    elif i == 3:
        return "Third"
    elif i == 4:
        return "Forth"
    elif i == 5:
        return "Fifth"
    elif i == 6:
        return "Sixth"
    elif i == 7:
        return "Seventh"
    elif i == 8:
        return "Eight"
    elif i == 9:
        return "Ninth"
    elif i == 10:
        return "Eleventh"
    elif i == 11:
        return "Eleventh"
    elif i == 12:
        return "Twelfth"
    else:

        print("wrong input in word_to_number")
        return "ERROR: Book does not exist!"


# def textToImage(text, book):
#     img = Image.open("C:\\Users\Lord of Eight peaks\\PycharmProjects\\StoicWallpaperGenerator\\autoMeditationsWallpaper\\MarcusAureliusWallpaper.png")
#     draw = ImageDraw.Draw(img)
#     draw.text((65, 700), (word_to_number(book)), (233, 67, 115), ImageFont.truetype("timesbd.ttf", 50))
#
#     number_of_lines = 0
#     font_size = 40 - float(len(text)) * 0.4
#     if font_size < 20:
#         font_size = 20
#
#     font = ImageFont.truetype("timesi.ttf", int(font_size))
#     text = stringBreaker(220 - font_size * 4, 1, text)
#
#     x = 530 + font_size * 0.5
#     y = 60
#     for line in text:
#
#         draw.text((x, y), line, (233, 67, 115), font=font)
#         if number_of_lines * 2 + font_size * 1.2 < 72:
#             x += font_size * 0.55
#
#         else:
#             x -= font_size * 0.4
#
#         y += 4 + font_size
#
#         number_of_lines += 1
#
#     img.save("sample-out.png")

def textToImage(text, book):
    img = Image.open(
        "C:\\Users\Lord of Eight peaks\\PycharmProjects\\StoicWallpaperGenerator\\autoMeditationsWallpaper\\MarcusAureliusWallpaper.png")
    draw = ImageDraw.Draw(img)
    draw.text((65, 700), "The " + (number_to_word(book)) + " Book", (233, 67, 115),
              ImageFont.truetype("timesbd.ttf", 50))




    x = 550
    y = 60
    #
    # text = stringBreaker(font_size, x, y, text)
    obj = TextFormatter(text, (1920 - x), (1920 - (x-x/2)), 990, 550, 35, 18)

    obj.format_input_string()


    font = ImageFont.truetype("timesi.ttf", obj.fontSizeMax)



    for line in obj.formatted_lines:

        draw.text((x, y), line, (233, 67, 115), font=font)
        if y < 610:
            x += obj.fontSizeMax / 2


        else:
            x -= obj.fontSizeMax / 2

        y += obj.fontSizeMax

    img.save("sample-out.png")
