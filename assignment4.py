# Task 1: Read a File and Handle Errors

filename = "sample.txt"

try:
    print("Reading file content:")

    with open(filename, "r") as file:
        line_number = 1
        for line in file:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")


#Task2
# Step 1: Take input and write to file
text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")

print("Data successfully written to output.txt.\n")

# Step 2: Take additional input and append to file
additional_text = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(additional_text + "\n")

print("Data successfully appended.\n")

# Step 3: Read and display final content
print("Final content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)



