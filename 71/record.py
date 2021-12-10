import heapq


class RecordScore:
    """Class to track a game's maximum score"""

    def __init__(self):
        self.heap = []

    def __call__(self, val):
        heapq.heappush(self.heap, val)
        return heapq.nlargest(1, self.heap)[0]
