# Written By Matteo Vidali


# -------------------------- Required Functions ------------------------------------------------------------------

# This function takes a file name/path to file, and reads its contents in to a list of strings that each contain one
# Line of the given file.


def enlist_file(fn):
    strings = []                    # Making an empty list
    with open(fn) as file:          # Opens File
        for line in file:           # Loops over file
            strings.append(line)    # appends strings list with another line
    file.close                      # redundant close (the with function closes automatically) just there to confirm
    return strings                  # returns the list of strings


# This function takes a string (line) input, and a string including a comment character "/*" or "//"
# It searches text for these symbols, and returns a tuple which has the text before and after the comment character.


def split_comment(l, cs):
    if l.find(cs) != -1:                            # find() returns -1 when it doesn't find anything
        index = l.find(cs)                          # A variable storing the location of the substring
        r = (l[0:index], l[index+len(cs):])         # A tuple with the return value
    else:
        r = (l, " ")                                # Returns two values, before/after the comment (not including symb)
    return r                                        # If there was no comment substring, it will return an empty string


# This function takes a path to a file and a list of strings. It then writes the list of strings to the file, with each
# Element in the string being a new line.


def write_file(fn, l):
    file = open(fn, "w")           # Opens a new file for writing (used this instead of 'with')
    for el in l:                   # Loops over the list of strings
        file.write(el)             # Writes each string to the file
    file.close()                   # Close file


# --------------------------- TEST CASES ---------------------------------------------------------------------

# This is a name == main test to check my code. It is a tester. It checks to see if i am running this code with some
# other code, in which case name != main, so it does not run this. Otherwise, it is running as its own program in which
# case it runs this code as if it was the main function of the code.
if __name__ == "__main__":

    # Opening two text files with my function, and writing some stuff to them
    write_file("a.txt", ["hello", "world", "this line // has a comment"])
    write_file("b.txt", ["this", "is", "python"])


    # Reading the new files into string-lists and printing them to check that everything worked well
    # the output should be [txt from string 1] [txt from string 2]
    b = enlist_file("b.txt")
    a = enlist_file("a.txt")
    print(b, a)


    # Splitting the previous files at specific comment markers the first of which will work, but the second one won't
    # be able to split because the substring does not exist in the second string - should output everything fine
    c, d = split_comment("this // comment", "//")
    e, f = split_comment("that ?? comment", "//")
    print(c, d)
    print(e, f)


