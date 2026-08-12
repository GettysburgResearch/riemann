# L-91331 — The SHARP source has a positive canonical-child partition at every rough prime

Claim ID: `L-91331`  
Status: **PROVED EXACT POSITIVE SOURCE-PARTITION THEOREM**  
Created: 2026-08-12  
Depends on: `L-91109`, `L-91320`, `L-91330`  
RH status: **unproved**

## 1. One positive atom for the RH-sensitive output

Retain

\[
 \Psi=L+2R.
\]

At the squarefree source level, define

\[
\boxed{
 w_\Psi(x,n)=w_2(x,n)+2w_1(x,n)
 =\frac{4\sqrt x}{n}-\frac3{\sqrt n}.
}
\tag{L-91331.1}

For every `n<=x`,

\[
 w_\Psi(x,n)
 =\frac1{\sqrt n}
  \left(4\sqrt{x/n}-3\right)
 \ge\frac1{\sqrt n}>0.
\tag{L-91331.2}

Thus the full SHARP block has a native positive source atom; it need not be
represented as a signed observation of the diagonal `(X,Y)` modes.

## 2. Strong no-upward parity shadow on one reset window

For an active odd threshold `t`, let

\[
 \mathcal H_{\Psi,t}(x)
 =\mathcal H^0_{2,t}(x)+2\mathcal H_{1,t}(x),
\tag{L-91331.3}

where the two margins are those of `L-91320` and `L-91109`.
The directed bounds

\[
 \mathcal H^0_{2,t}(x)>-\frac9{50},
 \qquad
 \mathcal H_{1,t}(x)>\frac{39}{100}
\]

give

\[
\boxed{
 \mathcal H_{\Psi,t}(x)
 >-\frac9{50}+\frac{78}{100}
 =\frac35
}
\tag{L-91331.4
}

throughout

\[
 1\le x\le c_0^{-1}.
\]

Hence the odd `w_Psi` source admits a no-upward Hall transport into the even
source with fixed margin `>3/5`. The unspent even source mass is exactly
`Psi(x)`.

As in `L-91320/L-91321`, the transport produces a nonnegative interval seed,
a nonnegative residual even measure, exact divisor/radix-four destinations and
favorable score.

## 3. Exact one-prime child identity

Let `p` be prime and put

\[
 r=p^{-1/2},
 \qquad
 B_p=1-r.
\]

If `pn<=x`, then the general identity `L-91330.2` with the coefficients in
(L-91331.1) gives

\[
\boxed{
 w_\Psi(x,n)-w_\Psi(x,pn)
 =B_p w_\Psi(x/p,n)
  +4B_p\frac{\sqrt x}{n}.
}
\tag{L-91331.5
}

Both terms are positive. The first is the same SHARP source atom at the
canonical contracted endpoint `x/p`; the second is a pure positive square-root
slack.

For a positive finite source `nu(n)`, the truncated factor is therefore

\[
\boxed{
\begin{aligned}
 \mathcal E_{p,\Psi}[\nu](x)
 ={}&B_p\sum_{n\le x/p}\nu(n)w_\Psi(x/p,n)\\
 &+4B_p\sqrt x\sum_{n\le x/p}\frac{\nu(n)}n\\
 &+\sum_{x/p<n\le x}\nu(n)w_\Psi(x,n).
\end{aligned}}
\tag{L-91331.6
}

This is an exact positive partition of SHARP source mass.

## 4. Source-mass conservation and contraction

The three terms in (L-91331.6) are disjointly labelled as

```text
contracted child source;
positive harmonic slack;
positive activation frontier.
```

No source atom is duplicated. For `p>=67`, the child endpoint satisfies

\[
 x/p<c_0x.
\]

The frontier splits into the contracted slice and the already paid outer slice,
exactly as in `L-91317`.

Since `0<B_p<1`, the canonical child source is a strict submeasure after the
natural normalization. The omitted mass is present explicitly in the positive
slack/frontier terms; it is not discarded by an estimate.

## 5. Least-prime iteration

Assign every nontrivial rough squarefree integer to its unique least prime.
Apply (L-91331.6) to the source packet on that branch, then perform the local
no-upward parity projection before processing the next rough prime.

Along a path

\[
 p_1<p_2<\cdots<p_k,
\]

the terminal canonical source has coefficient

\[
 \prod_{j=1}^kB_{p_j}\le1
\]

and endpoint

\[
 x/(p_1\cdots p_k).
\]

Every other term created on the path is a positive slack or frontier source.
The scalar-port non-tensorization of `R-91303` is avoided because no independent
one-prime scalar ports are multiplied.

## 6. Target disintegration consequence

Attach the universal positive block source law `mu_Y` of `L-90028` to every
`w_Psi` source atom. Equation (L-91331.6) then becomes an exact positive measure
partition

\[
 \mu^{\rm parent}_\Psi
 =\mu^{\rm slack}_\Psi
  +\mu^{\rm frontier}_\Psi
  +\mu^{\rm child}_\Psi.
\tag{L-91331.7}

Applying the scale-free Markov kernel of `L-90028` disintegrates the corresponding
target measure in the same proportions. Therefore the canonical child, slack
and frontier target portions use the parent target once at the continuum level.

This is the source identity required by the sum-before-quantize theorem
`L-91329` for one rough factor.

## 7. Scope

Equation (L-91331.7) is exact for one positive projected source packet. To close
the complete rough tree, one must verify that the finite small-prime/parity
projection at every child supplies precisely such positive packets and that the
parallel least-prime partitions sum to the native parent source without a
boundary duplication.

```text
native positive SHARP source atom                  EXACT
reset-window no-upward Hall margin >3/5            DIRECTED EXACT
one-prime canonical-child source partition         EXACT
positive harmonic/frontier source                  EXACT
pathwise coefficient <=1 and scale contraction     EXACT
one-prime target disintegration                    EXACT
parallel all-prime source partition                OPEN / FINITE-TREE INDUCTION
all-generation branching reset                     OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVEN
```
