import random


def insult_me():
    word_a=random.choice(list_a)
    word_b=random.choice(list_b)
    word_c=random.choice(list_c)
    insult = "Thou " + word_a + " " + word_b + " " + word_c + "!"
    print(insult)
list_a=[]
list_b=[]
list_c=[]

with open("InsultsRusis.csv", "r") as f:
    for line in f:
        words=line.split(",")
        list_a.append(words[0].strip())
        list_b.append(words[1].strip())
        list_c.append(words[2].strip())
insult_me()
