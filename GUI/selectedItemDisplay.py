class SelectedItemDisplay:
    def __init__(self, startPos):
        self.x = startPos[0]
        self.y = startPos[1]
        self.item = None

    def draw(self, screen):
        pass

    def updateSelectedItem(self, item):
        self.item = item