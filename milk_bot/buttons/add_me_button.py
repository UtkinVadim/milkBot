from telebot.types import KeyboardButton, Message

from milk_bot.models import MilkBuyer
from milk_bot.dataclasses import BuyerAnswer
from milk_bot.buttons.base_button import BaseButton


class AddMeButton(BaseButton):
    def __init__(self):
        self.text = "Я тоже хочу покупать молоко."
        self.keyboard_button = KeyboardButton(self.text)

    def get_an_answer(self, message: Message) -> BuyerAnswer:
        buyer = MilkBuyer.objects.filter(id=message.from_user.id).first()
        answer = "Ты и так в очереди🫣"

        if not buyer:
            answer = "Хорошо👍"
            buyer = MilkBuyer.add_new_buyer(message.from_user)

        return BuyerAnswer(buyer_id=buyer.id, message=answer)
