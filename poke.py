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
    name = input('Enter username')
    n = 1
    play = 'y'
    score = 0
    
    while play == 'y':
        print('Round: ', n)
        my_pokemon1 = random_pokemon()
        my_pokemon2 = random_pokemon()
        my_pokemon3 = random_pokemon()

        while True:
            print(
                f'In your deck, there are: \n{my_pokemon1["name"]}, Id: {my_pokemon1["id"]}, Height: {my_pokemon1["height"]}, weight: {my_pokemon1["weight"]},\n {my_pokemon2["name"]}, Id:  {my_pokemon2["id"]}, Height: {my_pokemon2["height"]}, Weight: {my_pokemon2["weight"]},\n lastly, you have {my_pokemon3["name"]}, Id: {my_pokemon3["id"]}, Height: {my_pokemon3["height"]}, Weight: {my_pokemon3["weight"]}.\n Which pokemon would you like? (1,2 or 3?)')
            my_choice = input()

            if my_choice == '1':
                my_pokemon = my_pokemon1
                break
            elif my_choice == '2':
                my_pokemon = my_pokemon2
                break
            elif my_choice == '3':
                my_pokemon = my_pokemon3
                break
            else:
                print('Error, check your inputs')
                continue

        print('You chose {}'.format(my_pokemon['name']))

        while True:
            stat_choice = input('Which stat do you want to use? (id, height, weight) ')
            if stat_choice == 'id' or stat_choice == 'height' or stat_choice == 'weight':
                break
            else:
                print('Error, check your inputs')
                continue

        opponent_pokemon = random_pokemon()
        print('The opponent chose {}'.format(opponent_pokemon['name']))

        my_stat = my_pokemon[stat_choice]
        opponent_stat = opponent_pokemon[stat_choice]

        if my_stat > opponent_stat:
            print(f'You Win! Your number was {my_stat}, your opponent number was {opponent_stat}')
            n = n + 1
            score = score + 1
                
        elif my_stat < opponent_stat:
            print(f'You Lose! Your number was {my_stat}, your opponent number was {opponent_stat}')
            n = n + 1
            score = 0
                
        elif ValueError:
            print('Error, check your inputs')
            continue

        else:
            print(f'Draw! Your number was {my_stat}, your opponent number was {opponent_stat}')
            n = n + 1
                
        while True:
            print('Your win streak is: ', score)
            print('Do you want to play again? y/n')
            play = input()
            if play == 'n':
                print('Okay, goodbye {} :)'.format(name))
                print('Final win streak: ', score)
                break
            elif play == 'y':
                print('Okay, another round!')
                break
            else:
                print('Error, check you inputs')
                continue
                
    with open('scores.txt', 'r') as text_file:
        scores = text_file.read()
    scores = scores + str(score) + '\n'
    with open('scores.txt', 'w+') as text_file:
        text_file.write(scores)


run()
