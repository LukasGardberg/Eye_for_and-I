nbr_lines = int(input())

text = ""

for _ in range(nbr_lines):
    text += input() + '\n'

text = text.rstrip()

output_string = ""

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

for string in text.splitlines():
    i = 0

    new_string = string

    # Loop trough the string, check for substitutions
    while (i < len(new_string)):

        # check for subst. 4, 3, 2 chars ahead
        for n in range(4, 1, -1):
            s = new_string[i:i+n]

            if(s.lower() in substitutions.keys()):
                # Check if our substitution should be capitalized
                if(s[0].isupper()):
                    sub = substitutions[s.lower()].capitalize()
                else:
                    sub = substitutions[s]

                new_string = (new_string[:i] + sub +
                              new_string[i+n:])

                # We made a substitution, exit loop
                break

        i += 1

    output_string += new_string + '\n'

print(output_string.rstrip())
