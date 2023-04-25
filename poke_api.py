import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    pokemon = search_pokemon_entries('squirtle')
    #pass

def search_pokemon_entries(poke_entry):
    """Searches the PokeAPI for information on a Pokemon

    Args:
        poke_entry (str): The name or PokeDex number of a Pokemon

    Returns:
        dict: A dictionary with information on the Pokemon
    """
    # Clean the search term
    poke_entry = str(poke_entry).strip().lower()

    # Send a GET request for a pokemon that matches the name or ID
    print(f'Getting information for {poke_entry}...', end='')
    resp_msg = requests.get(POKE_API_URL + poke_entry)

    # Check whether the request was successful
    if resp_msg.ok:
        print('success')
        return resp_msg.json()
    else:
        print("failure")
        print(f"Response code: {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")

if __name__ == "__main__":
    main()