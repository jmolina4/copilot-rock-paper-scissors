from main import Game
from main import app
from fastapi.testclient import TestClient

from unittest import mock
import pytest

'''
This test will check that rock wins against scissors and looses against paper. I'd need to mock the random value to be able to test it.
'''


def test_rock_wins_against_scissors_and_lizard_and_looses_against_paper_and_spock():
    game = Game()
    
    with mock.patch('random.choice', return_value='scissors'):
        result1 = game.play(user1_input='rock')
        assert(result1 == 'The winner is: user')

    with mock.patch('random.choice', return_value='paper'):
        result2 = game.play(user1_input='rock')
        assert(result2 == 'The winner is: computer')
        
    with mock.patch('random.choice', return_value='lizard'):
        result1 = game.play(user1_input='rock')
        assert(result1 == 'The winner is: user')

    with mock.patch('random.choice', return_value='spock'):
        result2 = game.play(user1_input='rock')
        assert(result2 == 'The winner is: computer')

def test_paper_wins_against_rock_and_looses_against_scissors():
    game = Game()
    
    with mock.patch('random.choice', return_value='rock'):
        result1 = game.play(user1_input='paper')
        assert(result1 == 'The winner is: user')
    
    with mock.patch('random.choice', return_value='scissors'):
        result2 = game.play(user1_input='paper')
        assert(result2 == 'The winner is: computer')
    
def test_scissors_wins_against_paper_and_looses_against_rock():
    game = Game()
    
    with mock.patch('random.choice', return_value='paper'):
        result1 = game.play(user1_input='scissors')
        assert(result1 == 'The winner is: user')
        
    with mock.patch('random.choice', return_value='rock'):
        result2 = game.play(user1_input='scissors')
        assert(result2 == 'The winner is: computer')
    
def test_same_value_results_in_tie():
    game = Game()
    
    with mock.patch('random.choice', return_value='scissors'):
        result1 = game.play(user1_input='scissors')
        assert(result1 == 'The winner is: tie')
        
    with mock.patch('random.choice', return_value='rock'):
        result2 = game.play(user1_input='rock')
        assert(result2 == 'The winner is: tie')
        
    with mock.patch('random.choice', return_value='paper'):
        result3 = game.play(user1_input='paper')
        assert(result3 == 'The winner is: tie')
    
def test_invalid_user1_input_raises_exception():
    game = Game()
    try:
        game.play(user1_input='invalid')
    except ValueError as e:
        assert(str(e) == 'Invalid option: invalid')
    else:
        assert(False)
    
def test_post_rock_endpoint():
    client = TestClient(app)    
    with mock.patch('random.choice', return_value='paper'):
        response = client.post("/rock")
    assert response.status_code == 200
    assert response.json() == 'The winner is: computer'
    
def test_post_paper_endpoint():
    client = TestClient(app)    
    with mock.patch('random.choice', return_value='scissors'):
        response = client.post("/paper")
    assert response.status_code == 200
    assert response.json() == 'The winner is: computer'
    
def test_post_scissors_endpoint():
    client = TestClient(app)    
    with mock.patch('random.choice', return_value='rock'):
        response = client.post("/scissors")
    assert response.status_code == 200
    assert response.json() == 'The winner is: computer'

def test_invalid_option_endpoint():
    client = TestClient(app)    
    response = client.post("/invalid")
    print(response.json())
    assert response.status_code == 404
    