def chooseEnviroment(count):
    if count == 0:
        return ["Dirty", "Dirty"]
    elif count == 1:
        return ["Dirty", "Clean"]
    elif count == 2:
        return ["Clean", "Dirty"]
    elif count == 3:
        return ["Clean", "Clean"]
    return None


def chooseInitialPosition(count):
    if count == 0:
        return "Right"
    elif count == 1:
        return "Left"
    return None


def response(response, configuration, location):
    print("===============" + location)
    if response == "Limpando A.":
        configuration[0] = "Clean"
    elif response == "Limpando B.":
        configuration[1] = "Clean"
    elif response == "Left" or response == "Right":
        location == response

    return [configuration, location]


def actionAgent(configuration, location):
    if location == "Left":
        if act(configuration[0]) == "Suck":
            return "Limpando A."
        else:

            return moveAgent(location)
    elif location == "Right":
        if act(configuration[1]) == "Suck":
            return "Limpando B."
        else:
            return moveAgent(location)


def act(status):
    if status == "Dirty":
        print("Limpando")
        return "Suck"
    return None


def moveAgent(location):
    if location == "Right":
        print("ANDANDO PARA A ESQUERDA")
        return "Left"
    elif location == "Left":
        print("ANDANDO PARA A DIREITA")
        return "Right"
    return None
