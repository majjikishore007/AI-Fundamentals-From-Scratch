## Objective 

'''
Gpa calculator
'''

import numpy as np
import pandas as pd


grades = [85, 92, 78, 65, 88, 72, 95, 81, 79, 90]
grades_np = np.array(grades)

weights = [0.1, 0.15, 0.1, 0.05, 0.2, 0.1, 0.1, 0.1, 0.05, 0.05]
weights_np = np.array(weights)

print("weights sum to:", np.sum(weights_np))

# 1.final grade calculation
final_grade = np.sum(grades_np * weights_np)
print("Final Grade:", final_grade)

# 2. Apply Curve
curve = 5
# add 5 points to each grade
curved_grades= grades_np + curve
print("Curved Grades:", curved_grades)

# 3. Identify the highest
# use boolean indexing to find the highest grade that are above 90

high_achievers = curved_grades[curved_grades > 90]
print("High Achievers (above 90):", high_achievers)

