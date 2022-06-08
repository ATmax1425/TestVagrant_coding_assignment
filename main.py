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


run = True
while run:
    task = input("which task you want to run, ex 1,2,3,4 :")
    if task.isdigit():
        task = int(task)
        if 0 < task < 5:
            if task == 1:
                print(IPL_DATA)
            elif task == 2:
                # testing the code
                # 2nd Task
                print("Output of 2nd task")
                print(_2_consecutive_losses(data=IPL_DATA))
            elif task == 3:
                # 3re Task
                try:
                    wins = input("consecutive losses or wins, ex l,w :")
                    if wins == "l":
                        wins = False
                    elif wins == "w":
                        wins = True
                    else:
                        raise IndexError
                    n = int(input("Enter value of n, ex 1,2,3,4 :"))
                    print("Output of 3rd task")
                    print(find_consecutive(data=IPL_DATA, wins=wins, n=n))
                except:
                    print("Please insert valid values")
            elif task == 4:
                # 4th Task
                try:
                    wins = input("consecutive losses or wins, ex l,w ")
                    if wins == "l":
                        wins = False
                    elif wins == "w":
                        wins = True
                    else:
                        raise IndexError
                    n = int(input("Enter value of n, ex 1,2,3,4 :"))
                    print("Output of 4th task")
                    print(find_consecutive_and_get_average_points(data=IPL_DATA, wins=wins, n=n))
                except:
                    print("Please insert valid values")
    else:
        print("please enter valid task number")

    if input("Do you want to run more tests, ex y,n :") != 'y':
        run = False

input("press any key to exit")
