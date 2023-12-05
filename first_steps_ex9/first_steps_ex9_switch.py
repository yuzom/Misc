# DNA complement program
# The issue with the last program is it cannot be generalized to inputs where case matters
# Create a program which can handle upper and lower case

input_string = input("Enter a DNA sequence consisting of the letters A, T, C, and G")

def switcher(some_char):

    match some_char:
        case 'a':
            return 't'
        case 'A':
            return 'T'
        case 't':
            return 'a'
        case 'T':
            return 'A'
        case 'c':
            return 'g'
        case 'C':
            return 'G'
        case 'g':
            return 'c'
        case 'G':
            return 'C'
        case _:
            return some_char

input_list = list(input_string)

output_list = [switcher(i) for i in input_list]

print(''.join(output_list))


# Generalized example for handling sentences. The sentence below has letters which have been switched.
# The same function switcher() will be able to unswitch the letters.

# "This is a sentence where the letters 'A' and 'T', 'C' and 'G' have been switched; please correct this sentence."
wrong_sentence = "Ahis is t senaenge where ahe leaaers 'T' tnd 'A', 'G' tnd 'C' htve been swiaghed; pletse gorrega ahis senaenge."

wrong_list = list(wrong_sentence)

corrected_list = [switcher(i) for i in wrong_list]

print(''.join(corrected_list))
