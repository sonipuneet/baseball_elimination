from FlowNetwork import FlowNetwork

from FlowEdge import FlowEdge

from FordFulkerson import FordFulkerson


class BaseballElimination:

    def __init__(self, filename):

        self._teams = {}
        self._wins = []
        self._losses = []
        self.againstList = []
        self._remain = []
        self._cert = None

        i = 0  # index of the team
        # read the file, each line store the game info of a team
        with open(filename) as f:
            self.teamNum = int(f.readline())  # first line if the team num

            for line in f:
                linelist = line.split()
                team = linelist[0]
                self._teams[team] = i
                self._wins.append(int(linelist[1]))
                self._losses.append(int(linelist[2]))
                self._remain.append(int(linelist[3]))
                # store rest of the line as against info
                self.againstList.append(linelist[4:])
                i += 1

    def numberOfTeams(self):
        return self.teamNum

    def teams(self):
        return self._teams.keys()

    def wins(self, team):
        return self._wins[self.teams[team]]

    def losses(self, team):
        return self.self._wins[self.teams[team]]

    def remaining(self, team):
        return self._remain[self.teams[team]]

    def against(self, team1, team2):
        index1 = self._teams[team1]
        index2 = self._teams[team2]
        return int(self.againstList[index1][index2])

    def isEliminated(self, team):
        if self.isTrivial(team):
            return True
        return self.isNontrivial(team)

    def certificateOfElimination(self, team):
        if self.isEliminated(team):
            return self.cert
        return None

    def isTrivial(self, team):
        self.cert = []

        current = self._wins[self._teams[team]] + \
            self._remain[self._teams[team]]
        for t in self._teams:
            if self._wins[self._teams[t]] > current:
                self.cert.append(t)
                return True
        return False

    def isNontrivial(self, team):
        self.cert = []
        size = 2 + self.teamNum + (self.teamNum-1) * (self.teamNum-2)//2
        network = FlowNetwork(size)
        sink = size - 1
        source = sink - 1
        teamIndex = self._teams[team]
        current = self._wins[teamIndex] + self._remain[teamIndex]
        maxFlow = 0
        # connect team node to sink node
        for i in range(self.teamNum):
            if i != teamIndex:
                network.addEdge(FlowEdge(i, sink, current - self._wins[i]))
        # game nodes index start from teamNum
        gameNode = self.teamNum
        for i in range(self.teamNum):
            if i != teamIndex:
                for j in range(i+1, self.teamNum):
                    if j != teamIndex and int(self.againstList[i][j]) != 0:
                        # connect scource node to game nodes
                        network.addEdge(
                            FlowEdge(source, gameNode, int(self.againstList[i][j])))
                        maxFlow += int(self.againstList[i][j])
                        # connect game nodes to team nodes

                        network.addEdge(FlowEdge(gameNode, i, 1000000000))
                        network.addEdge(FlowEdge(gameNode, j, 1000000000))
                        gameNode += 1

        # compute maxflow
        maxflow = FordFulkerson(network, source, sink)
        if maxflow.value() == maxFlow:
            return False
        # store min cut as certificate
        for team in self._teams.keys():
            if (maxflow.inCut(self._teams[team])):
                self.cert.append(team)
        return True
