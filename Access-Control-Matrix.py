import random
import logging

# @author Gabriel Tinsley
# Hands-On Lab 1 CS331

# Part 1: Initialize Access Control Matrix (ACM)
# Configure logging to track operations
logging.basicConfig(filename='acm_test_results.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Create an empty ACM
ACM = {}

# Predefined pools of subjects, objects, and rights
subjects_pool = ["Alice", "Bob", "Charlie", "Eve", "Mallory"]
objects_pool = ["File1", "File2", "Printer", "Server1", "Database"]
rights_pool = ["read", "write", "execute", "own"]

# Select at least 4 subjects and 4 objects
subjects = random.sample(subjects_pool, 4)
objects = random.sample(objects_pool, 4)

# Assign random rights (at least 3) to each subject-object pair
for subject in subjects:
    ACM[subject] = {}
    for obj in objects:
        assigned_rights = random.sample(rights_pool, 3)
        ACM[subject][obj] = assigned_rights

# Funcation to display ACM
def display_acm():
    print("Access Control Matrix:")
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

# Part 2: Securely Grant and Revoke Rights
# Function to grant a right only if the subject owns the object
def grant_right_secure(subject, obj, right):
    if subject in ACM and obj in ACM[subject]:
        if right not in ACM[subject][obj]:
            if "own" in ACM[subject][obj]: # Ownership check
                ACM[subject][obj].append(right)
                log_operation(subject, obj, f"Grant {right}", "SUCCESS")
                print(f"Right '{right}' assigned to {subject} for {obj}.")
            else:
                log_operation(subject, obj, f"Grant {right}", "DENIED - lacks own right")
                print(f"Subject '{subject}' does not own object '{obj}'.")
        else:
            log_operation(subject, obj, f"Grant {right}", "DENIED - already exists")
            print(f"Right '{right}' already exists for {subject} on {obj}.")
    else:
        log_operation(subject, obj, f"Grant {right}", "DENIED - invalid subject or object")
        print("Invalid subject or object.")

# Function to revoke a right from a subject for a specific object
def revoke_right_secure(subject, obj, right):
    if subject in ACM and obj in ACM[subject]:
        if right in ACM[subject][obj]:
            ACM[subject][obj].remove(right)
            log_operation(subject, obj, f"Revoke {right}", "SUCCESS")
            print(f"Right '{right}' revoked from {subject} for {obj}.")
        else:
            log_operation(subject, obj, f"Revoke {right}", f"FAILURE - right does not exist for {subject} and {obj}")
            print(f"Right '{right}' does not exist for {subject} on {obj}.")
    else:
        log_operation(subject, obj, f"Revoke {right}", "FAILURE - invalid subject or object")
        print("Invalid subject or object.")

# Function for test cases to Grant and Revoke rights
def test_cases():
    print("Running Test Cases...")
    grant_right_secure('Alice', 'File1', 'execute')  # Success if 'Alice' owns 'File1'
    grant_right_secure('Eve', 'Database', 'own')  # Failure if 'Mallory' does not own 'Printer'
    revoke_right_secure('Alice', 'File1', 'read')  # Success if 'Alice' has 'read' on 'File1'
    revoke_right_secure('Charlie', 'Server1', 'execute')  # Failure if 'Charlie' lacks 'execute' on 'Server1'

# Part 3: Security Testing Functions
# Function to simulate unauthorized access attempts
def simulate_unauthorized_access(subject, obj, right):
        if subject in ACM and obj in ACM[subject]:
            if right not in ACM[subject][obj]:
                log_operation(subject, obj, right, f"DENIED - {subject} tried to {right} {obj} but lacks permission.")
                print(f"DENIED: {subject} tried to {right} {obj} but lacks permission.")
            else:
                log_operation(subject, obj, right, f"ALLOWED - {subject} accessed {obj} with {right}.")
                print(f"ALLOWED: {subject} accessed {obj} with {right}.")
        else:
            log_operation(subject, obj, right, "FAILURE - invalid subject or object")
            print("Invalid subject or object.")

# Function to simulate privilege escalation attempts
def simulate_privilege_escalation(subject, obj, right):
        if subject in ACM and obj in ACM[subject]:
            if "own" not in ACM[subject][obj]:
                log_operation(subject, obj, "Privilege Escalation Attempt", "SECURITY ALERT")
                print(f"SECURITY ALERT: {subject} attempted to escalate privileges on {obj}.")
            else:
                ACM[subject][obj].append(right)
                log_operation(subject, obj, "Privilege Escalation", "SECURITY SUCCESS")
                print(f"SECURITY SUCCESS: {subject} owns {obj} and added {right}.")
        else:
            log_operation(subject, obj, right, "FAILURE - invalid subject or object")
            print("Invalid subject or object.")

# Part 4: Logging operations format
# Function to log access attempts
def log_operation(subject, obj, action, result):
    logging.info(f" | {subject} | {obj} | {action} | {result}")

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