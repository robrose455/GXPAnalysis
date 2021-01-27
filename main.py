import requests


class Player:

    def __init__(self, role, currentgold, id, teamcolor):
        self.role = role
        self.currentgold = currentgold
        self.id = id
        self.teamcolor = teamcolor


def main():
    key = "RGAPI-6378461c-0e9c-4504-81f2-9ac932f69724"

    # GRABS ENCRYPTED ACCOUNT ID
    URL = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Yung%20Rose?api_key=" + key
    response = requests.get(URL)
    responseJson = response.json()
    accountId = responseJson['accountId']

    # GRABS MATCH LIST FROM GIVEN ACCOUNT ID
    URL = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountId + "?endIndex=20&api_key=" + key
    response = requests.get(URL)
    responseJson = response.json()
    matchList = responseJson['matches']

    # SHOWS MATCH LIST
    count = 1
    for x in range(len(matchList)):
        print(str(count) + ". ", end=" ")
        print(matchList[x])
        count = count + 1

    # SELECT GAME FROM MATCH LIST
    matchNumber = input("\nPick a game to analyze: ")
    match = matchList[int(matchNumber) - 1]
    gameId = match['gameId']

    # QUERY FRAME DATA FROM GIVEN GAME ID
    URL = "https://na1.api.riotgames.com/lol/match/v4/timelines/by-match/" + (str(gameId)) + "?api_key=" + key
    response = requests.get(URL)
    responseJson = response.json()
    frameLength = len(responseJson['frames']) - 1
    keepGoing = True
    frameNum = 1
    while keepGoing | (frameNum > frameLength):

        for x in range(10):
            playerData = responseJson['frames'][frameNum]['participantFrames'][str(x + 1)]
            print(playerData)

        print("Frame " + str(frameNum) + " out of " + str(frameLength))

        a = input("Enter Frame '#' to view or 'Exit' to exit: ")

        if a == 'Exit':
            keepGoing = False

        if int(a) >= frameLength:
            print("Frame out of range")

        else:
            frameNum = int(a)

    else:

        print("Done")


if __name__ == "__main__":
    main()
