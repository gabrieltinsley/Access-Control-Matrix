import random

# Access Control Matrix (ACM) for predifined subjects and objects and rights
# @author Gabriel Tinsley

# Intialize ACM
ACM = {}

# Predifined pools of subjects, objects, and rights
subjects_pool = ["Alice", "Bob", "Charlie", "Eve", "Mallory"]
objects_pool = ["File1", "File2", "Printer", "Server1", "Database"]
rights_pool = ["read", "write", "execute", "own"]

# Select atleast 4 subjects and 4 objects
subjects = random.sample(subjects_pool, 4)
objects = random.sample(objects_pool, 4)

for subject in subjects:
    ACM[subject] = {}
    for obj in objects:
        # Assign 3 random rights per subject-object pair
        assigned_rights = random.sample(rights_pool, k=3)
        ACM[subject][obj] = assigned_rights

# Print ACM table      
print("Access Control Matrix:")
print(" ".ljust(25), end="")
for obj in objects:
    print(obj.ljust(25), end="")
print()

for subject, access in ACM.items():
    print(subject.ljust(10), end=" | ")
    for obj in objects:
        rights = ", ".join(access[obj])
        print(rights.ljust(25), end=" | ")
    print()
