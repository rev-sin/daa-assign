from collections import defaultdict, deque
from typing import List, Tuple, Set

class SnakesAndLadders:
    def __init__(self, n: int, snakes: List[Tuple[int, int]], ladders: List[Tuple[int, int]]):
        self.n = n
        self.snakes = snakes
        self.ladders = ladders

    def path_exists(self) -> bool:
        target = self.n * self.n
        visited = set()
        queue = deque([1])

        while queue:
            position = queue.popleft()

            if position == target:
                return True

            for move in range(1, 7):
                next_position = position + move
                if next_position > target:
                    continue

                # Check for snake or ladder
                for start, end in self.snakes + self.ladders:
                    if next_position == start:
                        next_position = end
                        break

                if next_position not in visited:
                    visited.add(next_position)
                    queue.append(next_position)

        return False

    def snakes_ladders_share_start_end(self) -> bool:
        snake_starts = set()
        snake_ends = set()
        ladder_starts = set()
        ladder_ends = set()

        # Check snakes
        for start, end in self.snakes:
            if start in snake_starts or end in snake_ends:
                return False
            snake_starts.add(start)
            snake_ends.add(end)

        # Check ladders
        for start, end in self.ladders:
            if start in ladder_starts or end in ladder_ends:
                return False
            ladder_starts.add(start)
            ladder_ends.add(end)

        # Ensure no overlap between snakes and ladders
        if snake_starts & ladder_starts or snake_ends & ladder_ends:
            return False

        return True

    def is_cyc_util(self, adj: defaultdict, u: int, visited: List[bool], rec_stack: List[bool]) -> bool:
        visited[u] = True
        rec_stack[u] = True

        for neighbor in adj[u]:
            if not visited[neighbor]:
                if self.is_cyc_util(adj, neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[u] = False
        return False

    def loops_exist(self) -> bool:
        graph = defaultdict(list)

        for start, end in self.snakes + self.ladders:
            graph[start].append(end)

        visited = [False] * (self.n * self.n + 1)
        rec_stack = [False] * (self.n * self.n + 1)

        for node in range(1, self.n * self.n + 1):
            if not visited[node]:
                if self.is_cyc_util(graph, node, visited, rec_stack):
                    return True

        return False

    def ladder_from_start_to_end(self) -> bool:
        start = 1
        end = self.n * self.n
        for ladder_start, ladder_end in self.ladders:
            if ladder_start == start and ladder_end == end:
                return True
        return False

    def __repr__(self) -> str:
        return f"SnakesAndLadders(n={self.n}, snakes={self.snakes}, ladders={self.ladders})"
