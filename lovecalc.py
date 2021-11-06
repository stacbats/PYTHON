# Python learnings

# Love Calculator


print(" Welcome to teh love Calculator!!!!")
name1 = input("What is your name ? \n")
name2 = input("What is their name ? \n")

# inputting working files

combined_string = name1 + name2
lowercase_string = combined_string.lower()

t = lowercase_string.count("t")
r = lowercase_string.count("r")
u = lowercase_string.count("u")
e = lowercase_string.count("e")

true = t + r + u + e   # adds all up

l = lowercase_string.count("l")
o = lowercase_string.count("o")
v = lowercase_string.count("v")
e = lowercase_string.count("e")

love = l + o + v + e  # adds all up

love_score1 = str(true) + str(love)
love_score2 = int(love_score1)

if love_score2 <= 10 or love_score2 >= 90:
    print(f" Your love is {love_score2}, like mentos & coke." )
elif (love_score2 >= 40) or (love_score2 <= 50):
    print(f" Your love score is {love_score2}, You go alright together.")
else:
    print(f" Your score is {love_score2}")
