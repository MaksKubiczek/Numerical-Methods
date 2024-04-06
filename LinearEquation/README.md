# Linear Equations Solver

This Python script contains two functions for solving systems of linear equations using different methods: Gaussian elimination and Gaussian-Crout elimination with partial column pivoting. The script reads input data from files, performs computations, and prints the results.

## Function: `solve_linear_equations`

This function solves a system of linear equations using Gaussian elimination method. Here's a brief overview of the steps performed:

1. **Reading Data**: The function reads the coefficients of the linear equations from a file.
2. **Partial Row Pivoting**: It performs partial row pivoting to maximize the pivot element.
3. **Gaussian Elimination**: Gaussian elimination is applied to transform the coefficient matrix into an upper triangular form.
4. **Back Substitution**: Finally, back substitution is used to find the values of the unknowns.

## Function: `solve_linear_equations_crout`

This function solves a system of linear equations using Gaussian-Crout elimination method with partial column pivoting. Here's what it does:

1. **Reading Data**: Similar to the first function, it reads the coefficients of the linear equations from a file.
2. **Partial Column Pivoting**: It performs partial column pivoting to maximize the pivot element in each column.
3. **Gaussian-Crout Elimination**: The function applies Gaussian-Crout elimination to transform the coefficient matrix into upper triangular form.
4. **Back Substitution**: Back substitution is then performed to find the values of the unknowns.

## File Input

Both functions expect the filename of a text file containing the coefficient matrix of the system of linear equations as input. Each row in the file represents one equation, with the coefficients separated by whitespace.

## Output

After performing the computations, the script prints the following:

- The original matrix and the matrix after computations.
- The solution of the system of equations, including the values of the unknowns.
- Additional information such as the vector of column numbers (in the case of the Crout method).

## Usage

To use the script, call the `solve_linear_equations` and `solve_linear_equations_crout` functions with the filename of the input file as an argument.

Example:

```python
if __name__ == "__main__":
    solve_linear_equations("MN-6-1.txt")  # Using Gaussian elimination method
    solve_linear_equations_crout("MN-6-2.txt")  # Using Gaussian-Crout method
```

## Author

This project was created by ([MaksKubiczek](https://github.com/MaksKubiczek)).

## License

This project is licensed under the [MIT License]. For more information, see the LICENSE file.
