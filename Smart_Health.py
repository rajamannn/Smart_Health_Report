import time
import matplotlib.pyplot as plt

# ---------------- FOOD DATA ----------------
food_suggestions = {
    "male": {
        "veg": {
            "Mild": [
                "Banana shake with milk",
                "Peanut butter sandwich",
                "Rice + dal",
                "Dry fruits",
                "Paneer toast"
            ],
            "Moderate": [
                "Banana + oats shake",
                "Paneer sabzi",
                "Rice + curd + ghee",
                "Sweet potato",
                "Dates & peanuts"
            ],
            "Severe": [
                "Full cream milk (2 times)",
                "Banana peanut butter smoothie",
                "Paneer curry",
                "Rice + dal + ghee",
                "Nuts + seeds mix"
            ]
        },
        "nonveg": {
            "Mild": [
                "Banana shake",
                "Boiled eggs (2–3)",
                "Rice + dal",
                "Peanut butter sandwich",
                "Dry fruits"
            ],
            "Moderate": [
                "Banana oats shake",
                "Chicken breast",
                "Rice + curd + ghee",
                "Boiled eggs (4)",
                "Dates & peanuts"
            ],
            "Severe": [
                "Full cream milk",
                "Protein smoothie",
                "Chicken / egg curry",
                "Rice + dal + ghee",
                "Nuts + seeds mix"
            ]
        }
    },
    "female": {
        "veg": {
            "Mild": [
                "Milk + dates",
                "Fruit smoothie",
                "Peanut chikki",
                "Rice + dal",
                "Nuts"
            ],
            "Moderate": [
                "Banana oats smoothie",
                "Paneer sabzi",
                "Rice + curd",
                "Sweet potato",
                "Homemade laddoo"
            ],
            "Severe": [
                "Full cream milk",
                "Banana peanut butter shake",
                "Paneer + ghee roti",
                "Rice + dal + ghee",
                "Dry fruits + seeds"
            ]
        },
        "nonveg": {
            "Mild": [
                "Milk + dates",
                "Fruit smoothie",
                "Boiled eggs",
                "Rice + dal",
                "Nuts"
            ],
            "Moderate": [
                "Banana oats smoothie",
                "Egg curry / fish",
                "Rice + curd",
                "Sweet potato",
                "Peanuts"
            ],
            "Severe": [
                "Full cream milk",
                "Egg & banana smoothie",
                "Chicken / fish curry",
                "Rice + dal + ghee",
                "Dry fruits + seeds"
            ]
        }
    }
}

# -------- NORMAL BMI FOOD --------
normal_bmi_food = {
    "male": {
        "veg": [
            "Chapati + dal",
            "Vegetable curry",
            "Curd",
            "Seasonal fruits",
            "Handful nuts"
        ],
        "nonveg": [
            "Chapati + dal",
            "Boiled eggs",
            "Grilled chicken",
            "Vegetables",
            "Fruits"
        ]
    },
    "female": {
        "veg": [
            "Chapati + sabzi",
            "Curd",
            "Sprouts",
            "Fruits",
            "Nuts"
        ],
        "nonveg": [
            "Chapati + sabzi",
            "Boiled eggs",
            "Fish / chicken",
            "Vegetables",
            "Fruits"
        ]
    }
}

# ---------------- MAIN LOOP ----------------
while True:
    try:
        print("\n----------------------------------")
        print(" SMART HEALTH & DIET ANALYZER")
        print("----------------------------------")

        name = input("Name: ")
        age = int(input("Age: "))
        height = float(input("Height (cm): "))
        weight = float(input("Weight (kg): "))
        gender = input("Gender (Male/Female): ").lower()
        blood_group = input("Blood Group: ").upper()
        diet = input("Diet (Veg / Non-Veg): ").lower()
        sleep = float(input("Daily Sleep Hours: "))

        print("\nActivity Level")
        print("1. No Exercise")
        print("2. Light Exercise")
        print("3. Moderate Exercise")
        print("4. Daily Exercise")
        activity = int(input("Choose (1-4): "))

        print("\nProcessing...")
        time.sleep(1.5)

        # -------- BMI --------
        h = height / 100
        bmi = round(weight / (h * h), 2)

        if bmi < 18.5:
            status = "Underweight"
            goal = "Gain Weight"
        elif bmi < 24.9:
            status = "Normal"
            goal = "Maintain Weight"
        elif bmi < 29.9:
            status = "Overweight"
            goal = "Reduce Weight"
        else:
            status = "Obese"
            goal = "Reduce Weight Strictly"

        # -------- GAIN LEVEL --------
        gain_level = None
        if bmi < 16:
            gain_level = "Severe"
        elif bmi < 17.5:
            gain_level = "Moderate"
        elif bmi < 18.5:
            gain_level = "Mild"

        # -------- WATER & SLEEP --------
        water = round(weight * 0.033, 1)
        rec_sleep = 9 if age < 18 else 8 if age < 60 else 7.5

        # -------- BMR --------
        if gender in ["male", "m"]:
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161

        factors = [1.2, 1.375, 1.55, 1.725]
        calories = int(bmr * factors[activity - 1])

        g_key = "male" if gender in ["male", "m"] else "female"
        d_key = "veg" if diet == "veg" else "nonveg"

        # -------- REPORT --------
        print("\n=================================")
        print("          FINAL REPORT")
        print("=================================")
        print("Name:", name)
        print("Gender:", g_key.capitalize())
        print("Blood Group:", blood_group)
        print("Diet:", "Vegetarian" if diet == "veg" else "Non-Vegetarian")
        print("BMI:", bmi, "(", status, ")")
        print("Goal:", goal)
        print("---------------------------------")
        print("Water Intake:", water, "Liters/day")
        print("Recommended Sleep:", rec_sleep, "Hours")
        print("Your Sleep:", sleep, "Hours")
        print("Calories Needed:", calories, "kcal")
        print("=================================")

        # -------- FOOD OUTPUT --------
        if goal == "Gain Weight" and gain_level:
            print("\n🍽️ FOOD SUGGESTIONS (WEIGHT GAIN)")
            for food in food_suggestions[g_key][d_key][gain_level]:
                print("-", food)

        elif status == "Normal":
            print("\n🍽️ FOOD SUGGESTIONS (MAINTENANCE)")
            for food in normal_bmi_food[g_key][d_key]:
                print("-", food)

        else:
            print("\n🍽️ FOOD SUGGESTIONS")
            print("No special food intake required.")
            print("Maintain a healthy balanced diet.")

        # -------- SINGLE PIE CHART --------
        values = [
            (bmi / 40) * 100,
            (sleep / rec_sleep) * 100,
            (water / (weight * 0.04)) * 100,
            (calories / 2500) * 100
        ]
        labels = ["BMI", "Sleep", "Hydration", "Calories"]

        plt.figure(figsize=(7, 7))
        plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title("Overall Health Balance")
        plt.show()

        print("Project By: Aman Raj")

    except:
        print("\n❌ Invalid input. Please try again.")

    again = input("\nGenerate another report? (y/n): ").lower()
    if again != "y":
        print("\nThank you for using the system 👍")
        break
