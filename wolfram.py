'''Wolfram elementary one-dimensional cellular automaton.'''


mapping = {0: ' ', 1: '\u2588'}


def rule30(M):
    N = [0] * len(M)
    for i in range(len(M)-1):
        if all([M[i-1] == 1, M[i] == 0, M[i+1] == 0]):
            N[i] = 1
        elif all([M[i-1] == 0, M[i] == 1, M[i+1] == 1]):
            N[i] = 1
        elif all([M[i-1] == 0, M[i] == 1, M[i+1] == 0]):
            N[i] = 1
        elif all([M[i-1] == 0, M[i] == 0, M[i+1] == 1]):
            N[i] = 1
    return N


def rule90(M):
    N = [0] * len(M)
    for i in range(len(M)-1):
        if all([M[i-1] == 1, M[i] == 0, M[i+1] == 0]):
            N[i] = 1
        elif all([M[i-1] == 0, M[i] == 0, M[i+1] == 1]):
            N[i] = 1
    return N


if __name__ == '__main__':
    length = 15
    M = [0]*length + [1] + [0]*(length+1)
    for i in range(16):
        print(' '.join(map(lambda x: mapping[x], M)))
        M = rule90(M)