from __future__ import annotations
import pygame as pg
from src import settings as S
from src.game import Game


def main() -> None:
    pg.init()

    try:
        pg.mixer.pre_init(44100, -16, 2, 512)
    except Exception:
        pass

    screen = pg.display.set_mode((S.WIDTH, S.HEIGHT))
    pg.display.set_caption(S.TITLE)
    clock = pg.time.Clock()


    game = Game(screen, clock)
    # Loop runs one full session (start screen → play → game over)
    game.run()


    pg.quit()

if __name__ == "__main__":
    main()