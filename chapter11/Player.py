class Player:

    def __init__(self, id, first, last, position):
        self.id = id
        self.first = first
        self.last = last
        self.position = position
        
    def add_assist(self):
        self.assists = assists + 1