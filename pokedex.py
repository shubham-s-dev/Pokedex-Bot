import requests

pokemon_name = input("enter your pokemon:")
search_name = pokemon_name.lower().strip() 
display_name = pokemon_name.title()
poke_url = f"https://pokeapi.co/api/v2/pokemon/{search_name}"
tele_key ="YOUR_KEY_HERE"
chat_id = "YOUR_ID_HERE"
tele_photo_url = f"https://api.telegram.org/bot{tele_key}/sendPhoto"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    print(f"Searching for {display_name}...")
    response = requests.get(poke_url, timeout= 10)
    if response.status_code ==  200:

        request = response.json()
        data = request
    
        weight = data['weight']
        image_link = data['sprites']['front_default']
        pokemon_type = data['types'][0]['type']['name']


        print(f"Found! Type: {pokemon_type}, Weight: {weight}")
        
        image_response = requests.get(image_link) 
        with open("pokemon.png", "wb") as file:
            file.write(image_response.content)

        print("IMAGE SAVED")

        with open("pokemon.png","rb") as f:
            file = {"photo" : f}

            caption_text = f"🦁 POKEDEX RESULT 🦁\n\nName: {display_name}\nType: {pokemon_type}\nWeight: {weight}"
            
            tele_params = {
                "chat_id": chat_id, 
                "caption": caption_text
            }
            
            final_res = requests.post(tele_photo_url, data=tele_params, files=file)
            print("Sent to Telegram! ")

    elif response.status_code == 404:
        print(f" '{display_name}' not found. Spelling check karein.")

    elif response.status_code == 401 :
        print("INVALID KEY")

except Exception as e :
    print(f"ERROR : {e}")




