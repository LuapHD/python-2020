def initPlayers():

    players = \
    [
        {
            "name" : "Paul",
            "score": '12',
            "backpack": [ 'Fackel', 'Schwert', 'Trank', 'Ring der Zerstörung' ]
        },
        {
            "name" : "Stephan",
            "score": '43',
            "backpack": [ 'Schlafsack', 'Isomatte', 'Gaskocher', 'Dose Ravioli' ]
        }
    ]

    x = input('Willst du auf player1 oder auf player2 zugreifen (1 oder 2) ?')

    z = int(x) - 1

    y = input('Willst du den Namen (N) , den Score (S) , den Backpack (B) oder alles einsehen (a) ')
    if (y == 'N'):
        print ('Name ' + players[z]['name'])

    elif (y == 'S'):
        print('Score ' + players[z]['score'])

    elif (y == 'B'):

        for i in range(0, 4):
            print('In dem Backpack sind ' + players[z]['backpack'][i] + '.' )

    elif (y == 'a'):
        print('Name ' + players[z]['name'])

        print('Score ' + players[z]['score'])

        for Gegenstand in players[z]['backpack']:
            print('Du hast ' + Gegenstand + '.')

    else:
        quit('Falsche Angabe')

initPlayers()