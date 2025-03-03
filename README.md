# Task-Bot

## Overview  
Helper Bot is a basic virtual assistant built with Python and Tkinter. It allows users to set reminders and ask simple questions in a chatbot-style interface. The bot provides popup notifications for reminders and responds to basic questions.  

## Features  
- **Chat-Based Interface** – A simple and interactive UI for user input.  
- **Reminder System** – Set a task with a countdown timer.  
- **Popup Notifications** – Alerts users when a reminder is due.  
- **Predefined Responses** – Answers common questions in a human-like way.  

## Technologies Used  
- **Python** – Core functionality of the bot.  
- **Tkinter** – Used to create the graphical user interface.  
- **Threading** – Ensures the UI remains responsive while the reminder runs.  
- **Messagebox** – Provides popup alerts for reminders.  

## Installation  
### Requirements  
Make sure you have Python installed. Tkinter is usually included with Python, but if needed, install it using:  
```sh
pip install tk
```

## Usage  
1. Run the Python script:  
```sh
python helper_bot.py
```
2. **Setting a Reminder**:  
   - Enter a task description.  
   - Enter the time in seconds.  
   - Click **Set Reminder** – A popup alert will notify you when time is up.  
3. **Asking a Question**:  
   - Type a question in the input field.  
   - Click **Get Answer** to see the response.  

## Example Questions the Bot Can Answer  
- **hello** → "Hello! How can I assist you today?"  
- **how are you** → "I'm just a virtual assistant, but I'm here to help!"  
- **what is your name** → "I'm your friendly chatbot!"  
- **bye** → "Goodbye! Have a great day!"  
- **tell me a joke** → The bot will respond with a programming joke.  

## Notes  
- The bot currently provides predefined responses.  
- Future updates may include AI-powered responses or voice interaction.  


## Author  
Developed by Kanisha.  
![Screenshot 2025-03-03 230711](https://github.com/user-attachments/assets/d7d92190-a526-4671-a979-15203c813636)
