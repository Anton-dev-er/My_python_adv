from telebot import TeleBot
from Dz_15.table_for_bot import UsersData, db

from envparse import Env

env = Env()
TOKEN = env.str("TOKEN")
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['reg'])
def save_data(message):
    users_list = [i.nickname for i in UsersData.query.all()]
    if message.chat.username not in users_list:
        user = UsersData(nickname=message.chat.username, chat_id=message.chat.id)
        db.session.add(user)
        db.session.commit()
        bot.send_message(chat_id=message.chat.id, text="Succesfully registered")
    else:
        bot.send_message(chat_id=message.chat.id, text="You are already registered")


if __name__ == "__main__":
    bot.polling()
