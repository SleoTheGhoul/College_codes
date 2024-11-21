import sys

def teams(n):
    teams = []  # To store team names
    print(f"Enter {n} team names \n")
    for _ in range(n):  # To store the team names
        teams.append(input())

    m = 0  # To store the maximum length
    max_len = 0  # To help find the maximum length
    count2 = 0  # To act as a counter

    # To find the longest team name
    for i in range(n):
        for j in range(i+1, n):
            if len(teams[max_len]) < len(teams[j]):
                max_len = j
                m = len(teams[max_len])
                count2 += 1

    if count2 == 0:  # If the first word is the longest
        m = len(teams[0])

    ch = [[' ' for _ in range(n)] for _ in range(m)]  # To store the team names in vertical order
    count = 0  # To act as a counter
    l = 0  # To act as a counter

    # To help print the team names
    for i in range(m):
        for j in range(n):
            if l >= len(teams[count]):  # To see if a space is needed
                ch[i][j] = ' '
            else:  # To store the team name
                ch[i][j] = teams[count][l]
            print(ch[i][j], end="      ")
            count += 1
        print()
        count = 0
        l += 1

def main():
    print("Enter no. of teams (2<N<9)\n")
    N = int(input())  # To store the no. of teams

    if 2 > N or N > 9:  # To check if the no. of teams is valid or not
        print("No. of teams invalid")
        sys.exit(0)
    else:
        teams(N)
    print("")

if __name__ == "__main__":
    main()

