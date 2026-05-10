from trainer import mode_time, mode_words
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
