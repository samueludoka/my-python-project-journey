def search():
    print("search")


def phone_book():
    print("Phone Book")
    print("""
    1 -> Search
    2 -> Service Nos
    3 -> Add name
    4 -> Erase
    5 -> Edit
    6 -> Assign tone
    7 -> Send b'card
    8 -> Option
    9 -> speed dials
    10 -> Voice tags
    11 -> Go back to main menu""")
    phone_book_menu = input("enter option: ")
    if phone_book_menu == 1:
        search()
    elif phone_book_menu == 2:
        print("Service Nos")
    elif phone_book_menu == 3:
        print("Add name")
    elif phone_book_menu == 4:
        print("Erase")


def chat():
    print("Chat")


def call_register():
    print("Call register")


def messages():
    print("Messages")


print("""
1 -> Phone book
2 -> Messages
3 -> Chat
4 -> Call register
5 -> Tones
6 -> Settings
7 -> Call divert
8 -> Games
9 -> Calculator
10 -> Reminders
11 -> Clock
12 -> Profiles
13 -> Sim services
        """)
option = input("select option: ")
if option == 1:
    phone_book()


    def search():
        print("search")
elif option == 2:
    messages()
elif option == 3:
    chat()
elif option == 4:
    call_register()
print("""
1 -> Search
2 -> Service Nos
3 -> Add name
4 -> Erase
5 -> Edit
6 -> Assign tone
7 -> Send b'card
8 -> Option
9 -> speed dials
10 -> Voice tags
11 -> Go back to main menu""")


print(phone_book())
