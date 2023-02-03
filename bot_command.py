from telegram import Update
from telegram.ext import CallbackContext
from spy import *


def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')

def calc_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    operation = str(items[2])
    y = int(items[3])

    if operation == '+':
        update.message.reply_text(f'{x} + {y} = {x+y}')
        print('Сложение')
    elif operation == '-':
        update.message.reply_text(f'{x} - {y} = {x-y}')
        print('Вычитание')
    elif operation == '/':
        update.message.reply_text(f'{x} / {y} = {x/y}')
        print('Деление')
    elif operation == '*':
        update.message.reply_text(f'{x} * {y} = {x*y}')
        print('Умножение')
    else:
        print('Неизвестная операция') 


    # update.message.reply_text(f'{x} + {y} = {x+y}')