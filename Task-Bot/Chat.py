import time
import tkinter as tk
from threading import Thread
from tkinter import ttk, messagebox

# Function to handle reminders
def set_reminder():
    task = entry_task.get().strip()
    try:
        seconds = int(entry_time.get().strip())
        if not task:
            output_label.config(text="⚠️ Please enter a valid task.")
            return
        
        output_label.config(text=f"⏳ Reminder set for '{task}' in {seconds} seconds.")
        root.update()
        time.sleep(seconds)
        output_label.config(text=f"⏰ Reminder: {task}!")
        messagebox.showinfo("Reminder", f"⏰ Reminder: {task}!")  # Popup alert
    except ValueError:
        output_label.config(text="⚠️ Please enter a valid number.")

# Function to handle simple Q&A
def answer_question():
    question = entry_question.get().strip().lower()
    if not question:
        output_label.config(text="⚠️ Please enter a question.")
        return

    responses = {
        "hello": "Hello! How can I assist you?",
        "how are you": "I'm just a virtual assistant, but I'm here to help!",
        "what is your name": "I'm your virtual assistant!",
        "bye": "Goodbye! Have a great day!"
    }
    response = responses.get(question, "I'm not sure about that. Try asking something else.")
    output_label.config(text=response)

# Function to run reminders in a separate thread (prevents GUI from freezing)
def start_reminder_thread():
    Thread(target=set_reminder, daemon=True).start()

# Creating GUI
root = tk.Tk()
root.title("Helper bot")
root.geometry("400x400")
root.configure(bg="#F0F0F0")  # Light gray background
root.resizable(False, False)  # Fix window size

# Header label
header_label = tk.Label(root, text="Chat Bot", font=("Arial", 16, "bold"), bg="#F0F0F0", fg="#333")
header_label.pack(pady=10)

# Frame for Reminder Section
frame_reminder = tk.Frame(root, bg="#E3F2FD", padx=10, pady=10, bd=2, relief="ridge")
frame_reminder.pack(pady=10, fill="x", padx=20)

tk.Label(frame_reminder, text="Set a Reminder", font=("Arial", 12, "bold"), bg="#E3F2FD").pack()

entry_task = ttk.Entry(frame_reminder, font=("Arial", 12), width=25)
entry_task.pack(pady=5)
entry_task.insert(0, "Enter task here")

entry_time = ttk.Entry(frame_reminder, font=("Arial", 12), width=25)
entry_time.pack(pady=5)
entry_time.insert(0, "Enter time in seconds")

reminder_button = ttk.Button(frame_reminder, text="Set Reminder", command=start_reminder_thread)
reminder_button.pack(pady=5)

# Frame for Question Section
frame_question = tk.Frame(root, bg="#FFEBEE", padx=10, pady=10, bd=2, relief="ridge")
frame_question.pack(pady=10, fill="x", padx=20)

tk.Label(frame_question, text="Ask a Question", font=("Arial", 12, "bold"), bg="#FFEBEE").pack()

entry_question = ttk.Entry(frame_question, font=("Arial", 12), width=25)
entry_question.pack(pady=5)

question_button = ttk.Button(frame_question, text="Get Answer", command=answer_question)
question_button.pack(pady=5)

# Output Label
output_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="blue", bg="#F0F0F0")
output_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
