if __name__ == '__main__':
    # read the number of commands
    N = int(raw_input())
    L = []
    # execute N commands
    for x in xrange(N):
        # read a line and split on spaces
        cmd = raw_input().split()
        #print(cmd)
        # process the command
        if cmd[0] == "insert":
            L.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "pop":
            L.pop()
        elif cmd[0] == "print":
            print L
        elif cmd[0] == "sort":
            L.sort()
        elif cmd[0] == "append":
            L.append(int(cmd[1]))
        elif cmd[0] == "remove":
            L.remove(int(cmd[1]))
        else:
            L.reverse()
#https://www.hackerrank.com/challenges/python-lists
