import cv2

cap = cv2.VideoCapture("E:\downloads\Comp 1.mp4")

while True:
    status, frame = cap.read()
    h,w,_ = frame.shape
    if not status:
        print("Status is missng")
        break
    frame_sm = cv2.resize(frame,(w//2, h//2))
    cv2.imshow('output',frame_sm)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()