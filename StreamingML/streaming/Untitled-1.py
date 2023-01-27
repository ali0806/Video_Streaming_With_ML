import cv2

# Open the video file
cap = cv2.VideoCapture("movie.mp4")

# Get the frames from the video
frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

# Create the video grid
grid_size = (2, 2) # (rows, columns)
rows = []
for i in range(grid_size[0]):
    row = frames[i*grid_size[1]]
    for j in range(1, grid_size[1]):
        row = cv2.hconcat([row, frames[i*grid_size[1] + j]])
    rows.append(row)
result = rows[0]
for i in range(1, len(rows)):
    result = cv2.vconcat([result, rows[i]])

# Show the video grid
cv2.imshow("Video Grid", result)
cv2.waitKey(0)
