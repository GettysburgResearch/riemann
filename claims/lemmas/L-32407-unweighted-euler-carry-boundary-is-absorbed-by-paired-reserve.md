# L-32407 — The unweighted Euler carry boundary is absorbed by the paired reserve

Claim ID: `L-32407`  
Title: The plus Euler inverse has a four-value divisor potential, and its entire unweighted carry-image energy is uniformly absorbed by the parity-paired Selberg reserve away from one finite bottom row  
Status: **PROPOSED COMPLETE EXACT CARRY-ROW LEMMA**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #263 `L-26201/L-26205`; `L-32406`; `X-32402`  
Scope: carry-image boundary of the plus Euler source; no claim that a pure carry window controls the RH-sensitive physical source before the reviewed source-convolved localization

## 1. Unweighted plus Euler source

Retain

\[
B_{\mathcal E}(s)
={P(s)\over\zeta(s)},
\qquad
P(s)=(1-2^{1-s})(1-2^{1/2-s})^2.
\tag{L-32407.1}
\]

Write `z=2^{-s}`. Then

\[
P(z)=1-(2+2\sqrt2)z+(2+4\sqrt2)z^2-4z^3.
\tag{L-32407.2}
\]

If `b_E` is the coefficient sequence of `B_E`, then

\[
\mathbf1*b_{\mathcal E}
=\delta_1-(2+2\sqrt2)\delta_2
 +(2+4\sqrt2)\delta_4-4\delta_8.
\tag{L-32407.3}
\]

Thus its floor potential

\[
H(x)=\sum_{q\le x}b_{\mathcal E}(q)\left\lfloor{x\over q}\right\rfloor
=\sum_{m\le x}(\mathbf1*b_{\mathcal E})(m)
\tag{L-32407.4}
\]

is exactly

\[
\boxed{
H(x)=
\begin{cases}
0,&0\le x<1,\\
1,&1\le x<2,\\
-1-2\sqrt2,&2\le x<4,\\
1+2\sqrt2,&4\le x<8,\\
-3+2\sqrt2,&x\ge8.
\end{cases}}
\tag{L-32407.5}
\]

No Möbius sum survives in this carry coordinate.

## 2. Exact unweighted carry charge

For a split `n=j+(n-j)` define

\[
Y_{\mathcal E}(n,j)
=\sum_{q\le n}b_{\mathcal E}(q)\chi_{n,q}(j)
=H(n)-H(j)-H(n-j).
\tag{L-32407.6}
\]

In particular, once `n,j,n-j>=8`,

\[
\boxed{
Y_{\mathcal E}(n,j)=3-2\sqrt2=(\sqrt2-1)^2>0.
}
\tag{L-32407.7}
\]

So the unweighted source is not an indefinite bulk direction. Its complete interior carry charge is one fixed positive constant; only the seven endpoint-neighbor widths on each side differ from that constant.

Using

\[
{7\over5}<\sqrt2<{3\over2},
\]

all values in (L-32407.5) have absolute value below four. Hence

\[
|Y_{\mathcal E}(n,j)|<12
\tag{L-32407.8}
\]

for every row and split.

Define its normalized row energy

\[
\boxed{
\mathcal B_{\mathcal E}(n)
={1\over n+1}\sum_{j=0}^n|Y_{\mathcal E}(n,j)|^2.
}
\tag{L-32407.9}
\]

Then

\[
\boxed{
\mathcal B_{\mathcal E}(n)<144.
}
\tag{L-32407.10}
\]

For `n>=16` one may sharpen this to the exact formula

\[
\boxed{
\mathcal B_{\mathcal E}(n)
={17n-145+(228-12n)\sqrt2\over n+1},
}
\tag{L-32407.11}
\]

because the two endpoint strips have width seven and every remaining position has charge `3-2sqrt2`.

## 3. Paired Selberg reserve

Use the notation of `L-32406` and put

\[
\mathcal R_{\rm pair}(n)
={1\over n+1}\sum_{j=0}^n
\left[
P_0(n,j)^2+P_1(n,j)^2-S_0(n,j)
\right].
\tag{L-32407.12}
\]

`L-32406` proves

\[
\mathcal R_{\rm pair}(n)\ge0
\qquad(n\ge2).
\tag{L-32407.13}
\]

The exact finite proof object `X-32402` gives more. Its directed minimum over

\[
6\le n<30000
\]

is the scaled integer

```text
61414768714590273867636140072 / 2^96,
```

which is strictly larger than `3/4`, since

```text
61414768714590273867636140072
-
3*2^94
=
1993646828892020672478177320
>0.
```

The same checker gives directed lower bounds greater than `3/4` for the direct small rows `n=2,4,5`; `n=3` is the exact equality row.

For `n>=30000`, the elementary tail proof of `L-32406` gives

\[
\mathcal R_{\rm pair}(n)
\ge {n^2\log^22\over30}-36n-42n\log n.
\tag{L-32407.14}
\]

At `n=30000` the bracket calculation in `L-32406` already exceeds `174`, and it is increasing thereafter. In particular it is much larger than `3/4`.

Thus

\[
\boxed{
\mathcal R_{\rm pair}(n)>{3\over4}
\quad\text{for }n=2\text{ or }n\ge4,
}
\tag{L-32407.15}
\]

while

\[
\boxed{\mathcal R_{\rm pair}(3)=0.}
\tag{L-32407.16}
\]

## 4. Uniform boundary absorption

Combining (L-32407.10) and (L-32407.15),

\[
144<200\cdot{3\over4},
\]

so for every nonexceptional row

\[
\boxed{
\mathcal B_{\mathcal E}(n)
\le200\,\mathcal R_{\rm pair}(n),
\qquad n=2\text{ or }n\ge4.
}
\tag{L-32407.17}
\]

The constant `200` is deliberately crude. The statement is homogeneous: after multiplying the entire row by any scalar amplitude, both sides acquire its squared modulus.

At the sole exceptional row `n=3`, the unweighted carry energy is finite and explicit:

\[
\mathcal B_{\mathcal E}(3)=\frac12,
\tag{L-32407.18}
\]

while the paired reserve vanishes. This row belongs in the fixed bottom table rather than in a cofinal recurrence.

## 5. Meaning for the parity route

The local carry ledger is now closed in both sectors:

```text
complete mixed logarithmic Selberg forcing
    -> absorbed by paired generalized-prime energy (L-32406);

unweighted plus-source carry image
    -> constant positive interior + fixed endpoint strip
    -> absorbed by the same paired reserve (this lemma),
       except one finite bottom row.
```

Thus an all-scale theorem may no longer cite an uncontrolled **carry-image** unit-source boundary for the plus Euler channel.

This does not license the false shortcut rejected on PR #269. A pure carry window contains a zeta factor and can cancel one inverse-zeta pole. The remaining production step must use the reviewed source-convolved / independent-frequency localization, or an equivalent pole-preserving physical congruence, before this carry-row absorption is imported into the RH-sensitive physical block.

## 6. Proof boundary

Closed exactly:

1. the finite divisor prefix of the plus Euler inverse;
2. the constant interior unweighted carry charge;
3. the fixed-width endpoint structure;
4. a uniform absolute carry-energy bound;
5. absorption by the complete paired Selberg reserve on every row except `n=3`;
6. isolation of that one finite bottom row.

Still open:

1. the pole-preserving physical congruence placing this carry boundary inside the independent-frequency source-convolved block;
2. the resulting global block recurrence;
3. RH.
