# L-32416 — Simple radix-four plus/minus perfect reconstruction

Claim ID: `L-32416`  
Title: Two finite radix-four inverse-zeta sources form a constant critical frame, reconstruct the ordinary inverse-zeta source and current at zero delay, and orthogonalize to nonnegative generalized-prime channels  
Status: **PROPOSED COMPLETE EXACT ANALYTIC/DIRICHLET LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: elementary Euler products and two-channel polarization  
Scope: exact source/filter/current algebra; no global energy estimate or RH conclusion

## 1. Two finite sources

Put

\[
 a(s)=4^{1-s}
\]

and define

\[
\boxed{
 B_-(s)=\frac{1-a(s)}{\zeta(s)},
 \qquad
 B_+(s)=\frac{1+a(s)}{\zeta(s)}.
}
\tag{L-32416.1}
\]

Let

\[
 A_\pm=B_\pm^{-1},
 \qquad
 L_\pm=-A_\pm'/A_\pm,
 \qquad
 q_\pm=B_\pm L_\pm=B_\pm'.
\tag{L-32416.2}
\]

Both bare inverse sources are only two taps:

\[
 b_\pm=(\varepsilon\pm4\delta_4)*\mu.
\tag{L-32416.3}
\]

The minus source is exactly the finite main-pole source of `L-32415`.

## 2. Constant critical analysis frame

On the critical line `s=1/2+it`,

\[
 |a(s)|=2.
\]

Therefore

\[
\boxed{
 |1-a(s)|^2+|1+a(s)|^2=10.
}
\tag{L-32416.4}
\]

Equivalently

\[
\boxed{
 |B_-(1/2+it)|^2+|B_+(1/2+it)|^2
 =\frac{10}{|\zeta(1/2+it)|^2}.
}
\tag{L-32416.5}
\]

Thus the pair is an exact constant frame for the reciprocal-zeta source on the critical boundary. No finite Bezout polynomial or delayed synthesis is required.

For every nontrivial zeta zero `rho`, neither `1-a(rho)` nor `1+a(rho)` vanishes: zeros of either finite factor lie on `Re(s)=1`. Hence every nontrivial zeta-zero pole is retained in both channels.

## 3. Zero-delay perfect reconstruction

The two filters satisfy

\[
 (1-a)+(1+a)=2.
\]

Consequently

\[
\boxed{
 B_0(s):=\frac1{\zeta(s)}
 =\frac{B_-(s)+B_+(s)}2.
}
\tag{L-32416.6}
\]

Differentiating this exact identity gives

\[
\boxed{
 q_0(s):=B_0'(s)
 =\frac{q_-(s)+q_+(s)}2.
}
\tag{L-32416.7}

There is no derivative gauge and no delayed boundary in either reconstruction.

Writing `L=log 4`, differentiation of `a(s)` also gives the orthogonal current identity

\[
\boxed{
 \frac{q_+(s)-q_-(s)}2
 =a(s)\,[q_0(s)-L B_0(s)].
}
\tag{L-32416.8}

Hence on the critical line

\[
\boxed{
 \frac{|q_-|^2+|q_+|^2}{2}
 =|q_0|^2+4|q_0-LB_0|^2.
}
\tag{L-32416.9}

The pair current therefore contains the complete ordinary RH-sensitive current with coefficient one plus one explicit nonnegative detail square. The bare `B_0` leg becomes deterministic after the atomized carry factor `zeta(s)N_theta(s)`.

## 4. Generalized-prime channels

The logarithmic derivatives are

\[
 L_-(s)
 =-\frac{\zeta'}\zeta(s)
  +(\log4)\sum_{r\ge1}4^r4^{-rs},
\tag{L-32416.10}
\]

\[
 L_+(s)
 =-\frac{\zeta'}\zeta(s)
  +(\log4)\sum_{r\ge1}(-1)^r4^r4^{-rs}.
\tag{L-32416.11}
\]

Let their coefficient sequences be `Lambda_-` and `Lambda_+`, and define the orthogonalized channels

\[
\boxed{
 \Lambda_0=\frac{\Lambda_-+\Lambda_+}{2},
 \qquad
 \Lambda_1=\frac{\Lambda_--\Lambda_+}{2}.
}
\tag{L-32416.12}
\]

Then both are coefficientwise nonnegative. Explicitly,

\[
\boxed{
 \Lambda_0(n)
 =\Lambda(n)
  +(\log4)\sum_{\substack{r\ge1\\r\text{ even}}}
   4^r\mathbf1_{n=4^r}\ge0,
}
\tag{L-32416.13}
\]

\[
\boxed{
 \Lambda_1(n)
 =(\log4)\sum_{\substack{r\ge1\\r\text{ odd}}}
   4^r\mathbf1_{n=4^r}\ge0.
}
\tag{L-32416.14}
\]

Thus the sign-alternating local generalized-prime tower of the plus source disappears after the exact two-channel orthogonalization.

## 5. Complete paired second moment

For each channel put

\[
 C_\pm=\Lambda_\pm\log+\Lambda_\pm*\Lambda_\pm.
\]

Averaging and using `Lambda_\pm=Lambda_0\pm Lambda_1` gives exactly

\[
\boxed{
 C_{\rm pair}:=\frac{C_-+C_+}{2}
 =\Lambda_0\log
  +\Lambda_0*\Lambda_0
  +\Lambda_1*\Lambda_1.
}
\tag{L-32416.15}

Every coefficient of `C_pair` is nonnegative.

For any carry row, if

\[
 P_r=\sum_q\Lambda_r(q)\chi_q,
 \qquad r=0,1,
\]

then

\[
\boxed{
 \frac{P_-^2+P_+^2}{2}=P_0^2+P_1^2.
}
\tag{L-32416.16}

Thus both the first-moment Hermitian energy and the complete second-moment forcing have an exact nonnegative orthogonal basis.

## 6. Physical bare-source geometry

The atomized carry window has multiplier `zeta(s)N_theta(s)`. Therefore

\[
\boxed{
 \zeta(s)N_\theta(s)B_\pm(s)
 =(1\pm4^{1-s})N_\theta(s).
}
\tag{L-32416.17]

(The closing bracket in the tag is typographical only.)

Hence each bare physical source is a deterministic two-tap field. The pair reconstruction (L-32416.6)--(L-32416.7) remains exact after physical localization and in every independent-frequency block.

## 7. Interpretation

The pair has the simultaneous features

```text
finite inverse-source filters             two taps each;
critical analysis frame                   exact constant 10;
ordinary inverse-zeta reconstruction       zero delay;
ordinary current reconstruction            zero delay / no gauge;
orthogonal generalized primes              nonnegative;
paired complete Selberg forcing            nonnegative;
all nontrivial zeta poles                  retained.
```

This is substantially simpler than a delayed Bezout reconstruction. It does not by itself prove an energy estimate: the paired source-convolved reflected identity still has to be placed in a positive Hermitian row/physical ledger before the paired reserve can be spent.

## 8. Proof boundary

Closed exactly:

1. finite source definitions;
2. constant critical frame;
3. exact source and current reconstruction;
4. exact current-detail orthogonal decomposition;
5. coefficientwise nonnegative generalized-prime orthogonalization;
6. coefficientwise nonnegative complete paired Selberg forcing;
7. deterministic two-tap bare physical fields.

Open:

1. the all-row paired Selberg–Kummer reserve (proved separately in `L-32417`);
2. source-convolved independent-frequency use of that reserve;
3. an unconditional subexponential current bound;
4. RH.
