class Player:
    def __init__(self, rank, elo):
        self.index = rank
        self.rating = elo

    def get_rating(self):
        return self.rating

    def get_rank(self):
        return self.index

    def set_rating(self, new_elo):
        self.rating = new_elo

    def set_rank(self, new_rank):
        self.index = new_rank