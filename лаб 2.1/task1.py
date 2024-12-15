# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Phone:
    def __init__(self, used_memory_capacity: float, photo_memory_capacity: float):

        self.used_memory_capacity = 118
        self.photo_memory_capacity = 2

        if not isinstance(used_memory_capacity,(int,float)):
                raise TypeError("Объем используемой памяти должен быть int/ float")

        if not isinstance(photo_memory_capacity,(int,float)):
                raise TypeError("Объем памяти, занимаемый фото, должен быть int/ float")

        if used_memory_capacity <= 0:
                raise ValueError("Объем заполненной памяти не может быть равным нулю/ меньше нуля")

        if photo_memory_capacity < 0:
                raise ValueError("Объем памяти, занимаемый фото, не может быть меньше нуля")

    def upload_photo(self, photo, phone_memory) -> float:
        ...
    def delete_photo(self, photo, phone_memory) -> float:
        ...
        #:raise ValueError: Если объем фото превышает объем заполненной памяти


class Cat:
    def __init__(self, color: str, weight: float, amount_of_feed: float):
        self.color = 'grey'
        self. weight = 2000
        self.amount_of_feed = 200

        if not isinstance(color, str):
                raise TypeError("Цвет кота должен быть str")

        if not isinstance(weight,(int,float)):
                raise TypeError("Вес кота должен быть int/ float")

        if not isinstance(amount_of_feed ,(int,float)):
                raise TypeError("Вес корма кота должен быть int/ float")

        if weight <= 0:
                raise ValueError("Котик не может весить ноль грамм/ меньше нуля")

        if amount_of_feed <= 0:
                raise ValueError("Котик не может остаться голодным")

    def weight_feed_cat(self, animal_weight, weight_feed)->float:
        ...

    def increase_feed_twice(self, weight_feed, degree=2)->float:
        ...

class Hair:
    def __init__(self, color: str, new_color:str, lenght: float, new_lenght: float):
        self.color = 'red'
        self.new_color = 'black'
        self.lenght = 20
        self.new_lenght = 5

        if lenght <= 0:
                raise ValueError("Длина волос не может быть равна нулю или меньше него")

        if new_lenght < 0:
                raise ValueError("Длина отрезанных волос не может быть меньше нуля")

        if not isinstance(lenght,(int,float)):
                raise TypeError("Длина волос должна быть int/ float")

        if not isinstance(new_lenght,(int,float)):
                raise TypeError("Длина отрезанных волос должна быть int/ float")

        if not isinstance(color, str):
                raise TypeError("Цвет волос должен быть str")

        if not isinstance(new_color, str):
                raise TypeError("Цвет волос должен быть str")

    def repaint(self, color_one, color_two) -> str:
        ...

    def cut_off(self,lenght_of_hair, lenght_to_cut) -> float:
        ...
        #:raise ValueError: Если длина отрезанных волос больше изначальной
if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
