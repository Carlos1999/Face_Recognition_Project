from imutils.video import VideoStream
import face_recognition
import pickle
import time
import cv2

def modo_cadastro_rostos():
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    writer = None
    time.sleep(2.0)

    knownEncodings = []
    knownNames = []

    while True:
        # grab the frame from the threaded video strea
        frame = vs.read()
        # exibe o quadro
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        # se 'q' foi pressionada, para o loop
        if key == ord("q"):
            break
        elif key == ord("p"):
            image = frame
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # detect the (x, y)-coordinates of the bounding boxes
            # corresponding to each face in the input image
            boxes = face_recognition.face_locations(rgb,
                                                    model="hog")
            if len(boxes) == 0:
                print("no face found!")
            else:
                print("{} face(s) found".format(len(boxes)))
                
                # compute the facial embedding for the face
                encodings = face_recognition.face_encodings(rgb, boxes)

                
            # loop over the recognized faces
            numero_rosto = 1
            for (top, right, bottom, left) in boxes:
                cv2.putText(image, str(numero_rosto) , (left, top-10 ),cv2.FONT_HERSHEY_SIMPLEX, 0.7 , (0 , 0, 0 ), 2 )
                # draw the predicted face name on the image
                cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
                numero_rosto += 1
                
            
            # show the output image
            cv2.imshow("Image", image)
            cv2.waitKey(0)
            
            
            # loop over the encodings
            numero_rosto = 1
            for encoding in encodings:
                nome = input("Informe qual o nome  do rosto "+str(numero_rosto)+" contido na imagem:")
                cv2.putText(image, nome , (left+20, top-10 ),cv2.FONT_HERSHEY_SIMPLEX, 0.7 , (0 , 0, 0 ), 2 )
                # add each encoding + name to our set of known names and
                # encodings
                knownEncodings.append(encoding)
                knownNames.append(nome)
                numero_rosto += 1
            
            cv2.imshow("Image", image)
            cv2.waitKey(0)
            
            print(knownNames)
    # libera o uso da camera e fecha a janela aberta

    cv2.destroyAllWindows()
    vs.stop()

    print("[INFO] serializing encodings...")
    data_leitura = pickle.loads(open("encodings.pickle", "rb").read())
    data_gravar = {"encodings": knownEncodings+data_leitura["encodings"], "names": knownNames+data_leitura["names"]}
    f = open("encodings.pickle", "wb")
    f.write(pickle.dumps(data_gravar))
    f.close()
