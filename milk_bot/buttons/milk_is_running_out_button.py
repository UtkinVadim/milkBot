from telebot.types import KeyboardButton, Message

from milk_bot.models import MilkBuyer
from milk_bot.dataclasses import BuyerAnswer
from milk_bot.buttons.base_button import BaseButton


class MilkIsRunningOutButton(BaseButton):
    def __init__(self):
        self.text = "Молоко кончается!"
        self.keyboard_button = KeyboardButton(self.text)

    def get_an_answer(self, message: Message) -> (BuyerAnswer, BuyerAnswer):
        sender_answer = BuyerAnswer(buyer_id=message.from_user.id,
                                    message="Я сообщил✉️")

        buyer = MilkBuyer.objects.first()
        buyer_answer = BuyerAnswer(buyer_id=buyer.id,
                                   message=f"{buyer.first_name}, купи молока😢")

        return sender_answer, buyer_answer
