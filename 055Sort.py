# sort() method = used with lists
# sort() function = used with iterables

# LIST
students = ["Squidward","Sandy","Patrick","Spongbob","Mr.Krabs"]

students.sort()

for i in students:
    print(i)

print("----------------")
# --------------------------
# try reversing the list
students.sort(reverse=True)

for i in students:
    print(i)

print("----------------")
# ---------------------------
# TUPLE
players = ("Squidward","Sandy","Patrick","Spongbob","Mr.Krabs")

sorted_players = sorted(players)

for i in sorted_players:
    print(i)

print("----------------")
# reversing

sorted_players = sorted(players,reverse=True)

for i in sorted_players:
    print(i)

print("----------------")
# -------------------------------------------------
# sort using key
# LIST OF TUPLES
student_record = [("Squidward","F",60),
            ("Sandy","A",33),
            ("Patrick","D",36),
            ("Spongbob","B",20),
            ("Mr.Krabs","C",78)]

student_record.sort()

for i in student_record:
    print(i)

print("----------------")
# -----------------------
# sort using the 2nd column
grade = lambda grades:grades[1] # indexes start in 0,1,2...
student_record.sort(key=grade)

for i in student_record:
    print(i)

print("----------------")
# try reverse
student_record.sort(key=grade,reverse=True)

for i in student_record:
    print(i)

print("----------------")
# -----------------------
# sort using the 3rd column
age = lambda age:age[2] # indexes start in 0,1,2...
student_record.sort(key=age)

for i in student_record:
    print(i)

print("----------------")
# try reverse
student_record.sort(key=age,reverse=True)

for i in student_record:
    print(i)

print("----------------")

# -------------------------------------------------------------
# TUPLES OF TUPLES
player_record = (("Squidward","F",60),
            ("Sandy","A",33),
            ("Patrick","D",36),
            ("Spongbob","B",20),
            ("Mr.Krabs","C",78))

age_record = lambda age_record:age_record[2]
sorted_player_record = sorted(player_record,key=age_record)

for i in sorted_player_record:
    print(i)