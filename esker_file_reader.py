import sys

def read_file(file_name):
    try:
        # open the file and attempt to parse it
        with open(file_name) as file:
            report = []
            # dictionary used to store word length frequency
            length_frequency = {}
            char_count = 0
            line_count = 0
            word_count = 0
            letter_count = 0
            figure_count = 0
            other_count = 0
            # loop through every line of the file
            for line in file:
                line_count += 1
                char_count += len(line)
                # loop through every substring/word
                for word in line.split():
                    # this boolean is used to omit substrings that don't contain letters or other chars
                    only_digits = True
                    # this boolean is used to omit substrings that don't contain numbers or letters
                    only_other = True
                    # loop through every char in a substring/word
                    for c in word:
                        # check if the char is a digit
                        if c.isdigit():
                            figure_count += 1
                            only_other = False
                        # check if the char is a letter
                        elif c.isalpha():
                            letter_count += 1
                            only_digits = False
                            only_other = False
                        # check if the char is some other character
                        else:
                            other_count += 1
                            only_digits = False
                    # only increment the word_count if the substring/word has ONLY numbers
                    if only_digits != True and only_other != True:
                        word_count += 1

                        # count the word length frequency of valid words
                        word_length = len(word)
                        if word_length in length_frequency:
                            length_frequency[word_length] += 1
                        else:
                            length_frequency[word_length] = 1

            # sort the word frequency dictionary from smallest to largest
            sorted_dict = dict(sorted(length_frequency.items(), key=lambda item: item[0]))         

            # store the report fields in an array that will be used to print the report
            report.append(file.name)
            report.append(line_count)
            report.append(char_count)
            report.append(letter_count)
            report.append(figure_count)
            report.append(other_count)
            report.append(word_count)
            report.append(sorted_dict)
        return report
    except IOError as error:
        # file was unable to be opened and read
        return 0

def print_report(result):
    print("=====================")
    print("File name: ", result[0])
    print("Number of lines: ", result[1])
    print("Number of characters (total): ", result[2])
    print("Number of letters: ", result[3])
    print("Number of figures: ", result[4])
    print("Number of other characters: ", result[5])
    print("Number of words: ", result[6])
    for x, y in result[7].items():
        print("Number of %i letter words: %i" % ( x, y))
    print("=====================")

def main():
    # check that a file name parameter is included 
    if len(sys.argv) != 2:
        raise ValueError('Please provide the name of the file to be read.')
    
    # check that the file exists
    result = read_file(sys.argv[1])
    # Check that the file was opened and read correctly
    if result == 0:
        print("Error: File does not appear to exist.")
        quit()
    else:
        # If successfuly opened and read, print the report
        print_report(result)
          

if __name__ == '__main__':
    main()