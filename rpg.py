import os
import sqlite3


DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")


conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = "SELECT COUNT(*) FROM armory_item;"
curs.execute(query)
curs.execute(query).fetchall()


# - How many total Characters are there?
t1 = "Total characters are: "
q1 = """SELECT
            count(distinct character_id)
        FROM
            charactercreator_character;"""
r1 = curs.execute(q1).fetchall()
print(t1, r1[0])


#  - How many of each specific subclass?
# CLERICS:
t2 = "Total number of clerics are: "
q2 = """SELECT
            count(distinct character_ptr_id)
        FROM
            charactercreator_cleric;"""
r2 = curs.execute(q2).fetchall()
print(t2, r2[0])


# FIGHTERS:
t3 = "Total number of fighters are: "
q3 = """SELECT
            count(distinct character_ptr_id)
        FROM
            charactercreator_fighter;"""
r3 = curs.execute(q3).fetchall()
print(t3, r3[0])

# MAGE:
t4 = "Total number of mages are: "
q4 = """SELECT
            count(distinct character_ptr_id)
        FROM
            charactercreator_mage;"""
r4 = curs.execute(q4).fetchall()
print(t4, r4[0])

# NECROMANCER:
t5 = "Total number of necromancers are: "
q5 = """SELECT
            count(distinct mage_ptr_id)
        FROM
            charactercreator_necromancer;"""
r5 = curs.execute(q5).fetchall()
print(t5, r5[0])


# THIEF:
t6 = "Total number of thieves are: "
q6 = """SELECT
            count(distinct character_ptr_id)
        FROM
            charactercreator_thief;"""
r6 = curs.execute(q6).fetchall()
print(t6, r6[0])


# - How many total Items?
t7 = "Total number of different items characters can carry are: "
q7 = """SELECT
            count(distinct item_id)
        FROM
            armory_item;"""
r7 = curs.execute(q7).fetchall()
print(t7, r7[0])


# - How many of the Items are weapons? How many are not?
t8 = "Total number of different weapons available are: "
q8 = """SELECT
            count(distinct item_ptr_id)
        FROM
            armory_weapon;"""
r8 = curs.execute(q8).fetchall()
print(t8, r8[0])


# - How many Items does each character have? (Return first 20 rows)
q9 = """
select c.name 
	,count(ci.item_id)
FROM
	charactercreator_character_inventory ci 
LEFT JOIN charactercreator_character c ON 
	c.character_id = ci.character_id
group by 
	ci.character_id
LIMIT 20;"""
r9 = curs.execute(q9).fetchall()
print(r9)


# - How many Weapons does each character have? (Return first 20 rows)
q10 = """
select c.name 
	,count(ci.item_id)
FROM
	charactercreator_character_inventory ci 
LEFT JOIN charactercreator_character c ON 
	c.character_id = ci.character_id
WHERE
	ci.item_id > 137
group by 
	ci.character_id
LIMIT 20;"""
r10 = curs.execute(q10).fetchall()
print(r10)

# - On average, how many Items does each Character have?
t11 = "The average number of items each character carries is: "
q11 = """
SELECT
    count(DISTINCT item_id)
FROM
    charactercreator_character_inventory
Group BY
    character_id;"""
r11 = curs.execute(q11).fetchall()
print(t11, r11[0])

# - On average, how many Weapons does each character have?
t12 = "The average number of weapons each character carries is: "
q12 = """
SELECT
    count(DISTINCT item_id)
FROM
    charactercreator_character_inventory
WHERE
    item_id > 137
Group BY
    character_id;"""
r12 = curs.execute(q12).fetchall()
print(t12, r12[0])