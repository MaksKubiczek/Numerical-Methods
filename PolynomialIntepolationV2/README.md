# Polynomial Interpolation Project

## Overview

This Python project aims to perform polynomial interpolation using the Gram method. Polynomial interpolation is a method of finding a polynomial function that passes through a given set of data points. The Gram method is a technique used to approximate a polynomial that best fits the given data points.

## Project Components

### 1. Loading Data

- Data is loaded from a file named "input_points.txt".
- Each line in the file contains a pair of x and y coordinates representing data points.

### 2. Calculation Functions

- **Newton's Coefficients:** Calculates the coefficients for Newton's interpolation.
- **Polynomial Function:** Computes the value of a polynomial function given a value of x and its degree.
- **F Function:** Calculates the F function used in Gram's method.
- **Gram's Calculation:** Performs the Gram method to approximate the polynomial that best fits the data points.

### 3. Result Display

- Display the number of nodes (data points).
- Display the coefficients ck, sk for the Gram method.
- Display the interpolated values of Ym(x) for each data point.

## Input Data

The input data consists of a set of data points loaded from the "input_points.txt" file.

## Results

- Number of nodes: [Number of nodes]
- Coefficients ck, sk:
  - [Coefficients ck, sk]
- Interpolated values of Ym(x) for each data point:
  - [Interpolated values of Ym(x)]

## Author

This project was created by [Maksymilian Kubiczek] ([@MaksKubiczek](https://github.com/MaksKubiczek)).

## License

This project is licensed under the [MIT License]. For more information, see the LICENSE file.