# Features
# Read in template file
# Parse the template
# Present choices to user
# Get input from user
# Inject users input into template
# Display to user
# Write completed mad lib to file

welcome_message = """
**************************************
**    Welcome to the MadLib CLI!   **
**    Follow directions below.     **
**************************************"""

def read_file_contents(file_path):
    file = open(file_path)
    file_contents = file.read()
    file.close()
    return file_contents

def parse_template(contents):
    parsed_contents = "" # parsed output string
    parsed_words = []
    in_brackets = False # flag for brackets
    temp_word_string = ""

    num_brackets = contents.count('{') + contents.count('}')
    if (num_brackets > 0 and num_brackets % 2 == 0):
        # Template file is valid, continue
            for char in contents:
                if char == '{':
                    parsed_contents += char
                    in_brackets = True
                elif char == '}':
                    parsed_contents += char
                    in_brackets = False
                    parsed_words.append(temp_word_string)
                    temp_word_string = ""
                elif in_brackets:
                    temp_word_string += char
                else:
                    parsed_contents += char
    else:
        raise Exception("Incorrect template format")
    
    return (parsed_contents, tuple(parsed_words))

def show_user_cli():
    print(welcome_message)
    print("For this madlib template, please fill out the following: \n")
    
def merge_with_user_input(parsed_contents, responses):
    return parsed_contents.format(*responses)

def write_file_contents(file_path, file_content):
    with open(file_path, 'wb') as f:
        f.write(file_content)

def main():
    # Read file before showing user input to ensure file is correct
    file_string = read_file_contents("madlib_cli/assets/madlib_template.txt")
    parsed_string, word_tuple = parse_template(file_string)

    # Show user interface
    show_user_cli()

    user_words = []

    # Parse user input
    for word in word_tuple:
        input_val = input("Please enter " + word + ":\n")
        user_words.append(input_val)
    
    # Create completed Madlib string
    completed_madlib = merge_with_user_input(parsed_string, user_words)

    # Print results to user before writing to file
    print("Thanks!  See your completed Madlib below and in assets folder:\n")
    print(completed_madlib + "\n")

    # Write to output file
    write_file_contents("madlib_cli/assets/madlib_template_FILLED.txt", completed_madlib.encode())

if __name__ == "__main__":
    main()