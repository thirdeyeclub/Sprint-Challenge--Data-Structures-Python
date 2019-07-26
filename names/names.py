import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#og Duplicate
duplicates = []
# for name_1 in names_1:
#     for names_2 in names_2:
#         if names_1 == names_2:
#             duplicates.append(name_1)
#runtime: 6 seconds
newSet = set(names_1)
for name in names_2:
    if name in newSet:
        duplicates.append(name)

# runtime: 0.006981372833251953 seconds
end_time = time.time()

print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


