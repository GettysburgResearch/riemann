# T-28001 — Mersenne-collar fragmentation implies RH

Claim ID: `T-28001`  
Title: A nonnegative exact carry flow whose only negative eta-source load has subpower Mersenne mass proves the Riemann hypothesis  
Status: **FULL PROPOSED PROOF — `MCF` IS THE SINGLE OPEN FINITE THEOREM**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-28001`, `L-28002`; atomized carry/Pascal identities of PR #247; the standard one-sided Mellin–Landau theorem  
RH status: **not proved**

## 1. Exact carry-flow target

Fix an integer endpoint `X`. For

\[
2\le q\le n\le X,
\qquad
1\le j<n,
\]

let

\[
\chi_{n,q}(j)
=\left\lfloor\frac nq\right\rfloor
-\left\lfloor\frac jq\right\rfloor
-\left\lfloor\frac{n-j}{q}\right\rfloor
\in\{0,1\}.
\tag{T-28001.1}
\]

The critical all-integer target is

\[
w_X(q)=q^{-1/2}\log(X/q).
\tag{T-28001.2}
\]

## 2. Mersenne-Collar Fragmentation (`MCF`)

For every `epsilon>0` and all sufficiently large `X`, construct coefficients

\[
d_X(n,j)\ge0
\]

such that the following hold.

### 2.1 Exact saturation

\[
\boxed{
\sum_{n=q}^{X}\sum_{j=1}^{n-1}
 d_X(n,j)\chi_{n,q}(j)
=w_X(q)
\qquad(2\le q\le X).
}
\tag{T-28001.3}

### 2.2 Binary-window support

Let

\[
L(n)=2^{\lfloor\log_2n\rfloor}.
\]

If `n` is not a Mersenne integer, every active split satisfies

\[
\boxed{
n-L(n)<j<L(n).}
\tag{T-28001.4}

If

\[
n=2^r-1,
\]

only the two extreme splits are permitted:

\[
\boxed{j=1\quad\text{or}\quad j=n-1.}
\tag{T-28001.5}

### 2.3 Subpower Mersenne collar

Put

\[
\boxed{
\mathfrak M_X
=
\sum_{2^r-1\le X}
[d_X(2^r-1,1)+d_X(2^r-1,2^r-2)].
}
\tag{T-28001.6}

The required estimate is

\[
\boxed{
\mathfrak M_X\le C_\epsilon X^\epsilon.
}
\tag{T-28001.7}

Statements (T-28001.3)--(T-28001.7) are the **Mersenne-Collar Fragmentation theorem**.

## 3. Exact eta-source lower bound

Let `a_eta(q)` be the coefficient of `1/eta(s)` from `L-28001`, and put

\[
\mathcal R_\eta(X)
=
\sum_{q=2}^{X}
\frac{a_\eta(q)}{\sqrt q}
\log(X/q).
\tag{T-28001.8}

By exact saturation and finite interchange,

\[
\mathcal R_\eta(X)
=
\sum_{n,j}d_X(n,j)Y_n(j),
\tag{T-28001.9}

where `Y_n(j)` is the exact source profile of `L-28002`.

For every non-Mersenne active row, the support condition gives

\[
Y_n(j)\ge1.
\]

At a Mersenne row the two permitted extreme splits satisfy

\[
Y_n(j)=-1.
\]

Therefore

\[
\boxed{
\mathcal R_\eta(X)
\ge-\mathfrak M_X.
}
\tag{T-28001.10}

Under `MCF`, for every `epsilon>0`,

\[
\boxed{
\mathcal R_\eta(X)
\ge-C_\epsilon X^\epsilon.
}
\tag{T-28001.11}

No unsigned total-flow or carry-slack estimate is used.

## 4. Mellin transform

Initially for `Re(z)>1/2`, termwise integration gives

\[
\begin{aligned}
\int_1^\infty
\mathcal R_\eta(X)X^{-z-1}dX
&=
\frac1{z^2}
\sum_{q\ge2}\frac{a_\eta(q)}{q^{z+1/2}}\\
&=
\boxed{
\frac{\eta(z+1/2)^{-1}-1}{z^2}.
}
\end{aligned}
\tag{T-28001.12}

The Euler factor in `eta(s)` has zeros only on `Re(s)=1`, and zeta has no real zero in `(0,1)`. Hence the right side has no positive-real singularity other than the explicit boundary terms, while every hypothetical zeta zero

\[
\rho=\beta+i\gamma,
\qquad
\beta>1/2,
\]

produces an uncancelled pole at

\[
z=\rho-1/2.
\tag{T-28001.13}

## 5. One-sided Landau exclusion

Assume `MCF` and suppose an off-line zero has horizontal displacement

\[
\delta=\beta-1/2>0.
\]

Choose

\[
0<\epsilon<\delta.
\]

By (T-28001.11), for sufficiently large `X`,

\[
F_\epsilon(X)
:=\mathcal R_\eta(X)+C_\epsilon X^\epsilon
\ge0.
\]

Its Mellin transform is the right side of (T-28001.12), plus a function whose only new singularity is on the real line at `z=epsilon` and an entire compact-initial correction.

The pole at `z=delta+i\gamma` forces the abscissa of convergence of the nonnegative transform to be at least `delta`. Landau's one-sign theorem then forces a singularity at the real point `z=delta`. The explicit transform has no such real singularity. This is a contradiction.

Thus no zeta zero has real part greater than `1/2`. Functional-equation symmetry excludes zeros to the left of the critical line.

Therefore

\[
\boxed{
\mathrm{MCF}\Longrightarrow\mathrm{RH}.
}
\tag{T-28001.14}

## 6. Why this is a genuinely finite proposal

`MCF` asks for one finite nonnegative split flow at every endpoint. Its allowed support is explicit:

```text
central binary window on every ordinary row;
two extreme edges on the logarithmic Mersenne collar.
```

The target, carry indicators, support test, and collar mass are finite elementary objects involving floors, logarithms, square roots, and nonnegative real coefficients.

It is stronger than the current two-pass packing and weaker than unrestricted exact Carry Saturation in one important direction: it permits negative eta-source contribution, but only on `O(log X)` declared rows and charges only their actual flow mass.

## 7. Proposed construction

The intended producer is:

1. use the exact central residual for the first two positive stages;
2. route every later non-Mersenne divergence through the binary central window;
3. use Pascal four-cycles to move any exterior edge into that window without changing carry loads;
4. send unavoidable dyadic-boundary divergence to the two extreme Mersenne edges;
5. prove by half-scale descent that the total Mersenne edge mass is polylogarithmic.

The exact cycle and half-scale ledgers must be emitted. This construction is not completed in the current branch.

## 8. Automatic rejection

Reject an asserted `MCF` proof if it:

```text
uses a negative flow coefficient;
omits any carry column;
uses an exterior split on a non-Mersenne row;
uses a non-extreme split on a Mersenne row;
forgets one orientation of an extreme edge;
takes absolute values before Pascal-cycle recombination;
pays an undeclared power-sized Mersenne collar;
uses finite computation as the cofinal estimate;
fails the 2/3 Mertens mutation.
```

## 9. Exact status

```text
eta source / carry sign localization       proposed complete exact
MCF finite flow construction               open / RH-bearing
MCF -> eta Riesz lower envelope             complete conditional
eta Riesz lower envelope -> RH              complete conditional
Riemann Hypothesis                          unproved
```

This is the preferred elementary-facing completion target produced by the central-cascade audit.