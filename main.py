import functions


punctuation = [0, 0, 0, 0, 0, 0, 0, 0]

location = "Left"

configuration = ["Dirty", "Dirty"]

print(
    f"POSIÇÃO: {location}  CONFIGURAÇÃO: [{configuration[0]}][{configuration[1]}]")

for i in range(4):
    response = functions.response(functions.actionAgent(
        configuration, location), configuration, location)
    print(response[1])
    location = response[1]
    configuration = response[0]
    print(
        f"POSIÇÃO: {location} CONFIGURAÇÃO :[{configuration[0]}][{configuration[1]}]")
