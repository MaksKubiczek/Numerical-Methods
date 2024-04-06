# Lagrange Interpolation Project

This Python project aims to demonstrate Lagrange interpolation, both with data from a file and with manually provided data. Lagrange interpolation is a method of constructing new data points within the range of a discrete set of known data points. In this project, the Lagrange interpolation polynomial is computed and evaluated at specified points.

## How it Works

### lagrange_interpolation_with_file Function

This function reads data points from a file containing x and y coordinates of interpolation nodes. It then calculates the Lagrange interpolation polynomial and evaluates it at a specified point. The results are displayed, including the number of interpolation nodes, the data points, the point at which the polynomial is evaluated, and the value of the Lagrange interpolation polynomial at that point.

### lagrange_interpolation Function

This function performs Lagrange interpolation using manually provided x and y values. It computes the Lagrange interpolation polynomial and evaluates it at a specified point.

## Results

1. **Interpolation with Data from a File**
   - Number of interpolation nodes: 4
   - Data:

    ```
     1.000000 1.000000
     2.000000 4.000000
     3.000000 9.000000
     4.000000 16.000000
    ```
   - Point at which the polynomial is evaluated: -1
   - Value of the Lagrange interpolation polynomial at point -1 is: -2.000000

   - Number of interpolation nodes: 4
   - Data:
     ```
     1.000000 1.000000
     2.000000 4.000000
     3.000000 9.000000
     4.000000 16.000000
     ```
   - Point at which the polynomial is evaluated: 0.5
   - Value of the Lagrange interpolation polynomial at point 0.5 is: 2.625000

2. **Interpolation with Manual Data**
   - The cubic root of 50 is approximately 3.6336.

The results demonstrate the application of Lagrange interpolation in approximating values within a given range of data points, both with data from a file and manually provided data.

## Technologies

- Python
- Lagrange Interpolation

## Author

This project was created by [Maksymilian Kubiczek]([@MaksKubiczek](https://github.com/MaksKubiczek)).

## License

This project is licensed under the [MIT License]. For more information, see the LICENSE file.