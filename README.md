# Fibonacci-Matrices

## Using Matrices to Compute Fibonacci Numbers

- Select a vector (u0) of two consecutive Fibonacci values
- Select the index of the Fibonacci number to be computed from the starting vector
- Find the eigenvalues as well as the egigenvectors. 
- Create a diagonal 2x2 matrix with the eigenvalues placed along the diagonal. 
- Find the inverse of the eigenvector matrix. 
- Scale the diagonal matrix by N
- Multiply the eigenvector matrix by the diagonal matrix
- Multiply the resulting matrix by the product of u0 and the inverse of the eingenvector matrix
- The Resulting vector contains [Fn + 1, Fn]