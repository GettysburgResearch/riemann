# R-91310 — The proposed positive binary-return matrices overdraw the SHARP target

Claim ID: `R-91310`  
Status: **EXACT MATRIX COUNTEREXAMPLE / BLOCKING SCOPE CORRECTION**  
Created: 2026-08-13  
Refutes: PR #424 `L-91452` target-conservation identity and every descendant using the same matrices  
RH status: **unproved**

## 1. Advertised matrices

PR #424 `L-91452` defines, for `r=p^-1/2`,

\[
 C_r=(1-r)
 \begin{pmatrix}
 1+2r&0\\
 r&1-2r
 \end{pmatrix},
\tag{R-91310.1}
\]

\[
 H_r=r
 \begin{pmatrix}
 r&2(1-r)\\
 0&2-r
 \end{pmatrix}.
\tag{R-91310.2}
\]

It claims that the SHARP target functional

\[
 t=(1,2)
\]

is conserved:

\[
 t(C_r+H_r)=t.
\tag{R-91310.3-FALSE}
\]

## 2. Exact multiplication

Direct multiplication gives

\[
 tC_r
 =(1-r)(1+4r,\,2-4r),
\tag{R-91310.4}
\]

and

\[
 tH_r
 =(r^2,\,6r-4r^2).
\tag{R-91310.5}
\]

Therefore

\[
\boxed{
 t(C_r+H_r)
 =\bigl(1+3r-3r^2,\,2\bigr)
 =t+3r(1-r)(1,0).
}
\tag{R-91310.6}

For every `0<r<1`, the first target coefficient is strictly larger than one.
Thus the two positive branches overdraw the parent target whenever the input has
positive equality coordinate `L`.

The score calculation does not repair this.  With `s=(2,1)`,

\[
 s(C_r+H_r)
 =s+3r(1-r)(1,1),
\tag{R-91310.7}

so the same excess appears in the score ledger as well as in the target ledger.

## 3. Small exact witness

Take

\[
 r=\frac19,
 \qquad
 u=\binom10.
\]

Then the parent target is

\[
 tu=1,
\]

whereas the two branches have total target

\[
\boxed{
 t(C_{1/9}+H_{1/9})u
 =1+\frac13-\frac1{27}
 =\frac{35}{27}>1.
}
\tag{R-91310.8}

No floating computation is involved.

## 4. Stronger impossibility for the advertised survival matrix

The survival matrix alone already spends too much target on the pure `L` ray:

\[
 tC_re_1=(1-r)(1+4r)
 =1+3r-4r^2.
\]

For every

\[
 0<r<\frac34,
\]

and in particular for every rough prime `p>=67`, this exceeds one.  Hence no
entrywise-nonnegative hazard matrix can be added to this fixed survival matrix
and restore exact target conservation.

A repair must alter the survival matrix itself, not merely modify the hazard
branch.

## 5. Status effect

The following statements are blocked for the matrices (R-91310.1)--(R-91310.2):

```text
positive binary return is target exact                 FALSE
survival + hazard is a subpacket of one parent target FALSE
native three-ledger cocycle based on those matrices   BLOCKED
T-91561 composition using that target identity        BLOCKED
```

This counterexample does not refute:

```text
component-row identities independent of C_r,H_r;
exact nested detail targets Theta_Y;
finite Hall certificates for separately valid channels;
Riemann Hypothesis.
```

Any corrected binary return must satisfy target conservation before Hall,
row-score, capacity, or recursive arguments are applied.

## 6. Replay

The companion exact replay returns

```text
PASS_BINARY_RETURN_TARGET_OVERDRAW_COUNTEREXAMPLE
```

and checks (R-91310.6)--(R-91310.8) with `Fraction` arithmetic.

```text
matrix multiplication                              EXACT
universal target excess 3r(1-r)L                  EXACT
r=1/9 witness 35/27                               EXACT
positive hazard repair with fixed C_r             IMPOSSIBLE FOR r<3/4
corrected conservative binary matrices             OPEN
Riemann Hypothesis                                 UNPROVEN
```
