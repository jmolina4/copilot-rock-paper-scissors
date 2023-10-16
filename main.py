'''
Image you are a python expert with knowledge of pytest and TDD

I want to test my rock, paper, scissors game. Here is how the game works:
- When the python script gets executed you would need to choose between rock, paper, scissors, lizard and spock. The output would look like: "Plase choose, rook, paper, scissors, lizard or spock: <input>"
- Then the computer will chose as well. The output would look like: "The computer chose: <random_value>"
- Then we will show what the user chose in the following format: "The user chose: <input>"
- Finally we will show the winner in the following format: "The winner is: <winner>"

The logic goes as follows:
- Rock wins against scissors and lizard
- Scissors wins against paper and lizard
- Paper wins against rock and spock
- Lizard wins against paper and spock

An example of the execution would be:
python main.py
Plase choose, rook, paper or scissors: rock
The computer chose: paper
The user chose: rock
The winner is: computer

main.py will contain a class called Game with the following methods:
- play(self, user_input): This method will receive the user input and will return the winner

Imagine that now I want to create an API on top of this logic. The endpoints allowed would be the following ones:
- POST /rock: This endpoint will return the winner of the game when the user chooses rock
- POST /paper: This endpoint will return the winner of the game when the user chooses paper
- POST /scissors: This endpoint will return the winner of the game when the user chooses scissors

An example of the execution would be:
curl -X POST http://localhost:5000/rock
The winner is: computer

I want to use fastapi to create this API. I want to use pytest to test the API using TDD.
'''

import random
from typing import Optional

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post('/{user1_input}')
def post_endpoint(user1_input: str):
    game = Game()
    try:
        return game.play(user1_input)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

class Game:
    def __init__(self):
        self.winning_combinations = [('rock', 'scissors'), ('rock', 'lizard'), ('paper', 'rock'), ('paper', 'spock'), ('scissors', 'paper'), ('scissors', 'lizard')]
        self.options = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.second_player_name = 'computer'
    
    def play(self, user1_input: str) -> str:
        self._validate_options(user1_input)

        computer = random.choice(self.options)
        
        if user1_input == computer:
            return 'The winner is: tie'
    
        if (user1_input, computer) in self.winning_combinations:
            return f'The winner is: user'
        else:
            return f'The winner is: {self.second_player_name}'

    def _validate_options(self, user1_input: str) -> None:
        if user1_input not in self.options:
            raise ValueError(f'Invalid option: {user1_input}')
       