
class FaceManager:


    def __init__(self):
        self.current_expression = NeutralFace
        self.next_expression = None

        self.current_frame_idx = 0

        self.face_list = list(pf.interpolate('Neutral', 'Happy', 100))

    def set_next_expression(self, expression, interpolation_duration=2):
        self.next_expression = expression
        self.face_list = list(pf.interpolate(self.current_expression, self.next_expression , 100))
        self.current_frame_idx = 0


    # eye animation: 2s
    # 30fps -> 33ms
    # -> 60 frames
    # pf.interpolate(from_face, to_face, 30) -> 60 frames



    # 1st loop: 33ms -> return face_list[0]
    # 2nd loop: 33ms -> return face_list[1]
    # 3rd: 66ms -> return face_list[3] !!


    def get_next_face(elapsed_time):

        
        # have we completed the animation yet?
        if self.current_frame_idx == len(self.face_list):
            self.current_expression = self.next_expression
            self.next_expression = None
            return self.current_expression


        self.current_frame_idx += 1 

        return self.face_list[self.current_frame_idx]

        
