import math
import cv2
import numpy as np


def calculate_distance(point1, point2):
    point1 = np.array(point1)
    point2 = np.array(point2)
    return np.linalg.norm(point2 - point1)

def foot_center(x1, y1, x2, y2):
    return int((x1 + x2) // 2), int(y2 - 20)

def closest_point_on_lines(points, center_box):
    closest_distance = float("inf")
    closest_point = None
    center_box = np.array(center_box)

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            point1 = np.array(points[i])
            point2 = np.array(points[j])

            line_vec = point2 - point1
            center_vec = center_box - point1
            t = np.dot(center_vec, line_vec) / np.dot(line_vec, line_vec)
            t = np.clip(t, 0, 1)

            closest_point_on_line = point1 + t * line_vec
            distance = np.linalg.norm(center_box - closest_point_on_line)

            if distance < closest_distance:
                closest_distance = distance
                closest_point = closest_point_on_line

    return closest_distance, closest_point.tolist()

def is_point_in_circle(circle_center, circle_radius, point):
    circle_center = np.array(circle_center)
    point = np.array(point)
    distance = np.linalg.norm(circle_center - point)
    return distance <= circle_radius

def check_point_position(line_points, point):
    line_point1, line_point2 = map(np.array, line_points)
    point = np.array(point)
    slope = (line_point2[1] - line_point1[1]) / (line_point2[0] - line_point1[0])
    intercept = line_point1[1] - slope * line_point1[0]

    return 'down' if point[1] > slope * point[0] + intercept else 'up'

def show_user_line(frame, points):
    if len(points) >= 2:
        cv2.polylines(frame, [np.array(points)], True, (0, 255, 255))



def show_user_line(frame, points):
    if len(points) >= 2:
        cv2.polylines(frame, [np.array(points)], True, (0, 255, 255))





def draw_user_area(frame, capture, points, center_box, line_id, line_color=(0, 255, 0)):
    # cap_size = get_cam_sizes(capture=capture)
    # cap_diag = np.sqrt(cap_size[0] ** 2 + cap_size[1] ** 2)

    if len(points) >= 2:
        show_user_line(frame=frame, points=points)

        distance, line_start_xy = closest_point_on_lines(points, center_box)

        line_start_x1, line_start_y1 = int(line_start_xy[0]), int(line_start_xy[1])
        line_end_x1, line_end_y1 = center_box.astype(int)

        # Çizginin uzunluğunu hesaplayın
        line_length = calculate_distance((line_start_x1, line_start_y1), (line_end_x1, line_end_y1))

        # Çizginin uzunluğunu video boyutlarına göre oranlayın
        # line_ratio = line_length / cap_diag

        cv2.line(
            frame,
            (line_start_x1, line_start_y1),
            (line_end_x1, line_end_y1),
            line_color,
            thickness=1,
        )