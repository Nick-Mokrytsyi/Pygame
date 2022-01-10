class Stats():

    def __init__(self):
        """" """
        self.score = None
        self.guns_left = None
        self.reset_stats()
        self.flag = True
        with open('high_score.txt','r') as file:
            self.high_score = int(file.readline())

    def reset_stats(self):
        """"The stats changing during the game"""
        self.guns_left = 2
        self.score = 0
