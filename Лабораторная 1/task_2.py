# TODO Найдите количество книг, которое можно разместить на дискете
Volume = 1.44
Page = 100
Line = 50
Symbol = 25
Bytes = 4
Volume *= (1024 ** 2)
Bytes *= (Page * Line * Symbol)
print("Количество книг, помещающихся на дискету:", round(Volume // Bytes))
