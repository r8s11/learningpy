import sys
import pygame

class AliensInvation:
    """Initialze the game, and create game resources."""
    pygame.init()

    self.screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        print("hello")

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AliensInvation()
    ai.run_game()
