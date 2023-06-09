import telebot
from telebot import types
import sys
import psycopg2

bot = telebot.TeleBot('6270732664:AAHZmJWbDy18m565LN-yI__bROUT0RoXOzI')

conn = psycopg2.connect(dbname='hive_db', user='postgres', password='12345678', host='localhost') #для сервака

cursor = conn.cursor()

postgreSQL_select_Query = "select * from hive_db"

cursor.execute(postgreSQL_select_Query)
hive_records = cursor.fetchall()

cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")


@bot.message_handler(commands=['start'])
def start(message):
   bot.send_message(message.chat.id, 'Бот запущен')


@bot.message_handler(commands=['stop'])
def stop():
   sys.exit(0)


@bot.message_handler(commands=['info'])
def info(message):
   
   postgreSQL_select_Query = "select * from hive_db"
   cursor.execute(postgreSQL_select_Query)
   hive_records = cursor.fetchall()

   time = [row[1] for row in hive_records]
   date = [row[2] for row in hive_records]
   humid = [row[3] for row in hive_records]
   temp = [row[4] for row in hive_records]
   weight = [row[5] for row in hive_records]

   bot.send_message(message.chat.id, f"Текущая дата: {date[-1]}")
   bot.send_message(message.chat.id, f"Текущее время: {time[-1]}")
   bot.send_message(message.chat.id, f"Влажность в улье: {humid[-1]}%")
   bot.send_message(message.chat.id, f"Температура в улье: {temp[-1]} градуса")
   bot.send_message(message.chat.id, f"Вес улья: {weight[-1]}гр")


bot.polling(none_stop=True)
