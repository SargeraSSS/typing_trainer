import json
import random
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)


def load_words():
    # Open the words file and load it as a Python dictionary
    with open(os.path.join(BASE_DIR, 'words.json'), 'r', encoding='utf-8') as f:
        words_json = json.load(f)
        words_list = words_json['words']
    return words_list


def calculate_difficulty(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    score = 0
    same_letters_count = {}

    # Criterion 1: word length
    if len(word) <= 6:
        score += 0
    elif len(word) <= 11:
        score += 2
    else:
        score += 3

    # Criterion 2: consonant ratio depends on word length
    consonants_count = sum(
        1 for char in word if char not in vowels and char.isalpha())
    consonant_ratio = (consonants_count / len(word)) * 100

    if len(word) <= 6 and consonant_ratio > 75:
        score += 0
    elif len(word) <= 11 and consonant_ratio > 65:
        score += 2
    elif len(word) > 11 and consonant_ratio > 60:
        score += 4

    # Criterion 3: repeated letters
    for letter in word:
        same_letters_count[letter] = same_letters_count.get(letter, 0) + 1
    if max(same_letters_count.values()) >= 2:
        score += 1

    return score


def get_difficulty(score):
    difficulty = ''
    if score <= 0:
        difficulty = "Easy"
    elif score <= 3:
        difficulty = "Medium"
    else:
        difficulty = "Hard"
    return difficulty


def get_words(difficulty, count):
    words_list = [word for word in load_words() if difficulty ==
                  get_difficulty(calculate_difficulty(word))]
    random_words = random.sample(words_list, min(count, len(words_list)))
    return random_words
