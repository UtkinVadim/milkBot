from telebot.types import KeyboardButton, Message

from milk_bot.models import MilkBuyer
from milk_bot.dataclasses import BuyerAnswer
from milk_bot.buttons.base_button import BaseButton


class WhoIsNextButton(BaseButton):
    def __init__(self):
        self.text = "Сейчас кто покупает?"
        self.keyboard_button = KeyboardButton(self.text)

    def get_an_answer(self, message: Message) -> BuyerAnswer:
        buyer = MilkBuyer.objects.first()
        return BuyerAnswer(buyer_id=message.from_user.id,
                           message=f"Сейчас {buyer.full_name} покупает🥛")
