# Project: Solving Systems of Equations using Jacobi Method

## Description

This project focuses on solving systems of linear equations using the Jacobi method. It is an iterative algorithm that finds an approximate solution to systems of linear equations. The project includes functions for reading data from a file, checking whether a matrix is weakly diagonally dominant, and decomposing the matrix into lower-upper form and the inverse of matrix D. Additionally, both the Jacobi method algorithm and its version with a stopping condition based on a specified epsilon difference between successive approximations have been implemented.

## Components

1. **read_file(filename)**: Function to read data from a file. The file contains the matrix dimensions, its elements, and the vector of constants.  
2. **is_diagonally_dominant(n, A)**: Function to check whether the matrix is weakly diagonally dominant.
3. **decompose(n, A)**: Function to decompose the matrix into lower-upper (LU) form and the inverse of matrix D.
4. **jacobi(n, A, b, max_iter)**: Implementation of the Jacobi method algorithm.
5. **jacobi_stop(n, A, b, epsilon, max_iter)**: Implementation of the Jacobi method with a stopping condition based on the specified epsilon value.

## Usage

1. Run the `Jacobi.py` file.
2. The input file `data.txt` contains data in the following format: matrix dimensions, matrix elements, and the vector of constants.
3. The project reads data, checks whether the matrix is weakly diagonally dominant, and then decomposes the matrix.
4. Users can input the maximum number of iterations and the epsilon value for the stopping condition.
5. The project displays solutions for both methods (standard and with a stopping condition) and informs whether the stopping condition has been met.

## Technologies

- Python
- Jacobi Method
- File Handling

## Author

This project was created by ([MaksKubiczek](https://github.com/MaksKubiczek)).

## License

This project is licensed under the [MIT]. For more information, see the LICENSE file.
