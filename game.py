"""
Do not remove this file. Ensure your main function is in this file.

I will execute your game like this:

python3 game.py

Yes, you may add additional files to this folder.
"""
import copy
import random
import itertools
import time


def game():
    """
    A game function
    """
    init_story()
    columns = rows = 15
    character, board = generate_character(rows=rows, columns=columns), make_board(rows=rows, columns=columns)
    while not is_character_level_3(character=character) and is_alive(character["HP"]):
        describe_location(board=board, rows=rows, columns=columns, character=character)
        direction = get_user_choice()
        if validate_move(character=character, rows=rows, columns=columns, direction=direction):
            move_character(board, character, direction)
            if is_boss(rows=rows, columns=columns, character=character):
                break
            describe_location(board=board, rows=rows, columns=columns, character=character)
            check_for_monsters(character=character)
            check_character_attributes(character=character)
        else:
            print("You are about to go off the board! Don't do it again!\n")
    boss_stage = fight_with_boss(character=character) if is_alive(hp=character["HP"]) else False
    show_result(is_alive(character["HP"]), boss_stage)


def init_story():
    """ A function prints a story

    :postcondition: prints a sentence per 1.5 second when the function is invoked
    :return: nothing
    """
    story_list = ("A long time ago..", "There was a hero called a CS student who fights for the justice... ",
                  "He killed a lot of course monsters, and finally defeated the Exam Dragon...", "And peace has come..",
                  "A thousand of years, now, the CS Student is nowhere, and the dark seeps in...",
                  "The world needs a saver... ")
    print("*******************************************************************************")
    for sentence in story_list:
        print(sentence)
        time.sleep(1.5)
    print("*******************************************************************************\n\n\n")


def is_character_level_3(character: dict) -> bool:
    """ A function checks whether the character is in Level 3 or not.

    :param: character: a dict
    :precondition: character should contain proper key-value pairs that represents the attributes of the character
    :precondition: isinstance(character['Level'], int) is True
    :postcondition: checks if the character's level is 3 or not
    :return: return True if character['Level'] == 3 else False

    >>> level_2_character = {'Level': 2}
    >>> level_3_character = {'Level': 3}
    >>> is_character_level_3(level_2_character)
    False
    >>> is_character_level_3(level_3_character)
    True
    """
    return True if character['Level'] == 3 else False


def show_result(is_char_alive: bool, did_character_defeat_the_boss: bool):
    """ A function shows the result

    :param: is_char_alive: a bool that represents the character has positive hp or not
    :param: did_character_defeat_the_boss: a bool represents if the character won the boss
    :precondition: both argument can't be different. If they are different, it prints nothing.
    :postcondition: prints the end massage depends on what the situation is.
    :return: nothing
    """
    if not is_char_alive:
        print(r"""
            ███████╗ ██████╗ ██████╗ ██████╗ ██╗   ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗    ██████╗ ██╗███████╗██████╗ 
            ██╔════╝██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██║██╔════╝██╔══██╗
            ███████╗██║   ██║██████╔╝██████╔╝ ╚████╔╝      ╚████╔╝ ██║   ██║██║   ██║    ██║  ██║██║█████╗  ██║  ██║
            ╚════██║██║   ██║██╔══██╗██╔══██╗  ╚██╔╝        ╚██╔╝  ██║   ██║██║   ██║    ██║  ██║██║██╔══╝  ██║  ██║
            ███████║╚██████╔╝██║  ██║██║  ██║   ██║          ██║   ╚██████╔╝╚██████╔╝    ██████╔╝██║███████╗██████╔╝
            ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝          ╚═╝    ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝╚══════╝╚═════╝                                                                                             
        """)
    elif did_character_defeat_the_boss:
        print(r"""
             ██████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗  █████╗ ████████╗███████╗██╗
            ██╔════╝██╔═══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
            ██║     ██║   ██║██╔██╗ ██║██║  ███╗██████╔╝███████║   ██║   ███████╗██║
            ██║     ██║   ██║██║╚██╗██║██║   ██║██╔══██╗██╔══██║   ██║   ╚════██║╚═╝
            ╚██████╗╚██████╔╝██║ ╚████║╚██████╔╝██║  ██║██║  ██║   ██║   ███████║██╗
             ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
        """)


def generate_character(columns: int, rows: int) -> dict:
    """ A function starts a process to generate a character's attributes once it's executed.

    :param: row: an integer represents y_coord
    :param: column: an integer represents x_coord
    :precondition: rows and columns should be positive integers.
    :postcondition: execute some functions to make a character's attributes
    :return: a function
    """

    class_list = ("python warrior", "web dev assassin", "db guardian", "project sorcerer")
    name = get_name()
    char_class = get_class(class_list=class_list)
    return generate_character_attributes(name=name, char_class=char_class, rows=rows, columns=columns)


def is_alive(hp: int) -> bool:
    """ A function checks if the character is alive

    :param: hp: an int that represents the character's hp
    :precondition: hp >= 0, possibly hp < 0
    :postcondition: checks if hp is greater than 0
    :return: return True if hp > 0 else return False
    >>> pos_hp = 76
    >>> neg_hp = -15
    >>> is_alive(pos_hp)
    True
    >>> is_alive(neg_hp)
    False
    """
    return hp > 0


def is_this_alphabet_word(word: str) -> bool:
    """ A function check whether the str contains only alphabet characters.

    It generates a set based on the value of the word parameter and check the difference with the set of lower cased
    alphabets to check if the word includes only alphabets.

    :param: word: a str
    :precondition: word should be a str object. Possibly it's empty
    :postcondition: the function checks the difference between word and set which is [a, z], and checks if the
                    difference is empty
    :return: return True if the word contains only alphabets else False

    >>> true_word = "edward"
    >>> false_word = "Edward Lee"
    >>> is_this_alphabet_word(true_word)
    True
    >>> is_this_alphabet_word(false_word)
    False
    """
    return set(word).difference({chr(num) for num in range(97, 123)}) == set()


def get_name() -> str:
    """ A function to get a correct name.

    :postcondition: it keeps iterating until it gets the proper name to return, and return name.title()
    :return: a str represents character's name
    """
    while True:
        try:
            name = input("Type your First name. It should contains only alphabets:").lower()
            if not is_this_alphabet_word(word=name) or name == '':
                raise ValueError("Invalid name! Do it again")
            return name.title()
        except ValueError as e:
            print(e)


def get_class(class_list: tuple) -> str:
    """ A function to get a correct command to get a class.

    :param: class_list: a tuple
    :precondition: class_list should contain proper elements that represent classes
    :postcondition: It shows the user the list of the available class first, then it will try to get a proper value
                    from the input, possibly throw an exception if the input is invalid. Return the str if it is valid.
    :return: a str represents character's class
    """
    print("\nChoose your Class:")
    for class_num, class_name in enumerate(class_list):
        print(f"{class_num + 1}) {class_name}")
    print("")
    while True:
        try:
            name = class_list[int(input("Type the name of the class you want to choose:")) - 1]
            return name
        except (TypeError, ValueError, IndexError):
            print("Type correct class name.\n")


def generate_character_attributes(name: str, char_class: str, columns: int, rows: int) -> dict:
    """ A function to concatenate the dict objects that contain character's attributes.

    :param name: a str
    :param char_class: a str
    :param columns: an integer represents x_coord
    :param rows: an integer represents y_coord
    :precondition: name and char_class are supposed to be a str obj that has a proper value
    :precondition: rows and columns > 0
    :postcondition: return a concatenated dict obj.
    :return: a dict
    >>> char_name = "Edward"
    >>> user_class = "python warrior"
    >>> fake_columns = fake_rows = 10
    >>> generate_character_attributes(char_name, user_class, fake_columns, fake_rows ) # doctest: +NORMALIZE_WHITESPACE
    {'Name': 'Edward', 'Class': 'python warrior', 'EXP': 0, 'Level': 1, 'Location': {'X': 5, 'Y': 5}, 'HP': 100,
    'Max HP': 100, 'Passive': 'pythonic', 'Damage': {'Max Damage': 12, 'Min Damage': 9}, 'Level Name': {'Level1':
    'python soldier', 'Level2': 'python warrior', 'Level3': 'python hero'}, 'Adding Level Up Attr Amount': {'Max HP':
    30, 'Max Damage': 10, 'Min Damage': 10}}
    """
    return dict(Name=name, Class=char_class, EXP=0, Level=1,
                Location={"X": columns // 2, "Y": rows // 2}) | class_attributes(char_class=char_class)


def class_attributes(char_class: str) -> dict:
    """ A function to get correct attributes of the class.

    :param char_class: str
    :precondition: char_class should be a sufficient class name
    :precondition: the function call a function that has a proper dict of the class's attributes
    :return: a dict that contains class' attr

    >>> class_name = "db guardian"
    >>> class_attributes(class_name) # doctest: +NORMALIZE_WHITESPACE
    {'HP': 120, 'Max HP': 120, 'Passive': 'security', 'Damage': {'Max Damage': 10, 'Min Damage': 5}, 'Level Name':
    {'Level1': 'query keeper', 'Level2': 'sql guardian', 'Level3': 'db guardian'}, 'Adding Level Up Attr Amount':
    {'Max HP': 30, 'Max Damage': 7, 'Min Damage': 5}}
    """
    attr_list = {"python warrior": python_warrior_attributes(), "web dev assassin": web_dev_assassin_attributes(),
                 "db guardian": db_guardian_attributes(), "project sorcerer": project_sorcerer_attributes()}
    return attr_list[char_class]


# python warrior has highest stat while there's no any 'passive' skills
def python_warrior_attributes() -> dict:
    """ A function returns dict of python warrior's attributes

    :postcondition: return the attributes of python warrior when the function is invoked
    :return: a dict

    >>> python_warrior_attributes() # doctest: +NORMALIZE_WHITESPACE
    {'HP': 100, 'Max HP': 100, 'Passive': 'pythonic', 'Damage': {'Max Damage': 12, 'Min Damage': 9}, 'Level Name':
    {'Level1': 'python soldier', 'Level2': 'python warrior', 'Level3': 'python hero'}, 'Adding Level Up Attr Amount':
    {'Max HP': 30, 'Max Damage': 10, 'Min Damage': 10}}
    """
    return {"HP": 100, "Max HP": 100, "Passive": "pythonic", "Damage": {"Max Damage": 12, "Min Damage": 9},
            "Level Name": {"Level1": "python soldier", "Level2": "python warrior", "Level3": "python hero"},
            "Adding Level Up Attr Amount": {"Max HP": 30, "Max Damage": 10, "Min Damage": 10}}


def web_dev_assassin_attributes() -> dict:
    """ A function returns dict of web dev assassin's attributes

        :postcondition: return the attributes of web dev assassin when the function is invoked
        :return: a dict

    >>> web_dev_assassin_attributes() # doctest: +NORMALIZE_WHITESPACE
    {'HP': 80, 'Max HP': 80, 'Passive': "employ's legend", 'Damage': {'Max Damage': 15, 'Min Damage': 5}, 'Level Name':
    {'Level1': 'html yegg', 'Level2': 'web dev assassin', 'Level3': 'react master'}, 'Adding Level Up Attr Amount':
    {'Max HP': 15, 'Max Damage': 15, 'Min Damage': 5}}
    """
    return {"HP": 80, "Max HP": 80, "Passive": "employ's legend", "Damage": {"Max Damage": 15, "Min Damage": 5},
            "Level Name": {"Level1": "html yegg", "Level2": "web dev assassin", "Level3": "react master"},
            "Adding Level Up Attr Amount": {"Max HP": 15, "Max Damage": 15, "Min Damage": 5}}


def db_guardian_attributes() -> dict:
    """ A function returns dict of db guardian's attributes

        :postcondition: return the attributes of db guardian when the function is invoked
        :return: a dict
    >>> db_guardian_attributes() # doctest: +NORMALIZE_WHITESPACE
    {'HP': 120, 'Max HP': 120, 'Passive': 'security', 'Damage': {'Max Damage': 10, 'Min Damage': 5}, 'Level Name':
    {'Level1': 'query keeper', 'Level2': 'sql guardian', 'Level3': 'db guardian'}, 'Adding Level Up Attr Amount':
    {'Max HP': 30, 'Max Damage': 7, 'Min Damage': 5}}

    """
    return {"HP": 120, "Max HP": 120, "Passive": "security", "Damage": {"Max Damage": 10, "Min Damage": 5},
            "Level Name": {"Level1": "query keeper", "Level2": "sql guardian", "Level3": "db guardian"},
            "Adding Level Up Attr Amount": {"Max HP": 30, "Max Damage": 7, "Min Damage": 5}}


def project_sorcerer_attributes() -> dict:
    """ A function returns dict of project sorcerer's attributes

    :postcondition: return the attributes of project sorcerer when the function is invoked
    :return: a dict
    >>> project_sorcerer_attributes() # doctest: +NORMALIZE_WHITESPACE
    {'HP': 70, 'Max HP': 70, 'Passive': 'agile', 'Damage': {'Max Damage': 13, 'Min Damage': 5}, 'Level Name':
    {'Level1': 'project apprentice', 'Level2': 'project sorcerer', 'Level3': 'github magician'}, 'Adding Level Up Attr
     Amount': {'Max HP': 10, 'Max Damage': 20, 'Min Damage': 5}}

    """
    return {"HP": 70, "Max HP": 70, "Passive": "agile", "Damage": {"Max Damage": 13, "Min Damage": 5},
            "Level Name": {"Level1": "project apprentice", "Level2": "project sorcerer", "Level3": "github magician"},
            "Adding Level Up Attr Amount": {"Max HP": 10, "Max Damage": 20, "Min Damage": 5}}


def make_board(rows: int, columns: int) -> dict:
    """ A function returns a dict of randomly generated map.

    The columns * rows sized map includes room A, B and C

    :param: row: an integer represents y_coord
    :param: column: an integer represents x_coord
    :precondition: both arguments should be positive integers.
    :postcondition: generates column * row map in a notation of dictionary which is included with randomly
                    generated rooms
    :return: a dict.
    """
    return {(x_cord, y_cord): room_generator() for y_cord in range(rows) for x_cord in range(columns)}


def room_generator() -> str:
    """ A function generate a random room.

    :postcondition: returns a room which is randomly picked from A, B and C
    :return: a str obj
    """
    return ('A', 'B', 'C')[random.randint(0, 2)]


def is_boss(rows: int, columns: int, character: dict) -> bool:
    """ A function checks if the character entered into the boss stage intentionally without becoming level 3

    :param rows: an int obj which represents Y-coord
    :param columns: and int obj which represents X-coord
    :param character: A dict that contains the attribute of the character
    :precondition: rows and columns should be positive integer
    :precondition: "X" in character["Location"] and "Y" in character["Location"] is True
    :postcondition: return True if the character entered the position where the boss is located else False
    :return: a bool

    >>> fake_character_location = {"Location": {"X": 9, "Y": 9}}
    >>> fake_rows = fake_columns = 10
    >>> is_boss(fake_rows, fake_columns, fake_character_location)
    True
    """
    return character["Location"]["X"] == columns - 1 and character["Location"]["Y"] == rows - 1


def describe_location(board: dict, columns: int, rows: int, character: dict):
    """ A function renders UI including the map

    :param board: A dict that includes the informations of the map.
    :param columns: and int obj which represents X-coord
    :param rows: an int obj which represents Y-coord
    :param character: A dict that contains the attribute of the character
    :precondition: board should has the information of the rows * columns sized map
    :precondition: rows and columns should be positive integer
    :precondition: character should contain proper key-value pairs.
    :postndition: it would print the information of the current situation in the game including map.
    :return: nothing

    >>> fake_rows = fake_columns = 3
    >>> fake_character = {"Location": {"X": 1, "Y": 1}, "Max HP": 100, "HP": 75, "Level": 1, "Level Name":\
    {"Level1": "CS student"}, "EXP": 1}
    >>> fake_board = {(0, 0): 'C', (1, 0): 'A', (2, 0): 'A', (0, 1): 'A', (1, 1): \
    'A', (2, 1): 'A', (0, 2): 'C', (1, 2): 'B', (2, 2): 'B'}
    >>> describe_location(fake_board, fake_columns, fake_rows, fake_character)
    '🙂' is your current location. '😈' is boss room. '.' represent empty rooms.
    <BLANKLINE>
     # * *
     * 🙂 *
     # ^ 😈
    HP: 75 Lv1: CS student EXP: 1
    <BLANKLINE>
    """
    board[(columns - 1, rows - 1)] = "Destination"
    board[(character["Location"]["X"], character["Location"]["Y"])] = "Character"
    character_icon = character_icon_generator(character=character)
    print(f"\'{character_icon}\' is your current location. \'\U0001F608\' is boss room. \'.\' represent empty rooms.\n")
    map_renderer(board=board, columns=columns, rows=rows, character_icon=character_icon)
    level = character['Level']
    print(f"HP: {character['HP']} Lv{level}: {character['Level Name'][f'Level{level}']} EXP: {character['EXP']}\n")


def character_icon_generator(character: dict) -> str:
    """ A function generates emoji of the character depends on the ratio of the character's current HP and Max Hp

    :param character: A dict that contains the attribute of the character
    :precondition: "HP" in character and "Max Hp" in charcter is True
    :postcondtion: returns a str obj that has value of emoji depends on the character's current health.
    :return: an emoji unicode string

    >>> fake_character = {"HP": 2, "Max HP": 10}
    >>> print(character_icon_generator(fake_character))
    🤕
    """
    if character["HP"] / character["Max HP"] >= 0.8:
        return "\U0001F601"
    elif character["HP"] / character["Max HP"] >= 0.5:
        return "\U0001F642"
    elif character["HP"] / character["Max HP"] >= 0.25:
        return "\U0001F613"
    else:
        return "\U0001F915"


def map_renderer(board: dict, columns: int, rows: int, character_icon: str):
    """ A function print ascii map UI

    :param board: A dict that includes the information of the map.
    :param columns: and int obj which represents X-coord
    :param rows: an int obj which represents Y-coord
    :param character_icon: an emoji unicode string that represent character's health status
    :precondition: board should have the information of the rows * columns sized map
    :precondition: rows and columns should be positive integer
    :precondition: character should contain proper key-value pairs.
    :postndition: it would print the information of the current situation in the game including map.
    :return: nothing
    """
    for y_cord in range(rows):
        for x_cord in range(columns):
            if board[(x_cord, y_cord)] == "Character":
                print(f' {character_icon}', end='')
            elif board[x_cord, y_cord] == "Destination":
                print(' \U0001F608', end='')
            elif board[x_cord, y_cord] == 'A':
                print(' *', end='')
            elif board[x_cord, y_cord] == 'B':
                print(' ^', end='')
            elif board[x_cord, y_cord] == 'C':
                print(' #', end='')
            elif board[x_cord, y_cord] == 'Empty Room':
                print(' .', end='')
        print('\n', end='')


def get_user_choice():
    """ Ask user to choose the direction

    User can choose to up, down, left, or right.

    :return: tuple contains the magnitudes of each axis.
    """
    direction_dictionary = {"north": (0, -1), "south": (0, 1), "west": (-1, 0), "east": (1, 0)}
    print("Decide where to go... ")
    for direction_num, direction in enumerate(direction_dictionary.keys()):
        print(f"{direction_num + 1}) goes to the {direction}")
    while True:
        try:
            direction_input = int(input("Input the direction. i.e. Up -> North: "))
            # this is to prevent accessing the tuple by zero or negative number.
            if direction_input <= 0:
                raise ValueError
            return direction_dictionary[list(direction_dictionary.keys())[direction_input - 1]]
        except (TypeError, IndexError, ValueError):
            print("Invalid Input(s)\n")


def validate_move(character: dict, direction: tuple, rows: int, columns: int) -> bool:
    """ Checks if character tries to go outside the map or not.

    :param character: A dict that contains the attribute of the character
    :param direction: A tuple that represents direction
    :param columns: and int obj which represents X-coord
    :param rows: an int obj which represents Y-coord
    :precondition: "X" in character["Location"] and "Y" in character["Location"] is True
    :precondition: -1 <= direction[0] < 1 and -1 <= direction[1] < 1
    :precondition: len(direction) == 2
    :precondition: rows and columns should be positive integer
    :postcondtition: checks if it is a valid move.
    :return: True if it is valid move else False

    >>> fake_character = {"Location": {"X": 0, "Y": 0}}
    >>> fake_direction_valid = (0, 1)
    >>> fake_direction_invalid = (-1, 0)
    >>> fake_rows = fake_columns = 2
    >>> validate_move(fake_character, fake_direction_valid, fake_rows, fake_columns)
    True
    >>> validate_move(fake_character, fake_direction_invalid, fake_rows, fake_columns)
    False
    """
    return (0 <= character["Location"]["X"] + direction[0] < columns and
            0 <= character["Location"]["Y"] + direction[1] < rows)


def move_character(board: dict, character: dict, direction: tuple):
    """ A function updates character's location with direction.

    :param board: A dict that includes the information of the map.
    :param character: A dict that contains the attribute of the character
    :param direction: A tuple that represents direction
    :precondition: board should contain key-value pairs given rows * columns map
    :precondition: "X" in character["Location"] and "Y" in character["Location"] is True
    :precondition: isinstance(character["Location"]["X"], int) and isinstance(character["Location"]["Y"], int) is True
    :precondition: -1 <= direction[0] < 1 and -1 <= direction[1] < 1
    :precondition: len(direction) == 2
    :precondition: direction should have valid scalars and magnitudes
    :return: nothing

    >>> fake_board = {(0, 0): "Character", (0, 1): "A", (1, 0): "B", (1, 1): "C"}
    >>> fake_character = {"Location": {"X": 0, "Y": 0}}
    >>> fake_direction = (0, 1)
    >>> move_character(fake_board, fake_character, fake_direction)
    >>> fake_board[(0, 0)]
    'Empty Room'
    >>> fake_character["Location"]["Y"]
    1
    """
    board[(character["Location"]["X"], character["Location"]["Y"])] = 'Empty Room'
    character["Location"]["X"] += direction[0]
    character["Location"]["Y"] += direction[1]


def check_character_attributes(character: dict):
    """ A function checks determines whether character is currently available to get leveled up or not.

    :param character: A dict that contains the attribute of the character
    :precondition: character should have proper key-value pair elements.
    :postcondition: initiates level up process if check_level_up() is True
    :return: nothing
    >>> fake_character = {'Adding Level Up Attr Amount': {'Max Damage': 10, 'Max HP': 30, 'Min Damage': 10}, \
    'Class': 'python warrior', 'Damage': {'Max Damage': 12, 'Min Damage': 9}, 'EXP': 10, 'HP': 100, 'Level': 1, \
    'Level Name': {'Level1': 'python soldier', 'Level2': 'python warrior', 'Level3': 'python hero'},\
    'Location': {'X': 2, 'Y': 2}, 'Max HP': 100, 'Name': 'Edward', 'Passive': 'pythonic'}
    >>> check_character_attributes(fake_character)
    Congrats! You leveled up. And now you are python warrior
    >>> fake_character["Level"]
    2
    """
    if check_level_up(character=character):
        update_char_attr(character=character)
        level = character['Level']
        print(f"Congrats! You leveled up. And now you are {character['Level Name'][f'Level{level}']}")


def check_level_up(character: dict) -> bool:
    """ A function to check if the character's stat is sufficient to get leveled up.

    :param character: A dict contains character's attributes
    :precondition: "EXP" in character and "Level" in character is True
    :precondition: isinstance(character["EXP"], int) and isinstance(character["Level"], int) is True
    :postcondition: checks if it is available to get leveled up
    :return: True if it is available else False

    >>> fake_character = {"EXP": 5, "Level": 2}
    >>> check_level_up(fake_character)
    False
    >>> fake_character["EXP"] = 10
    >>> check_level_up(fake_character)
    True
    """
    return (character["EXP"] >= 10 and character["Level"] == 1) or (character["EXP"] >= 10 and character["Level"] == 2)


def update_char_attr(character: dict):
    """ A function updates character's attr

    :param character: A dict contains character's attributes
    :precondition: character should contain proper key-value pairs that represent character's attr
    :postcondition: updates character's attr based on the amounts of data included in its dict.
    :return: nothing

    >>> fake_character = {'Adding Level Up Attr Amount': {'Max Damage': 10, 'Max HP': 30, 'Min Damage': 10}, \
    'Class': 'python warrior', 'Damage': {'Max Damage': 12, 'Min Damage': 9}, 'EXP': 10, 'HP': 100, 'Level': 1, \
    'Level Name': {'Level1': 'python soldier', 'Level2': 'python warrior', 'Level3': 'python hero'},\
    'Location': {'X': 2, 'Y': 2}, 'Max HP': 100, 'Name': 'Edward', 'Passive': 'pythonic'}
    >>> update_char_attr(fake_character)
    >>> fake_character # doctest: +NORMALIZE_WHITESPACE
    {'Adding Level Up Attr Amount': {'Max Damage': 10, 'Max HP': 30, 'Min Damage': 10}, 'Class': 'python warrior',
    'Damage': {'Max Damage': 22, 'Min Damage': 19}, 'EXP': 0, 'HP': 130, 'Level': 2, 'Level Name': {'Level1':
    'python soldier', 'Level2': 'python warrior', 'Level3': 'python hero'}, 'Location': {'X': 2, 'Y': 2}, 'Max HP':
     130, 'Name': 'Edward', 'Passive': 'pythonic'}
    """
    character["EXP"] = 0
    character["Level"] += 1
    character["Max HP"] += character["Adding Level Up Attr Amount"]["Max HP"]
    character["Damage"]["Max Damage"] += character["Adding Level Up Attr Amount"]["Max Damage"]
    character["Damage"]["Min Damage"] += character["Adding Level Up Attr Amount"]["Min Damage"]
    # character recovers their hp
    character["HP"] = character["Max HP"]


# didn't unitest because there's no function returns anything inside the function
def check_for_monsters(character: dict):
    """ A function to initiate to fight with norm monsters in 20% of chance

    :param character: A dict contains character's attributes
    :precondition: character should contain proper key-value pairs that represent character's attr
    :return: nothing
    """
    if random.randint(1, 5) == 1:
        fight_with_norm_monster(character=character)


# didn't unitest because there's no function returns anything inside the function
def fight_with_norm_monster(character: dict):
    """ A function processes fighting with normal monsters

    :param character: A dict contains character's attributes
    :precondition: character should contain proper key-value pairs that represent character's attr
    :return: nothing
    """
    monster = copy.deepcopy(norm_monster_generator(character=character))
    print(f"You faced {monster['Name']} monster.")
    win = fight(character=character, monster=monster)
    if win:
        print(f"{character['Name']} defeated {monster['Name']}!")
        gain_exp(character=character, monster=monster)


def gain_exp(character: dict, monster: dict):
    """ A function that gives character exp

    If the character's passive is 'agile', the character would get twice amount of exp

    :param character: A dict contains character's attributes
    :param monster: A dict contains monster's attributes
    :precondition: character should contain proper key-value pairs that represent character's attr
    :precondition: "EXP" in character and "Name" in character "Passive" in character is True
    :precondition: monster should contain proper key-value pairs that represent monster's attr
    :precondition: "EXP" in monster and "Name" in monster is True
    :postcondition: add monster's EXP to character's EXP if the character's passive is "agile" the amout would be twice
    :return: nothing

    >>> fake_chracter = {"Name": "Chris", "EXP": 1, "Passive": "agile"}
    >>> fake_monster = {"Name": "Edward", "EXP": 3}
    >>> gain_exp(fake_chracter, fake_monster)
    Chris got 6 exp defeating Edward
    >>> fake_chracter
    {'Name': 'Chris', 'EXP': 7, 'Passive': 'agile'}
    """
    exp = monster["EXP"] * 2 if character['Passive'] == "agile" else monster["EXP"]
    print(f"{character['Name']} got {exp} exp defeating {monster['Name']}")
    character["EXP"] += exp


def fight(character: dict, monster: dict) -> bool:
    """A function charges the whole fight process with monsters even boss.

    Player's turn to attack will be first, then monster's, and it keeps rotating until:
    1) the player kill monster
    2) character alive
    3) the monster doesn't flee away.

    :param character: A dict contains character's attributes
    :param monster: A dict contains monster's attributes
    :precondition: character should contain proper key-value pairs that represent character's attr
    :precondition: monster should contain proper key-value pairs that represent monster's attr
    :postcondition: it would keep rotating player's turn and monster's turn until the fight ends.
    :return: True if the fight was True for all 3 conditions above else False
    """
    player_turn, turn_bools, monster_flee = True, itertools.cycle([False, True]), False
    while monster["HP"] > 0 and is_alive(hp=character["HP"]) and not monster_flee:
        print(f"{character['Name']}: {character['HP']}, {monster['Name']}: {monster['HP']}")
        if player_turn:
            if get_command(boss_mode=monster["Is Boss"]) == "2":
                print(f"Whoo! Let's run away from {monster['Name']}!")
                break
            attack(attacker=character, victim=monster)
        elif not player_turn:
            attack(attacker=monster, victim=character)
        monster_flee, player_turn = True if is_flee(boss_mode=monster["Is Boss"]) else False, next(turn_bools)
        if monster_flee:
            print(f"{monster['Name']} has fled away!")
    return is_alive(hp=character["HP"]) and monster["HP"] <= 0 and not monster_flee


def get_command(boss_mode: bool) -> str:
    """ A function to get a command from user during fight

    "1" is accepting to fight and "2" is trying to flee else invalid, the function will ask until it gets a valid input.

    :param boss_mode: a bool that represents whether this fight is boss fight or not.
    :precondition: boss_mode should be True if it is in boss session else False.
    :postcondition: the function will require user to input the command, user can only fight in boss mode. And it would
                    keep asking user until they get valid input.
    :return: A str obj that refers fight or flee.
    """
    flee = ' or you can flee from monster by \"2\"'
    print('It\'s your turn! You can fight with the monster by typing "1"'
          f'{flee if not boss_mode else ""}:')
    while True:
        command = input("Input your command:").lower()
        if command == "1" or (command == "2" and not boss_mode):
            return command
        elif command == "2" and boss_mode:
            print("You cannot flee from the boss stage.")
        else:
            print("Invalid command! Do it again")


def attack(attacker: dict, victim: dict):
    """ A function processes attack.

    attacker will reduce victim's HP with its attack damage, possibly critical. And victim will possibly get a holf
    damage if its passive is 'security'

    :param attacker: a dict that represents attacker's attr
    :param victim: a dict that represents victim's attr
    :precondition: attacker and victim should have proper key-value pairs that represent its attr
    :postcondition: first it calls critical_counter() to determine the amount of damage. Then it checks if it is
                    available reduce the damage for the victim and reduce victim's hp by the damage
    :return: nothing
    """
    damage = critical_counter(attacker=attacker)
    if attacker["Damage"]["Max Damage"] == damage:
        print(f"{attacker['Name']} did critical {damage} damage to {victim['Name']}")
    else:
        print(f"{attacker['Name']} did {damage} damage to {victim['Name']}")
    if damage_dodger(victim=victim):
        damage //= 2
        print(f"{victim['Name']} dodged its damage to {damage} using \"{victim['Passive']}\"")
    victim["HP"] -= damage


def critical_counter(attacker: dict) -> int:
    """ A function determines a normal or critical damage in random

    The chance is 25% by default. If attacker has a passive 'employ's legend', the critical chance increases to 50%

    :param attacker: a dict that represents attacker's attr
    :precondition: attacker should have proper key-value pairs that represent its attr
    :postcondition: the function determines an attacker's damage. It can be critical damage in 25% chance, if it has
                    'employ's legend' passive, it would be 50%
    :return: an int obj that represents attacker's damage
    """
    adjust_num = 1 if attacker["Passive"] == "employ's legend" else 3
    random_num = random.randint(0, adjust_num)
    if random_num == 1 and attacker["Passive"] == "employ's legend":
        print(f"{attacker['Name']} used \"{attacker['Passive']}\"!")
    return attacker["Damage"]["Max Damage"] if random_num == adjust_num else attacker["Damage"]["Min Damage"]


def damage_dodger(victim: dict) -> bool:
    """ A function to check if the character is available to reduce the damage.

    If the victim has a passive "security", it will reduce the damage in 33% of chance.

    :param victim: a dict that represents victim's attr
    :precondition: "Passive" in victim is True
    :postcondition: check if the victim's passive is "security" and it is in 33% of chance
    :return:True if the postcondition is True else False
    """
    return True if victim["Passive"] == "security" and random.randint(0, 2) == 0 else False


def is_flee(boss_mode: bool) -> bool:
    """ A function returns if monster is available to flee away in 20% of chance not in boss mode

    :param boss_mode: a bool that represents if it is in boss mode or not
    :precondition: boss_mode should be False if it is invoked through fight_with_norm_monster()
    :postcondition: check if it is not boss mode and is in 20% of chance
    :return: True if postcondition is True else False
    """
    return not boss_mode and random.randint(0, 4) == 0


def norm_monster_generator(character: dict) -> dict:
    """ A function returns randomly generated normal monster based on character's level

    :param character: A dict contains character's attributes
    :precondition: "Level" in character is True
    :postcondition: generates a dict obj of randomly selected normal monster based on character's
                    level
    :return: A dict of a generated character
    """
    monsters = \
        {"Level1": ({"Name": "Algorithm", "Passive": None, "Is Boss": False, "HP": 20, "EXP": 4,
                     "Damage": {"Max Damage": 4, "Min Damage": 3}},
                    {"Name": "DataStructure", "Passive": None, "Is Boss": False, "HP": 15, "EXP": 4,
                     "Damage": {"Max Damage": 7, "Min Damage": 2}},
                    {"Name": "DB", "Passive": None, "Is Boss": False, "HP": 15, "EXP": 4,
                     "Damage": {"Max Damage": 30, "Min Damage": 1}}),
         "Level2": ({"Name": "OOP", "Is Boss": False, "Passive": None, "HP": 30, "EXP": 4,
                     "Damage": {"Max Damage": 7, "Min Damage": 5}},
                    {"Name": "SoftwareEngineering", "Is Boss": False, "Passive": None, "HP": 20, "EXP": 4,
                     "Damage": {"Max Damage": 10, "Min Damage": 3}},
                    {"Name": "AI/ML", "Is Boss": False, "Passive": None, "HP": 15, "EXP": 4,
                     "Damage": {"Max Damage": 60, "Min Damage": 2}})}
    return monsters[f"Level{character['Level']}"][random.randint(0, len(monsters[f"Level{character['Level']}"]) - 1)]


def fight_with_boss(character: dict) -> bool:
    """ A function processes fighting with boss monster

    fight with boss will generate a dict of the boss monster first, prints the scripts and initiates fighting with boss
    monster

    :param character: A dict contains character's attributes
    :precondition: character should contain proper key-value pairs that represent character's attr
    :postcondition: processes fighting with boss monster
    :return: True if character defeated the boss else False
    """
    boss = boss_monster_generator(character=character)
    level = character['Level']
    print("***********************************************************************************************************"
          "\n"
          f" Finally You, {character['Level Name'][f'Level{level}']} faced {boss['Name']}. You need to have an endless"
          f" fight with that dragon!\n"
          "***********************************************************************************************************"
          )
    return fight(character=character, monster=boss)


def boss_monster_generator(character: dict):
    """ A function returns a dict of boss monster's attributes.

    The boss monster's passive skill will be copied from the character's passive

    :param character: A dict contains character's attributes
    :precondition: "Passive" in character is True
    :postcondition: generates boss monster's attr
    :return: a dict that contains the boss' attr

    >>> fake_character = {"Passive" : "employ's legend"}
    >>> boss_monster_generator(fake_character) # doctest: +NORMALIZE_WHITESPACE
    {'Name': 'The Exam Dragon', 'Is Boss': True, 'Passive': "employ's legend", 'HP': 100, 'EXP': 0, 'Damage':
    {'Max Damage': 20, 'Min Damage': 10}}
    """
    return {"Name": "The Exam Dragon", "Is Boss": True, "Passive": character['Passive'], "HP": 100, "EXP": 0,
            "Damage": {
                "Max Damage": 20, "Min Damage": 10}}


def main():
    import doctest
    doctest.testmod(verbose=True)
    game()


if __name__ == "__main__":
    main()
