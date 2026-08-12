# L-91333 — The negative Hardy energy is exactly the crossed-zero model-space port

Claim ID: `L-91333`  
Status: **EXACT HARDY/MODEL-SPACE DEFECT IDENTITY**  
Created: 2026-08-12  
Depends on: `L-91034/L-91038`; standard inner-function model-space algebra  
RH status: **unproved**

## 1. Abstract half-plane setup

Let \(H^2_+=H^2(\mathbb C_+)\), with boundary decomposition

\[
L^2(\mathbb R)=H^2_+\oplus H^2_-.
\tag{L-91333.1}
\]

Let \(\mathfrak A\) and \(B\) be inner functions in \(\mathbb C_+\), and suppose the boundary-unimodular meromorphic function is

\[
\Theta=\frac{\mathfrak A}{B}.
\tag{L-91333.2}
\]

Let \(r\in H^2_+\) be outer and put

\[
f=\mathfrak A r\in H^2_+.
\tag{L-91333.3}
\]

On the boundary \(B^{-1}=\overline B\), hence

\[
\Theta r=\overline B\,f.
\tag{L-91333.4}
\]

Define the model space

\[
K_B=H^2_+\ominus BH^2_+.
\tag{L-91333.5}
\]

## 2. Exact Hankel/model identity

Decompose

\[
f=f_B+Bg,
\qquad
f_B=P_{K_B}f,
\qquad
g\in H^2_+.
\tag{L-91333.6}
\]

Then

\[
\overline Bf=\overline Bf_B+g.
\tag{L-91333.7}
\]

For every \(h\in H^2_+\),

\[
\langle \overline Bf_B,h\rangle_{L^2}
=
\langle f_B,Bh\rangle_{L^2}
=0,
\]

so \(\overline Bf_B\in H^2_-\). Therefore

\[
\boxed{
P_-(\Theta r)
=
\overline B\,P_{K_B}(\mathfrak A r).
}
\tag{L-91333.8}
\]

Multiplication by \(\overline B\) is unitary on the boundary, giving

\[
\boxed{
\|P_-(\Theta r)\|_{L^2}^2
=
\|P_{K_B}(\mathfrak A r)\|_{H^2}^2.
}
\tag{L-91333.9}
\]

The left side is the negative-energy/anti-causal content of the completed scattering section. The right side is exactly the crossed-zero model-space output port.

## 3. Vanishing criterion

Assume \(\mathfrak A\) and \(B\) are coprime inner functions. Then

\[
P_-(\Theta r)=0
\iff
\mathfrak A r\in BH^2_+.
\tag{L-91333.10}
\]

Since \(r\) is outer, the inner factor of \(\mathfrak A r\) is \(\mathfrak A\). Thus \(B\) divides \(\mathfrak A\). Coprimality forces \(B\) to be a unimodular constant. Hence

\[
\boxed{
P_-(\Theta r)=0
\iff
B\text{ is constant}.
}
\tag{L-91333.11}
\]

For the completed Xi quotient, \(B=B_\omega\) is the crossed-zero Blaschke product of `L-91034` and

\[
\mathfrak A_\omega=B_\omega\Theta_\omega
\]

is the coprime pole-removed inner factor. Therefore

\[
\boxed{
\|P_-(\Theta_\omega r)\|^2=0
\iff
\xi(s)\ne0
\quad
(\Re s>\tfrac12+\omega),
}
\tag{L-91333.12}
\]

apart from the already-declared cancellation convention.

## 4. Explicit finite-packet formula

If \(B\) is a finite Blaschke product and
\(\{e_j\}_{j=1}^{\deg B}\) is any orthonormal Takenaka–Malmquist basis of \(K_B\), then

\[
\boxed{
\|P_-(\Theta r)\|^2
=
\sum_{j=1}^{\deg B}
|\langle \mathfrak A r,e_j\rangle|^2.
}
\tag{L-91333.13}
\]

Repeated poles are represented by the corresponding Cauchy jets. This is the Hardy-space version of the explicit positive hyperbolic port vectors in `L-91034`.

For a single disk Blaschke factor \(B(z)=z^m\), (L-91333.9) reduces to

\[
\|P_-(\bar z^mf)\|_{L^2(\mathbb T)}^2
=
\sum_{j=0}^{m-1}|\widehat f(j)|^2.
\tag{L-91333.14}
\]

## 5. Consequence for the sector-bundle route

`L-91332` constructs the completed boundary section unconditionally in a direct-integral orbit representation. The present identity says that its failure to have positive energy is not an unspecified representation defect:

\[
\boxed{
\text{negative energy}
=
\text{crossed-zero model-space energy}.
}
\tag{L-91333.15}
\]

Thus the minimal completion theorem is to delete one explicit positive projection, not to construct translation covariance or a generic sector-changing Hilbert space.
