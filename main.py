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
            await query.message.reply_photo(
                photo="https://res.cloudinary.com/dvbgfwsxc/image/upload/v1753603165/WhatsApp_Image_2025-07-26_at_07.57.57_2f710033_jgnbhj.jpg",  # Replace this with your actual hosted image URL
                caption="🎓 Welcome to Aneel Academy Bot!\n🚀 Learn. Grow. Succeed. \n\n🎉You're now connected with Aneel Academy – your trusted companion for career-building courses and digital skills.\n\n🎁 Tap below to unlock your 🎂 *Birthday Special Offer* (for a limited time)!\n\nNeed help or want to explore more?\n👇 Check out the quick access buttons below.",
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
        # 📸 Send birthday offer image
        await query.message.reply_photo(
            photo="https://res.cloudinary.com/dvbgfwsxc/image/upload/v1753603372/Bday_-_2_2_oykuhh.png",  # 🔁 Replace with your birthday course image link
            caption="🎁 Birthday Special Courses: \n\n As a token of our love, enjoy access to premium learning at a special birthday rate! 🥳🎓\n\nLimited Time offer"
        )

        # 🎯 Show buttons for birthday courses
        await query.message.reply_text(
            "👇 Choose a course to explore birthday deals:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data.startswith("course_"):
        course_map = {
            "course_eh": ("Ethical Hacking V12.5", "https://res.cloudinary.com/dvbgfwsxc/image/upload/v1753604701/WhatsApp_Image_2025-07-27_at_13.53.57_c986ce63_gyhv9t.jpg"),
            "course_cc": ("Carding Full Course", "https://res.cloudinary.com/dvbgfwsxc/image/upload/v1753604704/WhatsApp_Image_2025-07-27_at_13.53.56_3264b8b6_yaokti.jpg"),
            "course_dw": ("Dark Web Full Course", "https://res.cloudinary.com/dvbgfwsxc/image/upload/v1753604699/WhatsApp_Image_2025-07-27_at_13.54.25_82828153_xs7u0u.jpg"),
            "course_all": ("All 3 Combo Course", "https://res.cloudinary.com/dvbgfwsxc/image/upload/v1753603372/Bday_-_2_2_oykuhh.png")
        }
        title, image_url = course_map[query.data]
        text = f"📚 *{title}*\n\nUsual Price: ₹999\n🎉 Offer Price: ₹699 (or ₹1444 for all)\n\n✅ Limited Time Offer"
        buttons = [
            [
                InlineKeyboardButton("🛒 Buy Now", callback_data="buy_now"),
                InlineKeyboardButton("❤️ All Combo", callback_data="course_all"),
                InlineKeyboardButton("🔙 Back", callback_data="show_offer")
            ]
        ]
        await query.message.reply_photo(photo=image_url, caption=text, reply_markup=InlineKeyboardMarkup(buttons), parse_mode="Markdown")

    elif query.data == "buy_now":
        await query.message.reply_photo(
            photo="https://res.cloudinary.com/dvbgfwsxc/image/upload/v1753605975/WhatsApp_Image_2025-07-27_at_14.15.49_8c2ac440_lr6xbq.jpg",  # 🔁 Replace with your actual image URL
            caption="💳 *Please complete your payment To our above QR Via Upi , Phonepe, Google pay, Paytm etc...*\n\nOnce done,send the Screenshot or UTR number to below bot Id ,\n\n Automatially we will verify and you Get private course channel Link.\n\n👉 [@your_livegram_bot](https://t.me/PaymentGateway_Aneel_Robot)",
            parse_mode="Markdown"
        )


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
