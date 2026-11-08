import sqlite3

def main():
    conn = sqlite3.connect("pets.db")
    cur = conn.cursor()

    while True:
        text = input("Enter a person's ID number (-1 to exit): ").strip()

        try:

            person_id = int(text)
        except ValueError:
            print("Error: please enter a whole number.")
            continue

        if person_id == -1:
            break

        cur.execute(
            "SELECT first_name, last_name, age FROM person WHERE id = ?",
            (person_id,),
        )
        person = cur.fetchone()

        if person is None:
            print("Error: no person with that ID exists.")
            continue

        first_name, last_name, age = person
        print(f"{first_name} {last_name}, {age} years old")

        cur.execute(
            """
            SELECT pet.name, pet.breed, pet.age, pet.dead
            FROM pet
            JOIN person_pet ON pet.id = person_pet.pet_id
            WHERE person_pet.person_id = ?
            """,
            (person_id,),
        )
        for pet_name, breed, pet_age, dead in cur.fetchall():
            # dead = 1 means the pet has died, so use past tense; otherwise present
            verb1 = "owned" if dead else "owns"
            verb2 = "was" if dead else "is"
            print(f"{first_name} {last_name} {verb1} {pet_name}, a {breed}, that {verb2} {pet_age} years old")

    conn.close()

if __name__ == "__main__":
    print("Running query_pets.py")
    main()
