import cv2
import dropbox
import time 
import random

start_time = time.time()

def take_snapshot(): 
    number=random.randint(0,100)
    #initializing cv2 
    videoCaptureObject = cv2.VideoCapture(0) 
    result = True

    while(result): 
        #read the frames while the camera is on 
        #ret is a dummy variable which returns a boolean value 
        ret,frame = videoCaptureObject.read() 
        img_name = "img"+str(number)+".png"
        #cv2.imwrite() method is used to save an image to any storage device 
        cv2.imwrite(img_name,frame) 
        start_time =time.time
        result = False 
    return img_name 
    print("snapshot taken")
    
   #releases the camera 
    videoCaptureObject.release()
    #closes all the window that might be opened while this process  
    cv2.destroyAllWindows()  
 
take_snapshot()

def upload_file(img_name): 
    access_token = "sl.BIEbu_GbvNduidL6CYzZGjlQVVDPuBsGlN86wuThMVbrMCoT8f4OL36cf9hRC-2VGZ64H8TtOq0zL4LLIqIJexvNxY0Gx_yB6K73kwLDjya4Nl9cRbkPYUBSdaJbBJxzEVy7GA6AIsdh" 
    file =img_name 
    file_from = file 
    file_to="/testFolder/"+(img_name) 
    dbx = dropbox.Dropbox(access_token) 
    
    with open(file_from, 'rb') as f: 
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main(): 
    while(True): 
        if ((time.time() - start_time) >= 5): 
            name = take_snapshot()
            upload_file(name)

main()