import tkinter as tk
import random

class Game(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Game Scrolling")
        self.master.geometry("500x500")

        # Membuat canvas
        self.canvas = tk.Canvas(self.master, bg="#ffffff", width=500, height=500)
        self.canvas.pack(expand=True, fill=tk.BOTH)

        # Membuat scrollbar
        self.scrollbar = tk.Scrollbar(self.master, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.canvas.config(scrollregion=(0, 0, 500, 1000))

        # Membuat karakter
        self.character = self.canvas.create_oval(50, 50, 100, 100, fill="#ff0000")

        # Membuat rintangan
        self.obstacles = []
        for i in range(10):
            x1 = random.randint(0, 400)
            x2 = x1 + random.randint(50, 100)
            y1 = i * 100 + 200
            y2 = y1 + random.randint(50, 100)
            obstacle = self.canvas.create_rectangle(x1, y1, x2, y2, fill="#00ff00")
            self.obstacles.append(obstacle)

        # Membuat tombol
        self.btn_up = tk.Button(self.master, text="Up", command=self.move_up)
        self.btn_up.pack(side=tk.LEFT, padx=10)

        self.btn_down = tk.Button(self.master, text="Down", command=self.move_down)
        self.btn_down.pack(side=tk.LEFT, padx=10)

        self.btn_left = tk.Button(self.master, text="Left", command=self.move_left)
        self.btn_left.pack(side=tk.LEFT, padx=10)

        self.btn_right = tk.Button(self.master, text="Right", command=self.move_right)
        self.btn_right.pack(side=tk.LEFT, padx=10)

    def move_up(self):
        self.canvas.move(self.character, 0, -10)

    def move_down(self):
        self.canvas.move(self.character, 0, 10)

    def move_left(self):
        self.canvas.move(self.character, -10, 0)

    def move_right(self):
        self.canvas.move(self.character, 10, 0)

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    game.mainloop()
