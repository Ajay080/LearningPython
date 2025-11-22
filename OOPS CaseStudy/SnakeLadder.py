import random


class Board:
    def __init__(self, size, snakes, ladders):
        self.size = size
        self.snakes = snakes
        self.ladders = ladders

    def get_final_position(self, position):
        # if snake
        if position in self.snakes:
            return self.snakes[position]

        # if ladder
        if position in self.ladders:
            return self.ladders[position]

        return position


class Game:
    def __init__(self, board, players):
        self.board = board
        self.players = players              # instance variable ✔
        self.current_turn = 0
        self.playing = True

    def roll_dice(self):
        return random.randint(1, 6)

    def get_current_player(self):
        return self.players[self.current_turn]

    def has_won(self, player):
        return player.position == self.board.size

    def all_players_done(self):
        return all(p.position == self.board.size for p in self.players)

    def play_turn(self):
        if self.all_players_done():
            print("All players have won!")
            self.playing = False
            return

        player = self.get_current_player()

        # If the player has already finished
        if self.has_won(player):
            print(f"{player.name} has already won! Skipping turn.")
            self.current_turn = (self.current_turn + 1) % len(self.players)
            return

        roll = self.roll_dice()
        print(f"{player.name} rolled a {roll}")

        new_pos = player.position + roll

        if new_pos > self.board.size:
            print(f"{player.name} needs an exact roll to win.")
        else:
            final_pos = self.board.get_final_position(new_pos)

            if final_pos > new_pos:
                print(f"{player.name} climbed a ladder to {final_pos}")
            elif final_pos < new_pos:
                print(f"{player.name} got bitten by a snake to {final_pos}")
            else:
                print(f"{player.name} moved to {final_pos}")

            player.position = final_pos
            if self.has_won(player):
                print(f"🎉 {player.name} wins the game!")

        # move turn
        self.current_turn = (self.current_turn + 1) % len(self.players)


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.position = 0


class SnakesLadders:
    def __init__(self):
        snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60,
                  87: 24, 93: 73, 95: 75, 98: 78}

        ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84,
                   36: 44, 51: 67, 71: 91, 80: 100}

        board = Board(100, snakes, ladders)

        players = [
            Player("Player1", "Red"),
            Player("Player2", "Blue"),
            Player("Player3", "Pink"),
            Player("Player4", "Green"),
        ]

        game = Game(board, players)

        while game.playing:
            game.play_turn()


if __name__ == "__main__":
    SnakesLadders()
