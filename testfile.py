
result = cur.execute("""SELECT title FROM Films WHERE year >= 1997 AND genre IN (SELECT id FROM genres WHERE title IN
            ('музыка', 'анимация'))""").fetchall()
result = cur.execute("""SELECT * FROM films WHERE year >= 1997 AND genre IN (SELECT id FROM genres 
                        WHERE title IN ('музыка', 'анимация'))""").fetchall()

# Вывод результатов на экран
for elem in result:
    print(elem[0])

con.close()