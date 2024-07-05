import heapq
def table_print(vector):
    for i in range(len(vector)):
        print(f"{i}\t\t{vector[i]}")

class Graph:
    def __init__(self, size):
        self.size = size                      # No. of vertices
        self.adj = [[] for _ in range(size)]  # In a weighted graph, store vertex and weight pair for every edge
        self.toll_list = [0] * size

    # Function to add an edge to the graph
    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        # self.adj[v].append((u, w))
    
    def set_toll(self, v, toll):
        self.toll_list[v] = toll

    # Prints shortest paths from src to all other vertices
    def cheapest_path_djkstra(self, src, dest, gas_price, fuel_consump):
        # Create a priority queue to store vertices that
        # are being preprocessed.
        pq = [(0, src)]

        # Create a list for costs and initialize all
        # costs as infinite (INF)
        cost = [float('inf')] * self.size
        cost[src] = 0

        path_tree = [-1] * self.size

        # Looping until the priority queue becomes empty
        while pq:
            # The first element in the tuple is the minimum cost vertex
            # Extract it from the priority queue
            current_cost, u = heapq.heappop(pq)

            for v, v_distance in self.adj[u]:
                price = self.toll_list[v] + (v_distance / fuel_consump) * gas_price
                # If there is a shorter path to v through u
                if cost[v] > cost[u] + price:
                    # Update the cost of v
                    cost[v] = cost[u] + price
                    heapq.heappush(pq, (cost[v], v))
                    path_tree[v] = u

        # Print shortest costs
        print("Vertex cost from source")
        table_print(cost)

        # print("Destination path from source")
        # table_print(path_tree)

        print("Destination path from source:")
        j = end
        while j > 0:
            print(j)
            print('^')
            print('|')
            j = path_tree[j]

        print(f"Cheapest route from {src} to {dest} is ${cost[dest]}")


# Driver program to test methods of the graph class
if __name__ == "__main__":
    # Create the graph given in the above figure
    vertices = 9
    start = 0
    end = 8
    gas_price = 5
    fuel_consump = 16
    g = Graph(vertices)

    # Making the above-shown graph
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)

    g.set_toll(1, 5)
    g.set_toll(3, 3)
    g.set_toll(5, 2)
    g.set_toll(7, 7)
    g.set_toll(8, 10)

    print(f"Number of locations: {vertices}")
    print(f"Start: {start}")
    print(f"Destination: {end}")
    print(f"Gas price: {gas_price}")
    print(f"Car fuel avg consumption: {fuel_consump}")
    print("Toll prices:")
    table_print(g.toll_list)

    # print(g.adj)
    g.cheapest_path_djkstra(start, end, gas_price, fuel_consump)