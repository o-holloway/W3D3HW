import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
from wrappers import PokeAPI
import urllib.request 

client = PokeAPI()

poke_name = input('Enter a Pokemon name: ').title()

poke_info = client.get_poke_info(poke_name)

if poke_info != None:
    print(poke_info)
    if input(f"Listen to {poke_name}'s default sound (Y/N)? ").lower() == "y":
        urllib.request.urlretrieve(poke_info.cry, 'temp.ogg')
        mixer.init()
        mixer.music.load('temp.ogg')
        mixer.music.set_volume(0.2)
        mixer.music.play()
else:
    print("No information found")
