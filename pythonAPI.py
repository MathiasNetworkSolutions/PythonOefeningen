import requests

# api_url = "https://jsonplaceholder.typicode.com/todos/1"
# response= requests.get(api_url)
# response.json()
# print(response.json())

# # get verzoek doen op een url (requests.get() )
# # dan gaan we json gebruiken om dat bestand als een josn te openen

# print(response.status_code)
# print(response.headers["Content-Type"])

# # idem hier, hier gaan we de status code en de headers opvragen


# #oef 1
# #Data uit api halen
# api_url = "https://jsonplaceholder.typicode.com/todos/1"
# response = requests.get(api_url)
# # JSON-response omzetten naar een Python-woordenboek
# data = response.json()

# # Titel ophalen uit het woordenboek
# title = data.get("title")  

# print("Titel:", title)

# #checken if bool = true: 
# # langere versie:
# # if data.get('completed')==true:
# if data['completed']:
#     print("Good job buddy")
# else:
#     print("back to work my man, job not done :(")


# # oef 2
# # covid 19 statistics
# api_url="https://disease.sh/v3/covid-19/countries/"
# response = requests.get(api_url)
# data = response.json()
# countryUser = str(input("Geef een land in: "))  # Specifiek land
# api_urlUser = f"https://disease.sh/v3/covid-19/countries/{countryUser}"
# response = requests.get(api_urlUser)

# data = response.json()
# total_cases = data.get("cases")
# total_deaths = data["deaths"]
# total_recovered = data.get("recovered")
# print(f"Statistieken voor {countryUser}:")
# print(f"Totaal aantal gevallen: {total_cases}")
# print(f"Totaal aantal sterfgevallen: {total_deaths}")
# print(f"Aantal herstelde patiënten: {total_recovered}")

# #oef3
# #joke time
# api_url= "https://v2.jokeapi.dev/joke/Any"
# # response = requests.get(api_url)
# userinput=int(input("Hoeveel jokes wil je? "))
# count=0
# # Controleren of het verzoek succesvol is
# while userinput > count:
#     response = requests.get(api_url)
#     if response.status_code == 200:
#         joke_data = response.json()
#         # Controleren of het een single-part of two-part joke is
#         if joke_data.get("type") == "single":
#             # Single-part grap
#             print(joke_data.get("joke"))
#         elif joke_data.get("type") == "twopart":
#             # Two-part grap
#             print(joke_data.get("setup"))
#             print(joke_data.get("delivery"))
#         print("\n")
#     else:
#         print(f"Fout bij het ophalen van een grap: {response.status_code}")
#     count += 1


# #oef4
# #hardware things of my pc
# # zien voor locale api server, niet nodig om info op te vragen
api_url = "http://localhost:8085/data.json"
response= requests.get(api_url)
data=response.json()
# print(response.json())
GPUnaam=data["Children"][0]["Children"][3]["Text"]
print(GPUnaam)


# # oef 4
# city=str(input("Geef een stad in: "))
# api_key= "2bea31ca7b49afb2e8f3436037acc3a6"
# api_url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
# response= requests.get(api_url)
# # data=response.json()
# # print(data)
# # print van de url zodat ik deze jusit in mijn browser kan plakken om te kijken hoe de syntax eruit ziet
# # print(api_url)

# # Controleren of het verzoek succesvol is
# if response.status_code == 200:
#     # JSON-data omzetten naar een Python-woordenboek
#     data = response.json()
    
#     # Gevraagde gegevens ophalen
#     # wel moeten zoeken
#     # om in een submenu te zoeken moet je dus eerst het menu specifieren om dan het item eruit te halen dat je wilt
#     temperatuur = data["main"]["temp"]
#     #bv in weather menu zoek ik naar menu 0, in menu 0 zoek ik naar beschrijving
#     weerbeschrijving = data["weather"][0]["description"]
#     vochtigheid = data["main"]["humidity"]
#     windsnelheid = data["wind"]["speed"] * 3.6  # m/s naar km/u
    
#     # Resultaten weergeven
#     print(f"Het weer in {city}:")
#     print(f"Temperatuur: {temperatuur}°C")
#     print(f"Weerbeschrijving: {weerbeschrijving}")
#     print(f"Vochtigheid: {vochtigheid}%")
#     print(f"Windsnelheid: {windsnelheid:.2f} km/u")
# else:
#     print(f"Fout bij het ophalen van de gegevens: {response.status_code}")
