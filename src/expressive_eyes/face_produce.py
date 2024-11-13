from time import sleep
import procedural_face as pf
import expressions as exp
import numpy as np
import cv2


class FaceProduce:

    def __init__(self):

        self.base_face = exp.Neutral()
        self.expression = exp.Neutral()
        self.rate = 60
        
    def running_faces(self, face_type, delay):

        for from_face, to_face in ((self.base_face, face_type), (face_type, self.base_face)):

            face_generator = pf.interpolate(from_face, to_face, self.rate // 3)
            
            if from_face == face_type:
                sleep(delay)

            for face in face_generator:
                im = face.render().convert('RGB')
                np_im = np.array(im)
                k = cv2.waitKey(1) & 0xFF
                cv2.imshow("all EYEZ on you", np_im)
                
                
