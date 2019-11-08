# baseball_elimination
Max Flow Min Cut Algorithm - Programming Assignment

Baseball Elimination Given the standings in a sports league at some point during the season,
determine which teams have been mathematically eliminated from winning their division.
In the baseball elimination problem, there is a league consisting of N teams. At some point during
the season, team i has wi wins and rij games left to play against team j. A team is eliminated if
it cannot possibly nish the season in rst place or tied for rst place. The goal is to determine
exactly which teams are eliminated.

Montreal is mathematically eliminated since it can nish with at most 80 wins and Atlanta al-
ready has 83 wins. Philadelphia is also mathematically eliminated. It can nish the season with
as many as 83 wins, which appears to be enough to tie Atlanta. But this would require Atlanta
to lose all of its remaining games, including the 6 against New York, in which case New York
would nish with 84 wins. We note that New York is not yet mathematically eliminated despite
the fact that it has fewer wins than Philadelphia.

Input:
Input consists of Multiple lines. First line have variable N that denotes number of teams.
Following N lines will have team name, number of wins,number of loses, remaining games to be
played and distribution of remaining games against each teams. Figure 1 describes a sample input
for required program.

Output:
Output consists of N lines. Which consists of status of each teams whether they are eliminated or
not. If eliminated then by which teams. Sample output for gure 1.
Philadelphia is eliminated by the subset of R = f Atlanta New York g
Montreal is eliminated by the subset of R = f Atlanta g
New York is not eliminated
Atlanta is not eliminated

Assumptions. Assume that no games end in a tie,no rainouts, Ignore wildcard possibilities,assume
that there are no whitespace characters in the name of a team.
Ref : https://www.cs.princeton.edu/courses/archive/spr03/cs226/assignments/baseball.html
