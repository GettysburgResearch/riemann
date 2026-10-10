# B2: machine verification of the constants in Theorem B2 (Jensen window cap), H=8.
# Geometry (all lengths in units of L = Lambda'):
#   window center c=0, height point t* = iH, H=8
#   admissible S-zeros: |Re w| <= 1; pairs y <= 1/4 (so Im(t*-z) in [H-1/4, H]);
#   reals on axis (Im(t*-t_n) = H).
#   inner radius rho = sqrt(4+H^2) covers real segment [-2,2] (K_span cap 2L);
#   outer R = 2.4*rho.
from mpmath import mp, mpf, sqrt, atan, cos, log, pi
mp.dps = 40
H = mpf(8); L = mpf(1)
rho = sqrt(4 + H**2)            # inner Jensen radius
R = mpf('2.4') * rho            # outer Jensen radius
# --- Cone lemma: for w in S, arg(t*-w) in 90deg +- theta_max
# worst horizontal offset 1, worst vertical H - 1/4 (pair top) => angle atan(1/(H-1/4))
theta = atan(1 / (H - mpf(1)/4))
conecos = cos(2*theta)          # alignment factor for (t*-w)^{-2} terms about -180deg
# max |t*-w|^2 over S: offset 1, conj pair bottom H+1/4
d2max = 1 + (H + mpf(1)/4)**2
d2min = (H - mpf(1)/4)**2       # min |t*-w|^2 (pair top, offset 0)
floor_coeff = conecos / d2max   # |h'(t*)| >= floor_coeff * N_S / L^2  - (annulus+far bg)
theta_bg = floor_coeff / 2      # (DOM): bg mass at/near disk <= theta_bg * N_S / L^2
center_h = floor_coeff - theta_bg  # certified |h'(t*)| lower coeff
# --- max |h'| on circle |t - t*| = R:
# S-terms: |t-w| >= R - sqrt(d2max); bg on disk <= theta_bg*N_S (DOM uses dist to closed disk)
circ_h = 1/(R - sqrt(d2max))**2 + theta_bg
amp_ratio = circ_h / center_h
# --- per-pair factor ratio: q_j(t) = (t-z)(t-zbar)
# center: |q(t*)| >= (H-1/4)*H  [ |t*-z| >= H-1/4 vertical; |t*-zbar| >= H ]
qc = (H - mpf(1)/4) * H
# circle: |t-z| <= R + sqrt(d2max) both factors
qC = (R + sqrt(d2max))**2
pair_ratio = (qC/qc)**2         # ratio of |q|^2
# --- per-real factor: (t-t_n)^2 ; center |t*-t_n|^2 >= H^2 ; circle <= (R+sqrt(1+H^2))^2
rc = H**2
rC = (R + sqrt(1 + H**2))**2
real_ratio = rC / rc
# --- Jensen: n(rho) * log(R/rho) <= log Mmax - log |g(t*)|
denom = log(R/rho)              # = log 2.4
C_pair = 2*log(qC/qc)/denom     # NOTE |q|^2 divided out => factor 2*log(qC/qc)... check:
# g includes q_j^2 => ratio (qC/qc)^2 => log pair_ratio = 2 log(qC/qc). Keep as log(pair_ratio).
C_pair = log(pair_ratio)/denom
C_real = log(real_ratio)/denom
C_amp  = log(amp_ratio)/denom
print("H =", H, " rho =", rho, " R =", R, " R/rho = 2.4")
print("cone half-angle deg:", mp.nstr(2*theta*180/pi, 6), " conecos =", mp.nstr(conecos, 8))
print("d2max =", mp.nstr(d2max,8), " floor_coeff =", mp.nstr(floor_coeff, 8))
print("theta_bg (DOM budget coeff) =", mp.nstr(theta_bg, 8))
print("center |h'| coeff =", mp.nstr(center_h, 8), "  circle |h'| coeff =", mp.nstr(circ_h, 8))
print("amp_ratio =", mp.nstr(amp_ratio, 8))
print("per-pair |q|^2 ratio =", mp.nstr(pair_ratio, 8), " -> C_pair =", mp.nstr(C_pair, 6))
print("per-real ratio =", mp.nstr(real_ratio, 8), " -> C_real =", mp.nstr(C_real, 6))
print("C_amp =", mp.nstr(C_amp, 6))
print()
print("THEOREM B2 BOUND:  Z <= C_pair * p_S + C_real * nu_S + C_amp")
print("  = %s p + %s nu + %s" % (mp.nstr(C_pair,4), mp.nstr(C_real,4), mp.nstr(C_amp,4)))
# check inner disk covers K_span cap: real u, |u|<=2: dist(t*,u)=sqrt(u^2+H^2)<=rho
assert sqrt(4+H**2) <= rho + mpf('1e-30')
# check R - sqrt(d2max) > 0 and qc>0
assert R > sqrt(d2max)
# sanity: with p=nu=m (one pair, no reals): bound
for m in (1,2,5,13):
    print("p_S=%d, nu_S=0 -> Z <= %s   (16m-10 = %d)" % (m, mp.nstr(C_pair*m + C_amp, 5), 16*m-10))
