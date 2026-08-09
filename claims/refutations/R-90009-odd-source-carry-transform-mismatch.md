# R-90009 — The odd-source carry in L-34406 is a prefix defect, not a second carry transform

Claim ID: `R-90009` (provisional range; allocate before integration)  
Status: **EXACT REFUTATION OF THE DISPLAYED CARRY FORMULA + REPAIR OF THE RELATIVE CENTERING**  
Authoring agent: `gpt56-sol`  
Date: 2026-08-09  
Targets: PR #346 `L-34406` §§2–6  
Scope: corrects the odd-source bare coordinate. It does not refute `L-34404`'s odd-prime reserve increment.

## 1. The incorrect inference

PR #346 `L-34406` defines
\[
B_{\rm odd}(s)=\prod_{p\ {m odd}}(1-p^{-s})
=\sum_n b_{\rm odd}(n)n^{-s},
\]
so
\[
b_{\rm odd}(n)=\mu(n)\mathbf 1_{2\nmid n}.
\]
It correctly observes
\[
\boxed{
\mathbf1*b_{\rm odd}=\sum_{r\ge0}\delta_{2^r}.
}
\tag{R-90009.1}
\]
The file then infers
\[
\mathcal L_{n,j}(b_{\rm odd})
\stackrel{\rm claimed}=\sum_{r\ge1}\chi_{n,2^r}(j).
\tag{R-90009.2}
\]
That step is false.

For the carry functional used throughout the Q4 graph,
\[
\mathcal L_{n,j}(f)
=\sum_{d\le n}f(d)\chi_{n,d}(j),
\]
`L-34001` gives the exact prefix identity
\[
\mathcal L_{n,j}(f)
=C_f(n)-C_f(j)-C_f(n-j),
\qquad
C_f(x)=\sum_{m\le x}(\mathbf1*f)(m).
\tag{R-90009.3}
\]
Thus (R-90009.1) must be **prefix-summed once**, not inserted into a second carry transform.

## 2. Correct odd bare charge

Put
\[
C_2(x)=\#\{r\ge0:2^r\le x\}.
\]
Then
\[
C_2(0)=0,
\qquad
C_2(x)=1+\lfloor\log_2x\rfloor\quad(x\ge1).
\tag{R-90009.4}
\]
Therefore the correct odd-source carry is
\[
\boxed{
Y_{\rm odd}(n,j)
=C_2(n)-C_2(j)-C_2(n-j).
}
\tag{R-90009.5}
\]
For a nontrivial split `n=j+k` with `j,k>=1`,
\[
\boxed{
Y_{\rm odd}(n,j)
=\lfloor\log_2n\rfloor
-\lfloor\log_2j\rfloor
-\lfloor\log_2k\rfloor-1.
}
\tag{R-90009.6}
\]
In particular the sign assertion `Y_odd>=0` in `L-34406` is also false.

A one-line counterexample to (R-90009.2) is
\[
(n,j,k)=(10,3,7).
\]
Equation (R-90009.6) gives
\[
Y_{\rm odd}(10,3)=3-1-2-1=-1,
\]
whereas
\[
\chi_{10,2}(3)+\chi_{10,4}(3)+\chi_{10,8}(3)=1+1+1=3.
\]

## 3. Exact dyadic scaling law

For every integer `m>=0`,
\[
C_2(2^m x)=C_2(x)+m
\qquad(x\ge1).
\]
Hence for every nontrivial split
\[
\boxed{
Y_{\rm odd}(2^m n,2^m j)
=Y_{\rm odd}(n,j)-m.
}
\tag{R-90009.7}
\]
In particular
\[
Y_{\rm odd}(2n,2j)=Y_{\rm odd}(n,j)-1,
\tag{R-90009.8}
\]
\[
Y_{\rm odd}(4n,4j)=Y_{\rm odd}(n,j)-2.
\tag{R-90009.9}
\]
Thus the scale-four invariance asserted in `L-34406.10` is false.

## 4. Source-level interpretation

Write `z=2^{-s}`. Since
\[
(1-z)B_{\rm odd}(s)=\frac1{\zeta(s)},
\]
one has exactly
\[
\boxed{
(\varepsilon-\delta_2)*b_{\rm odd}=\mu.
}
\tag{R-90009.10}
\]
For a nontrivial row,
\[
\mathcal L_{n,j}(\mu)=-1,
\tag{R-90009.11}
\]
because `1*mu=epsilon` and the prefix of `epsilon` equals one at each positive endpoint. Therefore
\[
\mathcal L_{2n,2j}((\varepsilon-\delta_2)*b_{\rm odd})=-1,
\]
which is the same statement as (R-90009.8).

Likewise
\[
(\varepsilon-\delta_4)*b_{\rm odd}
=(\varepsilon+\delta_2)*\mu,
\tag{R-90009.12}
\]
so on an aligned nontrivial scale-four row
\[
\boxed{
\mathcal L_{4n,4j}((\varepsilon-\delta_4)*b_{\rm odd})=-2.
}
\tag{R-90009.13}
\]

## 5. The cross-free idea is repairable by exact centering

Let
\[
J_{{\rm odd},\tau}(s)=\frac{A_{\rm odd}(s-\tau)}{A_{\rm odd}(s)},
\qquad
K_{{\rm odd},\tau}=b_{\rm odd}*J_{{\rm odd},\tau}.
\]
The uncentered source-difference leg used by `L-34406` is
\[
G_e^{(4)}(\tau)
=\mathcal L_{4e}((\varepsilon-\delta_4)*K_{{\rm odd},\tau}).
\]
Equation (R-90009.13) gives
\[
G_e^{(4)}(0)=-2,
\]
not zero.

However the **centered** leg
\[
\boxed{
\widetilde G_e^{(4)}(\tau)
=2+\mathcal L_{4e}((\varepsilon-\delta_4)*K_{{\rm odd},\tau})
}
\tag{R-90009.14}
\]
has
\[
\widetilde G_e^{(4)}(0)=0
\]
exactly. The added constant has zero first and second derivatives, so
\[
(\widetilde G_e^{(4)})'(0)
=Q_{\rm odd}(4e)-Q_{\rm odd}(e),
\]
and the second derivative is unchanged. Consequently, if the first scalar coordinate is the same relative Jordan ratio as in `L-34406`, the centered vector path has curvature
\[
\Delta_4R_{\rm odd}
+|Q_{\rm odd}(4e)-Q_{\rm odd}(e)|^2.
\tag{R-90009.15}
\]
So the attractive cross-free algebra can be salvaged, but **only after this explicit recentering**. The displayed proof and bare-charge interpretation in `L-34406` are not valid as written.

The scale-two version is even more natural and is developed in `L-90010`.

## 6. Boundary

Refuted exactly:

```text
L-34406.7  Y_odd = sum of dyadic carry columns
L-34406.10 scale-four invariance of Y_odd
L-34406.18 uncentered relative source coordinate equals zero
```

Retained:

```text
L-34404 odd-prime reserve definitions and scale-four asymptotics
odd-source factorization of the compact source
cross-free relative curvature after adding the exact constant +2
```

No RH conclusion is changed: RH remains unproved.