# ⌨️ Typing Trainer

Terminal-based typing speed trainer inspired by Monkeytype and ttyper.  
Built with Python + Rich — runs entirely in your terminal.

---

## Features

- **Two game modes** — timed session (30 or 60 sec) or fixed word count (25 or 50 words)
- **Three difficulty levels** — Easy / Medium / Hard, scored automatically based on word complexity
- **Real-time feedback** — green for correct words, red for wrong ones
- **Live stats** — WPM and accuracy after each session
- **Clean terminal UI** — two-panel layout via Rich (input box + word display)
- **Cross-platform** — works on Windows, Linux and macOS

---

## Difficulty System

Each word gets a score based on:

| Criterion | Details |
|---|---|
| Word length | short = 0pts, 7–11 = 2pts, 12+ = 3pts |
| Consonant ratio | high consonant % adds up to 4pts |
| Repeated letters | 3+ repeats of same letter adds 1–2pts |

| Score | Level |
|---|---|
| 0–1 | Easy |
| 2–3 | Medium |
| 4+ | Hard |

---

## Installation

```bash
git clone https://github.com/SargeraSSS/typing_trainer.git
cd typing_trainer
pip install -r requirements.txt
```

No virtual environment required — just clone and install.

---

## Usage

**Windows:**
```bash
python main.py
```
Or just double-click `run.bat`

**Linux/macOS:**
```bash
chmod +x run.sh
./run.sh
```
Or:
```bash
python3 main.py
```

---

## Project Structure

```
typing_trainer/
├── main.py          # entry point + menu
├── trainer.py       # game logic, input handling, modes
├── words.py         # word loading + difficulty scoring
├── words.json       # ~2500 curated English words
├── run.bat          # one-click launcher (Windows)
├── run.sh           # one-click launcher (Linux/macOS)
└── requirements.txt
```

---

## Stack

- Python 3.8+
- [Rich](https://github.com/Textualize/rich) — terminal UI
- `msvcrt` — raw keyboard input (Windows)
- `tty/termios` — raw keyboard input (Linux/macOS)