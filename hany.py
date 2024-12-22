
```
import random
import telegram
from telegram.ext import Updater, CommandHandler

توكن البوت
TOKEN = '8031140362:AAErrdZfWmSZpB-_Fvynx5g9OMw3Bg5zuHA'

إنشاء البوت
bot = telegram.Bot(token=TOKEN)

تعريف أوامر البوت
def start(update, context):
 context.bot.send_message(chat_id=(link unavailable), text="مرحباً! استخدم /أرقام لتحصل على أرقام وهمية.")

def ارقام(update, context):
 أرقام_وهمية = [random.randint(0, 9) for _ in range(10)]
 context.bot.send_message(chat_id=(link unavailable), text=' '.join(map(str, أرقام_وهمية)))

ربط البوت بالتلجرام
updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("أرقام", ارقام))

updater.start_polling()
updater.idle()
```