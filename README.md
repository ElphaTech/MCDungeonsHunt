# MCDungeonsHunt
A program to determine what items are needed as input for an Ancient Hunt to get a different item.

## To use:
### 1) Update all items in "itemRunes.json"
To do this go to the following websites and copy the code from the first place it mentions "| {{DuItemLink|scale=1.5|" to the end. This is normally around 15 lines down. For each piece of code, paste it into "sampleData.txt" and run "getItemRunes.json". This will create a file called "output.json". Copy all the code from it and paste it into the correct place in "itemRunes.json". For example if you did melee weapons first you should paste it after melee: `"melee": {...}`
- [Melee Weapon](https://minecraft.fandom.com/wiki/Template:Melee_Weapon_Runes?action=edit)
- [Ranged Weapon](https://minecraft.fandom.com/wiki/Template:Ranged_Weapon_Runes?action=edit)
- [Armour](https://minecraft.fandom.com/wiki/Template:Armor_Runes?action=edit)
- [Artifact](https://minecraft.fandom.com/wiki/Template:Artifact_Runes?action=edit)