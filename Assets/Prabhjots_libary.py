__author__ = 'prabh_000'


def ui(*args, border_width=5,
       border_symbol="="):  # this function gets what the user wants to prints and puts it into a list
    # then it send it to another function, it also gets the lenght of the biggiest word
    # and then prints that length of the symbol thyey want to print

    txt_lines = []
    for arg in args:
        txt_lines.append(arg)

    longest_word = max(txt_lines, key=len)
    inner_width = len(longest_word) + 10

    if inner_width < 60:
        inner_width = 60

    border(border_width, inner_width, border_symbol)
    lines(txt_lines, inner_width=inner_width, border_width=border_width, border_symbol=border_symbol)
    border(border_width, inner_width, border_symbol)


def ui_title(title, border_symbol="="):  # this does the same as ui() but only accepts one thing to print
    title = " " + title
    inner_len = len(title) + 10
    if inner_len < 60:
        inner_len = 60
    extra_space = inner_len - len(title)
    print(border_symbol * 5 + border_symbol * inner_len + border_symbol * 5)
    print(border_symbol * 5 + title + " " * extra_space + border_symbol * 5)


def border(border_width, inner_width, border_symbol):  # this prints the lenght of the biggest word in the border symbol
    length = int(border_width + inner_width + border_width)

    print(str(border_symbol) * length)


def lines(*args, inner_width, border_width=5,
          border_symbol="="):  # this prints the syblos around the text and then the text

    txt_lines = []
    for arg in args:
        txt_lines.append(arg)

    for lines in txt_lines:
        for line in lines:
            txt = " " + line
            extra_space = inner_width - len(txt)
            print(border_symbol * border_width + str(txt) + " " * extra_space + border_symbol * border_width)


def ui_input(arg, border_width=5, border_symbol="="):  # this does the same thing but returns a input
    inner_width = len(arg) + 10
    if inner_width < 60:
        inner_width = 60
    extra_space = 60 - len(arg) - 1

    return input(border_symbol * border_width + " " + arg + " ").upper()


def new_page():  # this prints lots of new lines to break up all the diffrents things that have been printed
    print("\n" * 100)
