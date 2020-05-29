#Submitted by thr3sh0ld
#graphs and topology using dfs
class Solution:
    def canFinish(self, numCourses, prerequisites):
        count = 0
        final = []
        graph = {course:{} for course in xrange(numCourses)}
        for course, i in prerequisites:
            graph[course][i] = True

        #incoming edge 
        for course in xrange(numCourses):
            if not graph[course]:
                final.append(course)

        # remove edge and find incoming
        while final:
            count += 1
            finished = final.pop()
            for course, j in graph.iteritems():
                if finished in j:
                    del j[finished]
                    if len(j) == 0:
                        final.append(course)

        return count == numCourses