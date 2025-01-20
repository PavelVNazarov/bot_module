# bot/bot.py
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from django.shortcuts import render
from .models import User, Trade

def admin_dashboard(request):
    users = User.objects.all()
    trades = Trade.objects.all()
    return render(request, 'bot/admin_dashboard.html', {'users': users, 'trades': trades})
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я Ваш бот.')

def view_users(update: Update, context: CallbackContext) -> None:
    users = User.objects.all()
    user_list = "\n".join([user.username for user in users])
    update.message.reply_text(f'Пользователи:\n{user_list}')

def main():
    updater = Updater("YOUR_TOKEN", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("view_users", view_users))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()