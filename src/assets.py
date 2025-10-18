from __future__ import annotations
import pygame as pg
from pathlib import Path
from typing import Dict, Tuple, List
from src import settings as S


class Assets:
    background: pg.Surface
    base: pg.Surface
    pipe: pg.Surface
    pipe_top: pg.Surface
    bird: pg.Surface
    digits: List[pg.Surface]
    sounds: Dict[str, pg.mixer.Sound]

    def __init__(self):
        self._load_images()
        self._load_sounds()

    def _load_images(self) -> None:
        def load(name: str) -> pg.Surface:
            surf = pg.image.load(str(Path(S.IMG_DIR, name))).convert_alpha()
            return surf
        self.background = load("background.png")
        self.base = load("base.png")
        self.pipe = load("pipe.png")
        self.pipe_top = pg.transform.rotate(self.pipe, 180)
        self.bird = load("bird.png")
        # Digits 0-9 for score
        self.digits = [load(f"digits/{i}.png") for i in range(10)]
    
    def _load_sounds(self) -> None:
        self.sounds = {}
        for key, fname in ("flap", "flap.wav"), ("point", "point.wav"),("hit", "hit.wav"):
                p = Path(S.SND_DIR, fname)
                if p.exists():
                    try:
                        self.sounds[key] = pg.mixer.Sound(str(p))
                    except pg.error:
                        pass
