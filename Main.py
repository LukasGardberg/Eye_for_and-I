def main():
    # nbr_lines = int(input())
    #
    # text = """"""
    #
    # for _ in range(nbr_lines):
    #     text += input() + '\n'
    #
    #     # Removes last newline
    # text = text.rstrip()
    #
    # # get_substitution(text, substitutions)
    nbr_lines = 1
    text = 'beebebeebebeebe'

    print(convert_multiline(text, nbr_lines))


def convert_multiline(input_string, nbr_lines):
    substitutions = {'at': '@',
                     'and': '&',
                     'one': '1',
                     'won': '1',
                     'too': '2',
                     'to': '2',
                     'two': '2',
                     'for': '4',
                     'four': '4',
                     'bea': 'b',
                     'bee': 'b',
                     'be': 'b',
                     'sea': 'c',
                     'see': 'c',
                     'eye': 'i',
                     'oh': 'o',
                     'owe': 'o',
                     'are': 'r',
                     'you': 'u',
                     'why': 'y'}

    # Converts the muliline string into an array containing all lines
    strings_to_convert = input_string.splitlines()

    multiline_output_string = """"""

    for string in strings_to_convert:
        multiline_output_string += convert_string(string, substitutions)
        multiline_output_string += '\n'

    return multiline_output_string.rstrip()


def convert_string(input_string, substitutions):
    # Assuming input_string is a String, split into array of words
    words = input_string.split()
    converted_words = []

    for word in words:

        # new_word = recursive_substitution(word.lower(), substitutions)
        new_word = get_substitution(word.lower(), substitutions)

        if(word[0].isupper()):

            new_word = new_word.capitalize()

        converted_words.append(new_word)

    return ' '.join(converted_words)


def get_substitution(word, substitutions):
    possible_substitutions = {}
    for sub in substitutions.keys():
        # Finds all indices of where 'key' exists in 'word'
        occurences = list(find_all(word, sub))

        # If some were found, store them with their corresponding
        # substitution in a dictionary
        if(len(occurences) != 0):
            for index in occurences:
                # If index already exists as a key, add the substring
                if index in possible_substitutions:
                    possible_substitutions[index].append(sub)
                else:
                    # Else, create it
                    possible_substitutions.update({index: [sub]})

    if(len(possible_substitutions) == 0):
        # If no substitutions can be found, just return the word
        return word
    else:
        substitutions_to_make = trim(possible_substitutions, substitutions)
        # print(substitutions_to_make)

        return recursive_substitution(word, substitutions_to_make)


def find_all(string, substring):
    # Generator: finds all indices of where 'substring' exists in 'string'
    # If none are found, returns nothing
    start = 0
    while True:
        start = string.find(substring, start)

        if start == -1:
            return

        yield start

        start += 1  # use start += 1 to find overlapping matches


def trim(possible_substitutions, substitutions):
    # Trims dictionary of 'illegal' substitutions
    # Outputs a dictionary of 'substring' - 'substitution' pairs
    indices = sorted(possible_substitutions)
    for index in indices:
        # If more than one subst. is possible, choose the longest one
        words = possible_substitutions[index]
        possible_substitutions.update({index: max(words)})

    # If two subst. overlap, remove the last one
    past_index = indices[0]
    for index in indices[1:]:
        overlap = past_index + len(possible_substitutions[index]) > index
        if(overlap):
            possible_substitutions.pop(index)
        past_index = index

    substitutions_to_make = {}
    for value in possible_substitutions.values():
        substitutions_to_make.update({value: substitutions[value]})

    print(substitutions_to_make)

    return substitutions_to_make


def recursive_substitution(word, substitutions):
    new_word = word

    for key in substitutions.keys():
        index = word.find(key)

        if(index != -1):
            new_word = word.replace(key, substitutions[key], 1)
            left_string = new_word[:index]
            right_string = new_word[index+len(substitutions[key]):]

            new_word = recursive_substitution(left_string, substitutions)
            new_word += substitutions[key]
            new_word += recursive_substitution(right_string, substitutions)

    return new_word


if __name__ == "__main__":
    main()
