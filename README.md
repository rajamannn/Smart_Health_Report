# 🩺 Smart Health & Diet Analyzer

A **menu-driven Python application** that analyzes a user's **health, lifestyle, and diet needs** based on personal inputs such as BMI, sleep, activity level, and dietary preference (Veg / Non-Veg).

The system generates a **personalized health report**, **food recommendations**, and a **visual health balance pie chart**.

---

## 🚀 Features

- 📏 BMI Calculation & Health Status
- 🎯 Personalized Health Goal (Gain / Maintain / Reduce Weight)
- 💧 Daily Water Intake Recommendation
- 😴 Recommended vs Actual Sleep Analysis
- 🔥 Daily Calorie Requirement (BMR + Activity Level)
- 🍽️ Diet Suggestions (Veg / Non-Veg)
- 📊 Single Pie Chart showing overall health balance
- 🔁 Multiple report generation in one run

---

## 🧠 Health Logic Implemented

- BMI-based classification:
  - Underweight
  - Normal
  - Overweight
  - Obese
- Weight gain intensity:
  - Mild
  - Moderate
  - Severe
- Gender-based BMR calculation
- Activity-based calorie adjustment
- Diet-based food recommendations

---

## 🍽️ Diet Recommendation System

Food suggestions are dynamically selected based on:
- Gender (Male / Female)
- Diet type (Vegetarian / Non-Vegetarian)
- BMI category
- Weight gain level (if underweight)

For normal BMI users, **maintenance diet plans** are provided.

---

## 📊 Visualization

The project generates **one combined pie chart** showing:
- BMI balance
- Sleep quality
- Hydration level
- Calorie intake ratio

This gives a **quick visual overview of overall health**.

---

## 🛠️ Technologies Used

- **Python 3**
- **Matplotlib**
- **Time Module**

---

## ▶ How to Run the Project

### Clone the Repository
```bash
git clone https://github.com/your-username/smart-health-diet-analyzer.git
