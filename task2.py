file_name = "output.txt"

f = open("file_name", "w")
text = input("Enter text to write to the file: ")
f.write(text)
f.write("\n")
print("Data successfully written to output.txt.\n")
f.close()

f = open("file_name", "a")
text = input("Enter additional text to append: ")
f.write(text)
f.write("\n")
print("Data successfully appended. \n")
f.close()

f = open("file_name", "r")
print("Final content of output.txt:")
print(f.read())
f.close()