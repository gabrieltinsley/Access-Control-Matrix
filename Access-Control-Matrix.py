import random
import logging
# @author Gabriel Tinsley
# Hands-On Lab 1 CS331
# Part 1
# Configure logging
logging.basicConfig(filename='acm_test_results.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Initialize ACM
ACM = {}

# Predefined pools of subjects, objects, and rights
subjects_pool = ["Alice", "Bob", "Charlie", "Eve", "Mallory"]
objects_pool = ["File1", "File2", "Printer", "Server1", "Database"]
rights_pool = ["read", "write", "execute", "own"]

# Select at least 4 subjects and 4 objects and 3 rights
subjects = random.sample(subjects_pool, 4)
objects = random.sample(objects_pool, 4)

for subject in subjects:
    ACM[subject] = {}
    for obj in objects:
        assigned_rights = random.sample(rights_pool, 3)
        ACM[subject][obj] = assigned_rights

# Display ACM table
def display_acm():
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
    print("===================================")

# Part 2
def grant_right_secure(subject, obj, right):
    if subject in ACM and obj in ACM[subject]:
        if right not in ACM[subject][obj]:
            if "own" in ACM[subject][obj]:
                ACM[subject][obj].append(right)
                logging.info(f"SUCCESS: Granted '{right}' to {subject} for {obj}.")
                print(f"Right '{right}' assigned to {subject} for {obj}.")
            else:
                logging.info(f"FAILURE: {subject} lacks 'own' rights on {obj}.")
                print(f"Subject '{subject}' does not own object '{obj}'.")
        else:
            logging.info(f"FAILURE: '{right}' already exists for {subject} on {obj}.")
            print(f"Right '{right}' already exists for {subject} on {obj}.")
    else:
        logging.info("FAILURE: Invalid subject or object.")
        print("Invalid subject or object.")

def revoke_right_secure(subject, obj, right):
    if subject in ACM and obj in ACM[subject]:
        if right in ACM[subject][obj]:
            ACM[subject][obj].remove(right)
            logging.info(f"SUCCESS: Revoked '{right}' from {subject} for {obj}.")
            print(f"Right '{right}' revoked from {subject} for {obj}.")
        else:
            logging.info(f"FAILURE: Right '{right}' does not exist for {subject} on {obj}.")
            print(f"Right '{right}' does not exist for {subject} on {obj}.")
    else:
        logging.info("FAILURE: Invalid subject or object.")
        print("Invalid subject or object.")

def test_cases():
    print("Running Test Cases...")
    grant_right_secure('Charlie', 'File1', 'execute')  # Success if 'Charlie' owns 'File1'
    grant_right_secure('Mallory', 'Printer', 'write')  # Failure if 'Mallory' does not own 'Printer'
    revoke_right_secure('Bob', 'File2', 'read')  # Success if 'Bob' has 'read' on 'File2'
    revoke_right_secure('Eve', 'Server1', 'execute')  # Failure if 'Eve' lacks 'execute' on 'Server1'

# Part 3
def simulate_unauthorized_access(subject, obj, right):
        if subject in ACM and obj in ACM[subject]:
            if right not in ACM[subject][obj]:
                logging.info(f"DENIED: {subject} tried to {right} {obj} but lacks permission.")
                print(f"DENIED: {subject} tried to {right} {obj} but lacks permission.")
            else:
                logging.info(f"ALLOWED: {subject} accessed {obj} with {right}.")
                print(f"ALLOWED: {subject} accessed {obj} with {right}.")
        else:
            logging.info("FAILURE: Invalid subject or object.")
            print("Invalid subject or object.")

def simulate_privilege_escalation(subject, obj, right):
        if subject in ACM and obj in ACM[subject]:
            if "own" not in ACM[subject][obj]:
                logging.info(f"SECURITY ALERT: {subject} attempted to escalate privileges on {obj}.")
                print(f"SECURITY ALERT: {subject} attempted to escalate privileges on {obj}.")
            else:
                ACM[subject][obj].append(right)
                logging.info(f"SUCCESS: {subject} now owns {obj}.")
                print(f"SUCCESS: {subject} now owns {obj}.")
        else:
            logging.info("FAILURE: Invalid subject or object.")
            print("Invalid subject or object.")

# User menu for command line arguments
def user_menu():
    while True:
        print("\nAccess Control Menu:")
        print("1. Display ACM")
        print("2. Grant Right")
        print("3. Revoke Right")
        print("4. Run Test Cases")
        print("5. Simulate unauthorized access")
        print("6. Simulate privilege escalation")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            display_acm()
        elif choice == '2':
            subject = input("Enter subject: ")
            obj = input("Enter object: ")
            right = input("Enter right to grant: ")
            grant_right_secure(subject, obj, right)
        elif choice == '3':
            subject = input("Enter subject: ")
            obj = input("Enter object: ")
            right = input("Enter right to revoke: ")
            revoke_right_secure(subject, obj, right)
        elif choice == '4':
            test_cases()
        elif choice == '5':
            subject = input("Enter subject: ")
            obj = input("Enter object: ")
            right = input("Enter right to access: ")
            print(f"Simulating unauthorized access...\n")
            simulate_unauthorized_access(subject, obj, right)
        elif choice == '6':
            subject = input("Enter subject: ")
            obj = input("Enter object: ")
            right = input("Enter right to escalate: ")
            print(f"Simulating privilege escalation...\n")
            simulate_privilege_escalation(subject, obj, right)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

# Launch Menu
user_menu()