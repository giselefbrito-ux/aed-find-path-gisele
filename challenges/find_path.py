
from data_structures.city_map import CityMap
import heapq
from math import hypot


def find_path(
    city_map: CityMap,
    start: int,
    goal: int,
) -> list[int]:

    if start == goal:
        return [start]

    def heuristic(node):
        x1, y1 = city_map.intersections[node]
        x2, y2 = city_map.intersections[goal]

        return hypot(x2 - x1, y2 - y1)

    open_set = []

    heapq.heappush(
        open_set,
        (heuristic(start), start)
    )

    came_from = {}

    g_score = {start: 0}

    while open_set:

        _, current = heapq.heappop(
            open_set
        )

        if current == goal:

            path = [current]

            while current in came_from:
                current = came_from[current]
                path.append(current)

            path.reverse()

            return path

        for neighbor in city_map.roads[current]:

            tentative_g = (
                g_score[current] + 1
            )

            if tentative_g < g_score.get(
                neighbor,
                float("inf")
            ):

                came_from[neighbor] = current

                g_score[neighbor] = tentative_g

                f_score = (
                    tentative_g
                    + heuristic(neighbor)
                )

                heapq.heappush(
                    open_set,
                    (
                        f_score,
                        neighbor
                    )
                )

    return []   
