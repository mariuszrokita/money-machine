#
# Line segment intersection using vectors
# see Computer Graphics by F.S. Hill
#
# Borrowed directly from http://www.cs.mun.ca/~rod/2500/notes/numpy-arrays/numpy-arrays.html

"""Set of utilities providing """

import math
from numpy import *


def perp(a):
    b = empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b


# line segment a given by endpoints a1, a2
# line segment b given by endpoints b1, b2
# return
def seg_intersect(a1, a2, b1, b2):
    da = a2 - a1
    db = b2 - b1
    dp = a1 - b1
    dap = perp(da)
    denom = dot(dap, db)
    num = dot(dap, dp)
    return (num / denom.astype(float)) * db + b1


def get_intersection_point_between_points(a1, a2, b1, b2):
    intersection_point = seg_intersect(a1, a2, b1, b2)
    intersection_point_x = intersection_point[0]

    if max([a1[0], b1[0]]) <= intersection_point_x <= min([a2[0], b2[0]]):
        return intersection_point
    else:
        return [nan, nan]


def convert_values_on_x_axis(intersection_points, y_series):
    """Returns list of intersection points with corrected values on x-axis.
       Values on x-axis are rounded up and converted into corresponding date."""
    corrected_intersection_points = []
    for intersect_point in intersection_points:
        # determine date of closest next day after intersection took place
        # print("+++++ intersect point: ", intersect_point[0])
        day_number = round(intersect_point[0])  # alternative: math.ceil(intersect_point[0])
        date = y_series.index.values[day_number]
        # print("+++++ calculated date: ", date)
        corrected_intersection_points.append(array([date, intersect_point[1]]))

    return corrected_intersection_points


def get_intersection_points(y_series_1, y_series_2):
    """Returns intersection points between two time series"""
    if len(y_series_1) != len(y_series_2):
        raise Exception("Lengths of both collections have to be same.")

    x_values = range(0, len(y_series_1), 1)

    intersection_points = []
    for x in x_values[:-1]:
        # print('--next iteration--')
        # print('point 1, [{}, {}]'.format(x, y_series_1[x]))
        # print('point 2, [{}, {}]'.format(x + 1, y_series_1[x + 1]))
        # print('point 3, [{}, {}]'.format(x, y_series_2[x]))
        # print('point 4, [{}, {}]'.format(x + 1, y_series_2[x + 1]))
        point = get_intersection_point_between_points(array([x, y_series_1[x]]),
                                                      array([x + 1, y_series_1[x + 1]]),
                                                      array([x, y_series_2[x]]),
                                                      array([x + 1, y_series_2[x + 1]]))

        # print("=== POINT: [{}, {}]".format(point[0], point[1]))
        if not math.isnan(point[0]):
            intersection_points.append(point)
            # print("=== POINT ADDED TO COLLECTION")

    intersection_points = convert_values_on_x_axis(intersection_points, y_series_1)
    return intersection_points

# def get_buy_sell_points(x_values, y_values_1, y_values_2):
#     intersection_points = get_intersection_points(x_values, y_values_1, y_values_2)
#
#     buy_points = []
#     sell_points = []
#
#     for i in intersection_points:
#         original_x = i[0]
#         next_business_day = int(original_x) + 1
#
#         # y_values_1 represents values of 'shorter' moving average
#         # y_values_2 represents values of 'longer' moving average
#         if y_values_1[next_business_day] < y_values_2[next_business_day]:
#             sell_points.append(i)
#         elif y_values_1[next_business_day] > y_values_2[next_business_day]:
#             buy_points.append(i)
#             # else:
#             #    raise Exception('y_values_1[next_business_day] = y_values_2[next_business_day]', 'exception')
#
#     return buy_points, sell_points
