import time
import picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    
    time.sleep(5)
    camera.start_recording('/home/pi/Desktop/video.h264')
    time.sleep(30)
    camera.stop_recording()
    camera.stop_preview()
    
