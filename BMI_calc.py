import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        feet = int(feet_entry.get())
        inches = int(inches_entry.get())
        
        # Convert height in feet and inches to meters
        total_height_meters = (feet * 0.3048) + (inches * 0.0254)
        
        if total_height_meters <= 0:
            raise ValueError("Height must be greater than zero.")
        
        bmi = weight / (total_height_meters ** 2)
        result_label.config(text=f"Your BMI is: {bmi:.2f}")
        
        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        
        category_label.config(text=f"Category: {category}")
        
        # Optionally, you could add a brief explanation based on the category
        explanation = get_bmi_explanation(category)
        explanation_label.config(text=explanation)
        
    except ValueError as e:
        messagebox.showerror("Input error", str(e))

def get_bmi_explanation(category):
    explanations = {
        "Underweight": "You may need to gain weight for optimal health.",
        "Normal weight": "Great job! Maintain a balanced diet and exercise.",
        "Overweight": "Consider a balanced diet and regular exercise.",
        "Obesity": "It's important to consult a healthcare provider for advice."
    }
    return explanations.get(category, "No explanation available.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place labels and entries
tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Height (feet):").grid(row=1, column=0, padx=10, pady=10)
feet_entry = tk.Entry(root)
feet_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Height (inches):").grid(row=2, column=0, padx=10, pady=10)
inches_entry = tk.Entry(root)
inches_entry.grid(row=2, column=1, padx=10, pady=5)

# Create and place the Calculate button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=3, columnspan=2, pady=10)

# Create and place the result label
result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2, pady=5)

# Create and place the category label
category_label = tk.Label(root, text="")
category_label.grid(row=5, columnspan=2, pady=5)

# Create and place the explanation label
explanation_label = tk.Label(root, text="", wraplength=250)
explanation_label.grid(row=6, columnspan=2, pady=5)

# Run the application
root.mainloop()
