# Finite B-spline continuation

The infinite convolution is not logically required for a rapidly decaying,
zero-free pole-annihilating window. A convolution of 24 equal rational boxes
already gives a degree-23 exact spline, transform decay `|t|^-24`, and a closed
post-100-zero moat below `2.1e-21` using crude rational logarithm bounds.

This removes FFT interpolation, Fourier truncation, and infinite-product tail
from the trust boundary. With normalized first differences, the selected line
background is reduced without worsening the high-zero moat. The remaining work
is one directed finite prime/phase scan over exact spline cells.
