from models import Cars

class Create:   
    def create( self):
        self.brand = str(input('Впишите марку: '))
        self.model = str(input('Впишите модель: '))
        self.year = int(input('Впишите год выпуска: '))
        self.engine_volume = round(float(input('Впишите объем двигателя: ')), 1)
        self.color = str(input('Впишите цвет: '))
        self.body_type = str(input('Впишите тип кузова: '))
        self.mileage = int(input('Впишите пробег: '))
        self.price = round(float(input('Впишите цену: ')), 2)
    def listing():      
        print('\n'.join((
    f"ID - {['id']}",
                f"Марка - {['brand']}",
    f"Модель - {['model']}",
    f"Год выпуска- {['year']}",
    f"Обьем двигателя - {['engine_volume']}",
    f"Цвет - {['color']}",
    f"Тип кузова - {['body_type']}",
    f"Пробег - {['mileage']}",
    f"Цена - {['price']}\n",
    )))
    def retrieve():
        num = int(input('Введите ID автомобиля для просмотра: '))
    list_ = []   
    for i in Cars.info:
        list_.append(i['id'])
    if num in list_:
        for i in Cars.info:            
    if num == i['id']:
        print('\n'.join((
    f"ID - {i['id']}",
    f"Марка - {i['brand']}",
    f"Модель - {i['model']}",
    f"Год выпуска- {i['year']}",
    f"Обьем двигателя - {i['engine_volume']}",
    f"Цвет - {i['color']}",
    f"Тип кузова - {i['body_type']}",
    f"Пробег - {i['mileage']}",
    f"Цена - {i['price']}\n",
    )))
    else: 
        raise Exception('Нет такого ID в базе данных')
    def update():
        num_choice_auto = int(input('Введите ID автомобиля для изменения параметров: '))
        list_ = []
        for i in Cars.info:
            list_.append(i['id'])
    if num_choice_auto in list_:
            num_choice_param = int(input('Для того, чтобы изменит параметры описания выберите цифру:\nМарка - 1\nМодель - 2\nГод выпуска - 3\nОбъем двигателя - 4\nЦвет - 5\nТип кузова - 6\nПробег - 7\nЦена - 8\n'))
        print(num_choice_param == 1)
    if num_choice_param in [1, 2, 3, 4, 5, 6, 7, 8]:
        if num_choice_param == 1:
        Cars.info[num_choice_auto]['brand'] = str(input('Впишите марку: '))
    elif num_choice_param == 2:
        Cars.info[num_choice_auto]['model'] = str(input('Впишите модель: '))
    elif num_choice_param == 3:
        Cars.info[num_choice_auto]['year'] = int(input('Впишите год выпуска: '))
    elif num_choice_param == 4:
        Cars.info[num_choice_auto]['engine_volume'] = round(float(input('Впишите объем двигателя: ')), 1)
    elif num_choice_param == 5:
        Cars.info[num_choice_auto]['color'] =  str(input('Впишите цвет: '))
    elif num_choice_param == 6:
        Cars.info[num_choice_auto]['body_type'] = str(input('Впишите тип кузова: '))
    elif num_choice_param == 7:
        Cars.info[num_choice_auto]['mileage'] = int(input('Впишите пробег: '))
    elif num_choice_param == 8:
        Cars.info[num_choice_auto]['price'] = round(float(input('Впишите цену: ')), 2)
    else:
        raise Exception('Команды под таким номером не существует')
else:
    raise Exception('Нет такого ID в базе данных')
    def delete():
        num = int(input('Введите ID автомобиля для удаления: '))
        list_ = []
    for i in Cars.info:
        list_.append(i['id'])
    if num in list_:
        Cars.info.pop(num)
    else: 
          raise Exception('Нет такого ID в базе данных')