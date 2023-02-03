
from telegram.ext import Updater, CommandHandler
from bot_command import hi_command
from bot_command import calc_command

updater = Updater('Token')


updater.dispatcher.add_handler(CommandHandler('hi', hi_command))

updater.dispatcher.add_handler(CommandHandler('calc', calc_command))



print('server start')
updater.start_polling()
updater.idle()


