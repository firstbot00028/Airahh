# ⚡ Aira Power Engine (Telegram Bot + Connection Fix)
### Developed by: Engineer Adam 💎

A powerful Telegram Bot framework integrated with a Flask dummy server to ensure 100% uptime on hosting platforms like Render. This engine handles custom commands, interactive menus, and simulated pairing requests.

---

## 🌟 Why Aira Power Engine?
Hosting Telegram bots on Render often leads to "Port Binding" errors because Render expects a web server. This project solves that by running a **background Flask thread** alongside the bot.

## ✨ Key Features
- **🚀 Port Fix:** Integrated Flask server to keep Render deployment alive.
- **🔘 Interactive UI:** Inline keyboard menus for easy navigation.
- **📞 Call/Bug Simulation:** Dedicated menus for simulated bug testing and call loops.
- **🔑 Pairing System:** Custom prefix pairing simulation for WhatsApp/other connections.
- **🧵 Multithreading:** Uses Python's `threading` to run the bot and web server simultaneously.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Library:** `python-telegram-bot` (v20+)
- **Web Framework:** Flask
- **Deployment:** Render / Railway / Local

## 🚀 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/your-username/aira-power-engine.git](https://github.com/your-username/aira-power-engine.git)

