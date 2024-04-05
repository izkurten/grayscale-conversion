# grayscale-conversion

convert a numpy.array that represents an RBG image into a grayscale image, using luminosity (based on the human eye's sensitivity) using weights for the RBG values.
Using colorimetric conversion to linear RBG and calculates luminance, then applies a gamma correction to convert linear luminance back to sRGB. That's how the image remains its perceptual properties.
