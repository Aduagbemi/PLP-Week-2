def modify_content(content):
    """
    Function to modify the content of the file.
    For this example, we'll just convert the text to uppercase.
    """
    return content.upper()


def read_and_write_file():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read from: ")

        # Try to open and read the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("File read successfully!")

        # Modify the content
        modified_content = modify_content(content)

        # Write the modified content to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            print(f"Modified content written to '{output_filename}' successfully!")

    except FileNotFoundError:
        print("Error: The file you entered does not exist.")
    except IOError:
        print("Error: The file could not be read or written to.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the function
read_and_write_file()
