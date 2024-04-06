# Project Description

This project demonstrates two numerical methods for root-finding: the Secant Method and Newton's Method. Root-finding methods are essential in solving equations where we need to find the values of \(x\) for which \(f(x) = 0\). The project includes Python implementations of both methods along with explanations of their workings and theoretical background.

## Secant Method

The Secant Method is an iterative algorithm for finding the roots of a real-valued function. It starts with two initial approximations \(x_{-1}\) and \(x_0\) and iteratively computes new approximations by intersecting the secant line through the points \((x_{-1}, f(x_{-1}))\) and \((x_0, f(x_0))\) with the x-axis. The process continues until a specified convergence criterion is met or a predetermined number of iterations is reached.

## Newton's Method

Newton's Method, also known as the Newton-Raphson Method, is another iterative root-finding algorithm. It starts with an initial approximation \(x_0\) and iteratively updates the approximation using the formula \(x_{\text{next}} = x - \frac{f(x)}{f'(x)}\), where \(f'(x)\) is the derivative of the function \(f(x)\). Like the Secant Method, it continues until a specified convergence criterion is met or a predetermined number of iterations is reached.

## Usage

To use the project, follow these steps:

1. Clone or download the repository.
2. Open the Python script containing the implementations of the Secant Method and Newton's Method.
3. Input the necessary parameters such as the initial approximations and the number of iterations.
4. Run the script to see the results of both methods.

## Technologies

- Python
- Numerical Methods
- Root-finding Algorithms

## Author

This project was created by ([MaksKubiczek](https://github.com/MaksKubiczek)).

## License

This project is licensed under the [MIT License]. For more information, see the LICENSE file.
