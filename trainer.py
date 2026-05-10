import time
from words import get_words
import random
from rich.console import Console
from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel
import sys

if sys.platform == 'win32':
    import msvcrt

    def getch():
        return msvcrt.getwch()
else:
    import tty
    import termios

    def getch():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
console = Console()


def type_session(words, time_limit=None):
    current_word_index = 0
    current_input = ""
    start_time = 0
    correct_words_count = 0
    total_attempts = 0
    session_start = 0
    total_time = 0
    result = []
    layout = Layout()
    layout.split_column(
        Layout(Panel(""), name="input", size=3),
        Layout(Panel(""), name="prompt"))
    with Live(layout, screen=True, auto_refresh=False) as live:
        render(words, current_word_index, current_input, result, layout)
        live.refresh()
        while True:
            if time_limit and session_start and time.time() - session_start > time_limit:
                break
            key = getch()
            if key == "|":
                break
            if key == '\b':
                if current_input:
                    current_input = current_input[:-1]
            elif key == ' ':
                total_attempts += 1
                if current_input == words[current_word_index]:
                    result.append(True)
                    correct_words_count += 1
                else:
                    result.append(False)
                current_word_index += 1
                current_input = ""
                if current_word_index == len(words):
                    break
            elif key == '\r':
                continue
            else:
                if not current_input and current_word_index == 0:
                    session_start = time.time()
                    start_time = time.time()
                current_input += key

            render(words, current_word_index, current_input, result, layout)
            live.refresh()
    return correct_words_count, total_attempts, time.time() - start_time


def render(words, current_word_index, current_input, result, layout):
    line = ""
    for index, word in enumerate(words):
        if index < len(result):
            if result[index] == True:
                line += f"[bold green]{word}[/bold green] "
            else:
                line += f"[bright_red]{word}[/bright_red] "
        elif index == current_word_index:
            line += f"[bold yellow]{word}[/bold yellow] "
        else:
            line += f"[grey34]{word}[/grey34] "

    layout["input"].update(Panel(current_input))
    layout["prompt"].update(Panel(line))


def equalty_test(lists_word, users_word):
    return users_word == lists_word


def mode_time(words_difficulty, time_limit):
    words = get_words(words_difficulty, 100)
    correct_words_count, total_attempts, total_time = type_session(
        words, time_limit)
    console.clear()
    print()
    print("Time's up!")
    WPM = (correct_words_count / time_limit) * 60
    print(f"Word in minute:  {round(WPM, 2)}")
    accuracy = (correct_words_count / total_attempts) * 100
    print(f"Accuracy is {round(accuracy, 1)}%")

# режим на кількість слів


def mode_words(words_difficulty, count):
    words = get_words(words_difficulty, count)
    correct_words_count, total_attempts, total_time = type_session(words)
    console.clear()
    print()
    print(f"Words typped correctly {correct_words_count}")
    WPM = (correct_words_count/total_time) * 60
    print(f"Word in minute:  {round(WPM, 2)}")
    accuracy = (correct_words_count / total_attempts) * 100
    print(f"Accuracy is {round(accuracy, 1)}%")


print("Please choose difficulty: 1 = Easy, 2 = Medium, 3 = Hard")
words_difficulty_ask = input('')
if words_difficulty_ask == '1':
    words_difficulty = "Easy"
elif words_difficulty_ask == '2':
    words_difficulty = "Medium"
elif words_difficulty_ask == '3':
    words_difficulty = "Hard"
else:
    words_difficulty = "Easy"
# Mode choosing
print("Chose time for a chalange: 1 = 30 sec, 2 = 60 sec, 3 = word count mode")
time_limit_ask = input('')
if time_limit_ask == '2':
    time_limit = 60
    mode_time(words_difficulty, time_limit)
elif time_limit_ask == '1':
    time_limit = 30
    mode_time(words_difficulty, time_limit)
elif time_limit_ask == '3':
    print("Please choose an ammount of words in test: 1 = 25, 2 = 50")
    words_ammount_ask = input("")
    if words_ammount_ask == '1':
        count = 25
        mode_words(words_difficulty, count)
    elif words_ammount_ask == '2':
        count = 50
        mode_words(words_difficulty, count)
    else:
        print("Something goes wrong. Please try again")
        words_ammount_ask

else:
    print("Something gone wrong")
    exit()
