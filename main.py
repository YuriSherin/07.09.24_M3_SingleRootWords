def  single_root_words(root_word, *other_words):
    same_words = []         # Объявим пустой список, куда будет помещен результат
    for s in other_words:   # Цикл по всем элементам кортежа
        # Если root_word входит в один из элементов кортежа или элемент кортежа входит в root_word
        if s.lower() in root_word.lower() or root_word.lower() in s.lower():
            same_words.append(s)    # Добавляем элемент в результирующий список
    return same_words       # Возвращаем результат

# Вызов функции с различными параметрами
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

# ======================== Test ========================
# ['richiest', 'orichalcum', 'richies']
# ['Able', 'Disable']