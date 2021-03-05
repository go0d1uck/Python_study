import math
import sys
from typing import List

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
posit_x = []
posit_y = []
ut_data = [[[] for _ in range(2)] for _ in range(4)]
sys.stdin = open("./UT.txt", "r")
ut_degree0 = -90
ut_degree1 = -30
ut_degree2 = 30
ut_degree3 = 90
limit = 200


def trans_coordinate(x, y, theta, pos_x, pos_y):
    r_x = x*math.cos(theta)-y*math.sin(theta)+pos_x
    r_y = x*math.sin(theta)+y*math.cos(theta)+pos_y
    return r_x, r_y


def trans_posit(distance, degree, theta, pos_x, pos_y):
    distance_to_center = 26
    x = 1.0*math.cos(math.radians(degree)) * \
        (distance+distance_to_center)/100
    y = 1.0*math.sin(math.radians(degree)) * \
        (distance+distance_to_center)/100
    return trans_coordinate(x, y, theta, pos_x, pos_y)


def addData(dis, degree, q, x, y, data: List[List[float]]):
    if dis <= limit:
        ux, uy = trans_posit(dis, degree, q, x, y)
        data[0].append(ux), data[1].append(uy)


def update(frames):
    ut, posit = input().split(',')
    x, y, q = map(float, posit.split(' '))
    ut = list(map(int, ut.split(' ')))
    posit_x.append(x), posit_y.append(y)
    addData(ut[0], ut_degree0, q, x, y, ut_data[0])
    addData(ut[1], ut_degree0, q, x, y, ut_data[1])
    addData(ut[2], ut_degree0, q, x, y, ut_data[2])
    addData(ut[3], ut_degree0, q, x, y, ut_data[3])
    return plt.scatter(posit_y, posit_x, s=6)


ani = FuncAnimation(plt.figure(), update, frames=500,
                    blit=True, interval=10)
plt.show()

# while True:
# a = np.array(posit_x)
# b = np.array(posit_y)
# plt.scatter(ut_data[0][1], ut_data[0][0], label="ut0", s=6)  # ut0
# plt.scatter(ut_data[1][1], ut_data[1][0], label="ut1", s=6)  # ut1
# plt.scatter(ut_data[2][1], ut_data[2][0], label="ut2", s=6)  # ut2
# plt.scatter(ut_data[3][1], ut_data[3][0], label="ut3", s=6)  # ut3
# plt.legend(loc='best')
# plt.savefig(str(limit)+".svg",format="svg")
# plt.show()
