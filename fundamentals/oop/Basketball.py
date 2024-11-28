class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

    def display_player_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Position: {self.position}")
        print(f"Team: {self.team}")
        return self

    @classmethod
    def get_team(cls, team_list):
        return [cls(player["name"], player["age"], player["position"], player["team"]) for player in team_list]



players = [
    {
        "name": "Kevin Durant", 
        "age": 34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age": 24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age": 32,  
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    }
]


team = Player.get_team(players)

for player in team:
    player.display_player_info()
    print("-" * 30)
