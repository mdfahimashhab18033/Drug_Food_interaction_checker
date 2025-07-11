**Drug-Food Interaction Checker** 

# 🧪 Drug-Food Interaction Checker

A command-line Python application designed to help users identify known interactions between specific **drugs and food items**. This tool is ideal for pharmacy students, healthcare enthusiasts, or anyone interested in how food can impact medication efficacy and safety.


## 📌 Overview

Certain foods can significantly alter how drugs are **absorbed**, **metabolized**, or **eliminated** in the body. This Python script enables users to input the name of a **drug** and a **food item**, and it will check if any known interaction exists between them. If a known interaction is found, the program provides a **clear caution message**.


## 🚀 Key Features

- 🔍 **Real-time Interaction Detection**  
  Instantly checks if a drug-food interaction is known.

- 🧾 **Predefined Interaction Database**  
  Contains a built-in dictionary of drug-food pairs and their warnings.

- ⚠ **Meaningful Alerts**  
  Displays understandable and medically-relevant caution messages.

- ❌ **Input Validation**  
  Alerts the user if the input drug or food is unrecognized.

- 🔁 **Continuous Input Loop**  
  Users can check multiple combinations until they type `stop`.


## 💻 How to Use

1. **Clone this repository** or **download** the Python file.

2. Open your terminal or any Python IDE.

3. Run the script using:

   ```bash
   python project.py
````

4. Follow the prompts:

   ```text
   Enter drug name: ciprofloxacin  
   Enter food item: milk  
   ⚠ Ciprofloxacin + Milk Interaction: Avoid milk and dairy. It reduces drug absorption.
   ```

5. Type `stop` at any prompt to exit the program.


## 🧠 Example Usage

```text
Enter drug name: ciprofloxacin  
Enter food item: milk  
⚠ Ciprofloxacin + Milk Interaction: Avoid milk and dairy. It reduces drug absorption.

Enter drug name: tamoxifen  
Enter food item: soy  
⚠ Tamoxifen + Soy Interaction: Soy may affect estrogen balance. Avoid excess intake.
```

## 📁 File Structure

```
project.py            # Main Python script
(drug-food database)  # Defined as a dictionary inside the script
```

## ✅ Future Improvements

* Load drug-food data from external **CSV/JSON** files
* Add a **Graphical User Interface (GUI)** using Tkinter or PyQt
* Implement **interaction history logging** to a file
* Expand interaction database using public medical datasets

## 👨‍💻 Author

**Mohammad Fahim Ashhab**
Developed as a practice project for **EDGE** program.
Feel free to contribute or suggest improvements!
