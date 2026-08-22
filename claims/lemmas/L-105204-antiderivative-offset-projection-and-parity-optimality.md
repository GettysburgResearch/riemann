# L-105204 — The antiderivative constant is one orthogonal residue mode, and odd antiderivatives are automatically optimal

Claim ID: `L-105204`  
Status: **PROVED EXACT FINITE-POLYNOMIAL THEOREM**  
Created: 2026-08-23  
Depends on: `L-104522`; `L-105100--L-105201`  
RH status: **not assumed**

Let `q` be a real polynomial of degree `m>=2` with simple real zeros

\[
c_1,\ldots,c_m.
\]

Fix one antiderivative `p_0` of `q`, and put

\[
p_C=p_0+C
\qquad(C\in\mathbb R).
\]

At the critical points define

\[
\rho_j(C)=\frac{p_C(c_j)}{q'(c_j)},
\qquad
b_j=\frac1{q'(c_j)}.
\tag{L-105204.1}
\]

Thus

\[
\rho(C)=\rho(0)+Cb
\tag{L-105204.2}
\]

as vectors in `R^m`.

## 1. The total first residue moment is constant-independent

The partial fraction expansion

\[
\frac1{q(z)}=\sum_{j=1}^m\frac{b_j}{z-c_j}
\]

has no `z^-1` term at infinity because `m>=2`. Therefore

\[
\boxed{
\sum_{j=1}^m b_j=0.
}
\tag{L-105204.3}

Consequently

\[
\boxed{
\sum_j\rho_j(C)=\sum_j\rho_j(0)
}
\tag{L-105204.4}

for every antiderivative constant. The constant can change the second residue
moment, but cannot create the negative first-moment carrier used by reverse
Rolle.

## 2. Exact orthogonal projection

Put

\[
D_0=\sum_jb_j^2>0,
\qquad
D_1=\sum_j\rho_j(0)b_j.
\]

The unique least-squares optimal antiderivative constant is

\[
\boxed{
C_*=-\frac{D_1}{D_0}.
}
\tag{L-105204.5}

Indeed,

\[
\boxed{
\sum_j\rho_j(C)^2
=
\sum_j\rho_j(C_*)^2
+D_0(C-C_*)^2.
}
\tag{L-105204.6}

Thus the entire constant dependence of the second residue moment is one
rank-one orthogonal mode.

Let

\[
A=-\sum_j\rho_j(C),
\]

which is independent of `C`. Whenever `A>0`, define

\[
\mathfrak C(C)=
\frac{A^2}{m\sum_j\rho_j(C)^2}.
\]

Then

\[
\boxed{
\mathfrak C(C)\le\mathfrak C(C_*),
}
\tag{L-105204.7}

and exactly

\[
\boxed{
\frac1{\mathfrak C(C)}
=
\frac1{\mathfrak C(C_*)}
+
\frac{mD_0}{A^2}(C-C_*)^2.
}
\tag{L-105204.8}

This separates the residue-coherence problem into:

```text
shape energy orthogonal to the barycentric mode b;
one scalar antiderivative-offset defect.
```

## 3. Parity-optimality

Suppose `q` is even and `p_0` is its odd antiderivative with `p_0(0)=0`.
The roots occur in pairs `+/-c`. Since `q'` and `p_0` are both odd,

\[
b(-c)=-b(c),
\qquad
\rho(0;-c)=\rho(0;c).
\]

Hence

\[
D_1=0
\]

by pair cancellation. Therefore

\[
\boxed{C_*=0.}
\tag{L-105204.9}

The parity-normalized odd antiderivative already minimizes the second residue
moment among all antiderivatives of `q`.

Applied to the Xi derivative ladder, every step whose parent
`Xi^(k-1)` is odd has no additive-offset loss. Only the alternating even-parent
steps carry the scalar defect in (L-105204.6).

## 4. Relation to the next derivative level

Let now `p` have degree `n>=5`, put `q=p'`, and retain simple zeros of `p'` and
`p''`. Residue calculus applied to

\[
\frac1{p'p''}
\]

and

\[
\frac p{p'p''}
\]

gives

\[
\boxed{
D_0
=
-\sum_{p''(d)=0}
\frac1{p'(d)p'''(d)},
}
\tag{L-105204.10
}

and

\[
\boxed{
\sum_{p'(c)=0}\frac{p(c)}{p''(c)^2}
=
-\sum_{p''(d)=0}
\frac{p(d)}{p'(d)p'''(d)}.
}
\tag{L-105204.11
}

There is no residue at infinity in these degree ranges. Thus the scalar
projection coefficient `C_*` itself is a ratio of two explicit next-level
cross-residue ledgers.

## 5. Meaning and scope

This theorem does not bound the shape energy or the even-level offset. It proves
that the latter is only one scalar, vanishes on every odd-parent Xi step, and
is encoded by the next derivative level. A low-band cascade may therefore
attack alternating parity steps differently rather than estimating one opaque
second moment at every level.
