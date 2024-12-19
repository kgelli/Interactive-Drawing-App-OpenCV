# OpenCV Drawing Application

A simple interactive drawing application built with Python and OpenCV that allows users to create drawings and shapes with different colors and thicknesses.

## Features

- Multiple drawing modes:
  - Freehand drawing
  - Circle drawing
  - Rectangle drawing
  - Line drawing
- Color options (Red, Green, Blue)
- Adjustable line thickness
- Save functionality

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy

To install the required packages:
```bash
pip install opencv-python numpy
```

## Usage

1. Run the script:
```bash
python canvas.py
```

2. The application will open with a white canvas window.

### Controls

- **Mouse Controls:**
  - Left Click + Hold: Draw/Create shapes
  - Release Left Click: Complete shape drawing

- **Keyboard Controls:**
  - `m`: Switch between drawing modes (freehand/circle/rectangle/line)
  - `c`: Change colors (Red/Green/Blue)
  - `+`: Increase line thickness
  - `-`: Decrease line thickness
  - `s`: Save drawing as "MyImage.png"
  - `q`: Quit application

### Drawing Modes

1. **Freehand Mode**
   - Click and drag to draw freely

2. **Circle Mode**
   - Click for center point
   - Drag to set radius
   - Release to complete

3. **Rectangle Mode**
   - Click for first corner
   - Drag to opposite corner
   - Release to complete

4. **Line Mode**
   - Click for start point
   - Drag to end point
   - Release to complete

## File Output

When saving, the drawing will be stored as "MyImage.png" in the same directory as the script.

## Technical Details

- Canvas Size: 800x600 pixels
- Default Color: Red (BGR format: 0,0,255)
- Default Thickness: 2
- Image Format: PNG (when saving)

## Error Handling

- The thickness cannot be reduced below 1
- The application can be safely closed using 'q' key or the window close button

## Future Enhancements

Potential features for future versions:
- Additional shape options
- More color choices
- Undo/Redo functionality
- Layer support
- Custom canvas sizes
