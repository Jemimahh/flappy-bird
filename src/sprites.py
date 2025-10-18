from __future__ import annotations
import random
import pygame as pg
from dataclasses import dataclass
from src import settings as S

@dataclass
class PipePair:
    top_surf: pg.Surface
    bot_surf: pg.Surface
    top_rect: pg.Rect
    bot_rect: pg.Rect
    speed_x:  float = S.SCROLL_SPEED
    passed: bool = False

    def update(self, dt: float) -> None:
        dx = int(self.speed_x * dt)
        # move rects horizontally
        self.top_rect.x += dx
        self.bot_rect.x += dx

    def draw(self, screen: pg.Surface) -> None:
        screen.blit(self.top_surf, self.top_rect)
        screen.blit(self.bot_surf, self.bot_rect)

    def offscreen(self) -> bool:
        # offscreen when the right edge has moved past the left of the screen
        return self.top_rect.right < 0
    
    def collides(self, rect: pg.Rect) -> bool:
        return rect.colliderect(self.top_rect) or rect.colliderect(self.bot_rect)
    
def make_pipe_pair(pipe_img: pg.Surface, pipe_top_img: pg.Surface) -> PipePair:
    gap = S.PIPE_GAP

    gap_y = random.randint(S.PIPE_MIN_Y + gap // 2, S.HEIGHT - S.PIPE_MIN_Y - gap // 2)
    
    top_rect = pipe_top_img.get_rect()
    bot_rect = pipe_img.get_rect()

    x = S.WIDTH + 40
    top_rect.bottomleft = (x, gap_y - gap // 2)
    bot_rect.topleft = (x, gap_y + gap // 2)

    return PipePair(top_surf=pipe_top_img,bot_surf=pipe_img, top_rect=top_rect, bot_rect=bot_rect)

class Bird(pg.sprite.Sprite):
    def __init__(self, image: pg.Surface, pos: tuple[int, int]) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.vel_y = 0.0

    def update(self, dt: float) -> None:
        self.vel_y = min(self.vel_y + S.GRAVITY * dt, S.MAX_FALL_SPEED)
        self.rect.y += int(self.vel_y * dt)

    def flap(self) -> None:
        self.vel_y = S.FLAP_STRENGTH
 


