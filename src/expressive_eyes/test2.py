from face_produce import *
import expressions as exp
import keyboard

fp = FaceProduce()
pfg = pf.ProceduralFaceGenerator()


while True:

    result = keyboard.read_key()

    if result == 'h':
        fp.running_faces(exp.Happiness(), 1)
        result == 0
        
    elif result == 's':
        fp.running_faces(exp.Sadness(), 1)
        result == 0

    elif result == 'a':
        fp.running_faces(exp.Anger(), 1)
        result == 0
    
    elif result == 'f':
        fp.running_faces(exp.Fear(), 1)
        result == 0

    elif result == 't':
        fp.running_faces(exp.Tiredness(), 1)
        result == 0

    elif result == 'd':
        fp.running_faces(exp.Disappointment(), 1)
        result == 0
        
    else:
        fp.running_faces(exp.Neutral(), 0)
        #pfg._blink(0.5)
        

    

