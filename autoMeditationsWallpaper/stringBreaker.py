
def stringBreaker(lenght, step, input_text):
    formated_lines = []
    leftover_line = ''
    line_number = 1
    for line in input_text:
        if line_number >= 19:

            lenght += step
        else:
            lenght -= step*0.3

        new_line = ''

        words = line.split()

        for word in words:

            if len(new_line) + len(word) >= lenght:
                formated_lines.append(new_line)
                line_number += 1
                new_line = ''
                leftover_line += word + " "

            elif len(leftover_line) + len(word) < lenght:
                leftover_line += " " + word

            elif len(leftover_line) + len(word) > lenght:
                new_line += leftover_line
                formated_lines.append(new_line)
                line_number += 1
                new_line = ''
                leftover_line = word
        lenght -= step

    if len(leftover_line) > 0:
        formated_lines.append(leftover_line)
        line_number += 1
        leftover_line = ""
    return formated_lines

