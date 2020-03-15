# -*- coding: utf-8 -*-
import sys
import unicodedata


def print_unicode_table(words):
    print("decimal hex chr {0:^40}".format("name"))
    print("------- ----- --- {0:-<40}".format(""))

    code = ord(" ")
    end = sys.maxunicode

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        if words is None or string_has_all_substrings(name.lower(), words):
            print("{0:7} {0:5X} {0:^3c} {1}".format(code, name.title()))
        code += 1
# End print_unicode_table


def string_has_all_substrings(string, substrings_list):
    for word in substrings_list:
        if word not in string:
            return False
    return True


# Start main script
words = []

if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [{{strings}}]".format(sys.argv[0]))
        words = None
    else:
        words = [arg.lower() for arg in sys.argv[1:]]

if words is not None:
    print_unicode_table(words)

# End main script
