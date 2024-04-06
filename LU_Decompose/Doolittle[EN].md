# Doolittle's LU Decomposition Algorithm

## Overview

This project implements Doolittle's LU decomposition algorithm in Python. LU decomposition factors a matrix into the product of a lower triangular matrix (L) and an upper triangular matrix (U). It is often used to solve systems of linear equations and to compute the determinant and inverse of a matrix.

## Description

The `doolittle` function in the script `doolittle.py` takes a filename as input, which contains the matrix data to perform LU decomposition. It reads the data from the file, constructs the augmented matrix, performs LU decomposition using Doolittle's algorithm, and then solves the system of equations to find the unknown vector.

The steps involved in the algorithm are as follows:

1. Read data from the file: The function reads numerical data from the specified file, assuming space-separated values, and constructs a matrix.

2. Augmented matrix creation: It creates an augmented matrix by appending an extra column to the original matrix, which represents the constants in the system of linear equations.

3. LU decomposition: Doolittle's algorithm decomposes the augmented matrix into lower triangular matrix (L) and upper triangular matrix (U).

4. Solve for vector Y: It solves LY = B for Y using forward substitution.

5. Solve for vector X: It solves UX = Y for X using backward substitution.

6. Check for zero on the diagonal: It checks if there is a zero on the diagonal of the matrix U, which would cause division by zero and invalidate the solution.

7. Display results: The function displays the augmented matrix, matrices L and U, as well as the vectors Y and X.

## Usage

To use the script, simply call the `doolittle` function with the filename of the data as an argument. Ensure that the data file contains the matrix in the correct format.

Example usage:

```python
result = doolittle("data.txt")
```

## File Structure

- `doolittle.py`: Main script containing the implementation of Doolittle's LU decomposition algorithm.

- `data.txt`: Sample data file containing the matrix data.

## Requirements

- Python 3.x

## Author

This project was created by [Maksymilian Kubiczek]([@MaksKubiczek](https://github.com/MaksKubiczek)).
