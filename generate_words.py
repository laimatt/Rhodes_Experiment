import csv
import json
import random


csvoutput = open('Pokemon_Names_Pervasive_Harmony.csv', 'w', newline='')
# csvoutput = open('Pokemon_Names_First_Last_Harmony.csv', 'w', newline='')
writer = csv.writer(csvoutput)
writer.writerow(['Word'])


generated_words_list = ["CiCi", "CiCe","CeCi"]
# generated_words_list = ["CiCo", "CiCe","CeCi"]
consonants = ['p', 'b']

for i in range(3):
    word = generated_words_list[i]
    for x in consonants:
        word_list = list(word)
        word_list[0] = x
        word = "".join(word_list)
        for y in consonants:
            word_list = list(word)
            word_list[2] = y
            word = "".join(word_list)
            # word = word + "(correct)"
            # word = "".join("(incorrect)") 
            print(word)
            writer.writerow([word + "(correct)"])


print(generated_words_list)
csvoutput.close()