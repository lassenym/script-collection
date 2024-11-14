import cloudscraper, sys

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[34m"
BLACK = "\033[90m"
RESET = "\033[0m"


class Map:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Game:
    def __init__(self, enemy, date):
        self.maps = []
        self.enemy = enemy
        self.date = date

    def add_map(self, map_obj):
        self.maps.append(map_obj)



def get_html(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    }
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    
    else:
        print(f"Failed to retrieve the page :( Status code {response.status_code}")
        exit()


def parse_text(text):
    text = str(text).split('\n')
    temp = ""
    temp_game = Game("Unknown", "TBD")
    for i, line in enumerate(text):
        if '<tr class="group' in line:
            new_map = Map(text[i+5].split("span")[1].split("<")[0][1:], text[i+6].split('Detail">')[1].split("<")[0].replace(" ", ""))

            if temp is not line.split('group-')[1][0]:
                if temp_game.date != "TBD":
                    temp_game.maps.reverse()
                    results.append(temp_game)

                temp_game = Game(text[i+4].split("</")[0].split(">")[3], text[i+1].split("team")[1][2:10])
                temp_game.add_map(new_map)
            else:
                temp_game.add_map(new_map)
            
            temp = line.split('group-')[1][0]

        
def wincheck(game):
    win = 0
    lose = 0
    for map in game.maps:
        if int(map.score.split("-")[0]) > int(map.score.split("-")[1]):
            win += 1
        else:
            lose += 1
    if win > lose:
        return True
    else:
        return False

def print_last_matches(x):
    print()
    for i in range(x):
        print()
        print(f"{BLACK}========{RESET}{results[x-1-i].date}{BLACK}============{RESET}\n")
        if wincheck(results[x-1-i]):
            print(f"        {BLUE}{results[x-1-i].enemy}{RESET} ({GREEN}W{RESET})")
        else:
            print(f"        {BLUE}{results[x-1-i].enemy}{RESET} ({RED}L{RESET})")
        print("")
        for map in results[x-1-i].maps:
            if int(map.score.split("-")[0]) > int(map.score.split("-")[1]):
                color = GREEN
            else:
                color = RED

            print(f"        {color}{map.name}: {map.score}{RESET}")
    print(f"\n{BLACK}============================{RESET}")
    print()



url = 'https://www.hltv.org/stats/teams/matches/5995/g2'
#url = 'https://www.hltv.org/stats/teams/matches/4608/natus-vincere'
results = []

parse_text(get_html(url))

input = int(sys.argv[1]) if len(sys.argv) > 1 else 3
print_last_matches(input)