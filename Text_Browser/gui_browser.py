import os
import sys
import tkinter as tk
from tkinter import messagebox

# File reading class
class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = self.read_file()

    def read_file(self):
        if not os.path.exists(self.file_path):
            messagebox.showerror("Error", f"The file '{self.file_path}' does not exist.")
            return []
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.readlines()
        except Exception as e:
            messagebox.showerror("Error", f"Error reading file: {e}")
            return []

# Pagination class: Divide content into pages.
class Pagination:
    def __init__(self, content, page_size):
        self.pages = [content[i:i + page_size] for i in range(0, len(content), page_size)]

    def get_page(self, page_number):
        return self.pages[page_number] if 0 <= page_number < len(self.pages) else None

# GUI Class
class TextBrowserGUI:
    def __init__(self, root, file_path, page_size=10):
        self.root = root
        self.root.title("Text Browser")
        
        self.file_reader = FileReader(file_path)
        self.content = self.file_reader.content
        self.total_lines = len(self.content)

        self.pagination = Pagination(self.content, page_size)
        self.total_pages = len(self.pagination.pages)
        self.current_page = 0

        self.text_area = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED, width=80, height=20)
        # state=tk.DISABLED: Lock editing so that the user cannot modify the text.
        self.text_area.pack()

        # Navigation buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()
        
        self.prev_button = tk.Button(self.button_frame, text="Previous", command=self.prev_page)
        self.prev_button.pack(side=tk.LEFT, padx=5)
        
        self.quit_button = tk.Button(self.button_frame, text="Quit", command=root.quit)
        self.quit_button.pack(side=tk.LEFT, padx=5)
        
        self.next_button = tk.Button(self.button_frame, text="Next", command=self.next_page)
        self.next_button.pack(side=tk.LEFT, padx=5)

        self.update_page()
        # When the interface is loaded for the first time, display the content of page 0 in the text area.

    def update_page(self):
        page_content = self.pagination.get_page(self.current_page)
        if page_content is None: 
            # If there is no valid page (returns None), the method terminates.
            return
        
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, ''.join(page_content))
        self.text_area.insert(tk.END, f"\nPage {self.current_page + 1}/{self.total_pages}, Total Lines: {self.total_lines}")
        self.text_area.config(state=tk.DISABLED)

    def next_page(self):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            self.update_page()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_page()

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python text_browser_gui.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    root = tk.Tk()
    TextBrowserGUI(root, file_path)
    root.mainloop()

if __name__ == "__main__":
    main()
