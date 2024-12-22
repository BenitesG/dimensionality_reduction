import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Process & load the image
image = Image.open("image.jpg") 
image_rgb = np.array(image)

# Grey
image_gray = image_gray = 0.2989 * image_rgb[:, :, 0] + 0.5870 * image_rgb[:, :, 1] + 0.1140 * image_rgb[:, :, 2]  
image_array = np.array(image_gray, dtype=float)


# Visualization of all the images (original and grey)
plt.figure(figsize=(15, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original")
plt.subplot(1, 2, 2)
plt.imshow(image_array, cmap="gray")
plt.title("Grey Scale")
plt.show()
