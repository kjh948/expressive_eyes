#### MAIN ROBOT CONTROLLER, DOING A LOT OF THINGS


from expressive_eyes.face_manager import FaceManager
import cv2
import time

fm = FaceManager(1280,720)

face_str = 'Neutral'
elapsed_time = 0

while True: # main loop of my robot controller

    begin_time = time.time()

    # TASK 1: do speech processing... take 10-20ms

    # TASK 2: update eyes on screen... takes 3-4ms
    face = fm.get_next_face(elapsed_time)
    cv2.imshow("robot screen", face)

    # TASK 3: do move the robot... takes 20-25ms
    # do something else


    elapsed_time = time.time() - begin_time # -> 30ms
