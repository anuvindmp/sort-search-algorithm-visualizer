import tkinter as tk

class Block:
    def __init__(self, value):
        self.value = value

class SearchingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Linear Search Visualizer")

        path = "MAIN/Assets/fonts/static/RobotoMono-SemiBold.ttf"

        self.heading_label = tk.Label(root, text="Linear Search Visualization", font=(path, 20, "bold"))
        self.heading_label.pack()

        self.description_label = tk.Label(root, text="• Linear Search checks each element in the list sequentially \n"
                                                "• It stops when finding the target element or reaching the end of the list.", wraplength=800,
                                    justify="center")
        self.description_label.pack()

        self.canvas = tk.Canvas(root, width=800, height=400, background="#05161A")
        self.canvas.pack()

        self.input_label = tk.Label(root, text="Enter array (comma-separated):")
        self.input_label.pack()

        self.input_entry = tk.Entry(root, width=50)
        self.input_entry.pack()

        self.target_label = tk.Label(root, text="Enter target value:")
        self.target_label.pack()

        self.target_entry = tk.Entry(root, width=50)
        self.target_entry.pack()

        self.search_button = tk.Button(root, text="Search", command=self.start_searching)
        self.search_button.pack()

        self.array = []

    def start_searching(self):
        self.array = [int(x.strip()) for x in self.input_entry.get().split(",")]
        target = int(self.target_entry.get())
        self.draw_blocks()
        self.linear_search(target)

    def draw_blocks(self, found_index=None):
        self.canvas.delete("all")
        width = 800 / len(self.array)
        for i, value in enumerate(self.array):
            x0, y0 = i * width, 400
            x1, y1 = x0 + width, 400 - value * 20
            if found_index is not None and i == found_index:
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="#00FF00")
            else:
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="#BDF3FF")
            self.canvas.create_text((x0 + x1) / 2, y1 - 10, text=str(value), fill="white", font=("Helvetica", 20, "bold"))

    def linear_search(self, target, index=0):
        if index < len(self.array):
            self.draw_blocks(index)
            self.root.update_idletasks()
            self.root.after(500, self.linear_search_step, target, index)
        else:
            print("Element not found.")
            self.draw_blocks()  # Reset the blocks when element not found
            self.canvas.create_text(400, 180, text="Element not found", fill="red", font=("Helvetica", 20, "bold"))

    def linear_search_step(self, target, index):
        if self.array[index] == target:
            print(f"Element {target} found at index {index}.")
            self.draw_blocks(index)
            self.canvas.create_text(400, 180, text=f"Element {target} found at index {index}", fill="#00FF00", font=("Helvetica", 20, "bold"))
        else:
            index += 1
            self.root.after(500, self.linear_search, target, index)

def main():
    root = tk.Tk()
    app = SearchingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
