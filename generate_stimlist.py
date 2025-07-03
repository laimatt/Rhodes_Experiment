import csv
import json
import random

def generate_words(generated_words_list, consonants):
    res_list = []
    for i in range(3):
        word = generated_words_list[i]
        for x in consonants:
            word_list = list(word)
            word_list[0] = x
            word = "".join(word_list)
            for y in consonants:
                # print(word_list)
                word_list = list(word)
                word_list[2] = y
                word = "".join(word_list)
                print(word)
                res_list.append(word)
                # writer.writerow([word + "(correct)"])
    print(res_list)
    return res_list


# csvoutput = open('Pokemon_Names_Pervasive_Harmony.csv', 'w', newline='')
# csvoutput = open('Pokemon_Names_First_Last_Harmony.csv', 'w', newline='')
csvoutput = open('stims.csv', 'w', newline='')

writer = csv.writer(csvoutput)
writer.writerow(['stimuli', 'corrAns'])


generated_words_list_ph = ["CiCi", "CiCe","CeCi"]
generated_words_list_fl = ["CiCo", "CiCe","CeCi"]
consonants = ['p', 'b']
list1 = generate_words(generated_words_list_ph, consonants)
list2 = generate_words(generated_words_list_fl, consonants)
print(list1)

for word in list1:
    for word2 in list2:
        writer.writerow([word + "(correct)" + "                 " + word2 + "(incorrect)", "left"])
        writer.writerow([word2 + "(incorrect)" + "                 " + word + "(correct)", "right"])

csvoutput.close()