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

For users with **normal BMI**, maintenance diet plans are provided.

---

## 📊 Visualization

The project generates **one combined pie chart** showing:
- BMI balance
- Sleep quality
- Hydration level
- Calorie intake ratio

This gives a **quick visual overview of overall health**.

---

## 🖼️ Screenshots & Output Preview

The following screenshots are attached in this repository for reference:

- **figure_1.png** → Overall Health Balance **Pie Chart**
- **output_1.png** → Sample **Console Output (User Input & Health Report)**
- **output_2.png** → Sample **Food Recommendation Output**

> 📌 *These screenshots help in understanding the program output and visualization without running the code.*

---

## 🛠️ Technologies Used

- **Python 3**
- **Matplotlib**
- **Time Module**

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/smart-health-diet-analyzer.git
