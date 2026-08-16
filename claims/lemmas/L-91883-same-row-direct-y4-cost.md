# L-91883 — Every physical column, the terminal reserve, and the native `Y_4` price close on the same row

Claim ID: `L-91883`  
Status: **PROPOSED COMPLETE CAPACITY / NATIVE-COST THEOREM ON FROZEN ANALYTIC INPUTS — REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-91882`; frozen adjacent-error, collar, terminal, sparse-`Y_4`, Chebyshev and positive radix-four inverse theorems  
RH status: **unproved**

Fix `X>=10^12` and the row `d_X` with identifier `rid_X` from `L-91882`.

## 1. Exact response complement

Applying the native detail observation to (L-91882.9) gives

\[
\boxed{
 e_X^{(4)}
 :=\Omega_X-\Xi(d_X)
 =(1-\tau_K)\Omega_X
 +\tau_K\left[
  \Xi(\overline c_{X,\mathrm{top}})
  +\mathcal D_4v(E_{X,\mathrm{out}}-C_{X,\mathrm{ret}})
 \right].
}
\tag{L-91883.1}
\]

This equality is defined after ordinary observations at `q` and `4q` have been summed on the one row. No branchwise detail inequality is used.

## 2. Every nonterminal column, including `q<K`

The adjacent error is localized by its actual outer cells. The frozen estimates give, for every `q>=2`,

\[
 |v_q(E_{X,\mathrm{out}})|
 <\frac{57}{2q\sqrt K},
\]

\[
 \left|
 \mathcal D_4v_q(E_{X,\mathrm{out}}-C_{X,\mathrm{ret}})
 \right|
 <\frac{971}{4q\sqrt K}.
\tag{L-91883.2}
\]

The proof sums the actual multiples `jq>=K+2`, so no column `2<=q<K` is omitted. The estimate is monotone under the choice of the retained-cell subset; including the fixed top cells in `E_(X,out)` cannot exceed the full absolute tail sum used in the displayed bound.

For `2<=q<=X/4`,

\[
 \frac{|
 \mathcal D_4v_q(E_{X,\mathrm{out}}-C_{X,\mathrm{ret}})
 |}{\Omega_X(q)}
 <\frac{129}{\sqrt K}.
\tag{L-91883.3}
\]

Therefore

\[
 \tau_K\left(1+\frac{129}{\sqrt K}\right)
 =\frac{\sqrt K+129}{\sqrt K+130}<1,
\]

and

\[
 e_X^{(4)}(q)>0
 \qquad(2\le q\le X/4).
\tag{L-91883.4}
\]

## 3. Terminal annulus

The top row omitted in (L-91882.4) is exactly the positive outer Volterra packet used by the frozen terminal theorem. Its response removal is greater than

\[
5033X^{-3/2}.
\]

The complete terminal finite/continuum and collar overfill for the same bulk row is less than

\[
4452X^{-3/2}.
\]

Thus the same row retains the strict terminal reserve

\[
\boxed{581X^{-3/2}>0.}
\tag{L-91883.5}
\]

Above retained support, triangularity gives zero response. Hence

\[
\boxed{e_X^{(4)}(q)\ge0\qquad(q\ge2).}
\tag{L-91883.6}
\]

## 4. Ordinary complement

The finite positive radix-four inverse gives

\[
\boxed{
 e_X^{\rm ord}(q)
 :=\sum_{h\ge0}2^he_X^{(4)}(4^hq)\ge0,
}
\tag{L-91883.7}
\]

and therefore

\[
\boxed{
 \Xi(d_X)+e_X^{(4)}=\Omega_X,
 \qquad
 \Gamma(d_X)+e_X^{\rm ord}=w_X.
}
\tag{L-91883.8}
\]

Both complements belong to `rid_X`.

## 5. Direct native price

Exact native duality gives

\[
\boxed{
 \Delta_X
 :=J_\Lambda(X)-\mathcal H(d_X)
 =\langle Y_4,e_X^{(4)}\rangle\ge0.
}
\tag{L-91883.9}
\]

The complete charge classes are:

```text
one common square-root thinning        <12012
nonterminal signed comparison          <4
terminal signed comparison             <48972
literal positive top/bottom omissions  <1
identity inner/bonus channels           0 comparison cost
auxiliary matrix port                   0
```

The thinning bound follows from the elementary estimate

\[
J_\Lambda(X)<16(\log2)\sqrt X.
\]

The signed terms are paid by absolute `Y_4` pairing, never by a positive-source mass theorem. Consequently

\[
\boxed{
0\le J_\Lambda(X)-\mathcal H(d_X)<60989.
}
\tag{L-91883.10}
\]

No estimate for `J_Lambda(X)-4sqrt(X)` is used.
