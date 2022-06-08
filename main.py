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


# TestVagrant_coding_assignment
# 2nd Task
# Programmatically retrieve the teams that have 2 consecutive losses

def _2_consecutive_losses(data: dict):
    # empty list that will hold teams names
    teams = []
    # looping throw data to get results of last 5 matches as 'results' and its location as 'i'
    for i, results in enumerate(data["Last_5"]):
        temp = 0
        # looping throw results to get every result
        for result in results:
            # if result is lose then adding 1 in temp variable
            if result == 0:
                temp += 1
            # else temp = 0
            else:
                temp = 0
            # if variable temp is equal to 2 that manse team has lost 2 consecutive times
            if temp == 2:
                # append team name in teams list
                teams.append(data["Team"][i])
                # and break this loop
                break
        # continue to check next results
    # at the end return teams list which have teams data
    return teams


# testing the code
# 2nd Task
print(_2_consecutive_losses(data=IPL_DATA))
