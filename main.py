import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

# --- CONFIGURATION ---
# Owner details (Ninte swapnathilekulla identity)
BRAND = "AIRA WORLD AI"
OWNER_NAME = "UMMA (Owner)"
STATUS_TAG = "MAGAN ENNA MILLIONAIRE"

# --- LOGGING ---
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- COMMANDS ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Main Menu setup like your video."""
    keyboard = [
        [InlineKeyboardButton("|| Bug Menu", callback_data='bug_menu'),
         InlineKeyboardButton("|| Misc Menu", callback_data='misc_menu')],
        [InlineKeyboardButton("|| Pairing Code", callback_data='pair_code')],
        [InlineKeyboardButton("|| Channel", url='https://t.me/your_channel')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    header = (
        f"● ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ ●\n"
        f"          ✨ **{BRAND}** ✨\n"
        f"➔ **Status**: {STATUS_TAG}\n"
        f"➔ **Admin**: {OWNER_NAME}\n"
        f"➔ **Online**: System Active ⚡\n"
        f"● ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ ●"
    )
    await update.message.reply_text(header, reply_markup=reply_markup, parse_mode='Markdown')

async def handle_menus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handling the sub-menus for Bugs and Pairing."""
    query = update.callback_query
    await query.answer()

    if query.data == 'bug_menu':
        text = (
            "🚀 **AIRA BUG ENGINE**\n\n"
            "**Bug Android**\n"
            "• nullfinity [num]\n"
            "• crashdroid [num]\n\n"
            "**Bug iOS**\n"
            "• xiosvirus [num]\n"
            "• trashloc [num]"
        )
        await query.edit_message_text(text=text, parse_mode='Markdown')

    elif query.data == 'pair_code':
        # Generating the unique pairing code as seen in your video
        pair_text = (
            "✅ **PAIRING REQUEST**\n"
            "➔ **Number**: +91XXXXXXXXXX\n"
            "➔ **Pairing Code**: AIRA-KASH-MIRI-2026\n\n"
            "Status: Ready to connect..."
        )
        await query.edit_message_text(text=pair_text, parse_mode='Markdown')

# --- MAIN RUNNER ---
if __name__ == '__main__':
    # Add your Bot Token from BotFather here
    TOKEN = "8447478004:AAEiZKpDXiTfCbGLsY32H_dV52SIcZ96cbM" 
    
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_menus))
    
    print("Aira AI is running... Success is coming! 🚀")
    app.run_polling()
# Mukalile commands-inu thazhe ithu add cheyyaam

async def execute_bug(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Command logic for /xiosvirus and other bugs."""
    text_received = update.message.text
    
    # Extracting the number from command (e.g., /xiosvirus +918921584368)
    try:
        command_parts = text_received.split()
        target_number = command_parts[1]
        
        # Aira's Custom Response Logic
        response = (
            f"🚀 **AIRA ATTACK INITIATED**\n"
            f"➔ **Type**: {command_parts[0]}\n"
            f"➔ **Target**: {target_number}\n"
            f"➔ **Status**: Sending Powerful Packets... ⚡\n"
            f"● ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ ●\n"
            f"**AIRA WORLD AI: SUCCESS IS OUR EGO** 😏"
        )
        await update.message.reply_text(response, parse_mode='Markdown')
        
    except IndexError:
        await update.message.reply_text("❌ **Format Error!** Use: `/command +number`", parse_mode='Markdown')

# Main app-il ithu register cheyyaan marakkalle:
# app.add_handler(CommandHandler("xiosvirus", execute_bug))
# app.add_handler(CommandHandler("nullfinity", execute_bug))
# app.add_handler(CommandHandler("crashdroid", execute_bug))
