# DNA complement program
# The issue with the last program is it cannot be generalized to inputs where case matters
# Create a program which can handle upper and lower case

input_string = input("Enter a DNA sequence consisting of the letters A, T, C, and G")

complementsDictionary = {"A":"T", "T":"A", "G":"C", "C":"G", "a":"t", "t":"a", "g":"c", "c":"g"}

input_list = list(input_string)

output_list = [complementsDictionary.get(i) for i in input_list]

print(''.join(output_list))


# Generalized example for handling sentences. The sentence below has letters which have been switched.
# The same function switcher() will be able to unswitch the letters.

# "This is a sentence where the letters 'A' and 'T', 'C' and 'G' have been switched; please correct this sentence."
wrong_sentence = "Ahis is t senaenge where ahe leaaers 'T' tnd 'A', 'G' tnd 'C' htve been swiaghed; pletse gorrega ahis senaenge."

wrong_list = list(wrong_sentence)

corrected_list = [complementsDictionary.get(i) if complementsDictionary.get(i) else i for i in wrong_list]

print(''.join(corrected_list))
