# Project: Polynomial Interpolation using Newton's Method

## Description

This project focuses on computing the value of the interpolating polynomial using Newton's method. Newton's method is an interpolation technique that finds a polynomial which best fits a set of data points. The project includes a function to compute the value of the Newton polynomial at a given point and a function to read data from a text file containing interpolation nodes and function values at those nodes.

## Functions

1. **newton_interpolation(x, nodes, values)**: Computes the value of the Newton polynomial at a given point based on a set of interpolation nodes and function values at those nodes.
2. **read_data(filename)**: Reads data from a text file containing interpolation nodes and function values at those nodes.

## Usage

1. Run the `main.py` file.
2. The input files `data1.txt` and `data2.txt` contain data in the format: number of interpolation nodes, interpolation nodes, and function values at those nodes.
3. The project reads data from the file, computes the value of the Newton polynomial at a selected point, and then displays the results.
4. Users can also compute the polynomial values for other points, which are directly defined in the script.

## Technologies

- Python
- Polynomial Interpolation
- File Handling

## Author

This project was created by ([MaksKubiczek](https://github.com/MaksKubiczek)).

## License

This project is licensed under the [MIT License]. For more information, see the LICENSE file.
