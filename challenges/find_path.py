
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

    def heuristica(node):
        return 0

    falta_pecorrer = []

    heapq.heappush(
        falta_pecorrer,
        (heuristica(start), start)
    )

    pais = {}

    g_score = {start: 0}

    while falta_pecorrer:

        _, atual = heapq.heappop(
            falta_pecorrer
        )

        if atual == goal:

            path = [atual]

            while atual in pais:
                atual = pais[atual]
                path.append(atual)

            path.reverse()

            return path

        for filho in city_map.roads[atual]:

            tentativa_g = (
                g_score[atual] + 1
            )

            if tentativa_g < g_score.get(
                filho,
                float("inf")
            ):

                pais[filho] = atual

                g_score[filho] = tentativa_g

                f_score = (
                    tentativa_g
                    + heuristica(filho)
                )

                heapq.heappush(
                    falta_pecorrer,
                    (
                        f_score,
                        filho
                    )
                )

    return []   
