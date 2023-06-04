import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20,230),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 1,
            color = (255,255,255))

cv2.putText(img,
            "Mercury",
            (120,250),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255))

cv2.putText(img,
            "Venus",
            (200,260),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255))

cv2.putText(img,
            "Earth",
            (290,270),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255))

cv2.putText(img,
            "Mars",
            (390,260),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255))

cv2.putText(img,
            "Jupiter",
            (590,370),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255))

cv2.putText(img,
            "Saturn",
            (760,320),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255))

cv2.putText(img,
            "Uranus",
            (970,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255))

cv2.putText(img,
            "Neptune",
            (1120,290),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255))

cv2.imshow("Output",img)