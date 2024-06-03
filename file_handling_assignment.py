# file_handling_assignment.py

def main():
    # Step 1: Create a new text file and write initial content
    try:
        with open("my_file.txt", 'w') as file:
            file.write("First line of text\n")
            file.write("Second line with a number: 123\n")
            file.write("Third line with another number: 456\n")
        print("Initial lines written to 'my_file.txt'")
    
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
    
    finally:
        # Step 2: Read and display the contents of the file
        try:
            with open("my_file.txt", 'r') as file:
                content = file.read()
            print("Contents of 'my_file.txt':")
            print(content)
        
        except FileNotFoundError:
            print("File not found. Please ensure 'my_file.txt' exists.")
        except PermissionError:
            print("Permission denied. Please check your file permissions.")
        except Exception as e:
            print(f"An unexpected error occurred while reading the file: {e}")
    
    # Step 3: Append additional lines to the file
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Fourth line appended to the file\n")
            file.write("Fifth line with a number: 789\n")
            file.write("Sixth line with another number: 101112\n")
        print("Additional lines appended to 'my_file.txt'")
    
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")
    
    finally:
        # Step 4: Read and display the updated contents of the file
        try:
            with open("my_file.txt", 'r') as file:
                updated_content = file.read()
            print("Updated contents of 'my_file.txt':")
            print(updated_content)
        
        except FileNotFoundError:
            print("File not found. Please ensure 'my_file.txt' exists.")
        except PermissionError:
            print("Permission denied. Please check your file permissions.")
        except Exception as e:
            print(f"An unexpected error occurred while reading the file: {e}")

if __name__ == "__main__":
    main()
