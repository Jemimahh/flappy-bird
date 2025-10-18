from __future__ import annotations
import pygame as pg
from typing import List 
from src import settings as S
from src.assets import Assets
from src.sprites import Bird, PipePair, make_pipe_pair

class Game:
    def __init__(self, screen: pg.Surface, clock: pg.time.Clock) -> None:
        self.screen = screen
        self.clock = clock
        self.assets = Assets()
        self.reset()

    def reset(self) -> None:
        self.score = 0
        self.background_x = 0
        self.base_x = 0
        self.bird = Bird(self.assets.bird, (S.WIDTH // 5, S.HEIGHT // 2))
        self.pipes: list[PipePair] = []
        self.spawn_timer = 0
        self.running = True

    def spawn_pipe(self) -> None:
        self.pipes.append(make_pipe_pair(self.assets.pipe, self.assets.pipe_top))

    def update(self, dt: float):
        self.bird.update(dt)
        # base_x should wrap by the base image width
        base_w = self.assets.base.get_width()
        self.base_x = (self.base_x + S.SCROLL_SPEED * dt) % -base_w

        for p in list(self.pipes):
            p.update(dt)
            if p.offscreen():
                self.pipes.remove(p)

            if not p.passed and p.top_rect.centerx < self.bird.rect.centerx:
                p.passed = True
                self.score += 1
                if "point" in self.assets.sounds:
                    self.assets.sounds["point"].play()
        
        self.spawn_timer += dt * 1000
        if self.spawn_timer >= S.PIPE_SPAWN_MS:
            self.spawn_timer = 0
            self.spawn_pipe()


        # Collisions with pipes or ground/ceiling
        for p in self.pipes:
            if p.collides(self.bird.rect):
                self.running = False
                if "hit" in self.assets.sounds:
                    self.assets.sounds["hit"].play()
                break

        if self.bird.rect.top <= 0 or self.bird.rect.bottom >= S.HEIGHT - self.assets.base.get_height():
            self.running = False
    
    def draw(self) -> None:
        self.screen.blit(self.assets.background, (0, 0))

        for p in self.pipes:
            p.draw(self.screen)


        # Base (tile twice for scrolling)
        base_w = self.assets.base.get_width()
        self.screen.blit(self.assets.base, (self.base_x, S.HEIGHT - self.assets.base.get_height()))
        self.screen.blit(self.assets.base, (self.base_x + base_w, S.HEIGHT - self.assets.base.get_height()))


        # Bird
        self.screen.blit(self.bird.image, self.bird.rect)


        # Score
        self._draw_score(self.score) 

    def _draw_score(self, value: int) -> None:
        digits = list(str(value))
        total_w = sum(self.assets.digits[int(d)].get_width() for d in digits)
        x = (S.WIDTH - total_w) // 2
        y = int(S.HEIGHT * 0.05)
        for d in digits:
            img = self.assets.digits[int(d)]
            self.screen.blit(img, (x, y))
            x += img.get_width()  

    

    def run(self) -> None:
        font = pg.font.SysFont(None, 36)
        title = font.render("Press SPACE to flap or ESC to quit", True, (255, 255, 255))
        title_rect = title.get_rect(center=(S.WIDTH // 2, S.HEIGHT // 2))

        # --- Show start screen once ---
        if not self.show_start_screen(font, title, title_rect):
            return

        # --- Main play loop ---
        while True:
            self.reset()
            self.spawn_pipe()
            self.play_game(font)

            replay = self.show_game_over_screen(font)
            if not replay:
                break


    def show_start_screen(self, font, title, title_rect):
        waiting = True
        while waiting:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    return False
                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_ESCAPE:
                        return False
                    if e.key == pg.K_SPACE:
                        waiting = False
            self.screen.blit(self.assets.background, (0, 0))
            self.screen.blit(title, title_rect)
            pg.display.flip()
            self.clock.tick(S.FPS)
        return True
    def play_game(self, font):
        self.running = True
        while self.running:
            dt = self.clock.tick(S.FPS) / 1000.0
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    self.running = False
                    return
                elif e.type == pg.KEYDOWN:
                    if e.key == pg.K_ESCAPE:
                        self.running = False
                        return
                    elif e.key in (pg.K_SPACE, pg.K_UP):
                        self.bird.flap()
                        if "flap" in self.assets.sounds:
                            self.assets.sounds["flap"].play()

            self.update(dt)
            self.draw()
            pg.display.flip()
    
    def show_game_over_screen(self, font):
        over = font.render(f"Game Over! Score: {self.score}", True, (255, 255, 255))
        prompt = font.render("Press SPACE to play again or ESC to quit", True, (255, 255, 255))
        over_rect = over.get_rect(center=(S.WIDTH // 2, S.HEIGHT // 2 - 24))
        prompt_rect = prompt.get_rect(center=(S.WIDTH // 2, S.HEIGHT // 2 + 24))

        pg.time.wait(800)
        showing = True
        while showing:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    return False
                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_ESCAPE:
                        return False
                    if e.key == pg.K_SPACE:
                        return True
            self.screen.blit(self.assets.background, (0, 0))
            self.screen.blit(over, over_rect)
            self.screen.blit(prompt, prompt_rect)
            pg.display.flip()
            self.clock.tick(S.FPS)


