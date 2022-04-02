import sqlite3
conn = sqlite3.connect('dz.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')

sp = [ 1, 5, 'asd', 8, 'nbv' ]
for i in sp:
    if isinstance(i, int):
        if i // 2 == 0:
            cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?, )''', (i, ))
            conn.commit()
        else:
            cursor.execute('''INSERT INTO tab_1(col_1) VALUES ('нечётное',)''')
            conn.commit()
    elif isinstance(i, str):
        cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?,)''', (i,))
        conn.commit()
        cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?,)''', (len(i),))
        conn.commit()
#cursor.execute('''INSERT INTO tab_1(col_1)(?,)''')
cursor.execute('''SELECT*FROM tab_1''')
rezult1 = cursor.fetchall()
cursor.execute('''SELECT*FROM tab_2''')
rezult2 = cursor.fetchall()
print(rezult1)
print(rezult2)

ind1 =1
ind2 =1

if len(rezult2) > 5:
    cursor.execute('''DELETE tab_1 WHERE id=ind1''')
    conn.commit()
    ind1 +=1
else:
    cursor.execute('''UPDATE tab_1 SET col_1 = 'hello' WHERE id=ind2''')
    conn.commit()
    ind2 += 1

cursor.execute('''SELECT*FROM tab_1''')
rezult1 = cursor.fetchall()
cursor.execute('''SELECT*FROM tab_2''')
rezult2 = cursor.fetchall()
print(rezult1)
print(rezult2)