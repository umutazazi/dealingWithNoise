from PIL import Image
import numpy as np
from scipy.ndimage import median_filter
from scipy.fftpack import fft2, ifft2, fftshift
import matplotlib.pyplot as plt

# Define the custom notch filter
def notch_filter(shape, notch_centers, radius=5):
    mask = np.ones(shape)
    for center in notch_centers:
        for i in range(shape[0]):
            for j in range(shape[1]):
                if np.sqrt((i - center[0])**2 + (j - center[1])**2) < radius:
                    mask[i, j] = 0
    return mask

# Load the image
im1 = Image.open('image24.tif').convert('L')
im1 = np.array(im1)

# Apply the median filter
im2 = median_filter(im1, 3)

# Perform FFT and shift zero frequency components to the center
im4 = fftshift(fft2(im1))

# Identify the coordinates of the notch centers manually or by some method
notch_centers = [(109, 87), (150, 169),(124, 122),(136, 135)]  # Replace these with actual coordinates

# Use the notch centers in the notch filter
im5 = notch_filter(im1.shape, notch_centers)

# Multiply the shifted FFT image and the notch filter
im6 = im4 * im5

# Perform inverse FFT on the filtered image
im3 = np.abs(ifft2(im6))

# Normalize im4 and save as 8-bit image
im4_save = np.log(1 + np.abs(im4))
im4_save = 255 * im4_save / np.max(im4_save)
Image.fromarray(im4_save.astype(np.uint8)).save('fourier_spectrum.jpg')

# Create the plots
fig, axs = plt.subplots(2, 3, figsize=(15,10))

axs[0, 0].imshow(im1, cmap='gray'), axs[0, 0].axis('off'), axs[0, 0].set_title('Noisy Image')
axs[0, 1].imshow(im2, cmap='gray'), axs[0, 1].axis('off'), axs[0, 1].set_title('Median Filter')
axs[0, 2].imshow(im3, cmap='gray'), axs[0, 2].axis('off'), axs[0, 2].set_title('Notch Filtered Image')
axs[1, 0].imshow(np.log(1 + np.abs(im4)), cmap='gray'), axs[1, 0].axis('off'), axs[1, 0].set_title('Fourier Spectrum')
axs[1, 1].imshow(im5, cmap='gray'), axs[1, 1].axis('off'), axs[1, 1].set_title('Notch Filters')
axs[1, 2].imshow(np.log(1 + np.abs(im6)), cmap='gray'), axs[1, 2].axis('off'), axs[1, 2].set_title('Result of Multiplication')

plt.show()
