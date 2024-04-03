class Game:
    def __init__(self, title):
        self.title = title
        

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0 and not hasattr(title, '__setitem__'):
            self._title = title
        
    def results(self):
        return [ result for result in Result.all if result.game == self ] 

    def players(self):
        player_list = []
        for result in Result.all:
            if result.game == self and result.player not in player_list:
                player_list.append(result.player)
        return player_list

    def average_score(self, player):
        scores = [ result.score for result in Result.all if result.player == player ]
        return sum(scores)/len(scores)

class Player:


    def __init__(self, username):
        self.username = username
        
    
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and (2 <= len(username) <= 16) and not hasattr(username, '__setitem__'):
            self._username = username

    def results(self):
        return [ result for result in Result.all if result.player == self ]

    def games_played(self):
        games = []
        for result in Result.all:
            if result.player == self and result.game not in games:
                games.append(result.game)
        return games

    def played_game(self, game):
        games = self.games_played()
        return game in games

    def num_times_played(self, game):
        games = [ result.game for result in Result.all if result.player == self ]
        if game in games:
            return games.count(game)
        else:
            return 0

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise ValueError("Player must be an instance of Player")

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if isinstance(score, int) and (1<=score<=5000) and not hasattr(self, '_score'):
            self._score = score
        
