# L-90228 — Finite test channels cannot amplify one off-line zero pair beyond one negative direction

Claim ID: `L-90228`  
Status: **PROPOSED COMPLETE EXACT LINEAR-ALGEBRA / CONTINUITY FIREWALL — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: exact off-line hyperbolic block `L-15613`; inertia under pullback  
Scope: every finite family of test functions, source filters, carriers, and linear channels applied to the same Weil form; no statement about nonlinear/tensor observables and no RH conclusion

## 1. One pair has one hyperbolic coordinate block

Fix one off-line functional-equation pair of multiplicity `m` and write its
exact zero-coordinate Hermitian block as

\[
 H_m=m
 \begin{pmatrix}
 0&1\\
 1&0
 \end{pmatrix}.
 \tag{L-90228.1}
\]

It has signature `(1,1)`.

Let `V` be any finite-dimensional coefficient space containing any finite
collection of test functions, Gabor carriers, source filters, derivatives, or
other linear channels. All evaluations of this one zero pair combine into one
linear map

\[
 A:V\longrightarrow\mathbb C^2.
\]

The pair contribution to the true Weil form on `V` is

\[
 Q_A=A^*H_mA.
 \tag{L-90228.2}
\]

Inertia under pullback gives

\[
 \boxed{
 \operatorname{rank}Q_A\le2,
 \qquad
 n_+(Q_A)\le1,
 \qquad
 n_-(Q_A)\le1.
 }
 \tag{L-90228.3}
\]

Thus enlarging the finite test family changes the evaluation map but does not
duplicate the zero-coordinate block. One off-line pair still consumes at most
one negative direction.

## 2. Finite multi-channel corollary

Suppose `J` linear channels are assembled simultaneously. If they are honest
restrictions of the same Weil form, the combined evaluation map is simply

\[
 A_{\rm all}:V_1\oplus\cdots\oplus V_J\longrightarrow\mathbb C^2.
\]

Therefore

\[
 n_-(A_{\rm all}^*H_mA_{\rm all})\le1.
 \tag{L-90228.4}
\]

A block-diagonal direct sum of `J` independent copies of `H_m` would produce
`J` negative directions, but that operation duplicates the same zero datum and
is not the restriction of the original Weil form. It cannot be used as a proof
amplifier.

## 3. Near-line collapse in every fixed finite compression

Let the centered ordinates of the pair be

\[
 z_\epsilon=\gamma-i\epsilon,
 \qquad
 \overline z_\epsilon=\gamma+i\epsilon,
 \qquad \epsilon>0.
\]

For a fixed finite family of entire transforms, let the two evaluation vectors
be `a(epsilon),b(epsilon) in C^d`. Real symmetry gives continuity and

\[
 a(0)=b(0)=u.
\]

The pulled-back pair matrix is

\[
 Q_\epsilon
 =m\bigl(a(\epsilon)b(\epsilon)^*
        +b(\epsilon)a(\epsilon)^*\bigr).
 \tag{L-90228.5}
\]

As `epsilon -> 0`,

\[
 \boxed{
 Q_\epsilon\longrightarrow2muu^*
 }
 \tag{L-90228.6}
\]

in operator norm. The limit is positive semidefinite of rank at most one.
Consequently every negative eigenvalue of `Q_epsilon` tends to zero:

\[
 \boxed{
 \lambda_{\min}(Q_\epsilon)_-\longrightarrow0.
 }
 \tag{L-90228.7}
\]

No fixed finite compression has a uniform negative spectral moat for all
off-line pairs, because a pair may approach the critical line arbitrarily
closely.

## 4. Exact two-coordinate mutation

Take

\[
 a_\epsilon=(1,\epsilon)^t,
 \qquad
 b_\epsilon=(1,-\epsilon)^t.
\]

Then

\[
 a_\epsilon b_\epsilon^t+b_\epsilon a_\epsilon^t
 =
 \begin{pmatrix}
 2&0\\
 0&-2\epsilon^2
 \end{pmatrix}.
 \tag{L-90228.8}
\]

The positive eigenvalue remains of order one while the unique negative
eigenvalue is exactly `-2 epsilon^2`. At `epsilon=0` the off-line pair is
spectrally indistinguishable from an on-line double in this finite model.

This is the local mechanism behind the sharp extremal configurations in
Claude's Zeta23 paper.

## 5. Consequences for the repository

### Claude/Gabor compression

Claude's rank--trace theorem can bound how many hyperbolic planes occur, but a
single residual pair remains one permitted negative direction and can have an
arbitrarily small finite-compression eigenvalue.

### Carrier packets (`PR #30/#91`)

Adding finitely many carriers or confluent packet coordinates can improve the
search for a negative Rayleigh vector, but it cannot make one off-line pair
have negative index larger than one.

### Xi-cardinal route (`PR #179/#199`)

The global Xi-cardinal difference has exact Weil value `-2m`, independent of
how close the pair is to the line. The hard theorem is therefore a uniformly
conditioned localization/synthesis bridge from that global cardinal direction
to finite source-complete packets. Claude's finite Gabor theorem does not
supply that bridge.

## 6. What can escape the firewall

The theorem does not rule out:

1. genuinely nonlinear or tensor observables;
2. unbounded channel families with a separately proved uniform limit theorem;
3. support beyond the bandwidth-one prime-side regime;
4. complete global Xi-cardinal localization;
5. a direct one-sided arithmetic theorem such as `CN3`.

It rules out only the idea that a larger but finite linear test family, by
itself, multiplies the index cost of one hypothetical off-line pair.

## 7. Proof boundary

Proved exactly:

- rank and inertia nonamplification for every finite linear channel family;
- operator-norm collapse of the pair matrix as the pair approaches the line;
- an exact canonical model with negative eigenvalue `-2 epsilon^2`.

Not proved:

- any lower bound on off-line depth;
- absence of off-line pairs;
- RH.
