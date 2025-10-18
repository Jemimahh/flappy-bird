# 🐤 Flappy Bird (Pygame)

A recreation of **Flappy Bird** built with [Pygame](https://www.pygame.org/news) — written in object-oriented Python.  
This version separates logic, assets, and configuration into distinct modules for easy extension, experimentation, and AI integration (e.g. genetic or NEAT algorithms).

---

## 🎮 Features
- Frame-rate-independent physics (`delta-time` system)
- Modular file structure (`src/` package)
- Collision-based game loop (pipes, base, ceiling)
- Dynamic pipe generation
- Sprite-based bird physics and gravity
- Optional sound effects for flap, hit, and point events
- Ready for **AI / Genetic Algorithm** control instead of keyboard input
- Compatible with both **pygame 2.6+** and **pygame-ce 2.5+**

---

## 🧱 Project Structure
```
flappy-bird/
├─ assets/
│  ├─ images/
│  │  ├─ background.png
│  │  ├─ base.png
│  │  ├─ bird.png
│  │  ├─ pipe.png
│  │  └─ digits/0.png ... 9.png
│  └─ sounds/
│     ├─ flap.wav
│     ├─ point.wav
│     └─ hit.wav
└─ src/
  ├─ __init__.py
  ├─ main.py
  ├─ game.py
  ├─ sprites.py
  ├─ assets.py
  └─ settings.py

```

---

## ⚙️ Installation

### 1️⃣ Create a virtual environment (recommended)
```bash
python -m venv .venv
# Activate it
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 2️⃣ Install dependencies
You can use either **pygame** or **pygame-ce**:

```bash
pip install pygame>=2.6.0
# or
pip install pygame-ce>=2.5.5
```

---

## ▶️ Running the Game

From the project root:
```bash
python -m src.main
```

Press **SPACE** to flap, **ESC** to quit.  
Your goal is to navigate between pipes and score as many points as possible.

---

## 🔊 Sound Effects

Place `.wav` files in `assets/sounds/`:

| File        | Event Triggered By   |
|--------------|----------------------|
| `flap.wav`   | Bird flap (SPACE/UP) |
| `point.wav`  | Passing a pipe pair  |
| `hit.wav`    | Collision or ground  |

You can download or create your own from free SFX libraries such as:
- [Pixabay Sounds](https://pixabay.com/sound-effects/)
- [Zapsplat](https://www.zapsplat.com/)
- [The Sounds Resource – Flappy Bird](https://www.sounds-resource.com/mobile/flappybird/sound/5309/)

---

## 🧠 AI / Genetic Algorithm Mode

The architecture allows easy substitution of human input with AI:
- Expose `Game` state variables (bird position, pipe gap, velocity)
- Replace keyboard checks in `game.run()` with your agent’s decisions
- Use fitness = `score` or survival time
- Perfect base for experiments with **NEAT** or custom genetic algorithms

---

## 🧪 Tests

Basic smoke tests are provided under `tests/test_smoke.py`:
```bash
pytest
```
These confirm imports, settings, and sprite creation all work.

---

## 🪶 Customization

You can modify difficulty or visuals through `src/settings.py`:

| Variable | Description | Default |
|-----------|--------------|----------|
| `PIPE_GAP` | Vertical gap between pipes | 150 |
| `SCROLL_SPEED` | Pipe/base horizontal speed | -180 |
| `FLAP_STRENGTH` | Bird’s upward impulse | -350 |
| `PIPE_SPAWN_MS` | Interval (ms) between new pipes | 1400 |

---

## 💡 Troubleshooting

**“ModuleNotFoundError: No module named 'settings'”**  
→ Run from project root:  
```bash
python -m src.main
```

**“TypeError: 'module' object is not callable”**  
→ Make sure imports use package syntax:
```python
from .game import Game
```

**No sound?**  
→ Check if `.wav` files exist and `pg.mixer.init()` is called without error.

---

## 🧑‍💻 Credits

Built with ❤️ using Python and Pygame.  
I will be using this to create/integate a genetic algorithms.

---

## 📄 License

This project is distributed under the **MIT License** — you can use it freely for learning or open-source projects.

---

*“One flap at a time.”*
