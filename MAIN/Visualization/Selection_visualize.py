import tkinter as tk

class Block:
    def __init__(self, value):
        self.value = value

class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer")

        path = "Assets/fonts/static/RobotoMono-SemiBold.ttf"

        self.heading_label = tk.Label(root, text="Selection Sort Visualization", font=(path, 20, "bold"))
        self.heading_label.pack()

        self.description_label = tk.Label(root, text="• Selection Sort divides the input list into two parts: a sorted "
                                                "  sublist and an unsorted sublist. Initially, the sorted sublist is "
                                                "  empty and the unsorted sublist is the entire input list. The "
                                                "  algorithm proceeds by finding the smallest (or largest, "
                                                "  depending on sorting order) element in the unsorted sublist, "
                                                "  swapping it with the leftmost unsorted element, and moving "
                                                "  the sublist boundaries one element to the right.", wraplength=800,
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
        self.selection_sort() 

    def draw_blocks(self):
        self.canvas.delete("all")
        width = 800 / len(self.array)
        for i, value in enumerate(self.array):
            x0, y0 = i * width, 400
            x1, y1 = x0 + width, 400 - value * 20
            color = "#BDF3FF"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            self.canvas.create_text((x0 + x1) / 2, y1 - 10, text=str(value), fill="white", font=("Helvetica", 20, "bold"))

    def selection_sort(self, i=0):
        n = len(self.array)
        if i < n - 1:
            min_index = i
            for j in range(i + 1, n):
                if self.array[j] < self.array[min_index]:
                    min_index = j
            if min_index != i:
                self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
                self.draw_blocks()
                self.root.update_idletasks()
                self.root.after(1000, self.selection_sort, i + 1)
            else:
                self.selection_sort(i + 1)
        else:
            self.draw_blocks()

def main():
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
