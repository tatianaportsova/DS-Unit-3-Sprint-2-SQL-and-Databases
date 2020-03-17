# module1-introduction-to-sql/assignment/rpg_queries.py

import os
import sqlite3

# construct a path to wherever your database exists
DB_FILEPATH  = os.path.join(os.path.dirname(__file__),"..", "rpg_db.sqlite3")
#DB_FILEPATH = 'rpg_db.sqlite3'

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

# query = 'SELECT COUNT(*) FROM armory_item;'
# How many total Characters are there? (302)
query = """
SELECT
  count (*) as characters_count
FROM charactercreator_character
"""

# result = cursor.execute(query)
# print("RESULT", result) #> returns cursorobject w/o results (need to fetch the results)
result = cursor.execute(query).fetchall()
print("RESULT", result)
print("How many total Characters are there?")

for row in result:
    print(type(row))
    print(row["characters_count"])
    print("______")

# How many total Items? (174)
query2 = """
SELECT
  count (*) as items_count
FROM armory_item
"""

result2 = cursor.execute(query2).fetchall()
print("RESULT 2", result2)
print("How many total Items?")

for row in result2:
    print(row["items_count"])
    print("______")

# How many Items does each character have? (Return first 20 rows)
query3 = """
SELECT 
  charactercreator_character.character_id
  ,charactercreator_character.name as Character_Name
  ,count(distinct charactercreator_character_inventory.item_id) as Item_Count
FROM charactercreator_character
JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
GROUP BY charactercreator_character.character_id
LIMIT 20
"""
result3 = cursor.execute(query3).fetchall()
print("How many Items does each character have? (Return first 20 rows)")

for row in result3:
    print(row["Character_Name"])
    print(row["Item_count"])
    print("______")

# How many Characters of each specific subclass?
query4 = """
SELECT
  count (*) as cleric_count
  ,count (*) as fighter_count
  ,count (*) as mage_count
  ,count (*) as necromancer_count
  ,count (*) as thief_count
FROM 
  charactercreator_cleric
  ,charactercreator_fighter
  ,charactercreator_mage
  ,charactercreator_necromancer
  ,charactercreator_thief
"""
result4 = cursor.execute(query4).fetchall()
print("How many Characters of each specific subclass?")

for row in result4:
    print("Cleric:",row["cleric_count"])
    print("Fighter:",row["fighter_count"])
    print("Mage:",row["mage_count"])
    print("Necromancer:",row["necromancer_count"])
    print("Thief:",row["thief_count"])
    print("______")