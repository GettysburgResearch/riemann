# X-15301 — Exact codimension-two source repair

This experiment is the finite arithmetic companion to `L-15302`.

## Verified finite identities

For three declared source modes, the checker reads exact rational values

```text
v_j = p_j(0)
m_j = integral p_j
chi_j = finite-Fourier eigenvalue
```

and requires `m_j=chi_j v_j`. It constructs

```text
a_0 = v_1 m_2 - v_2 m_1
a_1 = v_2 m_0 - v_0 m_2
a_2 = v_0 m_1 - v_1 m_0
```

then checks exactly

```text
sum a_j v_j = 0
sum a_j m_j = 0.
```

Under the separately declared orthonormal finite-Fourier packet, it also
reconstructs

```text
norm^2            = sum a_j^2
Fourier defect^2  = 2 sum a_j^2 (1-chi_j).
```

## Synthetic retained control

The exact packet

```text
v   = (1,2,3)
chi = (9/10,4/5,1/2)
m   = (9/10,8/5,3/2)
```

produces

```text
a                       = (-9/5,6/5,-1/5)
norm^2                  = 118/25
Fourier defect^2        = 158/125
normalized defect^2     = 79/295.
```

Retained verification SHA-256:

```text
365a4d600bd0e7a0029f53c595c7ec521cf8202ca95aff60cbd8fdb9e2b50b49
```

## Reproduction

```bash
python experiments/X-15301-codimension-two-source-repair/verify.py \
  experiments/X-15301-codimension-two-source-repair/certificates/synthetic.json

python -m unittest discover \
  -s experiments/X-15301-codimension-two-source-repair/tests -v
```

## Trust boundary

The checker verifies rational algebra only. It does not prove that any concrete
functions have the supplied values and integrals, are orthonormal, satisfy the
finite-Fourier eigenrelations, or lie in the Schwartz radical domain. Those are
explicit external gates. `L-15301` supplies a separate smooth compact source
construction.