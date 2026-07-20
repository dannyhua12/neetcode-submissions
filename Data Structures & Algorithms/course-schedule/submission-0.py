class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

        for course in range(numCourses):
            graph[course] = []

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = set()

        def dfs(curr):
            if len(graph[curr]) == 0:
                return True

            if curr in visited:
                return False

            visited.add(curr)

            for prereq in graph[curr]:
                if not dfs(prereq):
                    return False

            visited.remove(curr)
            graph[curr] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True