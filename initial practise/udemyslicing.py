parrot='Norwegian Blue'
print(parrot[0:7])
print(parrot[4:8])
print(parrot[6:13])
print(parrot[:12])
print(parrot[10:])
print(parrot[-4:-2])
print(parrot[-4:12])
print(parrot[0:6:2])
print(parrot[0:6:3])

number="7,486,738,163,647,325"
print(number[0::3])

number="7,486,738,163,647,325"
separators=number[0::3]
print (separators)
values="".join(char if char not in separators else" "for char in number).split()
print([int(val)for val in values])

letters='abcdefghijklmnopqrstuvwxyz'
backwards=letters[25::-1]
print(backwards)
word=letters[4::-1]
print(word)
words=letters[16:13:-1]
print(words)
world=letters[25:17:-1]
print(world)
worlds=letters[:-9:-1]
print(worlds)

#Norwegi
#egia
#ian Blu
#Norwegian Bl
#Blue
#Bl
#Bl
#Nre
#Nw
#787,343
#787,343
#[6, 16, 6, 25]
#zyxwvutsrqponmlkjihgfedcba
#edcba
#qpo
#zyxwvuts
#zyxwvuts





