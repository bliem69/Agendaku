def openFile(filepath = 'agenda.txt'):
    with open('agenda.txt', mode='r') as file:
        agendaku = file.readlines()
    return agendaku

def createAgenda(filepath = 'agenda.txt'):
    with open('agenda.txt', mode='w') as file:
        file.writelines([])

def saveAgenda(filepath = 'agenda.txt', agendaku = []):
    with open('agenda.txt', mode='w') as file:
        file.writelines(agendaku)
