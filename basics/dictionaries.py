
"==================Словари====================="
# Словарь (dict) - изменяемый, итерирумый, неиндексируемый, неупорядоченный тип данных, в котором значения хранятся в парах (ключ : значение)

dict_ = {"a":"hello", "b":2, "c":3}
print(dict_["a"]) # Hello

# ключами в словаре могут являться все неизменяемые типы данных
# значениями в словаре могут являться любые типы данных
# ключи должны быть уникальными

dict_ = {
    1:"hello", 
    4.5: {"a":5},
    # {"s":5}: 44  # TypeError: unhashable type: 'dict' 
}

print(dict_[4.5]) # {"a":5}
print(dict_[4.5]["a"]) # 5
# print(dict_["a"]) # KeyError: "a"

dict_ = {"a":2, "a":3, "a":4}
print(dict_) # {"a":4}
dict_["a"] = 5 
print(dict_) # {"a":5}



"================Методы словаря=================="
dict_.clear() # чистит словарь
print(dict_) # {}

dict_ = dict.fromkeys([1,2,4]) 
print(dict_) # {1:None, 2:None, 4:None}

dict_ = dict.fromkeys([1,2,4], "hello") 
print(dict_) # {1:"hello", 2:"hello", 4:"hello"}

dict_ = {"a":1, "b":2}
dict_["a"] # 1
dict_["c"] # KeyError

# метод get нужен только для получения значений
dict_.get("a") # 1
dict_.get("c") # None
dict_.get("c", 5) # 5
dict_.get("a", 5) # 1

dict_.keys() # dict_keys(['a', 'b'])
dict_.values() # dict_values([1, 2])
dict_.items() # dict_items([('a', 1), ('b', 2)])

dict1 = {1:"a", 2:"b", 3:"c"}
dict2 = {3:"d", 4:"e"}
dict1.update(dict2)
print(dict1) # {1:"a", 2:"b", 3:"d", 4:"e"}
print(dict2) # {3:"d", 4:"e"}


number = '23



dict_ = {}
dict_1 = dict()
print(type(dict_))
print






























