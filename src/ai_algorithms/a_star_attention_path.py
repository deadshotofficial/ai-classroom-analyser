import heapq

class AttentionNode:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost


class AStarAttentionAnalyzer:
    def __init__(self):
        self.graph = {}

    def add_state(self, name):
        node = AttentionNode(name)
        self.graph[name] = node
        return node

    def add_transition(self, state1, state2, cost):
        self.graph[state1].add_neighbor(self.graph[state2], cost)

    def heuristic(self, current, goal):
        heuristic_values = {
            "Attentive": 0,
            "Distracted": 2,
            "Yawning": 3,
            "Sleeping": 5
        }

        return abs(heuristic_values[current] - heuristic_values[goal])

    def a_star_search(self, start, goal):
        open_set = []
        heapq.heappush(open_set, (0, start))

        came_from = {}

        g_score = {state: float("inf") for state in self.graph}
        g_score[start] = 0

        f_score = {state: float("inf") for state in self.graph}
        f_score[start] = self.heuristic(start, goal)

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                return self.reconstruct_path(came_from, current)

            for neighbor, cost in self.graph[current].neighbors.items():
                tentative_g = g_score[current] + cost

                if tentative_g < g_score[neighbor.name]:
                    came_from[neighbor.name] = current
                    g_score[neighbor.name] = tentative_g

                    f_score[neighbor.name] = tentative_g + self.heuristic(
                        neighbor.name, goal
                    )

                    heapq.heappush(open_set, (f_score[neighbor.name], neighbor.name))

        return None

    def reconstruct_path(self, came_from, current):
        path = [current]

        while current in came_from:
            current = came_from[current]
            path.append(current)

        path.reverse()
        return path


def build_attention_graph():
    analyzer = AStarAttentionAnalyzer()

    states = [
        "Attentive",
        "Distracted",
        "Yawning",
        "Sleeping"
    ]

    for state in states:
        analyzer.add_state(state)

    analyzer.add_transition("Attentive", "Distracted", 2)
    analyzer.add_transition("Distracted", "Yawning", 2)
    analyzer.add_transition("Yawning", "Sleeping", 3)
    analyzer.add_transition("Distracted", "Attentive", 1)
    analyzer.add_transition("Yawning", "Attentive", 2)

    return analyzer


if __name__ == "__main__":
    analyzer = build_attention_graph()

    start_state = "Attentive"
    goal_state = "Sleeping"

    path = analyzer.a_star_search(start_state, goal_state)

    print("Optimal Attention Transition Path:")
    print(" -> ".join(path))