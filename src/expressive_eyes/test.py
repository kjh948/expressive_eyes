#!/usr/bin/env python
import procedural_face as pf
import expressions as exp
import numpy as np
#import pycozmo
import cv2


rate = 60
base_face = exp.Neutral()
expression = exp.Neutral()
x = 0

while x < 11:

    x = x+1

    for from_face, to_face in ((base_face, expression), (expression, base_face)):
        
        face_generator = pf.interpolate(from_face, to_face, rate // 3)

        for face in face_generator:
            im = face.render().convert('RGB')
            np_im = np.array(im)
            k = cv2.waitKey(1) & 0xFF
            cv2.imshow("all EYEZ on you", np_im)

            if x == 1:
                expression = exp.Boredom()

            elif x == 2:
                expression = exp.Fury()
            
            elif x == 3:
                expression = exp.Happiness()
            
            elif x == 4:
                expression = exp.Sadness()

            elif x == 5:
                expression = exp.Skepticism()
            
            elif x == 6:
                expression = exp.Tiredness()

            elif x == 7:
                expression = exp.Confusion()
            
            elif x == 8:
                expression = exp.Horror()

            elif x == 9:
                expression = exp.Rejection()

            else:
                expression = exp.Neutral()




# single interpolation
# for from_face, to_face in ((base_face, expression), (expression, base_face)):
#     face_generator = pf.interpolate(from_face, to_face, rate // 3)

#     for face in face_generator:
#         im = face.render().convert('RGB')
#         np_im = np.array(im)
#         k = cv2.waitKey(1) & 0xFF
#         cv2.imshow("all EYEZ on you", np_im)




# # List `of face expressions.
# expressions = [
#     exp.Anger(),
#     exp.Sadness(),
#     exp.Happiness(),
#     exp.Surprise(),
#     exp.Disgust(),
#     exp.Fear(),
#     exp.Pleading(),
#     exp.Vulnerability(),
#     exp.Despair(),
#     exp.Guilt(),
#     exp.Disappointment(),
#     exp.Embarrassment(),
#     exp.Horror(),
#     exp.Skepticism(),
#     exp.Annoyance(),
#     exp.Fury(),
#     exp.Suspicion(),
#     exp.Rejection(),
#     exp.Boredom(),
#     exp.Tiredness(),
#     exp.Asleep(),
#     exp.Confusion(),
#     exp.Amazement(),
#     exp.Excitement(),
# ]
