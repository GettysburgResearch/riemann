# Unequal structured-prime moments and the detector comparison

Date: 2026-10-20. Status: source-dependent unequal-length deduction and
an exact obstruction calculation. No improved numerical zero-free
boundary is asserted.

Source: Xu--Sang,
[arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2), dated
14 October 2026, Sections 6--7 and Proposition 7.2. The source HTML
SHA256 supplied by the independent source auditor is
91f75c5b4d090e4acf7ba9fb597f0ffb3ca3f62917fcfd35ecc7735277473af5.
The source imports the unmarked plain and inverse moments and buffered
detector; this note retains those dependencies.

## 1. Actual coefficient class and unequal lengths

Let the sixth-power-free row have norm comparable to \(Q\), and
let the total column length be \(P=Q^z\), with \(0<z\le1\) fixed.
Consider a fixed bounded number of independently weighted prime
factors of lengths \(P_i\), with \(\prod_iP_i\asymp P\). Every
supported prime has norm at least \(P^c\), for fixed \(c>0\).
The profiles are fixed smooth norm-annular functions, with the
polylogarithmic seminorm bounds of the source. Fixed ray filters
and fixed finite-order Hecke twists can be expanded into the
finite presentation family before assigning bins.

The unprojected coefficient is exactly the convolution
\[
 b(n)=\sum_{n=p_1\cdots p_j}\prod_i
                      w_i(Np_i/P_i)\nu_i(p_i).
\tag{1}
\]
The \(\nu_i\)'s are the fixed allowed characters. The prime
weights are not arbitrary bounded arithmetic sequences.
Pairwise disjoint norm windows make (1) squarefree automatically.
In that important case no repeated-prime error occurs.

The same finite-height contour argument as source Lemma 7.1
works at every \(P_i\): its tail is \(P_i^2Q^{-\tau J}\), and
one chooses the external derivative order \(J\) after the fixed
height exponent \(\tau\). All logarithmic lengths are in fixed
bounded ranges, and \(P_i\ge Q^{zc}\). On a zero-location bin
with label \(a\), it gives
\[
 \left|\sum_n b(n)\psi_u(n)\right|
                      \ll Q^\epsilon P^{a+O(e)}.
\tag{2}
\]
No Mellin contour crosses a zero outside the source's buffered
rectangle.

Write
\[
 \mathcal R(a)=
 \begin{cases}
 (31-32a)/(21-12a),&a\le11/12,\\
 2(1-a),&11/12\le a\le1.
 \end{cases}
\]
The literal source floor is \(a_0=51/100\). After normalization
by \(P^{-1/2}\), its proof therefore gives the exact envelope
\[
 E_{a_0}(z)=
 \max\left\{
  1+(2a_0-1)z,\
  \sup_{a_0\le a\le1}
             [\mathcal R(a)+(2a-1)z]
 \right\}.
\tag{3}
\]
Thus the squared row mean is \(O(Q^{E_{a_0}(z)+\epsilon})\).
This formula, with the source floor retained, requires no
unstated change to that detector. A proved common zero-free
boundary \(\beta\) may further restrict the nonfloor supremum
to \(a\le\beta\), with the usual arbitrarily small bin loss.

For the squarefree projection of a general overlapping convolution,
let
\[
 L(z)=\max\{1,z,5/6+z/3,1/3+5z/6\}.
\tag{4}
\]
The source repeated-prime argument at unequal lengths costs
\(Q^{L(z)-cz+\epsilon}\): its squared coefficient mass before
normalization is \(O(P^{1-c+\epsilon})\).
The non-sixth-power-free part is reduced by \(n=n_0t^6\);
Minkowski and \(\sum_{Nt\ge P^c}(Nt)^{-3}\ll P^{-2c}\)
give the smaller \(Q^{L(z)-4cz+\epsilon}\).
All row zeros at \(t\) remain until a positive row restriction
is removed. For disjoint physical prime windows both correction
terms are absent.

An extension to fixed infinite-order Hecke twists requires the
corresponding licensed balanced-type bin and moment adapter.
It is not a literal application of Proposition 7.2's finite ray
family. Likewise its stated polylogarithmic seminorm condition
must not be silently replaced by arbitrary polynomial-height
profiles.

## 2. Lowering the fixed floor, with its source adapter explicit

The proof of the pinned Ope26a detector permits any fixed
\(a_0=1/2+\rho\), \(\rho>0\). The independent global-source
review checked its lines 4214--4680: the buffered disks require
only \(a_0>1/2\); the shifted gamma line has real part
\(\Re(\rho_{\rm zero}-1/4)\ge a_0-1/4>1/4\); and the remote
error exponent is \(-3+(3/2)(5/4-a_0)<-15/8\).
The saturation error is \(O(\eta/(2a_0-1))\), so choose the
preliminary detector losses after this fixed floor.
Constants may depend on \(\rho\); no detector at the endpoint
\(a_0=1/2\), or uniformity as \(\rho\to0\), is asserted.

Choose \(\rho\) inside the requested final epsilon allowance
before the bin, moment and height losses. The resulting exponent
envelope on \(0<z\le1\), up to that allowance, is
\[
 E(z)=
 \begin{cases}
 1,&0<z\le2/3,\\[2mm]
 \displaystyle\frac83+\frac52z-\frac53\sqrt{6z},
                      &2/3\le z\le1.
 \end{cases}
\tag{5}
\]
Equation (5) uses this explicit proof adapter; equation (3)
remains the directly quoted-floor unequal-length statement.

Indeed, on the first branch of \(\mathcal R\),
\[
 \frac{d}{da}[\mathcal R(a)+(2a-1)z]
                    =2z-\frac{300}{(21-12a)^2}.
\]
For \(z\le2/3\), the maximum is at \(a=1/2\).
For \(2/3<z\le1\), strict concavity gives
\[
 a_*(z)=\frac{21-\sqrt{150/z}}{12}.
\]
Substitution yields (5). The branch \(a\ge11/12\) is smaller
throughout this range.

The arbitrary-coefficient exponent in (4) is \(1\) for
\(z\le1/2\), and \(5/6+z/3\) for \(1/2\le z\le1\).
The ideal structured gain is maximized at \(z=150/169\), where
it is exactly \(7/78\). At balance, (5) gives the source
normalized exponent \(\kappa_6-1\). These calculations concern
the actual structured prime vector, not a new operator norm.

## 3. Why this does not improve the present numerator endpoint

Here is an exact comparison even after granting the stronger
floor-limit formulation. Let a detector class have logarithmic
row count \(R\), local zero parameter \(\delta\), and effective
selected-prime amplitude \(g\), with the licensed source bounds
\[
 R\le1-\frac{2\delta}{3},\qquad 0\le g\le\frac\delta2.
\tag{6}
\]
For an ordinary normalized block of length \(Q^m\), the local
buffer already gives
\[
 \sum_{u\ {\rm in\ class}}|S_m(u)|
                    \ll Q^{R+\delta m/2+\epsilon}.
\tag{7}
\]

The strongest row-scale joint moment obtainable by combining
only the unmarked bin count with its pointwise prime and ordinary
bounds has the triangle
\[
                    2m+z\le2/3.
\tag{8}
\]
To see the threshold, the bin contribution has exponent
\(\mathcal R(a)+\delta(2m+z)\), where \(\delta=2a-1\), and
\[
 \frac{1-\mathcal R(a)}{\delta}
                    =\frac{10}{15-6\delta}\ge2/3.
\]
The infimum as \(\delta\) decreases to zero is \(2/3\).
This is a deduction from the bins, not an arbitrary-coefficient
mixed-moment assertion.

Grant (8), use its maximal prime length \(z=2/3-2m\), and divide
by the actual amplifier lower bound \(Q^{2gz}\). Fourth-moment
Hölder would then give the first-moment exponent
\[
 A_{\rm new}(m)=\frac{3R+1}{4}
                         -\frac g2(2/3-2m),
                    \qquad 0\le m\le1/3.
\tag{9}
\]
Subtracting the already available pointwise exponent in (7),
\[
 A_{\rm new}(m)-(R+\delta m/2)
       =\frac{1-R}{4}-\frac g3+(g-\delta/2)m.
\tag{10}
\]
The right side is minimized at \(m=1/3\), because \(g\le\delta/2\).
At that endpoint it is
\[
                 \frac{1-R}{4}-\frac\delta6\ge0
\]
by (6). Thus the whole putative gain is dominated by (7).
If the actual prime supply is shorter, the bound only worsens.

The source's existing amplified fourth moment is useful precisely
beyond this already controlled portion. The new smooth-prime
moment cannot be inserted as a smaller value of its \(6\kappa\)
coefficient: it contains neither its correlated ordinary factor
nor additional information within a fixed detected class.

## 4. The cubic-theta and actual terminal interfaces

The original side of the quadratic-pair absorption contains
\(\widetilde g(c)\kappa(c)\eta_j(c)\), with a full free cube
variable. This is not coefficient (1). An arbitrary outer
coefficient in the Type-I theorem is likewise not made a smooth
prime coefficient by dividing it by \(\widetilde g(p)\).
Such a Gauss factor is not a fixed Hecke character.

In the actual mixed terminal, the sextic row can be written with
digits \(3\) and \(4\) at the quadratic row and the prime label.
Its parameter norm is of order \(K^3L^4\), whereas the column
length is \(KL\) on the binding face. The resulting ratio
\[
 z=\frac{\log K+\log L}{3\log K+4\log L}\le1/3
\]
is already in the row-scale range of the general sextic large
sieve, before any issue about the Gauss coefficients is addressed.
The unequal structured-prime estimate therefore supplies no new
strict saving at that interface.

The useful outcome is the explicit unequal structured envelope
and the precise exclusion of an unsupported M2 or theta-family
substitution. It does not resolve the coherent marked mixed mean.
