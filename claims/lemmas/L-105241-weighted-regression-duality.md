# L-105241 — The positive line energy is an optimized weighted regression

Claim ID: `L-105241`  
Status: **PROVED EXACT**

In the notation of L-105240 put
\[
W(x)=F_{k+1}(x)^2+\delta^2F_k(x)^2
\]
and
\[
A=\int_{-T}^T\frac{F_{k+1}(x)^2}{W(x)}\,dx,
\quad
B=\int_{-T}^T\frac{F_{k+1}(x)F_{k-1}(x)}{W(x)}\,dx,
\quad
C=\int_{-T}^T\frac{F_{k-1}(x)^2}{W(x)}\,dx.
\]
Then
\[
\boxed{
\mathcal E_k(\lambda,\delta)
=\frac{\delta}{\pi}(A+2\lambda B+\lambda^2C).
}
\tag{1}
\]
If `C>0`, minimization over `lambda>=0` gives
\[
\boxed{
\inf_{\lambda\ge0}\mathcal E_k(\lambda,\delta)
=
\frac{\delta}{\pi}
\left(A-\frac{B_-^2}{C}\right),
\qquad
B_-=\max(-B,0).
}
\tag{2}
\]
Cauchy--Schwarz gives `B^2<=AC`, so the right side is nonnegative.

When `A,C>0`, define the continuous residue-coherence coordinate
\[
\chi_{k,\delta}=\frac{B_-^2}{AC}\in[0,1].
\]
Then
\[
\boxed{
\inf_{\lambda\ge0}\mathcal E_k(\lambda,\delta)
=
\frac{\delta A}{\pi}(1-\chi_{k,\delta}).
}
\tag{3}
\]
Thus low-order descent is reduced to a weighted adjacent-derivative
correlation, plus the side/bottom and companion-pole terms in L-105240.
This is the continuous analogue of the discrete residue coherence, but it is
expressed directly as a real-axis mean value of the actual Xi derivative
chain.
