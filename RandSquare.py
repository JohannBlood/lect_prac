from random import random


def randsquare(A, B):
    R = [(A[0], (B[0] + A[0]) / 2 - (B[1] - A[1]) / 2, B[0], (B[0] + A[0]) / 2 + (B[1] - A[1]) / 2),
         (A[1], (B[1] + A[1]) / 2 + (B[0] - A[0]) / 2, B[1], (B[1] + A[1]) / 2 - (B[0] - A[0]) / 2)]
    v1 = [R[0][1] - R[0][0], R[1][1] - R[1][0]]
    v2 = [R[0][3] - R[0][0], R[1][3] - R[1][0]]
    r1 = random()
    r2 = random()
    v1 = list(map(lambda x: x * r1, v1))
    v2 = list(map(lambda x: x * r2, v2))
    return v1[0] + v2[0] + R[0][0], v1[1] + v2[1] + R[1][0]

