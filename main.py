import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

# --- CONFIGURATION ---
BOT_TOKEN = "8573910741:AAG-mv1WxrFeoZJsf_VOXbajr4QDwIoRBYc" # Ninte puthiya token
CUSTOM_PAIR_PREFIX = "AIRA-ADAM"
SIGNATURE = "\n\n🚀 *Sent by Aira Power Engine*"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command with Buttons"""
    keyboard = [
        [InlineKeyboardButton("🔥 Bug Menu", callback_data='bug_menu')],
        [InlineKeyboardButton("🛠️ Misc Menu", callback_data='misc_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_msg = (
        "✨ **Airahh is back** ✨\n\n"
        f"✅ **PAIRING REQUEST**\n"
        f"➔ Pairing Code: {CUSTOM_PAIR_PREFIX}-2026\n\n"
        "Status: Ready to connect multiple devices... ⚡"
    )
    await update.message.reply_text(welcome_msg + SIGNATURE, reply_markup=reply_markup, parse_mode='Markdown')

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Buttons click cheyyumpol ulla response"""
    query = update.callback_query
    await query.answer()

    if query.data == 'bug_menu':
        bug_text = (
            "🔥 **Aira Powerful Bug Menu**\n\n"
            "📱 **Android:** nullfinity, crashdroid\n"
            "🍏 **iOS:** xiosvirus, trashloc"
        )
        await query.edit_message_text(text=bug_text + SIGNATURE, parse_mode='Markdown')

    elif query.data == 'misc_menu':
        # Misc menu-vil pairing command info vechu
        misc_text = (
            "🛠️ **Misc Menu (Settings)**\n\n"
            "🔗 **Connection:**\n"
            "Use `/pair +number` to connect new device.\n\n"
            "⚡ **Power:** Engine is running at 100%"
        )
        await query.edit_message_text(text=misc_text + SIGNATURE, parse_mode='Markdown')

async def pair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Pairing logic"""
    if not context.args:
        await update.message.reply_text("❌ Usage: /pair +91XXXXXXXXXX" + SIGNATURE, parse_mode='Markdown')
        return

    phone_number = context.args[0]
    pair_msg = (
        f"🚀 **Pairing Request Sent!**\n\n"
        f"📱 **Number:** `{phone_number}`\n"
        f"🔑 **Code:** `{CUSTOM_PAIR_PREFIX}`"
    )
    await update.message.reply_text(pair_msg + SIGNATURE, parse_mode='Markdown')

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('pair', pair))
    application.add_handler(CallbackQueryHandler(button_handler))

    print("⚡ Aira Power Engine with Buttons is Live!")
    application.run_polling()
