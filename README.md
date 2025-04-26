# Assignment 3: Functions and Modules in Python

## task 1:

### steps performed:
1. created a variable to store the name of the file
2. used try and except to catch an error if there is any 
3. in the try block:
    - used `open()` function to open the file and stored it in variable named f
    - made a count variable to keep count of the number of lines
    - used a for loop to print every line in file
4. in the except block:
    - if the file is not found, a `print()` function will display that the specified file was not found. 

### explanation:
- used `open()` function of python to open the file and stored it in a variable
- used for loop to go through each line of the file and displayed it 
- used try and except method to catch an error 

## task 2:

### steps performed:
1. created a variable to store the name of the file
2. used `open()` function with "w" parameter to open the file in write mode and assigned it to f
3. created a variable text which takes the input from the user 
4. used `write()` function to write the data stored in variable text to the specified file
5. used `print()` function to notify that the data was successfully written
6. used `close()` function to close the file
7. used `open()` function with "a" parameter to open the same file
8. created a variable text which takes the input from the user 
9. used `write()` function to write the data stored in variable text to the specified file
10. used `print()` function to notify that the data was successfully appended
11. used `open()` function to open the specified file in read mode
12. used `read()` function to read the content of the file

### explanation:
- `open()` function with "w" parameter was used to open the file in write mode so as to write data to the file
- `open()` function with "a" parameter was used to open the file in append mode so as to append data to the existing data in the file
- `open()` function with "r" parameter was used to open the file in read mode to read the content of the file
- `close()` function was used to close the file
