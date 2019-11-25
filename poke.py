import random
import requests

def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = "https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }
def run():
    #
    my_pokemon1 = random_pokemon()
    my_pokemon2 = random_pokemon()
    my_pokemon3 = random_pokemon()

    while True:
        while True:
            print('You have {}, {} and {} in your deck which pokemon would you like? (1,2 or 3?)'.format(my_pokemon1['name'], my_pokemon2['name'], my_pokemon3['name']))
            my_choice = input()

            if my_choice =='1':
                my_pokemon = my_pokemon1
                break
            elif my_choice =='2':
                my_pokemon = my_pokemon2
                break
            elif my_choice =='3':
                my_pokemon = my_pokemon3
                break
            else:
                print('Error, check your inputs')
                continue



        print('You chose {}'.format(my_pokemon['name']))
    #
        stat_choice = input('Which stat do you want to use? (id, height, weight) ')

        opponent_pokemon = random_pokemon()
        print('The opponent chose {}'.format(opponent_pokemon['name']))

        my_stat = my_pokemon[stat_choice]
        opponent_stat = opponent_pokemon[stat_choice]

        if my_stat > opponent_stat:
            print('You Win!')
        elif my_stat < opponent_stat:
            print('You Lose!')
        elif ValueError:
            print('Error, check your inputs')
            continue
        else:
            print('Draw!')

        break

run()
