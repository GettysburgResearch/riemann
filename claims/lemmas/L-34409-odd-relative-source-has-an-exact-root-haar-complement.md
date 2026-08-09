# L-34409 — The odd relative source has an exact root-Haar complement

Claim ID: `L-34409`  
Title: The corrected odd relative source is the low-pass member of a two-channel Möbius Haar pair; the complementary root-divergence source has zero bare charge and contributes a pure current square  
Status: **PROPOSED COMPLETE EXACT SOURCE/CURVATURE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring/review agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: `R-34402/L-34408`; PR #326 two-contact/root source; elementary aligned carry scaling  
Scope: exact aligned integer-row source and curvature algebra; no upper recurrence and no RH conclusion

## 1. Three sources over the common odd Jordan system

Let

\[
B_0(s)=\frac1{\zeta(s)},
\qquad
B_{\rm odd}(s)=\prod_{p\ {m odd}}(1-p^{-s})
=\frac{B_0(s)}{1-2^{-s}}.
\]

In coefficient notation,

\[
b_0=\mu,
\qquad
b_{\rm odd}=(\varepsilon-\delta_2)^{-1}*\mu.
\tag{L-34409.1}
\]

Retain the positive odd-prime Jordan deformation

\[
J_{{\rm odd},\tau}(s)
=\frac{A_{\rm odd}(s-\tau)}{A_{\rm odd}(s)}
\]

and define the base source path

\[
K_{0,\tau}=b_0*J_{{\rm odd},\tau}.
\tag{L-34409.2}
\]

Now introduce the two finite Haar filters

\[
\boxed{
b_+=(\varepsilon+\delta_2)*\mu,
\qquad
b_-=(\varepsilon-\delta_2)*\mu,
}
\tag{L-34409.3}
\]

with paths

\[
K_{\pm,\tau}=(\varepsilon\pm\delta_2)*K_{0,\tau}.
\tag{L-34409.4}
\]

Because

\[
\varepsilon-\delta_4
=(\varepsilon-\delta_2)*(\varepsilon+\delta_2),
\]

one has the exact source identity

\[
\boxed{
(\varepsilon-\delta_4)*b_{\rm odd}
=(\varepsilon+\delta_2)*\mu
=b_+.
}
\tag{L-34409.5}

Thus the source leg used by the odd relative curvature is not a new infinite source.  It is exactly the **plus/low-pass Haar channel** of the ordinary Möbius source.

The minus channel `b_-` is the two-contact/root-divergence source already isolated in the hinge programme.

## 2. Aligned carry scaling

For any arithmetic sequence `f` and row

\[
e=(n,j),\qquad n=j+k,
\]

one has exactly

\[
\boxed{
\mathcal L_{2e}(\delta_2*f)=\mathcal L_e(f).
}
\tag{L-34409.6}

Indeed the only nonzero coefficients of `delta_2*f` occur at `2m`, and

\[
\chi_{2n,2m}(2j)=\chi_{n,m}(j).
\]

Consequently, if

\[
G_0(e,\tau)=\mathcal L_e(K_{0,\tau}),
\]

then

\[
\boxed{
G_\pm(2e,\tau)
:=\mathcal L_{2e}(K_{\pm,\tau})
=G_0(2e,\tau)\pm G_0(e,\tau).
}
\tag{L-34409.7}

This identity holds at every Jordan order because the filters are independent of `tau`.

## 3. Bare charges

Since

\[
\mathbf1*\mu=\varepsilon,
\]

the base Möbius source has, on every nontrivial row,

\[
\boxed{Y_0(e)=\mathcal L_e(\mu)=-1.}
\tag{L-34409.8}

Therefore (L-34409.7) at `tau=0` gives

\[
\boxed{Y_+(2e)=-2,
\qquad
Y_-(2e)=0.}
\tag{L-34409.9}

Equivalently,

\[
\mathbf1*b_+=\varepsilon+\delta_2,
\qquad
\mathbf1*b_- =\varepsilon-\delta_2.
\]

The ordinary prefix of the first sequence stabilizes at two and that of the second at zero.  Hence the plus charge is the corrected odd relative charge `-2`, while the minus/root channel has **no bare-times-second-current term at all**.

## 4. Current and second-current coordinates

Let

\[
q_0=\mu*\Lambda_{\rm odd},
\qquad
t_0=\mu*C_{\rm odd}.
\]

For a row `e`, write

\[
Q_0(e)=\mathcal L_e(q_0),
\qquad
T_0(e)=\mathcal L_e(t_0).
\]

Differentiating (L-34409.7) at zero gives

\[
\boxed{
Q_\pm(2e)=Q_0(2e)\pm Q_0(e),
}
\tag{L-34409.10}

and

\[
\boxed{
T_\pm(2e)=T_0(2e)\pm T_0(e).
}
\tag{L-34409.11}

Because `1*t_0=C_odd`, the base second-current row is precisely the corrected ordinary-prefix boundary:

\[
\boxed{
T_0(e)=\mathcal D_C(e).
}
\tag{L-34409.12}

Apply the formulas with `e` replaced by `2e`.  The plus channel on `4e` is the odd relative source by (L-34409.5), so

\[
\boxed{
I_{\rm odd}(e)
=Q_+(4e)
=Q_0(4e)+Q_0(2e),
}
\tag{L-34409.13}

and

\[
\boxed{
T_{\rm odd}^{\rm rel}(e)
=T_+(4e)
=\mathcal D_C(4e)+\mathcal D_C(2e).
}
\tag{L-34409.14}

Equation (L-34409.14) gives a second, source-factor proof of the corrected identity in `R-34402`.

The complementary/root current is

\[
\boxed{
D_{\rm root}(e)
:=Q_-(4e)
=Q_0(4e)-Q_0(2e).
}
\tag{L-34409.15}

## 5. Exact Haar curvature identity

For a scalar Jordan source path with jets `(Y,Q,T)`, use the imaginary curvature

\[
\mathfrak C(Y,Q,T)=|Q|^2-YT.
\]

The base Möbius source has `Y_0=-1`, so

\[
\boxed{
\mathfrak C_0(e)
=|Q_0(e)|^2+T_0(e)
=|Q_0(e)|^2+\mathcal D_C(e).
}
\tag{L-34409.16}

The plus and minus curvatures at `4e` are

\[
\mathfrak C_+(4e)
=|Q_0(4e)+Q_0(2e)|^2
 +2[T_0(4e)+T_0(2e)],
\tag{L-34409.17}
\]

and, because `Y_-=0`,

\[
\boxed{
\mathfrak C_-(4e)
=|Q_0(4e)-Q_0(2e)|^2
=|D_{\rm root}(e)|^2.
}
\tag{L-34409.18}

Adding (L-34409.17)--(L-34409.18), the cross terms cancel:

\[
\boxed{
\mathfrak C_+(4e)+\mathfrak C_-(4e)
=2\mathfrak C_0(4e)+2\mathfrak C_0(2e).
}
\tag{L-34409.19}

This is an exact source-complete Haar/Parseval identity.  It includes the second-current boundaries; it is not only a first-derivative square identity.

Since the minus curvature is a square, (L-34409.19) also gives the unconditional upper placement

\[
\boxed{
\mathfrak C_+(4e)
\le2\mathfrak C_0(4e)+2\mathfrak C_0(2e).
}
\tag{L-34409.20}

The right side is automatically nonnegative because it equals the sum of the plus curvature and a square.

## 6. Full repaired relative curvature with its root complement

The repaired odd relative augmented curvature is

\[
\mathfrak A_{\rm rel}(e)
=\Delta_4R_{\rm odd}(e)+\mathfrak C_+(4e).
\]

Combining with (L-34409.18)--(L-34409.19) gives

\[
\boxed{
\begin{aligned}
\mathfrak A_{\rm rel}(e)
+|D_{\rm root}(e)|^2
={}&\Delta_4R_{\rm odd}(e)\\
&+2\mathfrak C_0(4e)
 +2\mathfrak C_0(2e).
\end{aligned}}
\tag{L-34409.21}

Thus the odd-relative route and the root/two-contact route are complementary coordinates of one two-channel Möbius curvature ledger.

This is the previously missing connection:

```text
odd relative low-pass current:
    Q_0(4e)+Q_0(2e), bare charge -2;

root high-pass current:
    Q_0(4e)-Q_0(2e), bare charge 0;

complete pair:
    exact Parseval curvature with no lost source term.
```

## 7. Consequence and remaining theorem

The corrected odd source no longer needs to be handled in isolation.  Any reflected block proof may retain the low-pass relative current and the root high-pass current together.  The high-pass channel is already a nonnegative square and cannot consume the Selberg reserve twice.

The remaining conclusion-producing task can therefore be stated more sharply:

> Place the base Möbius odd-Jordan curvatures at scales `4e` and `2e` in one coefficient-one independent-frequency block recurrence.  Equation (L-34409.21) then pays simultaneously for the full odd relative curvature and the root-current square.

No such upper recurrence is proved here.  In particular, (L-34409.21) is an exact orthogonal decomposition, not an RH proof.

## 8. Proof boundary

Closed exactly:

1. factorization of the odd relative source as the plus Möbius Haar channel;
2. identification of the minus channel with the root/two-contact source;
3. aligned all-order carry scaling;
4. bare charges `-2` and `0`;
5. corrected first- and second-current coordinates;
6. exact source-complete Haar curvature identity;
7. the full repaired relative/root complement identity.

Open:

1. a reflected upper recurrence for the base curvatures;
2. subpower control of the principal current;
3. RH.
