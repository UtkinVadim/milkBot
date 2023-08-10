from abc import ABC, abstractmethod

from mailbox import Message


class BaseButton(ABC):

    @abstractmethod
    def get_an_answer(self, message: Message):
        pass
