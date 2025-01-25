import tkinter as tk
from tkinter import messagebox, simpledialog

def show_books():
    try:
        with open("Library.txt") as books:
            content = books.read()
            messagebox.showinfo("Books", content)
    except FileNotFoundError:
        messagebox.showerror("Error", "Library.txt not found.")

def add_book():
    while True:
        added = simpledialog.askstring("Add", "Enter the book you need to add:")
        category = simpledialog.askstring("Add", "Enter the book category:")
        if added and category:
            with open("Library.txt", "a") as books:
                books.write(f"{added}[{category}]\n")
            another = messagebox.askquestion("Add another", "Add another book?")
            if another != 'yes':
                break

def delete_book():
    try:
        with open("Library.txt", "r") as books:
            all_books = books.readlines()

        delete = simpledialog.askstring("Delete", "Enter the book you need to delete:")
        initial_count = len(all_books)
        all_books = [book for book in all_books if book.strip() != delete]

        with open("Library.txt", "w") as books:
            books.writelines(all_books)

        final_count = len(all_books)
        if initial_count > final_count:
            messagebox.showinfo("Success", "Book deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Book not found.")
    except FileNotFoundError:
        messagebox.showerror("Error", "Library.txt not found.")

def search_book():
    try:
        with open("Library.txt", "r") as all_book:
            available_books = all_book.read().splitlines()

        searched_book = simpledialog.askstring("Search", "Enter the book you search for:")
        if searched_book in available_books:
            messagebox.showinfo("Result", f"{searched_book} is available")
        else:
            messagebox.showwarning("Result", f"{searched_book} is not available")
    except FileNotFoundError:
        messagebox.showerror("Error", "Library.txt not found.")

def add_borrowed_book():
    while True:
        added_b = simpledialog.askstring("Add", "Enter the Borrowed book:")
        name = simpledialog.askstring("Add", "Enter the name of the one who borrowed the book:")
        if added_b and name:
            with open("Borrowed.txt", "a") as books:
                books.write(f"{added_b}[{name}]\n")
            another = messagebox.askquestion("Add another", "Add another borrowed book?")
            if another != 'yes':
                break

def show_borrowed_books():
    try:
        with open("Borrowed.txt") as books:
            content = books.read()
            messagebox.showinfo("Borrowed Books", content)
    except FileNotFoundError:
        messagebox.showerror("Error", "Borrowed.txt not found.")

def search_borrowed_book():
    try:
        with open("Borrowed.txt", "r") as all_book:
            borrowed_books = all_book.read().splitlines()

        searched_book = simpledialog.askstring("Search", "Enter the borrowed book you search for:")
        if searched_book in borrowed_books:
            messagebox.showinfo("Result", f"{searched_book} is borrowed")
        else:
            messagebox.showwarning("Result", f"{searched_book} is not borrowed")
    except FileNotFoundError:
        messagebox.showerror("Error", "Borrowed.txt not found.")

def add_discount():
    while True:
        dis_book = simpledialog.askstring("Add", "Enter the book that has a discount:")
        dis_added = simpledialog.askstring("Add", "Enter the discount:")
        dis_time = simpledialog.askstring("Add", "Enter how long the discount lasts:")
        if dis_book and dis_added and dis_time:
            with open("Discount.txt", "a") as discount:
                discount.write(f"{dis_book}[{dis_added}][{dis_time}]\n")
            another = messagebox.askquestion("Add another", "Add another Discount?")
            if another != 'yes':
                break

def show_discounts():
    try:
        with open("Discount.txt") as discount:
            content = discount.read()
            messagebox.showinfo("Discounts", content)
    except FileNotFoundError:
        messagebox.showerror("Error", "Discount.txt not found.")

def delete_discount():
    try:
        with open("Discount.txt", "r") as discount:
            discount_books = discount.readlines()

        delete = simpledialog.askstring("Delete", "Enter the discount you need to delete:")
        discount_books = [d for d in discount_books if d.strip() != delete]

        with open("Discount.txt", "w") as discount:
            discount.writelines(discount_books)

        if len(discount_books) < len(discount.readlines()):
            messagebox.showinfo("Success", "Discount deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Not found.")
    except FileNotFoundError:
        messagebox.showerror("Error", "Discount.txt not found.")

def search_discount():
    try:
        with open("Discount.txt", "r") as discount_books:
            available_discounts = discount_books.read().splitlines()

        searched_discount = simpledialog.askstring("Search", "Enter the discount you search for:")
        if searched_discount in available_discounts:
            messagebox.showinfo("Result", f"{searched_discount} is available")
        else:
            messagebox.showwarning("Result", f"{searched_discount} is not available")
    except FileNotFoundError:
        messagebox.showerror("Error", "Discount.txt not found.")

def update_book():
    try:
        with open("Library.txt", "r") as books:
            all_books = books.readlines()

        books_update = simpledialog.askstring("Update", "Enter the book you need to update:")
        if books_update in [book.strip() for book in all_books]:
            new_name = simpledialog.askstring("Update", "Enter the new name of the book (leave blank to keep current):")
            new_category = simpledialog.askstring("Update", "Enter the new category of the book (leave blank to keep current):")

            new_name = new_name if new_name else books_update
            new_category = new_category if new_category else all_books[all_books.index(books_update)].split('[')[1][:-2]

            all_books = [f"{new_name}[{new_category}]\n" if book.strip() == books_update else book for book in all_books]

            with open("Library.txt", "w") as books:
                books.writelines(all_books)

            messagebox.showinfo("Success", "Book updated successfully.")
        else:
            messagebox.showwarning("Warning", "Book not found.")
    except FileNotFoundError:
        messagebox.showerror("Error", "Library.txt not found.")

def return_book():
    try:
        with open("Borrowed.txt", "r") as borrowed_books:
            all_borrowed_books = borrowed_books.readlines()

        book_to_return = simpledialog.askstring("Return", "Enter the borrowed book you want to return:")
        if book_to_return in [book.strip().split('[')[0] for book in all_borrowed_books]:
            all_borrowed_books = [book for book in all_borrowed_books if book.strip().split('[')[0] != book_to_return]
            with open("Borrowed.txt", "w") as borrowed_books:
                borrowed_books.writelines(all_borrowed_books)

            messagebox.showinfo("Success", "Book returned successfully.")
        else:
            messagebox.showwarning("Warning", "Book not found in borrowed list.")
    except FileNotFoundError:
        messagebox.showerror("Error", "Borrowed.txt not found.")

def book_statistics():
    try:
        with open("Library.txt", "r") as books:
            all_books = books.readlines()

        with open("Borrowed.txt", "r") as borrowed_books:
            all_borrowed_books = borrowed_books.readlines()

        total_books = len(all_books)
        total_borrowed = len(all_borrowed_books)

        messagebox.showinfo("Statistics", f"Total books available: {total_books}\nTotal books borrowed: {total_borrowed}")
    except FileNotFoundError:
        messagebox.showerror("Error", "Library.txt or Borrowed.txt not found.")

def show_categories():
    try:
        with open("Library.txt", "r") as books:
            all_books = books.readlines()

        categories = set(book.strip().split('[')[1][:-1] for book in all_books if '[' in book)
        messagebox.showinfo("Categories", "\n".join(categories))
    except FileNotFoundError:
        messagebox.showerror("Error", "Library.txt not found.")

def main():
    root = tk.Tk()
    root.title("Library System")

    tk.Button(root, text="Show Books", command=show_books).pack(pady=10)
    tk.Button(root, text="Add Book", command=add_book).pack(pady=10)
    tk.Button(root, text="Delete Book", command=delete_book).pack(pady=10)
    tk.Button(root, text="Search Book", command=search_book).pack(pady=10)
    tk.Button(root, text="Add Borrowed Book", command=add_borrowed_book).pack(pady=10)
    tk.Button(root, text="Show Borrowed Books", command=show_borrowed_books).pack(pady=10)
    tk.Button(root, text="Search Borrowed Book", command=search_borrowed_book).pack(pady=10)
    tk.Button(root, text="Show Discounts", command=show_discounts).pack(pady=10)
    tk.Button(root, text="Add Discount", command=add_discount).pack(pady=10)
    tk.Button(root, text="Delete Discount", command=delete_discount).pack(pady=10)
    tk.Button(root, text="Search Discount", command=search_discount).pack(pady=10)
    tk.Button(root, text="Update Book", command=update_book).pack(pady=10)
    tk.Button(root, text="Return Book", command=return_book).pack(pady=10)
    tk.Button(root, text="Show Book Statistics", command=book_statistics).pack(pady=10)
    tk.Button(root, text="Show Categories", command=show_categories).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()