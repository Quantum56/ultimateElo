class Player:
    def __init__(self, id, elo):
        self.index = id
        self._rating = elo

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, elo):
        self._rating = elo

    @property
    def id(self):
        return self.index