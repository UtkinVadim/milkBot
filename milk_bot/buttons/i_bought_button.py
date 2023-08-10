from telebot.types import KeyboardButton, Message

from milk_bot.models import MilkBuyer
from milk_bot.dataclasses import BuyerAnswer
from milk_bot.buttons.base_button import BaseButton


class IBoughtButton(BaseButton):
    def __init__(self):
        self.text = "Я купил молоко!"
        self.keyboard_button = KeyboardButton(self.text)

    def get_an_answer(self, message: Message) -> (BuyerAnswer, BuyerAnswer):
        buyer = MilkBuyer.objects.first()

        if message.from_user.id != buyer.id:
            return BuyerAnswer(buyer_id=message.from_user.id, message="Зачем🤔"), None

        buyer_answer = BuyerAnswer(buyer_id=buyer.id,
                                   message=f"Спасибо, {buyer.first_name}!🫶")

        buyer.position = MilkBuyer.objects.last().position + 1
        buyer.save()

        buyers = MilkBuyer.objects.all()
        for buyer in buyers:
            buyer.position -= 1
        MilkBuyer.objects.bulk_update(buyers, ["position"])

        next_buyer = MilkBuyer.objects.all().first()
        next_buyer_answer = BuyerAnswer(buyer_id=next_buyer.id,
                                        message="Твоя очередь покупать молоко🫵")

        return buyer_answer, next_buyer_answer
