import tkinter as tk
import random

window = tk.Tk()
window.title("My Chatbot")
window.geometry("400x500")

chat_area = tk.Text(window, state='disabled', wrap='word')
chat_area.pack(padx=10, pady=10, fill='both', expand=True)

entry = tk.Entry(window)
entry.pack(padx=10, pady=5, fill='x')
send_button = tk.Button(window, text="Send")
send_button.pack(pady=5)

greeting = ["hi", "hello", "hey"]
greet_responses = ["Hello", "Hi there!", "Hey!"]


def get_response(user_text):
    user_text = user_text.lower()

    if any(word in user_text for word in greeting):
        return random.choice(greet_responses)
    elif "how are you?" in user_text:
        return random.choice(["I'm great", "I'm good", "Doing awesome"])
    elif "bye" in user_text:
        return "see you later!"
    return "Hmm... I don't get that."


def send_message():
    user_text = entry.get()
    entry.delete(0, tk.END)

    chat_area.config(state='normal')
    chat_area.insert(tk.END, "you: " + user_text + "\n")
    bot_reply = get_response(user_text)
    chat_area.insert(tk.END, "bot: " + bot_reply + "\n")
    chat_area.config(state='disabled')
    chat_area.see(tk.END)


send_button.config(command=send_message)
entry.bind("<Return>", lambda event: send_message())

window.config(bg="#1e1e1e")
chat_area.configure(bg="#2b2b2b", fg="white")
entry.configure(bg="#3c3c3c", fg="white")

window.mainloop()
