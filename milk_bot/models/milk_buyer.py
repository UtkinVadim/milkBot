from __future__ import annotations

from django.db import models
from telebot.types import User


class MilkBuyer(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    position = models.PositiveSmallIntegerField()

    @property
    def full_name(self) -> str:
        full_name = ""
        full_name += self.first_name + " " if self.first_name else ""
        full_name += self.last_name if self.last_name else ""
        return full_name

    @classmethod
    def add_new_buyer(cls, tg_user: User) -> MilkBuyer.objects:
        last_buyer = cls.objects.all().last()

        position = 0 if not last_buyer else last_buyer.position + 1

        return cls.objects.create(id=tg_user.id,
                                  first_name=tg_user.first_name,
                                  last_name=tg_user.last_name,
                                  position=position)

    @classmethod
    def decrease_positions(cls, from_position: int) -> None:
        buyers = cls.objects.filter(position__gt=from_position)
        for buyer in buyers:
            buyer.position -= 1
        cls.objects.bulk_update(buyers, ["position"])

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ["position"]
