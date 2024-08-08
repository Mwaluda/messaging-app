import tkinter as tk
from tkinter import scrolledtext, ttk
import random

# Function to handle sending messages
def send_message():
    global current_sender
    if contact_status[selected_contact]:  # Check if the contact is online
        message = message_entry.get()
        if message:
            chat_window.config(state=tk.NORMAL)
            chat_window.insert(tk.END, f"{current_sender}: " + message + "\n")
            chat_window.config(state=tk.DISABLED)
            chat_window.yview(tk.END)
            message_entry.delete(0, tk.END)
            toggle_sender()
    else:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"System: {selected_contact} is offline and cannot receive messages.\n")
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)

# Function to handle contact selection
def select_contact(event):
    global selected_contact, current_sender
    selected_contact = contacts_listbox.get(contacts_listbox.curselection())
    current_sender = "You"  # Reset sender to "You" when a new contact is selected
    chat_window.config(state=tk.NORMAL)
    chat_window.delete(1.0, tk.END)
    chat_window.insert(tk.END, f"Chat with {selected_contact}\n")
    chat_window.config(state=tk.DISABLED)
    
    # Update online status
    if contact_status[selected_contact]:
        online_status_label.config(text=f"{selected_contact} is Online", fg="green")
    else:
        online_status_label.config(text=f"{selected_contact} is Offline", fg="red")

# Function to handle replying to messages
def reply_message():
    selected_message = chat_window.selection_get()
    if selected_message:
        message_entry.insert(0, f"Reply to: {selected_message}\n")

# Toggle between sending as "You" and as the selected contact
def toggle_sender():
    global current_sender
    current_sender = selected_contact if current_sender == "You" else "You"

# Initialize the main application window
app = tk.Tk()
app.title("Messaging App")
app.geometry("600x450")

# Set up the left sidebar for contacts
sidebar = tk.Frame(app, width=200, bg="#f0f0f0")
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# Add a title to the sidebar
sidebar_label = tk.Label(sidebar, text="Contacts", bg="#f0f0f0", font=("Arial", 14))
sidebar_label.pack(pady=10)

# Listbox to display contacts
contacts_listbox = tk.Listbox(sidebar, bg="#f8f8f8", bd=0, highlightthickness=0)
contacts_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Sample contacts and their online status
contacts = ["Mwaluda", "Maverick", "Serem", "Brian", "Titus"]
contact_status = {contact: random.choice([True, False]) for contact in contacts}  # Random online/offline status

for contact in contacts:
    contacts_listbox.insert(tk.END, contact)

# Bind the selection event
contacts_listbox.bind("<<ListboxSelect>>", select_contact)

# Set up the right side for chat
chat_frame = tk.Frame(app)
chat_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Online status label
online_status_label = tk.Label(chat_frame, text="", font=("Arial", 10))
online_status_label.pack(pady=(10, 0))

# Chat window
chat_window = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Enable selecting text in the chat window
chat_window.config(cursor="arrow")
chat_window.bind("<Button-1>", lambda e: chat_window.tag_remove(tk.SEL, "1.0", tk.END))

# Set up the message entry field and send button
message_entry_frame = tk.Frame(chat_frame)
message_entry_frame.pack(padx=10, pady=(0, 10), side=tk.BOTTOM, fill=tk.X)

message_entry = tk.Entry(message_entry_frame, width=50, font=("Arial", 12))
message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

send_button = tk.Button(message_entry_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT)

# Add a reply button
reply_button = tk.Button(chat_frame, text="Reply", command=reply_message)
reply_button.pack(pady=5, side=tk.BOTTOM)

# Variables to track the current contact and sender
selected_contact = None
current_sender = "You"

# Run the application
app.mainloop()
