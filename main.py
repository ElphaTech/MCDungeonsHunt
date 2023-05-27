import json

f = open( "ancients.json" , "rb" )
ancients = json.load(f)
f.close()
allLoot = {}
for ancient in ancients:
    for loot in ancients[ancient]["drops"]:
        allLoot[loot]=ancient

searchFor = input("What item do you want to get?: ").strip()
while searchFor not in allLoot:
    searchFor = input(f"Sorry, we couldn't find {searchFor}. Could you please repeat what you wanted?: ").strip()

print(f'The ancient you want to fight is {allLoot[searchFor]}. The runes required to summon it are {ancients[allLoot[searchFor]]["runes"]}.')