### Quiz
#Stwórz grę, która zawiera pytania z wiedzy ogólnej (Trivial pursuit)

quest1 = "Poland is in Europe.\na.yes\nb.no"
quest2 = "The longest river in Poland is:\na.Wisła\nb.Odra\nc.Wieprz"
quest3 = "National language in Poland is:\na.English\nb.French\nc.Polish"


print("Welcome to our Quiz. Answer this 3 questions!")
print(" ")
print(quest1)
ans1 = input("Your answer is: ")
score = 0
if ans1 == "a":
    print("Congrats!")
    score = score + 1
else:
    print("Bad answer :(")
print(" ")
print(quest2)
ans2 = input("Your answer is: ")

if ans2 == "a":
    print("Congrats!")
    score = score + 1
else:
    print("Bad answer.")

print(" ")

print(quest3)
ans3 = input("Your answer is: ")

if ans3 == "c":
    print("Congrats!")
    score = score + 1
else:
    print("Bad answer.")

print(" ")

print("Your final score is", score)

