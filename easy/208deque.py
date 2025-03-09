import time
from collections import deque

class RecentCounterDeque:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)


class RecentCounterList:
    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.pop(0)
        return len(self.requests)


# Тестируем скорость
counter_deque = RecentCounterDeque()
counter_list = RecentCounterList()

# Генерируем 100_000 вызовов ping()
times = list(range(0, 1000000, 10))  # Времена с шагом 10 мс

start = time.time()
for t in times:
    counter_deque.ping(t)
print("Deque time:", time.time() - start)

start = time.time()
for t in times:
    counter_list.ping(t)
print("List time:", time.time() - start)

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')':'(', ']':'[','}':'{'}
        stack = []
        for char in s:
            if char in bracket_map:
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack

