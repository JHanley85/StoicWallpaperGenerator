def stringBreaker(font_size, x, y, input_text):
    length = (1920 - x) / (font_size / 2)
    formatted_lines = []
    leftover_line = ''
    total_line_height = y

    for line in input_text:
        if total_line_height > 610:

            length += 1
        else:
            length -= 1

        new_line = ''

        words = line.split()

        for word in words:

            if len(new_line) + len(word) >= length:
                formatted_lines.append(new_line)
                total_line_height += font_size
                new_line = ''
                leftover_line += word + " "

            elif len(leftover_line) + len(word) < length:
                leftover_line += " " + word

            elif len(leftover_line) + len(word) > length:
                new_line += leftover_line
                formatted_lines.append(new_line)
                total_line_height += font_size
                new_line = ''
                leftover_line = word
        # total_line_height += font_size/2

    if len(leftover_line) > 0:
        formatted_lines.append(leftover_line)
        total_line_height += font_size
        leftover_line = ""

    if total_line_height > 990:
        if length < 190 and font_size == 20:
            print(length)
            print("Text to long! Reformatting with longer lines")

            return stringBreaker(font_size, x*0.9, y, input_text)

        print("Text to long! Reformatting with smaller font")
        return stringBreaker(20, x, y, input_text)


    return formatted_lines
