# Image Processing with Notch Filtering

This is a Python project that demonstrates the application of notch filtering in image processing. Notch filters are used to selectively remove specific frequency components from an image's Fourier spectrum. In this project, we apply a notch filter to a given image and visualize the different processing steps.

## Prerequisites

- Python 3.x
- Required packages: `PIL`, `numpy`, `scipy`, `matplotlib`

You can install the required packages using the following command:
```bash
pip install pillow numpy scipy matplotlib
```

## Usage

1. Clone the repository or download the `main.py` file.

2. Place the input image `image24.tif` in the same directory as the `main.py` file.

3. Run the `main.py` script using the following command:
```bash
python main.py
```

## Description

The `main.py` script performs the following steps:

1. Imports necessary libraries and modules.
2. Defines a custom notch filter function to remove specific frequency components from an image's Fourier spectrum.
3. Loads the input image (`image24.tif`) and converts it to grayscale.
4. Applies a median filter to the noisy image to reduce noise.
5. Performs Fast Fourier Transform (FFT) on the original image and shifts zero frequency components to the center.
6. Manually defines notch centers (replace with actual coordinates) and generates a notch filter.
7. Applies the notch filter to the FFT image by element-wise multiplication.
8. Performs inverse FFT to obtain the filtered image.
9. Creates and saves various plots for visualization, including the original image, median-filtered image, notch-filtered image, Fourier spectrum, notch filter, and result of multiplication.

## Output

The script generates a series of plots to visualize the image processing steps. The plots include:

- Original noisy image
- Median-filtered image
- Notch-filtered image
- Fourier spectrum of the original image
- Notch filter used
- Result of multiplication of FFT image and notch filter

## Notes

- Replace the `notch_centers` with actual coordinates that correspond to the frequencies you want to remove using the notch filter.
- The `notch_filter` function can be further customized based on your specific requirements.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Example 
![myplot](https://github.com/umutazazi/dealingWithNoise/assets/72599457/fa6f8e9b-b4a2-4bb4-8c96-987927527608)



---
