import random
import time


books_main = {"Harry Potter and the Sorcerer's Stone":
              {'Author Surname': 'Rowling', 'Genre': 'Fantasy', 'Rating': 2, 'Note': 'pretty mid'},
              'Norwegian Wood':
                  {'Author Surname': 'Murakami', 'Genre': 'Romance', 'Rating': 4, 'Note': 'Deep'}}
books_titles = []
books_authors = []
books_genres = []
books_ratings = []
books_notes = []


def list_books():
    global books_titles
    books_titles = list(books_main.keys())
    for key, value in books_main.items():
        books_authors.append(value["Author Surname"])
        books_genres.append(value["Genre"])
        books_ratings.append(value["Rating"])
        books_notes.append(value["Note"])


def books_add():
    new_book_title = input("Enter the name of the book to be added: ")
    new_book_author = input("Enter the surname of the book's author: ")
    new_book_genre = input("Enter the genre of the book: ")
    new_book_rating = input("Enter your rating for this book: ")
    new_book_note = input("Enter any note about this book: ")
    books_titles.append(new_book_title)
    books_authors.append(new_book_author)
    books_genres.append(new_book_genre)
    books_ratings.append(new_book_rating)
    books_notes.append(new_book_note)
    print('Book data added successfully.')


def books_remove():
    book_kill = input("Enter the title of the book you would like to remove.")
    i = 0
    found = False
    while not found and i < len(books_titles):
        if books_titles[i] == book_kill:
            books_titles.remove(books_titles[i])
            books_authors.remove(books_authors[i])
            books_genres.remove(books_ratings[i])
            books_ratings.remove(books_ratings[i])
            books_notes.remove(books_notes[i])
        else:
            i += 1
    if not found:
        print(f"The book {book_kill} was not found in the database.")
    else:
        print(f"The book {book_kill} was removed from the database.")


def clear_lists():
    books_titles.clear()
    books_authors.clear()
    books_genres.clear()
    books_ratings.clear()
    books_notes.clear()


def books_overwrite(dex, order):
    books_titles[order] = books_titles[dex]
    books_authors[order] = books_authors[dex]
    books_genres[order] = books_genres[dex]
    books_ratings[order] = books_ratings[dex]
    books_notes[order] = books_notes[dex]


def sort_books(sort_choice):
    list_books()
    books_raw = sort_choice
    sort_complete = False
    while not sort_complete:
        sort_complete = True
        o = 0
        for i in range(len(books_raw) - 1):
            if books_raw[i] > books_raw[i + 1]:
                temp = books_raw[i]
                books_raw[i] = books_raw[i + 1]
                books_raw[i + 1] = temp
                books_overwrite(i, o)
                o += 1
                sort_complete = False
        books_main.clear()
        n = 0
        i = 0
        while i < len(books_raw) and n < len(sort_choice):
            if books_raw[i] == sort_choice[n]:
                book_data = {'Author Surname': books_authors[n], 'Genre': books_genres[n],
                             'Rating': books_ratings[n], 'Note': books_notes[n]}
                books_main.setdefault(books_titles[n], book_data)
                i = 0
                n += 1
            else:
                i += 1


def display_books():
    for i in range(len(books_titles)):
        print('Book:', books_titles[i])
        print('Author:', books_authors[i])
        print('Genre:', books_genres[i])
        print('Rating:', books_ratings[i])
        print('Note:', books_notes[i])


def write_books(user_file):
    with open(user_file, 'w') as file:
        for i in range(len(books_titles)):
            file.write(f"{books_titles[i]}, {books_authors[i]}, "
                       f"{books_genres[i]}, {books_ratings[i]}, {books_notes[i]} \n")


def read_books(user_file):
    try:
        with open(user_file, 'r') as f:
            clear_lists()
            for line in f:
                title, author, genre, rating, note = line.strip().split(',')
                books_titles.append(title)
                books_authors.append(author)
                books_genres.append(genre)
                books_ratings.append(rating)
                books_notes.append(note)
    except FileNotFoundError:
        print('file not found')






# Bookbuddy - Xavi & James

def loading():
    for i in range(3):
        print("\rLoading", end="", flush=True)
        time.sleep(0.4)
        print("\rLoading.", end="", flush=True)
        time.sleep(0.4)
        print("\rLoading..", end="", flush=True)
        time.sleep(0.4)
        print("\rLoading...", end="", flush=True)
        time.sleep(0.4)
    print("\rI", end="", flush=True)
    time.sleep(0.1)
    print("\rIn", end="", flush=True)
    time.sleep(0.1)
    print("\rIni", end="", flush=True)
    time.sleep(0.1)
    print("\rInit", end="", flush=True)
    time.sleep(0.1)
    print("\rIniti", end="", flush=True)
    time.sleep(0.1)
    print("\rInitia", end="", flush=True)
    time.sleep(0.1)
    print("\rInitial", end="", flush=True)
    time.sleep(0.1)
    print("\rInitiali", end="", flush=True)
    time.sleep(0.1)
    print("\rInitializ", end="", flush=True)
    time.sleep(0.1)
    print("\rInitializi", end="", flush=True)
    time.sleep(0.1)
    print("\rInitializin", end="", flush=True)
    time.sleep(0.1)
    print("\rInitializing", end="", flush=True)
    time.sleep(0.1)
    print("\rInitializing.", end="", flush=True)
    time.sleep(0.1)
    print("\rInitializing..", end="", flush=True)
    time.sleep(0.1)
    print("\rInitializing...", end="", flush=True)
    time.sleep(0.1)


print("\r", end="", flush=True)


def main_menu():
    while 1 == 1:
        time.sleep(0.5)
        list_books()
        print(''' \033[32m                                                                                .--.           .---.        .-.
        ▀██▀▀█▄                   ▀██      ▀██                   ▀██      ▀██                   .---|--|   .-.     | J |  .---. |~|    .--.
         ██   ██    ▄▄▄     ▄▄▄    ██  ▄▄   ██ ▄▄▄  ▄▄▄ ▄▄▄    ▄▄ ██    ▄▄ ██   ▄▄▄▄ ▄▄▄     .--|===|MA|---|_|--.__| A |--|:::| |~|-==-|==|---.
         ██▀▀▀█▄  ▄█  ▀█▄ ▄█  ▀█▄  ██ ▄▀    ██▀  ██  ██  ██  ▄▀  ▀██  ▄▀  ▀██    ▀█▄  █      |TS| P |DE|===| |~~|BY| M |--| & |_|~|XAVI|  |___|-.
         ██    ██ ██   ██ ██   ██  ██▀█▄    ██    █  ██  ██  █▄   ██  █▄   ██     ▀█▄█       |  | S |  |===| |==|  | E |  |:::|=| |    |  |---|=|
        ▄██▄▄▄█▀   ▀█▄▄█▀  ▀█▄▄█▀ ▄██▄ ██▄  ▀█▄▄▄▀   ▀█▄▄▀█▄ ▀█▄▄▀██▄ ▀█▄▄▀██▄     ▀█        |  | K |  |   |_|__|  | S |__|   | | |    |  |___| |
                                                                                ▄▄ █         |~~|===|--|===|~|~~|%%|~~~|--|:::|=|~|----|==|---|=|
                                                                                 ▀▀          ^--^---'--^---^-^--^--^---'--^---^-^-^-==-^--^---^-^'''  "\033[3m" "\033[1m",
              "By: Xavi & James" "\033[22m")
        print('\033[0m')
        time.sleep(1)
        # https://www.asciiart.eu/books/books
        print("Enter", "\033[1m""\033[32m" + "1" + "\033[0m""\033[22m", "to add a book to your library" 
              "\nEnter " "\033[32m""\033[1m" + "2" + "\033[0m""\033[22m", "to remove a book from your library"
              "\nEnter""\033[32m""\033[1m" + " 3" + "\033[0m""\033[22m", "to search for a book in your library"
              "\nEnter""\033[32m""\033[1m" + " 4" + "\033[0m""\033[22m", "to display your library"
              "\nEnter""\033[32m""\033[1m" + " 5" + "\033[0m""\033[22m", "to save your books' data to a file"
              "\nEnter""\033[32m""\033[1m" + " 6" + "\033[0m""\033[22m", "to load your books' data from a file"
              "\nEnter", "\033[32m""\033[1m" + "999" + "\033[0m""\033[22m", "to exit your library")
        menu_input = (input("\033[1m" + "Enter your input → " + "\033[22m", ))

        if menu_input == '1':
            books_add()
        elif menu_input == '2':
            books_remove()
        elif menu_input == '3':
            pass
        elif menu_input == '4':
            print('What would you like to sort your books by? ')
            print("Enter", "\033[1m""\033[32m" + "1" + "\033[0m""\033[22m", "to sort alphabetically by title"
                  "\nEnter " "\033[32m""\033[1m" + "2" + "\033[0m""\033[22m",
                  "to sort alphabetically by author"
                  "\nEnter""\033[32m""\033[1m" + " 3" + "\033[0m""\033[22m", "to sort by genre"
                  "\nEnter""\033[32m""\033[1m" + " 4" + "\033[0m""\033[22m",
                  "to sort by rating (ascending)"
                  "\nEnter", "\033[32m""\033[1m" + "5" + "\033[0m""\033[22m", "to sort by rating (descending)")
            sort_option = (input("\033[1m" + "Enter your input → " + "\033[22m", ))
            if sort_option == "1":
                sort_books(books_titles)
            elif sort_option == "2":
                sort_books(books_authors)
            elif sort_option == "3":
                sort_books(books_genres)
            elif sort_option == "4":
                sort_books(books_ratings)
            elif sort_option == "5":
                pass
            else:
                print("Invalid option")
                main_menu()
            display_books()
        elif menu_input == '5':
            file_save = input('What file would you like to save your data to? ')
            write_books(file_save)
        elif menu_input == '6':
            file_load = input('What file would you like to read your data from? ')
            read_books(file_load)
        elif menu_input == '999':
            print('Thank you for using Bookbuddy!')
            exit()
        else:
            print("\033[91m" + "Invalid Input." + "\033[0m")
            main_menu()


def main():
    main_menu()


if __name__ == '__main__':
    main()
