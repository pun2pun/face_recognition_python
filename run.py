import face_recognition
import cv2
import matplotlib.pyplot as plt


ofset = 20
image = cv2.imread("matreial\\110.jpg")
cap = cv2.VideoCapture(0)

process_this_frame = True

pun_image = face_recognition.load_image_file("face\\0.jpg")
pun_encode = face_recognition.face_encodings(pun_image)[0]

chang_image = face_recognition.load_image_file("face\\1.jpg")
chang_encode = face_recognition.face_encodings(chang_image)[0]

known_face_encodings = [pun_encode,chang_encode]
known_face_names = ["Pun","Chang"]

face_locations = []
face_encodings = []
face_names = []
face_names = []


while(True):
    ret,frame = cap.read()
    frame_resize = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    frame_resize = frame_resize[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(frame_resize)
        face_encode_location = face_recognition.face_encodings(frame_resize, face_locations)

        

        for face_encoding in face_encode_location:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknow"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
        
            face_names.append(name)
    
    process_this_frame = not process_this_frame

    for(top, right, bottom, left),name in zip(face_locations, face_names):

        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()