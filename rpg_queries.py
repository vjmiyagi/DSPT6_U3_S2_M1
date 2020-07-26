import os
import sqlite3


DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")


connection = sqlite3.connect(DB_FILEPATH)


cursor = connection.cursor()


# How many total Characters are there?
t1 = "Total characters are: "
q1 = "SELECT COUNT(character_id) FROM charactercreator_character;"
r1 = cursor.execute(q1).fetchall()
print(t1, r1[0])

# How many of each specific subclass?
# CLERICS?
t2 = "Total number of Clerics: "
q2 = "SELECT COUNT(character_ptr_id) FROM charactercreator_cleric;"
r2 = cursor.execute(q2).fetchall()
print(t2, r2[0])


# FIGHTERS
t3 = "Total number of Fighters: "
q3 = "SELECT COUNT(character_ptr_id) FROM charactercreator_fighter;"
r3 = cursor.execute(q3).fetchall()
print(t3, r3[0])


# MAGE
t4 = "Total number of Mages: "
q4 = "SELECT COUNT(character_ptr_id) FROM charactercreator_mage;"
r4 = cursor.execute(q4).fetchall()
print(t4, r4[0])


# NECROMANCER
t5 = "Total number of Necromancers: "
q5 = "SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer;"
r5 = cursor.execute(q5).fetchall()
print(t5, r5[0])


# THIEF
t6 = "Total number of Thieves: "
q6 = "SELECT COUNT(character_ptr_id) FROM charactercreator_thief;"
r6 = cursor.execute(q6).fetchall()
print(t6, r6[0])
print()


# How many total Items?
t7 = "Total different items: "
q7 = "SELECT COUNT(item_id) FROM armory_item;"
r7 = cursor.execute(q7).fetchall()
print(t7, r7[0])


# How many items are weapons?
t8 = "Total different weapons: "
q8 = "SELECT COUNT(item_ptr_id) FROM armory_weapon;"
r8 = cursor.execute(q8).fetchall()
print(t8, r8[0])


# How many Items does each character have? (Return first 20 rows)
t9 = "Items carried by each character: "
q9 = """
    SELECT name as Name, COUNT(item_id) as Items
    FROM charactercreator_character c, charactercreator_character_inventory i
    WHERE c.character_id = i.character_id
    GROUP BY c.character_id;"""
r9 = cursor.execute(q9).fetchmany(20)
print(t9, r9)

# How many Weapons does each character have? (Return first 20 rows)

# TO DO

# On Average how many items does each Character have?


query = """
SELECT
    AVG(items) AS items
    ,AVG(weapons) AS weapons
FROM (
    SELECT
        c.character_id
        ,COUNT(i.item_id) AS items
        ,COUNT(w.item_ptr_id) AS weapons
    FROM charactercreator_character c
    LEFT JOIN charactercreator_character_inventory i ON
        i.character_id = c.character_id
    LEFT JOIN armory_weapon w ON
        w.item_ptr_id == i.item_id
    GROUP BY c.character_id
)
"""
results = cursor.execute(query).fetchmany(20)
print("RESULTS: ")
print(results)
