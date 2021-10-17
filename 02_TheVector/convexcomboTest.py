import numpy as np
from Tools.image import file2image as f
from Tools.image import color2gray as c
from Tools.image import image2file as i


# convex combinations of vectors returning n evenly spaced convex combinations between vec1 and vec2
def convexcombo(vec1, vec2, n):
    d = np.ndim(vec1)
    if np.ndim(vec2) != d:
        print("not same dimension")
        return
    return [[[alpha * vec1[i][j] + (1 - alpha) * vec2[i][j] for j in range(np.shape(vec1)[0])] for i in
             range(np.shape(vec1)[1])] for alpha in np.linspace(0, 1, n)]

def makeComboImages(convexCombo):
    for x in range(10):
        i(convexCombo[x], "testcombo" + str(x) + ".png")


pic1 = c(f("pic1.png"))
pic2 = c(f("pic2.png"))

# uncomment the following to make the combos ( note that it takes a few minutes to run this
# test = convexcombo(pic1, pic2, 10)

# uncomment the following to make the test images
# makeComboImages(test)

