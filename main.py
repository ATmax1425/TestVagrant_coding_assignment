# 1st Task
# Create a small data structure that holds details

IPL_DATA = {
    # Name of the teams
    "Team": ["GT", "LSG", "RR", "DC", "RCB", "KKR", "PBKS", "SRH", "CSK", "MI"],
    # points they have earned
    "Pts": [20, 18, 16, 14, 14, 12, 12, 12, 8, 6],
    #  result of last 5 matches
    "Last_5": [[1, 1, 0, 0, 1], [1, 0, 0, 1, 1], [1, 0, 1, 0, 0], [1, 1, 0, 1, 0], [0, 1, 1, 0, 0],
               [0, 1, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 0, 0, 0], [0, 0, 1, 0, 1], [0, 1, 0, 1, 1]]
}


# 3rd Task
# Generalize the same solution, so that we could get teams that have n consecutive losses/wins.

# this time we need to get more data
# 'data' will have IPL_DATA, if we need consecutive wins we can set 'wins' to True
# and if we need consecutive losses we will set it False, 'n' will have number of consecutive times
def find_consecutive(data: dict, wins: bool, n: int):
    teams = []
    for i, results in enumerate(data["Last_5"]):
        temp = 0
        for result in results:
            # changed 0 to 'wins' now we can check for consecutive wins or losses
            if result == wins:
                temp += 1
            else:
                temp = 0
            # changed 2 to 'n' for checking with different values
            # everything else is same
            if temp == n:
                teams.append(data["Team"][i])
                break
    return teams


# testing the code
# 3re Task
print(find_consecutive(data=IPL_DATA, wins=True, n=2))
