class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sort_times = []

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            sort_times.append((position[i], time))
        sort_times.sort(reverse=True)

        stack = []

        for _, time in sort_times:
            if not stack:
                stack.append(time)
            else:
                if time <= stack[-1]:
                    continue
                stack.append(time)

        return len(stack)