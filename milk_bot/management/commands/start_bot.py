from django.core.management.base import BaseCommand

from milk_bot.bot_config import tb as bot


class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        bot.infinity_polling()
