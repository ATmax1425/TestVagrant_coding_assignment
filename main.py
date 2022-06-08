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


# 4th Task
# Calculate the average points of these filtered teams

def find_consecutive_and_get_average_points(data: dict, wins: bool, n: int):
    # empty 'points' list that will hold teams points
    points = []
    for i, results in enumerate(data["Last_5"]):
        temp = 0
        for result in results:
            if result == wins:
                temp += 1
            else:
                temp = 0

            if temp == n:
                # for getting average points of e filtered teams
                # we are now appending Pts in points list
                points.append(data["Pts"][i])
                break
    # and we will calculate average with ( sum of points / number of points )
    average = sum(points) / len(points)
    # finally return the average
    return average


# testing the code
# 4th Task
print(find_consecutive_and_get_average_points(data=IPL_DATA, wins=True, n=2))
