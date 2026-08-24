# R-105400 — One frequency is not a low-rank error

For Gaussian translates `a_k(t)=exp(-(t-kh)^2/2)`, one phase `x` produces

\[
M_x(k,l)=\sqrt\pi e^{-x^2/4}e^{ix(k+l)h/2}e^{-(k-l)^2h^2/4}.
\]

Thus `M_x=D_x T_h D_x`, where `D_x` is invertible diagonal and `T_h` is the
strictly positive Gaussian Toeplitz Gram matrix. Hence `M_x` has full rank in
every finite dimension. One cannot remove one direction per prime.
