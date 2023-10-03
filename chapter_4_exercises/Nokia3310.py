def nokia_function():
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
    option = int(input("Select an option: "))
    if option == 1:
        print(phone_book())
    elif option == 2:
        print(messages())
    elif option == 3:
        print(chat())
    elif option == 4:
        print(call_register())
    elif option == 5:
        print(Tones())
    elif option == 6:
        print(settings())
    elif option == 7:
        print(call_divert())
    elif option == 8:
        print(games())
    elif option == 9:
        print(calculator())
    elif option == 10:
        print(remainder())
    elif option == 11:
        print(clock())
    elif option == 12:
        print(profiles())
    elif option == 13:
        print(sim_services())


def chat():
    print("Chat")


def call_register():
    print("Call register")
    print(""""
        1 -> Missed calls
        2 -> Received calls
        3 -> Dialled numbers
        4 -> Erase recent call duration
        5 -> Show call duration
        6 -> Show call costs
        7 -> Call cost settings
        8 -> Prepaid credit
    """)
    call_register_menu = int(input("enter call register options"))
    if call_register_menu == 1:
        print("missed calls")
    elif call_register_menu == 2:
        print("recieved calls")
    elif call_register_menu == 3:
        print("dialled numbers")
    elif call_register_menu == 4:
        print("erase recent calls")
    elif call_register_menu == 5:
        print("show call duration")
        print(""""
        1 -> Last call duration
        2 -> All calls duration
        3 -> Received calls duration
        4 -> Dialled calls duration
        5 -> Clear timers
        6 -> Return to call menu
        7 -> Return to main menu
        """)
        show_call_duration = int(input("show call duration options"))
        if show_call_duration == 1:
            print("Last call duration")
        elif show_call_duration == 2:
            print("All calls duration")
        elif show_call_duration == 3:
            print("Received calls duration")
        elif show_call_duration == 4:
            print("Dialled calls duration")
        elif show_call_duration == 5:
            print("Clear timers")
        elif show_call_duration == 6:
            print(call_register())
        elif show_call_duration == 7:
            print(nokia_function())
    elif call_register_menu == 6:
        print("show call cost")
        print(""""
        1 -> last call duration
        2 -> All calls cost
        3 -> Clear timer
        4 -> Return to call menu
        5 -> return to main menu
        """)
        show_call_cost = int(input("enter show call cost menu"))
        if show_call_cost == 1:
            print("last call duration")
        elif show_call_cost == 2:
            print("All calls duration")
        elif show_call_cost == 3:
            print("clear timers")
        elif show_call_cost == 4:
            print(call_register())
        elif show_call_cost == 5:
            print(nokia_function())
    elif call_register_menu == 7:
        print("call cost setting")
        print(""""
        1 -> Call cost setting
        2 -> show costs in
        3 -> return to call setting
        4 -> return to main menu
        """)
        call_cost_setting = int(input("enter call cost setting option"))
        if call_cost_setting == 1:
            print("call cost setting")
        elif call_cost_setting == 2:
            print("show call cost setting")
        elif call_cost_setting == 3:
            print(call_register())
        elif call_cost_setting == 4:
            print(nokia_function())
    elif call_register_menu == 8:
        print("prepaid credit")
    elif call_register_menu == 9:
        print("message validity")






def messages():
    print("messages")
    print(""""
        1 -> Write messages
        2 -> Inbox
        3 -> Outbox
        4 -> Picture messages
        5 -> Templates
        6 -> Smileys
        7 -> Message settings
        8 -> Info service
        9 -> Voice mailbox number
        10 -> service command editor
        11 -> return to main menu
        """)

    message_menu = int(input("enter message option"))
    if message_menu == 1:
        print("write message")
    elif message_menu == 2:
        print("inbox")
    elif message_menu == 3:
        print("outbox")
    elif message_menu == 4:
        print("picture messages")
    elif message_menu == 5:
        print("Templates")
    elif message_menu == 6:
        print("smileys")
    elif message_menu == 7:
        print("message setting")
        print(""""
            1 -> Set
            2 -> Common
            3 -> return to message menu
            4 -> return to main menu
            """)
        message_setting = int(input("enter message setting"))
        if message_setting == 1:
            print("set")
        elif message_setting == 2:
            print("common")
        elif message_setting == 3:
            print(messages())
        elif message_setting == 4:
            print(nokia_function())

    elif message_menu == 8:
        print("service info")
    elif message_menu == 9:
        print("service")
    elif message_menu == 10:
        print("service command editor")
    elif message_menu == 11:
        print("message validator")
    elif message_menu == 12:
        print(nokia_function())


def Tones():
    print("Tones")
    print(""""
        1 -> Ringing tone
        2 -> Ringing volume
        3 -> Incoming call alert
        4 -> Composer
        5 -> Message alert tone
        6 -> Keypad tones
        7 -> Warning and game tones
        8 -> Vibrating alert
        9 -> Screen saver
        """)
    tones = int(input("enter tones menu"))
    if tones == 1:
        print("ringing tone")
    elif tones == 2:
        print("ringing volume")
    elif tones == 3:
        print("incoming call alert")
    elif tones == 4:
        print("composer")
    elif tones == 5:
        print("message alert tone")
    elif tones == 6:
        print("keypad tones")
    elif tones == 7:
        print("warning and game tones")
    elif tones == 8:
        print("vibrating alert")
    elif tones == 9:
        print("screen saver")


def phone_Book():
    print("phone book")


def settings():
    print("settings")
    print(""""
        1 -> Call settings
        2 -> Phone settings
        3 -> security settings
        4 -> Restore factory settings
        """)
    setting = int(input("settings menu"))
        if setting == 1:
            print("call setting")
            print(""""
            1 -> Automatic redial
            2 -> Speed dialling
            3 -> Call waiting options
            4 -> Own number sending
            5 -> Phone line in use
            6 -> Automatic answer
            7 -> return to setting
            8 -> return main menu
            """)




def call_divert():
    print("call divert")


def games():
    print("games")


def calculator():
    print("calculator")


def remainder():
    print("remainder")


def clock():
    print("clock")


def profiles():
    print("profiles")


def sim_services():
    print("sim services")


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
    phone_book_menu = int(input("enter option: "))
    if phone_book_menu == 1:
        print("search")
    elif phone_book_menu == 2:
        print("Service Nos")
    elif phone_book_menu == 3:
        print("Add name")
    elif phone_book_menu == 4:
        print("Erase")
    elif phone_book_menu == 5:
        print("Edit")
    elif phone_book_menu == 6:
        print("Assign tone")
    elif phone_book_menu == 7:
        print("Send b'card")
    elif phone_book_menu == 8:
        print("option")
        print(""""
            1 -> Type of view
            2 -> Memory status 
            3 -> go back to phone book
            4 -> go back to main menu   
        """)
        option = int(input("enter option"))
        if option == 1:
            print("Type of view")
        elif option == 2:
            print("memory status")
        elif option == 3:
            print(phone_book())
        elif option == 4:
            print(nokia_function())
    elif phone_book_menu == 9:
        print("speed dials")
    elif phone_book_menu == 10:
        print("voice tags")
    elif phone_book_menu == 11:
        print(nokia_function())


print(nokia_function())
