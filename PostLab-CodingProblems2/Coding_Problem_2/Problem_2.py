'''
Write a program that allows the user to navigate through the lines of text in a file. 
The program prompts the user for a filename and inputs the lines of text into a list. 
The program then enters a loop in which it prints the number of lines in the file and 
prompts the user for a line number. Actual line numbers range from 1 to the number of 
lines in the file. If the input is 0, the program quits. Otherwise, the program prints 
the line associated with that number.
'''
def navigate_file():
    try:
        filename = input("Enter the filename: ")
        
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        print(f"The file '{filename}' has been loaded successfully.")
        
        while True:
            print(f"\nThe file contains {len(lines)} lines.")
            line_number = int(input("Enter a line number (1 to {} or 0 to quit): ".format(len(lines))))
            
            if line_number == 0:
                print("Exiting the program.")
                break
            elif 1 <= line_number <= len(lines):
                print(f"Line {line_number}: {lines[line_number - 1].strip()}")
            else:
                print("Invalid line number. Please try again.")
    
    except FileNotFoundError:
        print("Error: File not found. Please ensure the filename is correct.")
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    navigate_file()
