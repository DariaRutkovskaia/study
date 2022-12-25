import random

from art import logo, vs
from game_data import data

score = 0
print(logo)


def comparing(count_a, count_b):
    if count_a > count_b:
        return "a"
    else:
        return "b"


def game(compare_a, compare_b):
    global score
    while compare_a == compare_b:
        compare_b = random.choice(data)
    print(f"Compare A: {compare_a['name']}, {compare_a['description']} from {compare_a['country']} ")
    followers_a = compare_a['follower_count']
    print(vs)
    print(f"Compare B: {compare_b['name']}, {compare_b['description']} from {compare_b['country']} ")
    followers_b = compare_b['follower_count']

    answer = comparing(followers_a, followers_b)
    guess = input('a or b???\n').lower()

    if answer == guess:
        score += 1
        print(f"You're right!! current score: {score}")
        print("\n" * 2)
        game(compare_b, random.choice(data))
    else:
        print(f"You lose. Final score: {score}")


game(random.choice(data), random.choice(data))
