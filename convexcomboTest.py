import numpy as np
from image import file2image as f
from image import color2gray as c
from ch2_summer2021 import addn, scalar_vector_mult
from image import image2file as i

# convex combinations of vectors returning n evenly spaced convex combinations between vec1 and vec2
def convexcombo(vec1, vec2, n):



pic1 = c(f("pic1.png"))
pic2 = c(f("pic2.png"))

combos = convexcombo(pic1, pic2, 10)
