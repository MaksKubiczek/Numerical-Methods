# Project Description

This project focuses on solving systems of linear equations using the Gaussian elimination method. The Gaussian elimination method is a fundamental technique in numerical analysis for solving systems of linear equations by transforming the augmented matrix into row-echelon form.

## Functions

### `load_data(filename)`
- **Description:** Loads data from a file containing the system of linear equations.
- **Parameters:**
  - `filename`: Name of the file containing the data.
- **Returns:** Two lists `A` and `b`, representing the coefficient matrix and the constant vector of the system of equations, respectively.

### `Gauss(tab)`
- **Description:** Implements the Gaussian elimination method to solve the system of linear equations.
- **Parameters:**
  - `tab`: Augmented matrix representing the system of linear equations.
- **Returns:** Prints the augmented matrix and the solution vector of the system of equations.

## Steps

1. **Load Data:**
   - Load the system of linear equations from a file using the `load_data()` function.

2. **Perform Gaussian Elimination:**
   - Use the `Gauss()` function to perform Gaussian elimination on the augmented matrix obtained from the loaded data.

3. **Display Results:**
   - Display the augmented matrix before and after Gaussian elimination, along with the solution vector of the system of equations.

## Usage

1. Define the system of linear equations in a text file, where the first line represents the number of equations (n), and subsequent lines contain the coefficients of the equations and the constants on the right-hand side.
2. Run the Python script to solve the system of equations using the Gaussian elimination method.
3. View the displayed results, including the augmented matrices and the solution vectors.

## Technologies

- Python
- Numerical Methods
- Gaussian Elimination

## Author

This project was created by [Maksymilian Kubiczek] ([@MaksKubiczek](https://github.com/MaksKubiczek)).

## License

This project is licensed under the [MIT License]. For more information, see the LICENSE file.
