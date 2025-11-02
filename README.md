# Autonomous Agentic Trading Floor

A fully autonomous, agentic trading workstation that:

- reads live market data
- stores accounts + analytics
- automatically triggers agent plans + tools
- runs every **N minutes** (via `.env`)
- has a Neon Dark Trading Floor UI (Gradio)

## Features

| Feature | Details |
|--------|---------|
| ✅ Agentic planning | Agents decide what to buy/sell |
| ✅ Persistent storage | SQLite accounts + logs |
| ✅ Scheduler | Runs every N minutes (background) |
| ✅ Neon dark UI | Professional trading desk style |
| ✅ Realtime logs | Timeline + transaction reporting |
| ✅ Multiple model calls | integrated tracing + trace IDs |

---

## Requirements

### Python
- Python **3.12**
- create a venv

```bash
python -m venv .venv
source .venv/bin/activate  # linux/macos
.venv\Scripts\activate     # windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

example requirements:

```
gradio
python-dotenv
pandas
numpy
matplotlib
sqlalchemy
openai
```

(add other libs if your project uses them)

---

## .env configuration

create a `.env` file:

```
OPENAI_API_KEY=YOUR_KEY
RUN_EVERY_MINUTES=5
```

---

## How to Run **(important)**

This project intentionally runs as **two processes**, like a real trading floor.

### 1) Terminal A → background periodic worker

```bash
python trading_floor.py
```

### 2) Terminal B → UI

```bash
python app.py
```

Now open browser: http://localhost:7860

---

## Project Architecture

```
/project
│
├─ app.py               # main UI (Gradio)
├─ trading_floor.py     # background periodic execution
├─ util.py              # UI theme + helpers
├─ database/            # sqlite + logs
└─ agents/              # agent logic + tools
```

---

## Deploy

You can deploy the UI to **HuggingFace Spaces** and run the background worker separately.

- app.py → Space UI
- trading_floor.py → private worker / server cron job

This separation is intentional — just like real desks: UI and execution are not the same process.

---

## Screenshots / Demo 
*(GIF or short clip will boost engagement massively)*

---

PRs + criticism welcome.
