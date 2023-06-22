
#TODO:
# 1.Ask for user input -> ex : ditto
# 2.Create a dynamic URL based on step 1
# 3.Fetch the data from the url in step 2
# 4.Convert JSON to a dictionary
# 5.Print out pokemon data 
import requests

while True:
    Pokemon = input("Which pokemon do you want to find? ")
    Pokemon = Pokemon.lower()

    if Pokemon == 'quit':
        print("You choose to quit, I see you next time ")
        break

    url = f"https://pokeapi.co/api/v2/pokemon/{Pokemon}"

    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        print(f"Name is\t\t{data['name']}")
        print(f"The height is\t{data['height']}")

        print("\n")

        print("The moves are: ")
        for move in data['moves']:
            print(move['move']['name'])

        print("\n")

        print("The abilities are: ")
        for ability in data['abilities']:
            print(ability['ability']['name'])

    else:
        print("Pokemon not found")







