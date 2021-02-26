import random
import requests

def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }

def run():
    my_pokemon = input('Which Pokemon ID do you choose?(choose between 1 and 151): ')
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(my_pokemon)
    response = requests.get(url)
    pokemon = response.json()
    print('You chose {}'.format(pokemon['name']))

    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon['name']))

    stat_choice = input('Which stat do you want to use?(id,height or weight): ')
    my_stat = pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    score = 0
    if my_stat > opponent_stat:
        print('You win!')
        my_score = score + 1
        opponent_score = score
    elif my_stat < opponent_stat:
        print('You lose!')
        opponent_score = score + 1
        my_score = score
    else:
        print('Its a draw!')
        my_score = score
        opponent_score = score
    print('{} point/(s) have been added to your final score'.format(my_score))
    print('Your opponent has had {} point/(s) added to their final score'.format(opponent_score))

games = int(input('How many rounds do you want to play?'))
for game in range(games):
     run()