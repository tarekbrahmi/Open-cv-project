import cv2


def click_event(event, x, y, flags, params):

    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x, y), font,
                    1, (255, 0, 0), 1)
        cv2.imshow('controle-mouse-event', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x, y), font, 1,
                    (255, 255, 0), 1)
        cv2.imshow('controle-mouse-event', img)



    img = cv2.imread('image-test.png', 1)
    cv2.imshow('controle-mouse-event', img)
    cv2.setMouseCallback('controle-mouse-event', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
