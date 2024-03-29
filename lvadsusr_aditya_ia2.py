# -*- coding: utf-8 -*-
"""LVADSUSR-Aditya-IA2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zRZBgm8SZok0F-qAGVE-CbvPE0jpfu5L
"""

#question1
import numpy as np

def rgb_to_gray(rgb_image):

    if len(rgb_image.shape) != 3 or rgb_image.shape[2] != 3:
        raise ValueError("Input must be a 3D NumPy array with shape (height, width, 3)")


    gray_image = 0.2989 * rgb_image[:,:,0] + 0.5870 * rgb_image[:,:,1] + 0.1140 * rgb_image[:,:,2]


    gray_image = np.clip(gray_image, 0, 255)


    gray_image = gray_image.astype(np.uint8)

    return gray_image



rgb_image = np.random.randint(0, 256, (5, 5, 3), dtype=np.uint8)
print("RGB Image:")
print(rgb_image)


gray_image = rgb_to_gray(rgb_image)
print("\nGrayscale Image:")
print(gray_image)

#Question 2
import numpy as np

def normalize_data(data):

    means = np.mean(data, axis=0)
    stds = np.std(data, axis=0)


    normalized_data = (data - means) / stds

    return normalized_data


data = np.array([[170, 70, 30],
                 [165, 65, 25],
                 [180, 80, 35]])

normalized_data = normalize_data(data)

print("Original data:")
print(data)
print("\nNormalized data:")
print(normalized_data)

#question3

#question 4
import numpy as np


performances = np.array([
    [10, 12, 15, 18],
    [8, 9, 11, 13],
    [9, 11, 10, 14]
])

first_game = performances[:, 0]
last_game = performances[:, -1]

improvement = last_game - first_game

print("Improvement from first to last game for each athlete:")
print(improvement)

#question 5
import numpy as np


student_scores = np.array([
    [80, 75, 90, 85, 70],
    [60, 65, 70, 75, 80],
    [90, 85, 80, 75, -1],
    [70, 75, 80, 85, 90]
])


def calculate_last_3_avg(scores):

    mask = scores != -1

    scores[scores == -1] = 0
    \
    last_3_sum = np.sum(scores[:, -3:], axis=1)
    \
    num_valid_subjects = np.sum(mask[:, -3:], axis=1)

    last_3_avg = last_3_sum / num_valid_subjects
    return last_3_avg


average_last_3 = calculate_last_3_avg(student_scores)


for i, avg in enumerate(average_last_3):
    print(f"Student {i+1}: Average of last 3 subjects = {avg}")

#question 6

#question 7

#question 8