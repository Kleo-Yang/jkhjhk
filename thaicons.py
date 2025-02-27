import tkinter as tk
import random

# Thai consonants and their names
consonants = [
    ("ก", "กอ ไก่ (gor gai)"),
    ("ข", "ขอ ไข่ (khor khai)"),
    ("ค", "คอ ควาย (khor khwai)"),
    ("ง", "งอ งู (ngor ngu)"),
    ("จ", "จอ จาน (jor jan)")
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.flashcard = tk.Label(root, text="", font=("Arial", 50), width=10, height=3)
        self.flashcard.pack(pady=20)

        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card)
        self.flip_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.new_card)
        self.next_button.pack(pady=10)

        self.new_card()

    def new_card(self):
        self.current_card = random.choice(consonants)
        self.flashcard.config(text=self.current_card[0])

    def flip_card(self):
        self.flashcard.config(text=self.current_card[1])

root = tk.Tk()
app = FlashcardApp(root)
root.mainloop()

