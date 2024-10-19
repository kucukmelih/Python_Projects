import os  
import sys 
import tty  # Library used to change the input mode of the terminal
import termios  # Library used to change the terminal input/output settings

# File reading class
class FileReader:
    def __init__(self, file_path): 
        self.file_path = file_path  
        self.content = self.read_file()  # We store the content of the file after reading it

    # File reading function
    def read_file(self):
        if not os.path.exists(self.file_path):
            print(f"Error: The file '{self.file_path}' does not exist.")
            sys.exit(1)
        try:
            # We read the file and add each line to a list
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.readlines()
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)

# Pagination class 
class Pagination:
    def __init__(self, content, page_size):
        # We split the content into pages, each containing 'page_size' number of lines
        self.pages = [content[i:i + page_size] for i in range(0, len(content), page_size)]

    # Function to return the specified page number
    def get_page(self, page_number):
        # If the page number is valid, return the page, otherwise return None
        return self.pages[page_number] if 0 <= page_number < len(self.pages) else None

# Class for terminal operations
class TerminalManager:
    @staticmethod
    def display_page(content, current_page, total_pages, total_lines, show_footer=True):
        # Clear the terminal (use 'cls' for Windows and 'clear' for other systems)
        os.system('cls' if os.name == 'nt' else 'clear')
        # Print the content of the page
        print(''.join(content))
        # If the footer (page info) is to be shown
        if show_footer:
            print(f"\nPage {current_page + 1}/{total_pages}, Total Lines: {total_lines}")
            print("Press 'Space' to continue, 'B' for previous page, 'Q' to quit.")

# Class to handle user keyboard input
class InputHandler:
    @staticmethod
    def wait_for_input():
        # Get the file descriptor for changing terminal settings
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            # Set the terminal to raw mode so we can read inputs without waiting for a newline
            tty.setraw(fd)
            while True:
                # Read a character from the keyboard and convert it to uppercase
                char = sys.stdin.read(1).upper()
                # If the character is ' ', 'Q', or 'B', return it
                if char in [' ', 'Q', 'B']:
                    return char
        finally:
            # Restore the terminal to its old settings
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def main():
    if len(sys.argv) != 2:
        print("Usage: python text_browser.py <file_path>")
        sys.exit(1)

    # Use the FileReader class to read the file content
    file_reader = FileReader(sys.argv[1])
    content = file_reader.content  # Get the content
    total_lines = len(content)  # Calculate the total number of lines

    # Use the Pagination class to split the content into pages (10 lines per page)
    pagination = Pagination(content, page_size=10)
    total_pages = len(pagination.pages)  # Calculate the total number of pages
    current_page = 0  # Start on the first page

    # Infinite loop to navigate between pages
    while True:
        # Get the current page
        page_content = pagination.get_page(current_page)
        # If no page exists, break the loop
        if page_content is None:
            break

        # Display the page on the terminal
        TerminalManager.display_page(page_content, current_page, total_pages, total_lines)
        # Wait for user input (space, 'B', 'Q')
        user_input = InputHandler.wait_for_input()

        if user_input == 'Q':
            # Before quitting, display the page without the footer
            TerminalManager.display_page(page_content, current_page, total_pages, total_lines, show_footer=False)
            break
        # If the user presses the space key, move to the next page
        elif user_input == ' ':
            current_page = min(current_page + 1, total_pages - 1)  # Don't exceed the last page
        # If the user presses the 'B' key, go to the previous page
        elif user_input == 'B':
            current_page = max(current_page - 1, 0)  # Don't go below the first page

    # Exiting the program
    print("Exiting text browser...\n")

if __name__ == "__main__":
    main()
