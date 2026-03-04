import csv
import random
import os


roles = ["Batsman", "Bowler", "Allrounder", "Wicketkeeper"]

indian_first_names = ["Virat", "Rohit", "Surya", "Hardik", "Rishabh",
                      "KL", "Shubman", "Sanju", "Ishan", "Ravindra",
                     "Dhoni","Sachin","sehwag","Gambhir","Yuvaraj"]

overseas_first_names = ["David", "Steve", "Joe", "Ben", "Glenn",
                        "Jos", "Mitchell", "Kane", "Andre", "Travis",
                       "Henrich","Jhon","Rasidh","Kusanka","Adam"]

indian_last_names = ["Sharma", "Kohli", "Rahul", "Gill", "Pandya",
              "Verma","Kathik","iyer","Sumbet","Rathan","Reddy"]

overseas_last_names = ["warner","Williamson","Roy","Russel","Devillers","Khan","Philips",
                       "Malinga"]

# -------------- CREATE FILE --------------

os.makedirs("data", exist_ok=True)

with open("data/players.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # Header
    writer.writerow(["Name", "Country", "Role", "Base_Price", "Rating"])

    # 100 Indian Players
    for i in range(100):
        name = random.choice(indian_first_names) + " " + random.choice(indian_last_names)
        country = "India"
        role = random.choice(roles)
        base_price = random.randint(10, 80)
        rating = random.randint(1, 100)

        writer.writerow([name, country, role, base_price, rating])

    # 50 Overseas Players
    for i in range(50):
        name = random.choice(overseas_first_names) + " " + random.choice(overseas_last_names)
        country = "Overseas"
        role = random.choice(roles)
        base_price = random.randint(10, 80)
        rating = random.randint(1, 100)

        writer.writerow([name, country, role, base_price, rating])

print("150 Players generated successfully.")