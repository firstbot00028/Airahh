import os
import threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

# --- 1. RENDER CONNECTION FIX (Flask) ---
# Ithu Render-ile "Couldn't connect" / "Port issue" solve cheyyaanulla dummy server aanu.
app = Flask(__name__)

@app.route('/')
def home():
    return "Aira Power Engine is Running!"

def run_flask():
    # Render automatic aayi 'PORT' environment variable tharum, athillengil 8080 edukkum.
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# --- 2. CONFIGURATION ---
BOT_TOKEN = "8573910741:AAG-mv1WxrFeoZJsf_VOXbajr4QDwIoRBYc"
CUSTOM_PAIR_PREFIX = "AIRA-ADAM"
SIGNATURE = "\n\n🚀 *Sent by Aira Power Engine*"

# --- 3. BOT LOGIC ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Main Menu with Buttons"""
    keyboard = [
        [InlineKeyboardButton("🔥 Bug Menu", callback_data='bug_menu')],
        [InlineKeyboardButton("📞 Call Bug", callback_data='call_bug')],
        [InlineKeyboardButton("🛠️ Misc Menu", callback_data='misc_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    msg = "✨ **Airahh Power Engine** ✨\n\nStatus: Online & Fully Fixed ⚡"
    await update.message.reply_text(msg + SIGNATURE, reply_markup=reply_markup, parse_mode='Markdown')

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'bug_menu':
        bug_text = "🔥 **Aira Bug List**\n\n• nullfinity\n• crashdroid\n\nUsage: `/send_bug [type]`"
        await query.edit_message_text(text=bug_text + SIGNATURE, parse_mode='Markdown')

    elif query.data == 'call_bug':
        call_text = "📞 **Call Bug Menu**\n\n• `call-crash`: Hangs WhatsApp\n• `call-loop`: Continuous call\n\nUsage: `/call_bug [type] [number]`"
        await query.edit_message_text(text=call_text + SIGNATURE, parse_mode='Markdown')

    elif query.data == 'misc_menu':
        misc_text = "🛠️ **Misc Menu**\n\nUse `/pair +number` for connection."
        await query.edit_message_text(text=misc_text + SIGNATURE, parse_mode='Markdown')

async def pair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Pairing command"""
    if not context.args:
        await update.message.reply_text("❌ Usage: `/pair +91XXXXXXXXXX`" + SIGNATURE, parse_mode='Markdown')
        return
    num = context.args[0]
    pair_msg = f"🚀 **Pairing Request Sent!**\n📱 Number: `{num}`\n🔑 Code: `{CUSTOM_PAIR_PREFIX}`"
    await update.message.reply_text(pair_msg + SIGNATURE, parse_mode='Markdown')

if __name__ == '__main__':
    # Flask server background-il start cheyyunnu (Render port issue fix cheyyaan)
    threading.Thread(target=run_flask).start()
    
    # Telegram Bot start cheyyunnu
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('pair', pair))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    print("⚡ Aira Power Engine is Live and Connection fixed!")
    application.run_polling()
