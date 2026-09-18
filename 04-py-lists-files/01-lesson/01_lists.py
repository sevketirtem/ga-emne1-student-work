guests = ["Kermit","Miss Piggy","Gonzo"]
print(guests)

print("\n---\n")

mixed_bag = ["Tomas", 52, True]
print(mixed_bag)

print("\n---\n")

print(guests[0])
print(mixed_bag[1])
print(mixed_bag[2])

guests.append("Sevket")
print(guests)
print(len(guests))
guests.remove("Kermit")

print(guests)
print(len(guests))

#for i in guests:
    #print(f"Welcom,{i}")
    #"For i in guests" returns values but "for i in range(4) returns indeks" means position numbers
print("\n...\n")
for i in range(len(guests)):
    print(f"Welcome, {guests[i]}")

print("\n---\n")

scores = [3, 5, 23, 55]
print(len(scores))
print(sum(scores))

average = sum(scores) / len(scores)
print(f"Average: {average}")

print(min(scores))
print(max(scores))

#Bonus feature,from question
guests.insert(8,"Sedat")
print(guests)