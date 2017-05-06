from math import sin, cos, pi, atan2

def add(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

def sub(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    return result

def mult(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(A[i])):
                sum += A[i][k] * B[k][j]
            row.append(sum)
        result.append(row)
    return result

def rotate_2D(angle):
    return [[cos(angle), -sin(angle)],
            [sin(angle), cos(angle)]]

def rotate_3D_around_X_axis(angle):
    return [[1, 0, 0],
            [0, cos(angle), -sin(angle)],
            [0, sin(angle), cos(angle)]]

def rotate_3D_around_Z_axis(angle):
    return [[cos(angle), -sin(angle), 0],
            [sin(angle), cos(angle), 0],
            [0, 0, 1]]

def rotate_3D(angle, axis):
    [[x], [y], [z]] = axis
    ex_angle = pi / 2 - atan2(y, x)
    elim_x = rotate_3D_around_Z_axis(ex_angle)
    axis_2 = mult(elim_x, axis)
    [[x_2], [y_2], [z_2]] = axis_2
    ey_angle = pi / 2 - atan2(z, y)
    elim_y = rotate_3D_around_X_axis(ey_angle)
    rot = rotate_3D_around_Z_axis(angle)
    recr_y = rotate_3D_around_X_axis(-ey_angle)
    recr_x = rotate_3D_around_Z_axis(-ex_angle)
    comb = mult(recr_x, recr_y)
    comb = mult(comb, rot)
    comb = mult(comb, elim_y)
    comb = mult(comb, elim_x)
    return comb

