import tkinter as tk
import math

class Node:
    def __init__(self, value, visited=False):
        self.value = value
        self.visited = visited

class Graph:
    def __init__(self):
        self.nodes = [
            Node(4),
            Node(3),
            Node(2),
            Node(1),
            Node(0)
        ]
        self.edges = [
            (0, 1),
            (0, 4),
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 3),
            (3, 4)
        ]

class BFSVisualizer:
    def __init__(self, root, graph):
        self.root = root
        self.graph = graph
        self.visited_order = []  # Store the order of visited nodes
        self.root.title("Breadth First Search Visualization")

        self.heading_label = tk.Label(root, text="Breadth First Search", font=("Roboto", 20, "bold"), fg="#05161A")
        self.heading_label.pack(pady=15)

        self.description_label = tk.Label(root, text="Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.", wraplength=800, justify="left", fg="#05161A")
        self.description_label.pack()

        self.canvas = tk.Canvas(root, width=800, height=380, background="#05161A")
        self.canvas.pack(pady=5)

        self.visited_label = tk.Label(root, text="", justify="left", fg="#05161A")
        self.visited_label.pack()

        self.draw_graph()

        self.source_label = tk.Label(root, text="Enter source node:", justify="left")
        self.source_label.pack()

        self.source_entry = tk.Entry(root, width=50, fg="black", bg="white", justify="left")
        self.source_entry.pack()

        self.search_button = tk.Button(root, text="Run BFS", command=self.start_bfs, fg="white", bg="#05161A", width=20)
        self.search_button.pack(pady=10)

    def draw_graph(self):
        node_radius = 20
        for node in self.graph.nodes:
            x, y = self.get_node_position(node.value)
            self.canvas.create_oval(
                x - node_radius,
                y - node_radius,
                x + node_radius,
                y + node_radius,
                fill="white",
                outline="black",
                tags=f"node{node.value}"
            )
            self.canvas.create_text(x, y, text=node.value, fill="black", font=("Helvetica", 15))

        for edge in self.graph.edges:
            start_node, end_node = edge
            start_x, start_y = self.get_node_position(start_node)
            end_x, end_y = self.get_node_position(end_node)
            self.canvas.create_line(start_x, start_y, end_x, end_y, fill="gray")

    def get_node_position(self, node):
        angle = 2 * math.pi / len(self.graph.nodes) * (node - 1)
        x = self.canvas.winfo_width() * 3 / 4 + math.cos(angle) * 150 + 350
        y = self.canvas.winfo_height() / 2 + math.sin(angle) * 150 + 200
        return x, y


    def start_bfs(self):
        source_node = int(self.source_entry.get().strip())
        self.run_bfs(source_node)

    def run_bfs(self, start_node):
        queue = [start_node]
        self.graph.nodes[start_node - 1].visited = True

        while queue:
            current_node = queue.pop(0)
            self.canvas.itemconfig(f"node{current_node}", fill="yellow")
            self.visited_order.append(current_node)  # Store visited node
            self.update_visited_label(current_node)
            self.root.update()
            self.root.after(500)

            for neighbor in [n.value for n in self.graph.nodes if ((current_node, n.value) in self.graph.edges) or ((n.value, current_node) in self.graph.edges)]:
                if not self.graph.nodes[neighbor - 1].visited:
                    queue.append(neighbor)
                    self.graph.nodes[neighbor - 1].visited = True



    def update_visited_label(self, current_node):
        visited_order_str = ", ".join(map(str, self.visited_order))
        self.visited_label.config(text=f"Visited in order: {visited_order_str}. Current Node: {current_node}")
        print(f"Visited Node: {current_node}")

def main():
    root = tk.Tk()
    root.geometry("800x600")  
    graph = Graph()
    visualizer = BFSVisualizer(root, graph)
    root.mainloop()

if __name__ == "__main__":
    main()
