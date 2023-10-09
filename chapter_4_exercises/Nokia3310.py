# why do u have to print ur menu, cant u pust the message in your input function ??
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
    option = input("Select an option: ")
    if option == '1':
        print(phone_book())
    elif option == '2':
        print(messages())
    elif option == '3':
        print(chat())
    elif option == '4':
        print(call_register())
    elif option == '5':
        print(Tones())
    elif option == '6':
        print(settings())
    elif option == '7':
        print(call_divert())
    elif option == '8':
        print(games())
    elif option == '9':
        print(calculator())
    elif option == '10':
        print(remainder())
    elif option == '11':
        print(clock())
    elif option == '12':
        print(profiles())
    elif option == '13':
        print(sim_services())


def chat():
    print("pres 1 to return to main menu")
    print("Chat")
    chats = (input("chat menu"))
    if chats == '1':
        print(nokia_function())


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
        9 -> return to main menu
    """)
    call_register_menu = (input("enter call register options"))
    if call_register_menu == '1':
        print("missed calls")
    elif call_register_menu == '2':
        print("received calls")
    elif call_register_menu == '3':
        print("dialled numbers")
    elif call_register_menu == '4':
        print("erase recent calls")
    elif call_register_menu == '5':
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
        show_call_duration = (input("show call duration options"))
        if show_call_duration == '1':
            print("Last call duration")
        elif show_call_duration == '2':
            print("All calls duration")
        elif show_call_duration == '3':
            print("Received calls duration")
        elif show_call_duration == '4':
            print("Dialled calls duration")
        elif show_call_duration == '5':
            print("Clear timers")
        elif show_call_duration == '6':
            print(call_register())
        elif show_call_duration == '7':
            print(nokia_function())
    elif call_register_menu == '6':
        print("show call cost")
        print(""""
        1 -> last call duration
        2 -> All calls cost
        3 -> Clear timer
        4 -> Return to call menu
        5 -> return to main menu
        """)
        show_call_cost = (input("enter show call cost menu"))
        if show_call_cost == '1':
            print("last call duration")
        elif show_call_cost == '2':
            print("All calls duration")
        elif show_call_cost == '3':
            print("clear timers")
        elif show_call_cost == '4':
            print(call_register())
        elif show_call_cost == '5':
            print(nokia_function())
    elif call_register_menu == '7':
        print("call cost setting")
        print(""""
        1 -> Call cost setting
        2 -> show costs in
        3 -> return to call setting
        4 -> return to main menu
        """)
        call_cost_setting = (input("enter call cost setting option"))
        if call_cost_setting == '1':
            print("call cost setting")
        elif call_cost_setting == '2':
            print("show call cost setting")
        elif call_cost_setting == '3':
            print(call_register())
        elif call_cost_setting == '4':
            print(nokia_function())
    elif call_register_menu == '8':
        print("prepaid credit")
    elif call_register_menu == '9':
        print(nokia_function())


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

    message_menu = input("enter message option")
    if message_menu == '1':
        print("write message")
    elif message_menu == '2':
        print("inbox")
    elif message_menu == '3':
        print("outbox")
    elif message_menu == '4':
        print("picture messages")
    elif message_menu == '5':
        print("Templates")
    elif message_menu == '6':
        print("smileys")
    elif message_menu == '7':
        print("message setting")
        print("""
            1 -> Set
            2 -> Common
            3 -> return to message menu
            4 -> return to main menu
            """)
        message_setting = input("message setting menu")
        if message_setting == '1':
            print("set_input")
            print("""
            1 -> message center number
            2 -> message sent as
            3 -> message validity
            4 -> return to message
            5 -> return to main menu
            """)
            set_input = input("enter set_input menu")
            if set_input == '1':
                print("message center number")
            elif set_input == '2':
                print("message sent as")
            elif set_input == '3':
                print("message validity")
            elif set_input == '4':
                print(messages())
            elif set_input == '5':
                print(nokia_function())


        elif message_setting == '2':
            print("common")
            print(""""
            1 -> delivery reports
            2 -> reply via same centre
            3 -> character support
            4 -> return to message
            5 -> return to main menu
            """)
            common = input("enter common menu: ")
            if common == '1':
                print("delivery report")
            elif common == '2':
                print("reply via same centre")
            elif common == '3':
                print("character support")
            elif common == '4':
                print(messages())
            elif common == '5':
                print(nokia_function())

    elif message_menu == '8':
        print("service info")
    elif message_menu == '9':
        print("voice mailbox number")
    elif message_menu == '10':
        print("service command editor")
    elif message_menu == '11':
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
        10 -> return to main menu
        """)
    tones = (input("enter tones menu"))
    if tones == '1':
        print("ringing tone")
    elif tones == '2':
        print("ringing volume")
    elif tones == '3':
        print("incoming call alert")
    elif tones == '4':
        print("composer")
    elif tones == '5':
        print("message alert tone")
    elif tones == '6':
        print("keypad tones")
    elif tones == '7':
        print("warning and game tones")
    elif tones == '8':
        print("vibrating alert")
    elif tones == '9':
        print("screen saver")
    elif tones == '10':
        print(nokia_function())


def settings():
    print("settings")
    print(""""
        1 -> Call settings
        2 -> Phone settings
        3 -> security settings
        4 -> Restore factory settings
        5 -> return to main menu
        """)
    setting_menu = input("settings menu")
    if setting_menu == '1':
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
        call_setting = input("call setting menu")
        if call_setting == '1':
            print("Automatic redial")
        elif call_setting == '2':
            print("Speed dialling")
        elif call_setting == '3':
            print("Call waiting options")
        elif call_setting == '4':
            print("Own number sending")
        elif call_setting == '5':
            print("Phone line in use")
        elif call_setting == '6':
            print("Automatic answer")
        elif call_setting == '7':
            print(settings())
        elif call_setting == '8':
            print(nokia_function())
    elif setting_menu == '2':
        print("phone setting")
        print(""""
        1 -> Language
        2 -> Cell info display
        3 -> Welcome note
        4 -> Network selection
        5 -> Lights
        6 -> Confirm SIM service actions
        7 -> return to settings
        8 -> return to main menu
        """)
        phone_setting = input("phone setting menu")
        if phone_setting == '1':
            print("language")
        elif phone_setting == '2':
            print("call info display")
        elif phone_setting == '3':
            print("welcome note")
        elif phone_setting == '4':
            print("network selection")
        elif phone_setting == '5':
            print("lights")
        elif phone_setting == '6':
            print("Confirm SIM service actions")
        elif phone_setting == '7':
            print(settings())
        elif phone_setting == '8':
            print(nokia_function())
    elif setting_menu == '3':
        print("security settings")
        print(""""
        1 -> pin code request
        2 -> call baring service
        3 -> fixed dialling
        4 -> closed user group
        5 -> phone security
        6 -> change access codes
        7 -> return to settings
        8 -> return to main menu
        """)
        security = input("security settings menu")
        if security == '1':
            print("pin code request")
        elif security == '2':
            print("call baring service")
        elif security == '3':
            print("fixed dialling")
        elif security == '4':
            print("closed user group")
        elif security == '5':
            print("phone security")
        elif security == '6':
            print("change access codes")
        elif security == '7':
            print(settings())
        elif security == '8':
            print(nokia_function())
    elif setting_menu == '4':
        print("restore factory settings")
    elif setting_menu == '5':
        print(nokia_function())




def call_divert():
    print("call divert")
    print("press 1 -> to go back to menu")
    divert = (input("enter call divert menu"))
    if divert == '1':
        print(nokia_function())




def games():
    print("games")
    print("press 1 -> to go back to menu")
    game = (input("games menu"))
    if game == '1':
        print(nokia_function())




def calculator():
    print("calculator")
    print("press 1 -> to go back to menu")
    calculators = (input("calculator menu"))
    if calculators == '1':
        print(nokia_function())




def remainder():
    print("remainder")
    print("press 1 -> to go back to menu")
    remainders = (input("remainder menu"))
    if remainders == '1':
        print(nokia_function())




def clock():
    print("clock")
    print(""""
    1 -> Alarm clock
    2 -> Clock settings
    3 -> Date setting
    4 -> Stopwatch
    5 -> Countdown timer
    6 -> Auto update of date and time
    7 -> return to menu
    """)
    clocks = (input("clock menu"))
    if clocks == '1':
        print("alarm clock")
    elif clocks == '2':
        print("clock setting")
    elif clocks == '3':
        print("date setting")
    elif clocks == '4':
        print("stopwatch")
    elif clocks == '5':
        print("countdown timer")
    elif clocks == '6':
        print("Auto update of date and time")
    elif clocks == '7':
        print(nokia_function())


def profiles():
    print("profiles")
    print("press 1 -> to go back to menu")
    profile = (input("profile menu"))
    if profile == '1':
        print(nokia_function())


def sim_services():
    print("sim services")
    print("press 1 -> to go back to menu")
    sim = (input("sim services menu"))
    if sim == '1':
        print(nokia_function())


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
    phone_book_menu = (input("enter option: "))
    if phone_book_menu == '1':
        print("search")
    elif phone_book_menu == '2':
        print("Service Nos")
    elif phone_book_menu == '3':
        print("Add name")
    elif phone_book_menu == '4':
        print("Erase")
    elif phone_book_menu == '5':
        print("Edit")
    elif phone_book_menu == '6':
        print("Assign tone")
    elif phone_book_menu == '7':
        print("Send b'card")
    elif phone_book_menu == '8':
        print("option")
        print(""""
            1 -> Type of view
            2 -> Memory status 
            3 -> return to phone book
            4 -> return to main menu   
        """)
        option = (input("enter option"))
        if option == '1':
            print("Type of view")
        elif option == '2':
            print("memory status")
        elif option == '3':
            print(phone_book())
        elif option == '4':
            print(nokia_function())
    elif phone_book_menu == '9':
        print("speed dials")
    elif phone_book_menu == '10':
        print("voice tags")
    elif phone_book_menu == '11':
        print(nokia_function())


nokia_function()
