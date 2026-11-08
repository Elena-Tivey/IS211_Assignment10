import sqlite3
 
# Connect to the existing database in pets.db
conn = sqlite3.connect("pets.db")
cur = conn.cursor()
 
# Person: (id, first_name, last_name, age)
cur.execute("INSERT INTO person VALUES (1, 'James', 'Smith', 41)")
cur.execute("INSERT INTO person VALUES (2, 'Diana', 'Greene', 23)")
cur.execute("INSERT INTO person VALUES (3, 'Sara', 'White', 27)")
cur.execute("INSERT INTO person VALUES (4, 'William', 'Gibson', 23)")
 
# Pet: (id, name, breed, age, dead)
cur.execute("INSERT INTO pet VALUES (1, 'Rusty', 'Dalmation', 4, 1)")
cur.execute("INSERT INTO pet VALUES (2, 'Bella', 'Alaskan Malamute', 3, 0)")
cur.execute("INSERT INTO pet VALUES (3, 'Max', 'Cocker Spaniel', 1, 0)")
cur.execute("INSERT INTO pet VALUES (4, 'Rocky', 'Beagle', 7, 0)")
cur.execute("INSERT INTO pet VALUES (5, 'Rufus', 'Cocker Spaniel', 1, 0)")
cur.execute("INSERT INTO pet VALUES (6, 'Spot', 'Bloodhound', 2, 1)")
 
# Person_Pet: (person_id, pet_id)
cur.execute("INSERT INTO person_pet VALUES (1, 1)")
cur.execute("INSERT INTO person_pet VALUES (1, 2)")
cur.execute("INSERT INTO person_pet VALUES (2, 3)")
cur.execute("INSERT INTO person_pet VALUES (2, 4)")
cur.execute("INSERT INTO person_pet VALUES (3, 5)")
cur.execute("INSERT INTO person_pet VALUES (4, 6)")
 
conn.commit()
conn.close()
print("Data loaded into pets.db")

if __name__ == "__main__":
    print("Running load_pets.py") 
   
    