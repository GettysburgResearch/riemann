import Mathlib

namespace ChallengeDeps.XiPickThreeNode

def det3 (a b c d e f : ℝ) : ℝ :=
  a * d * f + 2 * b * c * e - a * e ^ 2 - d * c ^ 2 - f * b ^ 2

def pickEntry (x p y q : ℝ) : ℝ := (x * p + y * q) / (x + y)

def pickDet3 (x1 x2 x3 p1 p2 p3 : ℝ) : ℝ :=
  det3 p1 (pickEntry x1 p1 x2 p2) (pickEntry x1 p1 x3 p3)
    p2 (pickEntry x2 p2 x3 p3) p3

def delta3 (t1 t2 t3 : ℝ) : ℝ :=
  (t2 - t1) * (t3 - t1) * (t3 - t2)

def secondDivDiff (t1 t2 t3 y1 y2 y3 : ℝ) : ℝ :=
  y1 / ((t1 - t2) * (t1 - t3)) +
  y2 / ((t2 - t1) * (t2 - t3)) +
  y3 / ((t3 - t1) * (t3 - t2))

def denominator (x1 x2 x3 : ℝ) : ℝ :=
  (x1 + x2) ^ 2 * (x1 + x3) ^ 2 * (x2 + x3) ^ 2

end ChallengeDeps.XiPickThreeNode
