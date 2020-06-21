import random

def getFile(file):
    f = open(file, "r")
    lst = f.readlines()
    lst = [x.replace('\n', '') for x in lst]
    return lst

# words

# verbs with object
verbswob = getFile("./words/verbs with object.txt")
verbs = getFile("./words/verbs.txt")
nouns = getFile("./words/nouns.txt")
prepositions = getFile("./words/prepositions.txt")
adverbs = getFile("./words/adverbs.txt")

# sentence structures
struts = [1, 2, 3, 4]

# make up steps
while True:
    # num of steps
    lengths = [3, 4, 5]
    steps = random.choice(lengths)
    # random titles, the bad context makes it funnier
    print(random.choice(["How to start a business", "How to get Minecraft for FREE!!!!", "How to get money FAST!!!", "How to get hot chicks", "How to breed syrian hamsters", "How to keep food fresh on a roadtrip", "How to make your own movie", "How to have a successful YouTube channel", "How to be popular", "How to choose running shoes for beginners", "How to get rid of dry skin on your face", "How to dress for a gala", "How to make toys for dogs"]))
    for i in range(steps):
        strutchoice = random.choice(struts)
        # adverb/no adverb, verb w/ object, noun. Eg. swiftly sit on an apple
        if strutchoice == 1:
            print("step", str(i+1) + ":", random.choice([random.choice(adverbs), ""]) + random.choice(verbswob), random.choice(nouns))
            if i == steps-1:
                input()
        # adverb/no adverb, verb, preposition, noun. Eg. Swiftly run next to an apple
        elif strutchoice == 2:
            print("step", str(i+1) + ":", random.choice([random.choice(adverbs), ""]) + random.choice(verbs), random.choice(prepositions), random.choice(nouns))
            if i == steps-1:
                input()
        # adverb/no adverb, verb. Eg. swiftly run
        elif strutchoice == 3:
            print("step", str(i+1) + ":", random.choice([random.choice(adverbs), ""]) + random.choice(verbs))
            if i == steps-1:
                input()
        # adverb/no adverb, verb w/ object, noun, preposition, noun. Eg. Swiftly sit on an apple next to an orange.
        elif strutchoice == 4:
            print("step", str(i+1) + ":", random.choice([random.choice(adverbs), ""]) + random.choice(verbswob), random.choice(nouns), random.choice(prepositions), random.choice(nouns))
            if i == steps-1:
                input()
        # for reference: print("step", str(i+1) + ":", )
