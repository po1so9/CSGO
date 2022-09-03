import requests
import pprint
import sys
def main():
    id = (input("Enter Your Steam I'd: "))
    if len(id) != 17:
        sys.exit("Enter valid id(17 digits)")



    BASE_URL = ("https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=12A1D1DE83F9932934EDD6DF2BA00463&steamid="+id)
    try:
        data = requests.get(BASE_URL).json()
        printer = pprint.PrettyPrinter()

        Playerstats = data['playerstats']
        #printer.pprint(stats)
        stats = Playerstats['stats']


        """
        for i in stats[0]:
            print(i)
        """
        print()
        for stat in stats:
            for value in stat:
                print(stat[value])
            print("=================================================================")
            #print(stat)
    except:
        print("An Error Occurred")

if __name__ == "__main__":
    main()