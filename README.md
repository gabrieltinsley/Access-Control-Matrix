# Lab 1 # Access Control Matrix

* Author: Gabriel Tinsley
* Class: CS331 Section #002
* Semester: Spring 2025

## Overview
The Access-Control-Matrix class is a custom ACM structure that randomly creates an ACM using subjects, objects and rights from a predefined list. Every subject-object pair has at least three rights.

## Files
The following files are needed for my program
    * Access-Control-Matrix.py - Source file
    * acm_test_results.log - log file that stores access results
    * READEME.md - this file

## Compiling and Using
From the directory containing all source files, compile the driver class (and all dependencies), and run the program with the command:
> python .\Access-Control-Matrix.py

This will display the Access Control user menu with 7 options, the user will have to enter a number to run each option:

    * 1. Display ACM : this will output my drawing of the ACM with the subjects on the far left column and objects on the first row. Then for every subject-object pair there are 3 rights displayed.

    * 2. Grant Right : this will take user input, asking for subject, then object, and finally ask for right to grant before checking if the subject has the "own" right over the object. If so, then subject can add right if the right is not already there.

    * 3. Revoke Right : this will take user input, ask for subject, then object, and finally right to revoke. Success if the right exists in the subject-object pair, else failure.

    * 4. Run Test Cases : this will run the test cases for grant_right_secure and revoke_right_secure. The log file will show if the tests were successful.

    * 5. Simulate unauthorize access : this will take user input asking for subject, then object, and finally ask for right to use. If the subject-object pair does not have the right then that is unauthorized access, else subject-object pair can perform that right.

    * 6. Simulate privilege escalation : this will take user input, asking for subject, then object, and finally the right to gain. If the subject-object pair does not have the "own" right then that is privilege escalation and a "SECURITY ALERT" is printed to console. Else, that is a "SECURITY SUCCESS".

    * 7. Exit : this allows the user to exit the user menu.
----------
