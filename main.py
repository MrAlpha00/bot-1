from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# LINKS
CHANNEL_USERNAME = 'aneelacademy'
INSTAGRAM_LINK = 'https://www.instagram.com/aneelacademy.official/'
YOUTUBE_LINK = 'https://www.youtube.com/@aneelacademy'
WEBSITE_LINK = 'https://aneelacademy.com/'
APP_LINK = 'Coming Soon...'

ADMIN_ID = 7259807358  # Replace with your Telegram user ID

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("✅ Join Telegram Channel", url=f"https://t.me/{CHANNEL_USERNAME}")],
        [InlineKeyboardButton("📸 Instagram", url=INSTAGRAM_LINK)],
        [InlineKeyboardButton("▶️ YouTube", url=YOUTUBE_LINK)],
        [InlineKeyboardButton("🌐 Website", url=WEBSITE_LINK)],
        [InlineKeyboardButton("📱 App", callback_data="app_link")],
        [InlineKeyboardButton("✔️ I Joined✅", callback_data="verify_join")]
    ]
    await update.message.reply_text("🎉 To continue, please join our channel and follow our social links below:", reply_markup=InlineKeyboardMarkup(keyboard))

# VERIFY JOIN
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "verify_join":
        member = await context.bot.get_chat_member(chat_id=f"@{CHANNEL_USERNAME}", user_id=query.from_user.id)
        if member.status in ["member", "administrator", "creator"]:
            keyboard = [
                [InlineKeyboardButton("🎁 Birthday Special Offer", callback_data="show_offer")],
                [
                    InlineKeyboardButton("📩 Feedback", callback_data="feedback"),
                    InlineKeyboardButton("🆘 Help", callback_data="help"),
                    InlineKeyboardButton("🌐 Website", url=WEBSITE_LINK),
                    InlineKeyboardButton("📱 App", callback_data="app_link")
                ]
            ]
            await query.message.reply_text(
                "🎓 Welcome to Aneel Academy Bot!\n🚀 Learn. Grow. Succeed. \n\n🎉You're now connected with Aneel Academy – your trusted companion for career-building courses and digital skills.\n\n🎁 Tap below to unlock your 🎂 *Birthday Special Offer* (for a limited time)!\n\nNeed help or want to explore more?\n👇 Check out the quick access buttons below.",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        else:
            await query.message.reply_text("❌ You haven't joined the channel yet! Please join and click 'I Joined' again.")

    elif query.data == "show_offer":
        keyboard = [
            [InlineKeyboardButton("💻 Ethical Hacking - ₹9̶9̶9̶  ₹699", callback_data="course_eh")],
            [InlineKeyboardButton("💳 Carding Course -₹9̶9̶9̶  ₹699", callback_data="course_cc")],
            [InlineKeyboardButton("🌐 Dark Web Full - ₹9̶9̶9̶  ₹699", callback_data="course_dw")],
            [InlineKeyboardButton("🔥 All 3 Combo ₹1444", callback_data="course_all")]
        ]
        await query.message.reply_text(""🎂 *Happy Birthday from Aneel Academy!* 🎉\n\n"
    "🎁 Birthday Special Courses:\n"
    "As a token of our love, enjoy access to premium learning at a special birthday rate! 🥳🎓\n\n"
    "👇 Choose a course below to begin your journey:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data.startswith("course_"):
        course_map = {
            "course_eh": ("Ethical Hacking V12.5", "https://res.cloudinary.com/dvbgfwsxc/image/upload/v1733117802/Black_forever_PC_Desktop_Wallpaper_Background_1_jrvjnz.jpg"),
            "course_cc": ("Carding Full Course", "https://res.cloudinary.com/dvbgfwsxc/image/upload/v1733117802/Black_forever_PC_Desktop_Wallpaper_Background_1_jrvjnz.jpg"),
            "course_dw": ("Dark Web Full Course", "https://res.cloudinary.com/dvbgfwsxc/image/upload/v1733117802/Black_forever_PC_Desktop_Wallpaper_Background_1_jrvjnz.jpg"),
            "course_all": ("All 3 Combo Course", "https://res.cloudinary.com/dvbgfwsxc/image/upload/v1733117802/Black_forever_PC_Desktop_Wallpaper_Background_1_jrvjnz.jpg")
        }
        title, image_url = course_map[query.data]
        text = f"📚 *{title}*\n\nUsual Price: ₹999\n🎉 Offer Price: ₹699 (or ₹1444 for all)\n\n✅ Limited Time Offer"
        buttons = [
            [
                InlineKeyboardButton("🛒 Buy Now", callback_data="buy_now"),
                InlineKeyboardButton("🔙 Back", callback_data="show_offer")
            ]
        ]
        await query.message.reply_photo(photo=image_url, caption=text, reply_markup=InlineKeyboardMarkup(buttons), parse_mode="Markdown")

    elif query.data == "buy_now":
        await query.message.reply_text("💳 Please complete your payment via our LiveGram bot. We will verify and add you to the private course channel.\n\n👉 @your_livegram_bot")

    elif query.data == "feedback":
        await query.message.reply_text("📝 Please share your feedback here. We value it!")

    elif query.data == "help":
        await query.message.reply_text("💬 Need help? Contact admin here: @aneeladmin")

    elif query.data == "app_link":
        await query.message.reply_text("📱 Our App is launching soon. Stay tuned!")

# MAIN
def main():
    app = ApplicationBuilder().token("7597955527:AAGMPlrrQGQcZmdKyuwsIN1mO0-Ub9olmnY").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == '__main__':
    main()
