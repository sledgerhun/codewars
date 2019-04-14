"""
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. 
Each of them has a single 100, 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly 
in the order people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that moment. 
Otherwise return NO.
"""

def tickets(people):
    banknotes = {100: 0, 50: 0, 25: 0}

    for paid in people:
        banknotes[paid] += 1
        change = paid - 25

        for banknote in (50, 25):
            while banknote <= change and banknotes[banknote] > 0:
                banknotes[banknote] -= 1
                change -= banknote

    if change != 0:
        return 'NO'

    return 'YES'
