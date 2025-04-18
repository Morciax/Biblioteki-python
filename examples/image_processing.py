from PIL import Image, ImageFilter
import cv2
from skimage import data, filters
import matplotlib.pyplot as plt

# Pillow - rozmycie obrazu
img = Image.open("/Users/monikaturkowska/Desktop/example.jpg")
blurred = img.filter(ImageFilter.BLUR)
blurred.save("blurred.jpg")
blurred.show()

# OpenCV - wykrywanie krawędzi
image = cv2.imread("/Users/monikaturkowska/Desktop/example.jpg", 0)
edges = cv2.Canny(image, 100, 200)
cv2.imwrite("edges.jpg", edges)

plt.imshow(edges, cmap='gray')
plt.title("Krawędzie (Canny)")
plt.axis('off')
plt.show()

# scikit-image - filtr Sobela
camera = data.camera()
sobel = filters.sobel(camera)

plt.imshow(sobel, cmap='gray')
plt.title("Filtr Sobela (scikit-image)")
plt.axis('off')
plt.show()
