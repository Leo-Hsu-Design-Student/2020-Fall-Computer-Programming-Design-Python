#string formation
name='Leo'
age=22
message = 'This is %s. I am %d years old.' % (name,age)
print(message)

formatter_1 = "%s %s %s %s"
formatter_2 = "%s-%s-%s-%s"
formatter_3 = "1. %s\n2. %s\n3. %s\n4. %s"
print(formatter_1 % (1, 2, 3, 4))
print(formatter_2 % ("one", "two", "three", "four"))
print(formatter_2 % (True, False, False, True))
print(formatter_3 % (
 "I had this thing.",
 "That you could type up right.", "But it didn't sing.",
 "So I said goodnight."))