class Game:
    def __init__(self, title):
        self.title = title
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if not hasattr(self, '_title'):
            if isinstance(title, str) and 0<len(title):
                self._title=title


    def results(self):
        return [result for result in Result.all if result.game==self]

    def players(self):
        return list(set(result.player for result in self.results() ))

    def average_score(self, player):
        results=self.results()
        return sum(result.score for result in results)/len(results)

class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self,username):
        if isinstance(username, str) and 2<=len(username)<=16:
            self._username=username

    def results(self):
        return [result for result in Result.all if result.player==self]

    def games_played(self):
        return list(set(result.game for result in self.results()))

    def played_game(self, game):
        games_played=self.games_played()
        if game in games_played:
            return True
        else:
            return False

    def num_times_played(self, game):
        results=self.results()
        freq=0
        for result in results:
            if result.game==game:
                freq+=1
        return freq 


class Result:
    all=[]
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, score):
        if not hasattr(self, '_score'):
            if isinstance(score, int) and 1<=score<=5000:
                self._score=score
    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
           self._player=player 
    @property
    def game(self):
        return self._game
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
           self._game=game 