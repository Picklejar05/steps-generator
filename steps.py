import random

# words
verbswob = ["pick up", "mix", "grab", "eat", "sit on", "play", "listen to", "kick", "smell", "remove", "touch", "pick", "prepare", "portion", "pack", "freeze", "adjust", "wash", "pat"]
verbs = ["run", "fart", "sit", "smile", "freeze", "type", "poop", "play", "sleep", "die", "come out", "cum"]
nouns = ["a car", "a fence", "an apple", "a chair", "a road", "a tree", "a chicken", "a hat", "a building", "a van", "wood", "a pillow", "me", "the moon", "a pancake", "a smell", "a car", "a poop", "foods", "some food", "a cooler", "a container", "containers", "a bag", "bags", "your routine", "a cleanser", "your face", "water", "a clean towel", "moisturizer", "oil", "shea butter"]
prepositions = ["next to", "above", "below", "beside", "behind", "in front of", "inside of", "on"]
adverbs = ["carefully ", "quickly ", "sadly ", "openly ", "happily ", "crazily ", "wierdly ", "creepily "]

# sentence structures
struts = [1, 2, 3, 4]

# make up steps
while True:
    # num of steps
    poop = [3, 4, 5]
    steps = random.choice(poop)
    print(random.choice(["How to start a business", "How to get Minecraft for FREE!!!!", "How to get money FAST!!!", "How to get hot chicks", "How to breed syrian hamsters", "How to keep food fresh on a roadtrip", "How to make your own movie", "How to have a successful YouTube channel", "How to be popular", "How to choose running shoes for beginners", "How to get rid of dry skin on your face", "How to dress for a gala", "How to make toys for dogs"]))
    for i in range(steps):
        eatshit = random.choice(struts)
        if eatshit == 1:
            print("step", str(i+1) + ":", random.choice([random.choice(adverbs), ""]) + random.choice(verbswob), random.choice(nouns))
            if i == steps-1:
                input()
        elif eatshit == 2:
            print("step", str(i+1) + ":", random.choice([random.choice(adverbs), ""]) + random.choice(verbs), random.choice(prepositions), random.choice(nouns))
            if i == steps-1:
                input()
        elif eatshit == 3:
            print("step", str(i+1) + ":", random.choice([random.choice(adverbs), ""]) + random.choice(verbs))
            if i == steps-1:
                input()
        elif eatshit == 4:
            print("step", str(i+1) + ":", random.choice([random.choice(adverbs), ""]) + random.choice(verbswob), random.choice(nouns), random.choice(prepositions), random.choice(nouns))
            if i == steps-1:
                input()
        # print("step", str(i+1) + ":", )
