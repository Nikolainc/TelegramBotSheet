from telegram import Update, Message
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import help_command, get_command, add_command, del_command, getall_command, start_command

app = ApplicationBuilder().token("5670502593:AAHToD7GA3dMoySLZIM0wNo8ar85jZkOojg").build()
print("server start")

app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("get", get_command))
app.add_handler(CommandHandler("getall", getall_command))
app.add_handler(CommandHandler("add", add_command))
app.add_handler(CommandHandler("del", del_command))

app.run_polling()