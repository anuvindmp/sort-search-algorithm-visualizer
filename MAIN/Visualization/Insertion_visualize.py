import tkinter as tk

class Block:
    def __init__(self, value):
        self.value = value

class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer")

        path = "MAIN/Assets/fonts/static/RobotoMono-SemiBold.ttf"

        self.heading_label = tk.Label(root, text="Insertion Sort Visualization", font=(path, 20, "bold"))
        self.heading_label.pack()

        self.description_label = tk.Label(root, text="• Insertion Sort works by iterating through the array, \n"
                                                "• selecting one element at a time and inserting it into its \n"
                                                "• correct position in the sorted subarray.", wraplength=800,
                                    justify="center")
        self.description_label.pack()

        self.canvas = tk.Canvas(root, width=800, height=400, background="#05161A")
        self.canvas.pack()

        self.input_label = tk.Label(root, text="Enter array (comma-separated):")
        self.input_label.pack()

        self.input_entry = tk.Entry(root, width=50)
        self.input_entry.pack()

        self.sort_button = tk.Button(root, text="Sort", command=self.start_sorting)
        self.sort_button.pack()

        self.array = []

    def start_sorting(self):
        self.array = [int(x.strip()) for x in self.input_entry.get().split(",")]
        self.draw_blocks()
        self.insertion_sort() 

    def draw_blocks(self):
        self.canvas.delete("all")
        width = 800 / len(self.array)
        for i, value in enumerate(self.array):
            x0, y0 = i * width, 400
            x1, y1 = x0 + width, 400 - value * 20
            color = "#BDF3FF"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            self.canvas.create_text((x0 + x1) / 2, y1 - 10, text=str(value), fill="white", font=("Helvetica", 20, "bold"))

    def insertion_sort(self, i=1):
        if i < len(self.array):
            key = self.array[i]
            j = i - 1
            while j >= 0 and self.array[j] > key:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
            self.draw_blocks()
            self.root.update_idletasks()  
            self.root.after(700, self.insertion_sort, i + 1) 
        else:
            self.draw_blocks()

def main():
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
