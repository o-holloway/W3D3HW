import requests

class PokeInfo:
    def __init__(self,name,height,weight,cry):
        self.name = name.title()
        self.height = round((height / 0.254), 2) #decimeters to inches
        self.weight = round((weight / 4.5359237), 2) #hectograms to pounds
        self.cry = cry

    def __str__(self):
        return f"Name: {self.name}\nHeight: {self.height} in.\nWeight: {self.weight} lbs."
    
    
class PokeAPI:
    base_url = 'https://pokeapi.co/api/v2'

    def __init__(self):
        pass

    def __get(self,poke_name):
        request_url = f"{self.base_url}/pokemon/{poke_name.lower()}"
        response = requests.get(request_url)
        if response.ok:
            data = response.json()
            return data
        else:
            return None

    def get_poke_info(self,pokemon):
        poke_data = self.__get(pokemon)
        if poke_data:
            poke_name = poke_data['name']
            height = poke_data['height']
            weight = poke_data['weight']
            cry = poke_data['cries']['latest']
            poke_obj = PokeInfo(poke_name, height, weight, cry)
            return poke_obj
        else:
            print('No data for the pokemon:', pokemon)