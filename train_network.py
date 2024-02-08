import heapq


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, node):
        if node not in self.vertices:
            self.vertices[node] = {}

    def add_edge(self, frm, to, cost=0):
        self.add_vertex(frm)
        self.add_vertex(to)
        self.vertices[frm][to] = cost
        self.vertices[to][frm] = cost

    def distance_queue(self, start):
        distances = {node: float('infinity') for node in self.vertices}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def total_distance(self, path):
        total_distance = 0
        for i in range(len(path) - 1):
            frm = path[i]
            to = path[i + 1]
            total_distance += self.vertices[frm][to]
        return total_distance

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.vertices:
            return []
        paths = []
        for vertex in self.vertices[start]:
            if vertex not in path:
                new_paths = self.find_all_paths(vertex, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def alternate_routes(self, start, end):
        all_paths = self.find_all_paths(start, end)
        alternate_routes = []

        for path in all_paths:
            total_distance = self.total_distance(path)
            alternate_routes.append((path, total_distance))

        return alternate_routes

    def shortest_path(self, start, end):
        distances = self.distance_queue(start)
        path = [end]
        current_vertex = end

        while current_vertex != start:
            next_vertex = min(self.vertices[current_vertex], key=lambda x: distances[x])
            path.append(next_vertex)
            current_vertex = next_vertex

        return path[::-1]


def get_shortest_route(all_paths):
    if not all_paths:
        print("No routes available.")
        return

    shortest_route = min(all_paths, key=lambda x: x[1])
    return shortest_route[0]


def get_shortest_route_distance(all_paths):
    if not all_paths:
        print("No routes available.")
        return
    shortest_route = min(all_paths, key=lambda x: x[1])
    return shortest_route[1]
