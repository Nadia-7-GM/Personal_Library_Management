import json

# Library storage
library = []

# Load library from file
def load_library():
    global library
    try:
        with open("library.txt", "r") as file:
            library = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        library = []


# Save library in plain text format (each book on a new line)
def save_library():
    with open("library.txt", "w") as file:
        for book in library:
            file.write(f"Title: {book['title']}\n")
            file.write(f"Author: {book['author']}\n")
            file.write(f"Status: {book['status']}\n")
            file.write("-" * 30 + "\n")  # Separator for readability


# Add a book
def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    status = input("Have you read this book? (yes/no): ").strip().lower()

    book = {"title": title, "author": author, "status": "Read" if status == "yes" else "Unread"}
    library.append(book)
    save_library()
    print(f"✅ Book '{title}' added successfully!")

# Search for a book
def search_book():
    title = input("Enter book title to search: ").strip()
    found_books = [book for book in library if book["title"].lower() == title.lower()]

    if found_books:
        for book in found_books:
            print(f"📖 Title: {book['title']}, Author: {book['author']}, Status: {book['status']}")
    else:
        print("❌ Book not found!")

# Remove a book
def remove_book():
    title = input("Enter book title to remove: ").strip()
    global library
    new_library = [book for book in library if book["title"].lower() != title.lower()]

    if len(new_library) == len(library):
        print("❌ Book not found!")
    else:
        library = new_library
        save_library()
        print(f"✅ Book '{title}' removed successfully!")

# Display all books
def display_books():
    if not library:
        print("📚 Library is empty!")
    else:
        print("\n📖 Library Collection:")
        for i, book in enumerate(library, 1):
            print(f"{i}) {book['title']} by {book['author']} - {book['status']}")

# Show statistics
def show_statistics():
    total_books = len(library)
    read_books = sum(1 for book in library if book["status"] == "Read")
    unread_books = total_books - read_books

    print("\n📊 Library Statistics:")
    print(f"📚 Total Books: {total_books}")
    print(f"📖 Read Books: {read_books}")
    print(f"📕 Unread Books: {unread_books}")

# Main menu
def main_menu():
    load_library()
    while True:
        print("\n📚 Library Menu")
        print("1) Add a Book")
        print("2) Search a Book")
        print("3) Remove a Book")  # ✅ Fixed choice format
        print("4) Display All Books")
        print("5) Show Statistics")
        print("6) Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            remove_book()  # ✅ Remove book option added
        elif choice == "4":
            display_books()
        elif choice == "5":
            show_statistics()
        elif choice == "6":
            print("🚪 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
