
class Cars():
    
    def __init__(self, marks, models, yearm, obiem_mashiny, color, type_of_kyzof, probeg, price):
        self.marks = marks
        self.models = models
        self.yearm = yearm
        self.obiem_mashiny = obiem_mashiny
        self.color = color
        self.type_of_kyzof = type_of_kyzof
        self.probeg = probeg
        self.price = price

    def get_info(self):
        
        return '\n'.join((
            f"Марка - {self.marks}",
            f"Модель - {self.models}",
            
            f"Год  - {self.yearm}",
            f"Обьем двигателя  - {self.obiem_mashiny}",
            f"Цвет  - {self.color}",
            f"Тип кузова  - {self.type_of_kyzof}",
            f"Пробег  - {self.probeg}",
            f"Цена  - {self.price}",
        ))
     

Mersedes = Cars('Mersedes','W 124', 2005, 3.2, 'черный', 'седан', 0.0, 300000)



print(Mersedes.get_info())





