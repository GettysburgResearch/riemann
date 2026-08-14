# L-91687 — `Y_4`-zero columns are exact score-free triangular repair directions

Claim ID: `L-91687`  
Status: **PROVED EXACT RADIX-FOUR LP REDUCTION AND LOCAL TRANSFER LAW**  
Created: 2026-08-14  
Depends on: `L-91377`, `L-91378`, `L-91380`  
Replay: `X-91686-native-root-compiler-separator`  
RH status: **unproved**

## 1. Carry and radix-four maps

For a finite component row `d(n)`, write

\[
C_d(q)=\sum_{n\ge q}\beta_{nq}d(n),
\]

where, if `n=aq+r` with `0<=r<q`,

\[
\beta_{nq}=\frac{a(q-1-r)}{n+1}.
\tag{L-91687.1}
\]

The carry matrix `B=(beta_nq)` is triangular with

\[
\beta_{qq}=\frac{q-1}{q+1}>0.
\]

Let

\[
\Xi_d(q)=C_d(q)-2C_d(4q).
\]

Its finite positive inverse is

\[
\boxed{
(\mathcal R_4\Xi)(q)
=
\sum_{k\ge0}2^k\Xi(4^kq).
}
\tag{L-91687.2}
\]

Thus

\[
C_d=\mathcal R_4\Xi_d,
\qquad
d=B^{-1}\mathcal R_4\Xi_d.
\tag{L-91687.3}
\]

## 2. Exact direct slack LP with recursive capacity

Fix a native endpoint `X` and a source-owned recursive child packet with ordinary/detail responses

\[
R^{\rm ord},
\qquad
R^{(4)}.
\]

Because the child is a physical row packet,

\[
R^{\rm ord}=\mathcal R_4R^{(4)}.
\tag{L-91687.4}
\]

For a nonnegative unused-detail slack `s`, define

\[
\Xi_d=\Omega_X-R^{(4)}-s,
\tag{L-91687.5}
\]

and reconstruct

\[
\boxed{
 d(s)=B^{-1}\mathcal R_4
 [\Omega_X-R^{(4)}-s].
}
\tag{L-91687.6}
\]

Impose

\[
0\le s\le\Omega_X-R^{(4)},
\qquad
d(s)\ge0.
\tag{L-91687.7}
\]

Then detail feasibility is exact:

\[
\Xi_{d(s)}+R^{(4)}=\Omega_X-s\le\Omega_X.
\tag{L-91687.8}
\]

Applying the positive inverse (L-91687.2) gives ordinary feasibility automatically:

\[
\begin{aligned}
C_{d(s)}+R^{\rm ord}
&=w_X-\mathcal R_4s\\
&\le w_X.
\end{aligned}
\tag{L-91687.9}
\]

Thus, once the recursive packet is fixed and source-owned, the ordinary inequalities are redundant. The exact direct radix-four program is

\[
\boxed{
\min_{s}
\sum_qY_4(q)s(q)
}
\tag{L-91687.10}
\]

subject to (L-91687.7) and all retained source, target, score, and port constraints.

## 3. Exact zero-weight characterization

Recall

\[
Y_4(q)=\sum_{k=0}^{v_4(q)}2^k\Lambda(q/4^k).
\]

Every summand is nonnegative. Hence

\[
\boxed{
Y_4(q)=0
\iff
q/4^k\text{ is not a prime power for every }0\le k\le v_4(q).
}
\tag{L-91687.11}
\]

These columns are exact score-free slack directions in (L-91687.10).

## 4. Triangular row-transfer column

Let

\[
h^{(q)}=B^{-1}\mathcal R_4e_q.
\tag{L-91687.12}
\]

Increasing the slack at column `q` by `tau>=0` changes the reconstructed current row by

\[
\boxed{
 d(s+\tau e_q)=d(s)-\tau h^{(q)}.
}
\tag{L-91687.13}
\]

The top two entries are exact. Since `(R_4e_q)(q)=1`,

\[
\boxed{
h^{(q)}_q=\frac{q+1}{q-1}.}
\tag{L-91687.14}
\]

The ordinary column at `q-1` is zero, and triangular back-substitution gives, for `q>=4`,

\[
\boxed{
h^{(q)}_{q-1}
=-\frac{q(q-3)}{(q-1)(q-2)}.}
\tag{L-91687.15}
\]

Therefore increasing slack at `q`:

```text
decreases row q by      (q+1)/(q-1) times tau;
increases row q-1 by    q(q-3)/((q-1)(q-2)) times tau;
changes lower rows by the remaining triangular tail.
```

If `Y_4(q)=0`, this top-to-next-row transfer has exactly zero endpoint-score cost.

## 5. Verification

The replay verifies:

```text
Y4 recurrence and zero characterization       q<=5000;
zero-weight columns found                     3962;
exact triangular transfer columns checked     first 200 eligible q;
first zero columns                             6,10,14,15,18,21,...
```

All arithmetic is exact. Decimal output is display-only.

## 6. Scope

This lemma supplies a structured repair dictionary, not a complete current row. The lower triangular tail can create new negative rows, and source ownership does not follow from response-space algebra. A complete NRCT certificate must solve the full triangular LP together with the atomwise provenance and port ledger.

```text
direct radix-four slack LP                    EXACT
ordinary feasibility from detail slack        EXACT
Y4-zero characterization                      EXACT
score-free top-to-next-row transfer            EXACT
full nonnegative source-owned repair           OPEN
Native-Root Capacity Theorem                  OPEN
Riemann Hypothesis                            UNPROVEN
```
