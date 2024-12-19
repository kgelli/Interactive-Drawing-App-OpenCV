import cv2
import numpy as np

# Global variables
drawing = False
mode = "freehand"
color = (0, 0, 255)  # Start with red color
thickness = 2
start_x, start_y = -1, -1

def draw(event, x, y, flags, param):
    global drawing, start_x, start_y, img
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode == "freehand":
                cv2.line(img, (start_x, start_y), (x, y), color, thickness)
                start_x, start_y = x, y
                
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == "circle":
            radius = int(((x - start_x)**2 + (y - start_y)**2)**0.5)
            cv2.circle(img, (start_x, start_y), radius, color, thickness)
        elif mode == "rectangle":
            cv2.rectangle(img, (start_x, start_y), (x, y), color, thickness)
        elif mode == "line":
            cv2.line(img, (start_x, start_y), (x, y), color, thickness)

# Print manual
print("Manual Of the App")
print("1. Left Click to Start drawing ")
print("2. Press m to change mode : Circle , rectangle ,line , Free Hand")
print("3. Press c to change the colour : Red , Green , Blue ")
print("4. Press + or - for increasing or decreasing thickness ")
print("5. Press s to save ")
print("6. Press q to quit ")

# Create a white image
img = np.ones((600, 800, 3), dtype=np.uint8) * 255

# Create window
cv2.namedWindow("Drawing App", cv2.WINDOW_AUTOSIZE)
# Show the window first time
cv2.imshow("Drawing App", img)
# Now set the mouse callback
cv2.setMouseCallback("Drawing App", draw)

while True:
    cv2.imshow("Drawing App", img)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
    elif key == ord('m'):
        modes = ["circle", "rectangle", "line", "freehand"]
        mode = modes[(modes.index(mode) + 1) % len(modes)]
        print(f"Mode Changed to : {mode}")
    elif key == ord('c'):
        colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]  # Red, Green, Blue
        color = colors[(colors.index(color) + 1) % len(colors)]
        print(f"Colour Changed to : {'Red' if color == (0,0,255) else 'Green' if color == (0,255,0) else 'Blue'}")
    elif key == ord('+'):
        thickness += 1
        print(f"Thickness is increased to : {thickness}")
    elif key == ord('-'):
        if thickness > 1:
            thickness -= 1
            print(f"Thickness is decreased to : {thickness}")
    elif key == ord('s'):
        cv2.imwrite("MyImage.png", img)
        print("Drawing is saved as MyImage.png")

cv2.destroyAllWindows()