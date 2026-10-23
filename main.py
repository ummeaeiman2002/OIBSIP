
import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


DB_NAME = "bmi_records.db"


def create_table():
    try:
        with sqlite3.connect(DB_NAME) as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS bmi_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    weight REAL NOT NULL,
                    height REAL NOT NULL,
                    bmi REAL NOT NULL,
                    category TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
        print("Database connected successfully!")

    except sqlite3.Error as error:
        messagebox.showerror("Database Error", str(error))


def calculate_bmi():
    name = name_entry.get().strip()

    if not name:
        messagebox.showerror("Invalid Input", "Please enter your name.")
        return

    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror(
                "Invalid Input",
                "Weight and height must be greater than zero."
            )
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "orange"
        elif bmi < 25:
            category = "Normal weight"
            color = "green"
        elif bmi < 30:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"

        # Save the record in SQLite
        with sqlite3.connect(DB_NAME) as connection:
            connection.execute("""
                INSERT INTO bmi_history
                (name, weight, height, bmi, category)
                VALUES (?, ?, ?, ?, ?)
            """, (name, weight, height, bmi, category))

        result_label.config(
            text=f"Name: {name}\nBMI: {bmi:.2f}\nCategory: {category}",
            fg=color
        )

        print(f"BMI record saved for {name}!")

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers for weight and height."
        )

    except sqlite3.Error as error:
        messagebox.showerror(
            "Database Error",
            f"Could not save record:\n{error}"
        )


def view_history():
    history_window = tk.Toplevel(root)
    history_window.title("BMI History")
    history_window.geometry("650x450")
    history_window.configure(bg="#f0f4f8")

    tk.Label(
        history_window,
        text="BMI Records History",
        font=("Arial", 16, "bold"),
        bg="#f0f4f8"
    ).pack(pady=10)

    history_text = tk.Text(
        history_window,
        width=75,
        height=20,
        font=("Arial", 10)
    )
    history_text.pack(padx=10, pady=10, fill="both", expand=True)

    try:
        with sqlite3.connect(DB_NAME) as connection:
            records = connection.execute("""
                SELECT name, weight, height, bmi, category, created_at
                FROM bmi_history
                ORDER BY id DESC
            """).fetchall()

        if not records:
            history_text.insert(tk.END, "No records found.")
        else:
            for name, weight, height, bmi, category, date in records:
                history_text.insert(
                    tk.END,
                    f"Name: {name}\n"
                    f"Weight: {weight} kg | Height: {height} m\n"
                    f"BMI: {bmi:.2f} | Category: {category}\n"
                    f"Date: {date}\n"
                    f"{'-' * 50}\n"
                )

        history_text.config(state="disabled")

    except sqlite3.Error as error:
        history_window.destroy()
        messagebox.showerror("Database Error", str(error))


def show_bmi_graph():
    try:
        # Display the selected user's BMI history
        name = name_entry.get().strip()

        if not name:
            messagebox.showerror(
                "User Required",
                "Enter a user's name first to view their BMI trend."
            )
            return

        with sqlite3.connect(DB_NAME) as connection:
            records = connection.execute("""
                SELECT bmi, created_at
                FROM bmi_history
                WHERE name = ? COLLATE NOCASE
                ORDER BY id ASC
            """, (name,)).fetchall()

        if not records:
            messagebox.showinfo(
                "No Data",
                f"No BMI records found for {name}."
            )
            return

        bmis = [record[0] for record in records]
        dates = [record[1] for record in records]

        graph_window = tk.Toplevel(root)
        graph_window.title(f"BMI Trend - {name}")
        graph_window.geometry("800x500")

        figure, axis = plt.subplots(figsize=(8, 4.5))

        axis.plot(
            range(1, len(bmis) + 1),
            bmis,
            marker="o",
            linestyle="-"
        )

        axis.set_title(f"BMI Trend for {name}")
        axis.set_xlabel("Record Number")
        axis.set_ylabel("BMI")
        axis.grid(True)

        axis.set_xticks(range(1, len(bmis) + 1))
        axis.set_xticklabels(
            [f"{i}\n{date}" for i, date in enumerate(dates, start=1)],
            rotation=30,
            ha="right",
            fontsize=8
        )

        figure.tight_layout()

        canvas = FigureCanvasTkAgg(figure, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Close the Matplotlib figure when the graph window closes
        graph_window.protocol(
            "WM_DELETE_WINDOW",
            lambda: (plt.close(figure), graph_window.destroy())
        )

    except sqlite3.Error as error:
        messagebox.showerror("Database Error", str(error))

    except Exception as error:
        messagebox.showerror("Graph Error", str(error))


# Main application window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("430x510")
root.configure(bg="#f0f4f8")

create_table()

heading = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 20, "bold"),
    bg="#f0f4f8"
)
heading.pack(pady=12)

tk.Label(root, text="User Name", bg="#f0f4f8").pack()
name_entry = tk.Entry(root, justify="center")
name_entry.pack(pady=5)

tk.Label(root, text="Weight (kg)", bg="#f0f4f8").pack()
weight_entry = tk.Entry(root, justify="center")
weight_entry.pack(pady=5)

tk.Label(root, text="Height (meters)", bg="#f0f4f8").pack()
height_entry = tk.Entry(root, justify="center")
height_entry.pack(pady=5)

calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi,
    bg="#2563eb",
    fg="white",
    font=("Arial", 11, "bold")
)
calculate_button.pack(pady=8)

history_button = tk.Button(
    root,
    text="View BMI History",
    command=view_history,
    bg="#059669",
    fg="white",
    font=("Arial", 11, "bold")
)
history_button.pack(pady=5)

graph_button = tk.Button(
    root,
    text="View BMI Trend Graph",
    command=show_bmi_graph,
    bg="#7c3aed",
    fg="white",
    font=("Arial", 11, "bold")
)
graph_button.pack(pady=5)

result_label = tk.Label(
    root,
    text="Enter your details above",
    font=("Arial", 12, "bold"),
    bg="#f0f4f8"
)
result_label.pack(pady=8)

root.mainloop()
