# The unfiltered below-half short-trace contract is false at every order

**Status:** proposed analytic refutation, with a complete proof. The
refuted assertion is the pointwise complementary-frequency contract CT1
in the pinned PR #911 source. Its conditional implication to a physical
moment remains a valid implication with an impossible premise. The exact
norm-filtered representation and its negligible common-conjugate tube
remain valid. No native moment or zero-free conclusion is disproved.

**Scope:** every fixed integer \(k\ge1\), every fixed finite-order native
datum \(\nu\), the original fixed bad-prime set \(S\), all nonzero
Eisenstein element rows, and a fixed nonnegative Schwartz spatial weight
positive at zero. One fixed admissible cross-pair incidence is enough.
Every row-prime and principal nonunit zero is retained.

**New mechanism:** a universal principal pair Euler factor becomes
superpolynomially large on a short common-direction frequency interval.
The remaining two-slot native trace is analytic with only polynomial
growth, and its positive real-axis values cannot be superpolynomially
small throughout that interval. Right-half-plane maximum principles
transport this obstruction to every higher number of slots.

**Smallest conclusion-facing limitation:** this refutes an unfiltered
frequencywise majorant. The physical Mellin norm filter is absent from
that majorant. The argument supplies no lower bound contradicting the
filtered generalized moment, and no saving for its remaining signed
arithmetic contribution.

## 1. Exact statement being tested

Work over \(K=\mathbb Q(\sqrt{-3})\). Let \(N\) denote ideal norm or
element norm as appropriate, and retain the source's primary-generator
convention. Fix:

- an integer \(k\ge1\), with \(r=2k\);
- a finite-order Hecke datum \(\nu\);
- the source's fixed \(S\), containing the primes over \(6\) and the
  conductor of \(\nu\);
- \(1/3<\sigma<1/2\), \(h>0\), and a fixed \(b>0\);
- a nonnegative Schwartz function \(\Phi\) on \(\mathbb C\), with
  \(\Phi(0)>0\), radial if the source requires radiality.

Put \(D=Y/b\) and \(H=D^h\). All the claims below concern sufficiently
large real \(Y\). The source's intended \(h=1+\vartheta\), with
\(0<\vartheta\le1/10\), is included.

The pinned contract quantifies over every sufficiently large \(D\),
with \(Y=bD\); it does not restrict \(D\) or \(Y\) to dyadic values.
The cutoff sequence in Lemma 3.2 uses this real-scale quantifier.
No assertion about a separately restricted lacunary-scale contract
is inferred from that sequence alone.

No stronger property of \(\Phi\) is needed. In particular the argument
applies to a nonnegative Schwartz majorant with compactly supported
Fourier transform when that is the chosen source weight; it does not
replace it by a sharp row ball or a different spatial window.

For a nonzero element row \(u\), write
\[
\eta_u(n)=\nu(n)\chi_n(u).
\tag{1.1}
\]
The literal symbol is zero when \(n\) meets \(u\). On eligible primes
not meeting \(u\), \(|\eta_u(p)|=1\). Set
\[
\theta_{i,u}=\eta_u\quad(1\le i\le k),\qquad
\theta_{i,u}=\overline{\eta_u}\quad(k<i\le2k).
\tag{1.2}
\]

Choose a number \(\sigma_0\) with \(1/3<\sigma_0<\sigma\). Let \(P\)
be the squarefree product of all prime ideals outside \(S\) with
\[
Np\le (16r)^{1/\sigma_0}.
\tag{1.3}
\]
This is a **fixed** ideal. It does not change \(S\). Use the actual
incidence allocation
\[
q_{\{1,k+1\}}=P,\qquad q_I=1\quad(I\ne\{1,k+1\}).
\tag{1.4}
\]
Thus \(Q=P\), \(c_1=c_{k+1}=P\), and the other \(c_i\) equal one.
This allocation is eligible once \(Y\ge NP\). Its exact exterior row
multiplier is
\[
\omega_{\mathbf q}(u)
=\chi_P(u)\overline{\chi_P(u)}
=\mathbf1_{(u,P)=1}.
\tag{1.5}
\]
The fixed coefficient factors involving \(\nu(P)\) and Möbius signs
lie outside the source trace and do not alter its absolute value.

For this fixed allocation define the literal short polynomials
\[
T_{i,Y,u}(s)
=\sum_{\substack{Nn\le Y\\(n,SP)=1}}
       \mu_K(n)\theta_{i,u}(n)(Nn)^{-s},
\tag{1.6}
\]
and the finite collision factor
\[
\mathcal Q_{r,Y,P,u}(\mathbf s)
=\prod_{\substack{p\notin S,\ p\nmid P\\Np\le Y}}
\frac{1-\sum_{i=1}^r\theta_{i,u}(p)(Np)^{-s_i}}
     {\prod_{i=1}^r(1-\theta_{i,u}(p)(Np)^{-s_i})}.
\tag{1.7}
\]
A prime dividing \(u\) has all its variables zero in (1.7) and
contributes one. Define the exact unfiltered trace
\[
\mathscr T_{r,Y}(\mathbf s)
=\sum_{u\ne0}\Phi(u/\sqrt H)\mathbf1_{(u,P)=1}
     \mathcal Q_{r,Y,P,u}(\mathbf s)
     \prod_{i=1}^rT_{i,Y,u}(s_i).
\tag{1.8}
\]
Every nonzero element row, including all unit sectors and all power
rows, occurs in this expression. No coefficients have been replaced
by arbitrary vectors.

Fix
\[
0<\kappa<\arcsin(1/\sqrt{2k}).
\tag{1.9}
\]
Let \(\mathcal U_{Y,\kappa}\) be exactly the source's common-conjugate
tube: there is a real \(t\) with
\[
|t_i-t|\le\kappa/\log Y\quad(i\le k),\qquad
|t_{k+j}+t|\le\kappa/\log Y\quad(j\le k).
\tag{1.10}
\]
The source CT1 asks, in particular on the admissible allocation (1.4),
for a bound
\[
|\mathscr T_{r,Y}(\sigma+i\mathbf t)|
\le C H D^\epsilon\prod_i(1+|t_i|)^B
\quad(\mathbf t\notin\mathcal U_{Y,\kappa}),
\tag{1.11}
\]
with fixed finite \(B,C\), for every positive loss.

### Theorem 1.1. No polynomial complementary trace bound

For the fixed native data above, and for every fixed \(B\ge0\), there
are constants \(c>0\), \(C_B<\infty\), and an unbounded sequence of real
\(Y\), such that
\[
\boxed{
\sup_{\mathbf t\notin\mathcal U_{Y,\kappa}}
\frac{|\mathscr T_{r,Y}(\sigma+i\mathbf t)|}
     {\prod_i(1+|t_i|)^B}
\ \ge\
Y^{-C_B}
\exp\!\left(\frac{cY^{1-2\sigma}}{\log Y}\right).
}
\tag{1.12}
\]
In particular (1.11) is false. Even replacing \(D^\epsilon\) in CT1
by an arbitrary fixed power \(D^A\) does not repair it.

The theorem applies to each fixed order separately. It uses no
uniformity as \(k\) grows. The row height \(H=(Y/b)^h\) is polynomial
and is absorbed in the polynomial factors in the proof.

## 2. Analytic bounds and the unchanged paid tube

For each fixed finite \(Y\), (1.8) is holomorphic in
\(\Re s_i>0\). Indeed every denominator in (1.7) is nonzero there.
On the closed polyhalf-plane \(\Re s_i\ge\sigma\), ideal counting and
the finite prime product give a bound of the form
\[
|\mathscr T_{r,Y}(\mathbf s)|
\le C H Y^C\exp(CY^{1-\sigma})=:M_Y,
\tag{2.1}
\]
uniformly in every imaginary part and every larger real part. The
constant \(M_Y\) is finite for each \(Y\), which is all that is needed
in the half-plane maximum principles below.

For clarity, one may bound each short polynomial by
\[
\sum_{Nn\le Y}(Nn)^{-\sigma}\ll Y^{1-\sigma}.
\tag{2.2}
\]
The absolute numerator and inverse-denominator products in (1.7)
are at most
\[
\prod_{Np\le Y}
\frac{1+r(Np)^{-\sigma}}{(1-(Np)^{-\sigma})^r}
\le \exp\!\left(C\sum_{Np\le Y}(Np)^{-\sigma}\right)
\le\exp(CY^{1-\sigma}).
\tag{2.3}
\]
Deleting primes only decreases this common majorant. Schwartz
lattice counting gives
\[
\sum_{u\ne0}\Phi(u/\sqrt H)\ll_\Phi H.
\tag{2.4}
\]
These uniform majorants also justify normal convergence of the row
sum on compact subsets of the stated analytic domain.

The source's negligible tube is preserved. Here is a direct proof
of the part needed in this note. At an eligible prime \(q=Np\),
write \(z_i=q^{-\sigma}v_i\). In the tube (1.10), each of the \(k^2\)
cross pairs has real part at least \(\cos(2\kappa)\) after removing
the factor \(q^{-2\sigma}\); the \(k(k-1)\) same-side pairs have
real part at least \(-1\) each. Hence
\[
\Re\sum_{i<j}v_i v_j
\ge k^2\cos(2\kappa)-k(k-1)
=:\lambda>0.
\tag{2.5}
\]
By (1.3), the local logarithms in (1.7) can be expanded uniformly:
\[
\log\frac{1-\sum_i z_i}{\prod_i(1-z_i)}
=-\sum_{i<j}z_i z_j+O_r(q^{-3\sigma}).
\tag{2.6}
\]
The error sums absolutely because \(3\sigma>1\). Thus
\[
|\mathcal Q_{r,Y,P,u}|
\le C\exp\!\left(-\lambda
   \sum_{\substack{p\notin SPu\\Np\le Y}}(Np)^{-2\sigma}\right).
\tag{2.7}
\]
Here and below \(p\notin SPu\) means that \(p\) belongs to none of
the fixed or row-prime exclusions.

We use the classical prime-ideal theorem only in its unconditional
form \(\pi_K(x)\sim x/\log x\). Partial summation gives
\[
\sum_{\substack{p\notin SP\\Np\le Y}}(Np)^{-2\sigma}
\sim \frac{Y^{1-2\sigma}}{(1-2\sigma)\log Y}.
\tag{2.8}
\]
For each fixed \(\delta>0\),
\[
\sum_{p\mid u}(Np)^{-2\sigma}
\le C_\delta+\delta\log Nu,
\tag{2.9}
\]
by comparing each sufficiently large summand with
\(\delta\log Np\); the remaining finite prime set contributes a
constant. Consequently (2.7), (2.2), and the Schwartz row sum imply
\[
\sup_{\mathbf t\in\mathcal U_{Y,\kappa}}
|\mathscr T_{r,Y}(\sigma+i\mathbf t)|
\ll_{M} H Y^{-M}\qquad(M>0).
\tag{2.10}
\]
The arbitrary central frequency causes no loss. The positive
power \(Y^{1-2\sigma}/\log Y\) in the exponential dominates every
fixed polynomial cost, including the row-mask factor from (2.9).

Equation (2.10) is consistent with the pinned wide-tube theorem.
The refutation concerns its proposed pointwise complement.

## 3. The exact two-slot principal Euler factor

First work with one left slot and one right slot, but with exactly
the same fixed \(P,S,\nu,\Phi,H\). Set
\[
s_Y(z)=\sigma+\frac{iz}{\log Y},
\tag{3.1}
\]
where \(z\) is complex. Define
\[
F_Y(s)=\prod_{\substack{p\notin SP\\Np\le Y}}
                    (1-(Np)^{-2s}).
\tag{3.2}
\]
For a prime not dividing \(u\), put \(a=\eta_u(p)\) and \(x=q^{-s}\).
The exact local identity is
\[
\frac{1-(a+\bar a)x}{(1-ax)(1-\bar a x)}
=(1-x^2)E_p(a,x),
\tag{3.3}
\]
where
\[
E_p(a,x)=
\frac{1-(a+\bar a)x}
     {(1-ax)(1-\bar a x)(1-x^2)}.
\tag{3.4}
\]
The coefficients of degrees one and two in \(E_p-1\) vanish.
Uniformly for \(|a|=1\) and \(\Re s\ge\sigma_0\), (1.3) therefore
gives
\[
E_p(a,q^{-s})=1+O(q^{-3\sigma_0}).
\tag{3.5}
\]
All local numerators and denominators are bounded away from zero.
The finite products
\[
E_{Y,u}(s)=
\prod_{\substack{p\notin SPu\\Np\le Y}}
                         E_p(\eta_u(p),(Np)^{-s})
\tag{3.6}
\]
are consequently bounded above and below by positive fixed constants
in modulus on \(\Re s\ge\sigma_0\). The bounds are uniform in \(Y,u\)
and every imaginary part.

At a row-prime \(p\mid u\), the original collision factor is one.
Its exact restoration after extracting the universal (3.2) is
\[
R_{Y,u}(s)=
\prod_{\substack{p\mid u,\ p\notin SP\\Np\le Y}}
                         (1-(Np)^{-2s})^{-1}.
\tag{3.7}
\]
For every \(\delta>0\), uniformly on \(\Re s\ge\sigma_0\),
\[
|R_{Y,u}(s)|\ll_{\delta,\sigma_0}(Nu)^\delta.
\tag{3.8}
\]
This follows by bounding each sufficiently large prime factor by
\((Np)^\delta\), and paying the finitely many others once. In
particular no row-prime zero is changed to one without its exact
factor (3.7).

Write \(T_{+,Y,u}\) and \(T_{-,Y,u}\) for (1.6) with characters
\(\eta_u\) and \(\bar\eta_u\). Then
\[
\boxed{
\mathscr T_{2,Y}(s_Y(z),s_Y(z))
=F_Y(s_Y(z))G_Y(z),
}
\tag{3.9}
\]
with
\[
G_Y(z)=
\sum_{u\ne0}\Phi(u/\sqrt H)\mathbf1_{(u,P)=1}
 R_{Y,u}(s_Y(z))E_{Y,u}(s_Y(z))
 T_{+,Y,u}(s_Y(z))T_{-,Y,u}(s_Y(z)).
\tag{3.10}
\]
This is an identity on the complete physical row set.

### Lemma 3.1. Polynomial analytic bound for the residual trace

There are fixed \(C,C_1\) such that, for all sufficiently large \(Y\),
\[
G_Y\text{ is holomorphic on a neighborhood of }|z|\le4,
\qquad
\max_{|z|\le4}|G_Y(z)|\le C Y^{C_1}.
\tag{3.11}
\]

**Proof.** For large \(Y\), \(|z|\le4\) implies
\(\Re s_Y(z)\ge\sigma_0\). The products (3.6) are uniformly bounded,
and (3.8) retains the row-prime correction. The short factors are
bounded by \(CY^{1-\sigma_0}\). For fixed \(\delta>0\), Schwartz
lattice counting gives
\[
\sum_{u\ne0}\Phi(u/\sqrt H)(Nu)^\delta
\ll_{\Phi,\delta}H^{1+\delta}.
\tag{3.12}
\]
This proves (3.11), since \(H=(Y/b)^h\), and supplies a uniform
summable majorant for holomorphy. The same argument applies on a
slightly larger \(z\)-disk once \(Y\) is large enough. \(\square\)

### Lemma 3.2. Positive real-axis values on infinitely many cutoffs

There is a constant \(c_0>0\) and an unbounded sequence of
\[
Y\in\{p^2-\tfrac12,\ p^2\},
\tag{3.13}
\]
with \(p\) good rational primes, such that
\[
\boxed{G_Y(0)\ge c_0Y^{-2\sigma}.}
\tag{3.14}
\]

**Proof.** At \(z=0\), \(s_Y(0)=\sigma\) is real. At each nonzero
local phase \(a\),
\[
1-(a+\bar a)q^{-\sigma}
=1-2\Re(a)q^{-\sigma}>0
\]
by the fixed cutoff (1.3). The other real factors in (3.4) are
\(|1-aq^{-\sigma}|^2>0\) and \(1-q^{-2\sigma}>0\).
Hence \(E_{Y,u}(\sigma)>0\), and (3.7) is positive. Also
\[
T_{-,Y,u}(\sigma)=\overline{T_{+,Y,u}(\sigma)}.
\]
Every row summand in (3.10) is nonnegative.

The unit row \(u=1\) is retained by the exact \(P\)-mask. Its short
polynomial is the literal norm truncation
\[
U_Y=\sum_{\substack{Nn\le Y\\(n,SP)=1}}
                 \mu_K(n)\nu(n)(Nn)^{-\sigma}.
\tag{3.15}
\]
At a good rational prime \(p\), the total coefficient of norm
\(p^2\) has modulus one. If \(p\) is inert, the only ideal of norm
\(p^2\) is the prime ideal \((p)\), with coefficient \(-\nu((p))\).
If \(p\) splits as \(\mathfrak p\bar{\mathfrak p}\), the three
ideals of norm \(p^2\) are
\(\mathfrak p^2,\mathfrak p\bar{\mathfrak p},
\bar{\mathfrak p}^{\,2}\); the two squares have zero Möbius
coefficient and the middle ideal contributes \(+\nu((p))\).
The ramified rational prime is excluded. Good primes also avoid
the finitely many rational primes below \(SP\), so
\(|\nu((p))|=1\).

Thus
\[
|U_{p^2}-U_{p^2-1/2}|=p^{-2\sigma}.
\tag{3.16}
\]
At least one of these two values has modulus at least
\(\tfrac12p^{-2\sigma}\). There are infinitely many good rational
primes, so these choices give an unbounded sequence (3.13).

For the unit row, \(R_{Y,1}=1\) and \(E_{Y,1}(\sigma)\) is bounded
below uniformly by (3.5). Further,
\(\Phi(1/\sqrt H)\ge\Phi(0)/2\) for sufficiently large \(Y\).
Its one nonnegative summand in (3.10) is therefore at least
\(c p^{-4\sigma}\), which is comparable to \(Y^{-2\sigma}\).
All other rows can be retained. This proves (3.14).

The argument uses the actual fixed \(\nu\). It uses neither a
Liouville substitution nor a character selected anew with \(Y\).
\(\square\)

## 4. An elementary analytic propagation lemma

Let
\[
I=[1,5/4],\qquad \rho=5/11<1.
\tag{4.1}
\]
Suppose \(f_Y\) is holomorphic on a neighborhood of \(|z|\le4\),
\[
\max_{|z|\le4}|f_Y(z)|\le C Y^{C_1},
\qquad |f_Y(0)|\ge cY^{-C_0}.
\tag{4.2}
\]
Then some \(x_Y\in I\) satisfies
\[
|f_Y(x_Y)|\ge Y^{-C_2},
\tag{4.3}
\]
for a fixed finite \(C_2\), after increasing the lower threshold
for \(Y\).

Here is the quantitative interpolation proof. Take \(n\ge2\)
equally spaced nodes \(x_1,\ldots,x_n\) in \(I\), including its
endpoints. Let \(L_j\) be the Lagrange basis. With
\(\ell=1/4\) and \(b_I=5/4\),
\[
\sum_{j=1}^n|L_j(0)|
\le
\frac{(b_I(n-1)/\ell)^{n-1}2^{n-1}}{(n-1)!}
\le(10e)^{n-1}.
\tag{4.4}
\]
The first inequality uses the exact denominator
\((\ell/(n-1))^{n-1}(j-1)!(n-j)!\); the second is
\((n-1)!\ge((n-1)/e)^{n-1}\).

Cauchy's interpolation remainder on \(|\zeta|=4\) gives
\[
f_Y(0)-\sum_jf_Y(x_j)L_j(0)
=\frac{1}{2\pi i}\int_{|\zeta|=4}
\frac{f_Y(\zeta)}{\zeta}
\frac{\prod_j(-x_j)}{\prod_j(\zeta-x_j)}\,d\zeta.
\tag{4.5}
\]
Since \(|x_j|\le5/4\) and
\(|\zeta-x_j|\ge4-5/4=11/4\), its modulus is at most
\[
C Y^{C_1}\rho^n.
\tag{4.6}
\]
Choose
\[
n=\left\lceil
\frac{(C_1+C_0+2)\log Y}{\log(11/5)}
\right\rceil,
\tag{4.7}
\]
increasing it by a fixed constant if needed for \(C,c\).
Then the remainder is at most
\(\tfrac12cY^{-C_0}\). Equations (4.4)--(4.6) imply
\[
\max_j|f_Y(x_j)|
\ge \frac{cY^{-C_0}}{2(10e)^{n-1}},
\tag{4.8}
\]
which is a negative fixed power of \(Y\). This proves (4.3).
No derivative estimate for a moving truncation is used.

Apply this lemma to (3.11) and (3.14). Along their unbounded
sequence there are \(x_Y\in I\) such that
\[
|G_Y(x_Y)|\ge Y^{-C_2}.
\tag{4.9}
\]

## 5. Universal Euler growth away from the conjugate tube

Put \(\alpha=2\sigma\in(2/3,1)\). Uniformly for \(x\in I\), the
classical prime-ideal theorem and partial summation give
\[
\sum_{\substack{p\notin SP\\Np\le Y}}
(Np)^{-\alpha}
\exp\!\left(-2ix\,\frac{\log Np}{\log Y}\right)
=
\left(e^{-2ix}+o(1)\right)
\frac{Y^{1-\alpha}}{(1-\alpha)\log Y}.
\tag{5.1}
\]
To verify the uniform phase replacement, first discard
\(Np\le\delta Y\). Its weighted mass, relative to the right-hand
scale, tends to \(\delta^{1-\alpha}\). On the remaining primes
\(\log(Np)/\log Y\to1\) uniformly for fixed \(\delta>0\), uniformly
also in \(x\in I\). Let \(Y\to\infty\), then \(\delta\downarrow0\).
The finite exclusions in \(SP\) do not change the asymptotic.

Because \(2\alpha>1\), the quadratic remainder in the local logarithm
sums to \(O(1)\). Consequently
\[
\begin{aligned}
\log|F_Y(s_Y(x))|
&=-\Re\sum_{\substack{p\notin SP\\Np\le Y}}
       (Np)^{-\alpha}
       e^{-2ix\log(Np)/\log Y}+O(1)\\
&=\left(-\cos(2x)+o(1)\right)
       \frac{Y^{1-\alpha}}{(1-\alpha)\log Y}.
\end{aligned}
\tag{5.2}
\]
On \(I=[1,5/4]\), \(-\cos(2x)\ge-\cos2>0\).
Thus for a fixed \(c>0\),
\[
\boxed{
|F_Y(s_Y(x))|
\ge\exp\!\left(\frac{cY^{1-2\sigma}}{\log Y}\right)
\quad(x\in I)
}
\tag{5.3}
\]
for all sufficiently large \(Y\).

Combining (3.9), (4.9), and (5.3) proves the two-slot bound
\[
\boxed{
|\mathscr T_{2,Y}(s_Y(x_Y),s_Y(x_Y))|
\ge Y^{-C_2}
\exp\!\left(\frac{cY^{1-2\sigma}}{\log Y}\right)
}
\tag{5.4}
\]
along an unbounded sequence.

Both slot frequencies here equal \(x_Y/\log Y\). Their signs are
the same. They do not lie on a common-conjugate tube of allowed
width: such a tube would require \(x_Y\le\kappa\), whereas
\(x_Y\ge1>\pi/4\ge\kappa\) in the two-slot case.

This is a lower bound on the complete native signed row trace.
It was not obtained by replacing the signed row sum by a sum of
absolute values, or by deleting all but the unit row at nonreal
frequencies. The unit row is used only at the positive real point
to anchor the analytic propagation argument.

## 6. Collapse every higher-order trace to the two-slot face

The case \(k=1\) is already proved by Section 5 and the tube estimate
(2.10). In this section assume \(k\ge2\), so \(r\ge4\).

For fixed \(B\ge0\), let
\[
\mathfrak M_B(Y)=
\sup_{\mathbf t\in\mathbb R^r}
\frac{|\mathscr T_{r,Y}(\sigma+i\mathbf t)|}
     {\prod_i(1+|t_i|)^B}.
\tag{6.1}
\]
It is finite by (2.1). Choose a fixed integer \(J>B\), for example
\(J=\lceil B\rceil+1\).

### Lemma 6.1. Right-half-plane extension of the boundary bound

Keep slots \(1\) and \(k+1\) on the line \(\Re s=\sigma\), and set
all other slots equal to a real \(L\ge\sigma\). Then
\[
\begin{aligned}
&|\mathscr T_{r,Y}
  (\sigma+it_1,L,\ldots,\sigma+it_{k+1},L,\ldots)|\\
&\qquad\le
C_{r,B,\sigma}\,\mathfrak M_B(Y)
(1+L)^{J(r-2)}
(1+|t_1|)^B(1+|t_{k+1}|)^B.
\end{aligned}
\tag{6.2}
\]

**Proof.** Freeze every other variable on its boundary line and
consider the function \(f(s)\) of one slot to be moved. It is
holomorphic for \(\Re s>\sigma\), continuous at its boundary, and
bounded by the finite \(M_Y\) on the right half-plane. The quotient
\[
\frac{f(s)}{(1+s)^J}
\tag{6.3}
\]
is holomorphic there and tends to zero on the large right
semicircles, since \(f\) is bounded for this fixed \(Y\).
On \(s=\sigma+it\), (6.1) bounds (6.3) by
\[
C_{B,\sigma}\mathfrak M_B(Y)
\prod_{\text{other slots}}(1+|t_i|)^B.
\]
The half-plane maximum principle gives the same bound inside.
Evaluate at \(s=L\), costing \((1+L)^J\).

Repeat in each of the other \(r-3\) slots to be moved. At each
step (2.1) still supplies a finite right-half-plane bound, while
the preceding steps supply the boundary bound with the already
paid factors. This yields (6.2).

The limit of semicircle radii is taken for each fixed \(Y\).
No uniform bound on \(M_Y\) as \(Y\to\infty\), and no exchange of
that limit with the prime cutoff, is assumed. \(\square\)

### Lemma 6.2. Exponential accuracy of the two-slot face

Set \(L=Y\). For arbitrary real \(t_1,t_{k+1}\),
\[
\begin{aligned}
&\mathscr T_{r,Y}
  (\sigma+it_1,Y,\ldots,\sigma+it_{k+1},Y,\ldots)\\
&\qquad=
\mathscr T_{2,Y}(\sigma+it_1,\sigma+it_{k+1})
+O(H e^{-c_1Y})
\end{aligned}
\tag{6.4}
\]
for some \(c_1>0\). The error is uniform across all physical rows
before Schwartz summation.

**Proof.** For a slot moved to \(Y\), its literal short polynomial
satisfies
\[
T_{i,Y,u}(Y)=1+O(Y2^{-Y})
\tag{6.5}
\]
uniformly in \(u\), since there are \(O(Y)\) integral ideals of
norm at most \(Y\), and every nonunit ideal has norm at least two.
The character zeros can only decrease this positive error bound.

At a prime \(q\le Y\), every additional local variable has modulus
at most \(q^{-Y}\). If \(z,z'\) are the two retained variables, the
local collision quotient in (1.7) differs from
\[
\frac{1-z-z'}{(1-z)(1-z')}
\tag{6.6}
\]
by \(O_r(q^{-Y})\), uniformly for
\(|z|,|z'|\le q^{-\sigma}\). The fixed cutoff (1.3) keeps the
denominators uniformly away from zero.

Telescoping the finite products, using the common product majorant
(2.3), bounds their difference by
\[
C Y2^{-Y}\exp(CY^{1-\sigma}).
\tag{6.7}
\]
Multiplying the two retained short polynomials costs at most a
fixed power of \(Y\), and the other short factors satisfy (6.5).
Since \(Y^{1-\sigma}=o(Y)\), the complete per-row error is
\(O(e^{-c_1Y})\) after reducing \(c_1\).

The exterior factor (1.5) is unchanged. Summing its modulus
against the original Schwartz weight costs \(O(H)\) by (2.4).
Every row is retained, with no cutoff depending on its conductor.
This proves (6.4). \(\square\)

Use the point supplied by (5.4) in (6.2)--(6.4). Its two retained
frequencies are bounded by \(5/(4\log Y)\), so their polynomial
weights are bounded. The exponentially small error in (6.4) is
negligible beside (5.4). Therefore
\[
\mathfrak M_B(Y)
\ge
Y^{-C_{r,B}}
\exp\!\left(\frac{cY^{1-2\sigma}}{\log Y}\right)
\tag{6.8}
\]
along the unbounded sequence.

Finally (2.10) bounds the weighted supremum on
\(\mathcal U_{Y,\kappa}\) by \(O_M(HY^{-M})\). It cannot supply
(6.8). The same lower bound must hold for the complementary
supremum. This is Theorem 1.1. \(\square\)

## 7. What the refutation changes

The claim being refuted is stronger than the tested physical
moment in two essential ways.

First, CT1 takes a pointwise absolute value in all independent
Mellin frequencies. The source norm tests have not yet been
inserted. Second, it uses the finite rational collision factor
after replacing the single-slot finite Euler products by short
Möbius polynomials. That replacement is exact only after the
coefficient norm filter, as the source itself states.

The universal factor \(F_Y\) in (3.2) is strongly suppressed on
the conjugate tube and strongly amplified on the same-direction
interval in Section 5. This behavior is a property of that
unfiltered representation. It is not a growing native physical
moment.

In particular:

- The exact finite ideal-coefficient identity SC4 survives.
- The negligible tube component SC7 and WT5 survives.
- The source's independent-frequency CT1 is false at every fixed
  order, even with any fixed additional power loss.
- The conditional deduction CT1 \(\Rightarrow\) a diagonal
  moment remains logically correct but cannot establish that
  moment for this family.
- No failure of the actual second, fourth, or generalized native
  moment follows from this note.
- The earlier source-realizable indefinite finite kernels remain
  separate evidence; this proof does not rely on those numerical
  witnesses or their row windows.

A replacement must retain the physical coefficient norm filter,
or preserve a signed integration in the independent Mellin
frequencies, before asserting the conclusion-facing absolute
bound. Dividing out \(F_Y\) alone does not solve the problem: its
exact pair-coordinate convolution has to be restored when the
physical norm tests are applied.

The companion compression analysis treats that finite
coefficient operation separately. Its coefficient-norm bounds
must not be confused with the impossible unfiltered pointwise
bound refuted here.

## 8. Source pins and validation boundary

The exact historical repository source is PR #911, commit

    2f8b6a3898a722d0602a91dea73bac344a3bb7dd

under

    research/exploratory/2026-10-10-two-hour-continuation/literature/

The files were read at that commit, without modifying their bytes.

| File | Exact interface used | SHA-256 |
|---|---|---|
| PRIME_SLOT_CANCELLATION.md | P1--P4 family and Euler identity; P8 incidence allocation and trace quantifiers | d37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13 |
| SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md | SC1--SC4 literal short trace and coefficient-filtered identity; SC7 scoped negligible component | c538719277b1e7de70a7e3f872fb2720668bd43ca57c9cffff6ff29b6766d5ac |
| WIDE_SUBCRITICAL_TUBE.md | WT1--WT5 precise common-conjugate tube | 53568631060432784811d8474e8d774257664826e8fb9fa59c0ba47959745f02 |
| COMPLEMENTARY_SHORT_TRACE_CONTRACT.md | CT1 in Section CT2, and the conditional CT4--CT6 deductions | 968a2bee6d47f0a92fded0ab32c23963d31332f649dc0046604b7b568d48640c |
| PRIME_SLOT_ROUTE_STATUS.md | Historical status of the complementary trace as open | a03572f0f7be44bdd40befe2c86290095b54f84f2ba48f3e35a980f1e3a4fdde |

The only prime-distribution input is the classical unconditional
prime-ideal theorem
\(\pi_K(x)\sim x/\log x\), used in (2.8) and (5.1).
A primary proof reference personally inspected for this pass is
Sami Omar, *A note on the Prime Ideal Theorem*, Corollary 1:

https://www.wseas.us/e-library/conferences/corfu2004/papers/488-336.pdf

Only its classical prime-counting asymptotic is used. No GRH
error term, quasi-Riemann zero-free improvement, conductor-uniform
prime theorem, or cancellation estimate for the moving native
characters is imported. The remaining analytic ingredients are
ordinary ideal/lattice counting, elementary local Taylor
expansions, Cauchy interpolation, and the half-plane maximum
principle, with their needed proofs supplied above.

This note is a mathematical argument, not a proof by finite
enumeration. No zero computation, unbounded-order numerical
extrapolation, Lean replay, or original upstream proof
reproduction was performed. Independent review and exact source
commit receipts belong to the enclosing packet's validation
record; they do not turn the open physical moment into a theorem.
