# score.py

class Score:
    def __init__(self):
        self.scores = {}

    def load_scores(self):
        try:
            with open("scores.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    username, points, wins = line.strip().split(",")
                    self.scores[username] = (int(points), int(wins))
        except FileNotFoundError:
            # If scores file doesn't exist, initialize with an empty dictionary
            self.scores = {}

    def save_scores(self):
        with open("scores.txt", "w") as file:
            for username, (points, wins) in self.scores.items():
                file.write(f"{username},{points},{wins}\n")

    def update_score(self, username, points, wins):
        if username in self.scores:
            prev_points, prev_wins = self.scores[username]
            self.scores[username] = (prev_points + points, prev_wins + wins)
        else:
            self.scores[username] = (points, wins)

    def show_top_scores(self):
        if not self.scores:
            print("No scores available yet.")
            return

        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1][0], reverse=True)
        print("Top Scores:")
        for i, (username, (points, wins)) in enumerate(sorted_scores[:10], 1):
            print(f"{i}. {username} - Points: {points}, Wins: {wins}")