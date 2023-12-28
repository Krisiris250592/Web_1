from abc import ABC, abstractmethod


class BookInterface(ABC):
    @abstractmethod
    def save_to_file(self,file):
        pass

    def load_from_file(self,file):
        pass

    def show_all(self):
        pass

