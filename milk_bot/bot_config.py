from logging import getLogger

from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardMarkup

from config.settings import TG_TOKEN
from milk_bot.buttons import (
    AddMeButton,
    IBoughtButton,
    WhoIsNextButton,
    MilkIsRunningOutButton
)
from milk_bot.models import MilkBuyer

logger = getLogger(__name__)

# Telegram bot
tb = TeleBot(TG_TOKEN)

# Buttons
add_me_button = AddMeButton()
i_bought_button = IBoughtButton()
who_is_next_button = WhoIsNextButton()
milk_is_running_out_button = MilkIsRunningOutButton()

# Keyboards
buyer_markup = ReplyKeyboardMarkup(row_width=1)
buyer_markup.add(i_bought_button.keyboard_button,
                 who_is_next_button.keyboard_button,
                 milk_is_running_out_button.keyboard_button)

not_buyer_markup = ReplyKeyboardMarkup(row_width=1)
not_buyer_markup.add(add_me_button.keyboard_button)


@tb.message_handler(content_types=["text"])
def send_welcome(message: Message):
    buyer = MilkBuyer.objects.filter(id=message.from_user.id).first()
    default_answer = "Что случилось?"

    if message.text == add_me_button.text:
        buyer_answer = add_me_button.get_an_answer(message)
        tb.send_message(buyer_answer.buyer_id, buyer_answer.message, reply_markup=buyer_markup)
        return

    if not buyer:
        tb.send_message(message.from_user.id, default_answer, reply_markup=not_buyer_markup)
        return

    if message.text == i_bought_button.text:
        buyer_answer, next_buyer_answer = i_bought_button.get_an_answer(message)
        if not next_buyer_answer:
            tb.send_message(buyer_answer.buyer_id, buyer_answer.message, reply_markup=buyer_markup)
            return

        tb.send_message(buyer_answer.buyer_id, buyer_answer.message, reply_markup=buyer_markup)
        tb.send_message(next_buyer_answer.buyer_id, next_buyer_answer.message, reply_markup=buyer_markup)
        return

    if message.text == who_is_next_button.text:
        buyer_answer = who_is_next_button.get_an_answer(message)
        tb.send_message(buyer_answer.buyer_id, buyer_answer.message, reply_markup=buyer_markup)
        return

    if message.text == milk_is_running_out_button.text:
        sender_answer, buyer_answer = milk_is_running_out_button.get_an_answer(message)
        tb.send_message(sender_answer.buyer_id, sender_answer.message, reply_markup=buyer_markup)
        tb.send_message(buyer_answer.buyer_id, buyer_answer.message, reply_markup=buyer_markup)
        return

    if message.text == "leavemealone":
        buyer = MilkBuyer.objects.get(id=message.from_user.id)
        MilkBuyer.decrease_positions(from_position=buyer.position)
        buyer.delete()
        tb.send_message(message.from_user.id, "👋", reply_markup=not_buyer_markup)
        return

    tb.send_message(message.from_user.id, default_answer, reply_markup=buyer_markup)
