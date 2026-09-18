"""Discriminated contracts for new desks; legacy Spec stays replay-compatible."""
from __future__ import annotations
from decimal import Decimal
from typing import Annotated, Literal
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter, model_validator

Source = Literal['mobius', 'magnitude', 'random_signs', 'shuffled', 'liouville', 'alternating']

class Bounded(BaseModel):
    model_config = ConfigDict(extra='forbid', allow_inf_nan=False)

class CancellationSpec(Bounded):
    module: Literal['cancellation'] = 'cancellation'
    n: int = Field(64, ge=8, le=192)
    start: int = Field(1, ge=1, le=20000)
    split: int = Field(32, ge=1, le=191)
    width: float = Field(0.5, ge=0.03, le=4)
    exponent: float = Field(0.5, ge=0, le=1.5)
    source_a: Source = 'mobius'
    source_b: Source = 'magnitude'
    seed_a: int = Field(17, ge=0, le=2147483647)
    seed_b: int = Field(29, ge=0, le=2147483647)

    @model_validator(mode='after')
    def partition(self):
        if self.split >= self.n:
            raise ValueError('split must be strictly inside the finite window (split < n).')
        return self

class SweepSpec(Bounded):
    module: Literal['sweep'] = 'sweep'
    n: int = Field(48, ge=8, le=128)
    train_start: int = Field(1, ge=1, le=20000)
    holdout_start: int = Field(1001, ge=1, le=20000)
    source_a: Source = 'mobius'
    source_b: Source = 'random_signs'
    seed_a: int = Field(17, ge=0, le=2147483647)
    seed_b: int = Field(29, ge=0, le=2147483647)
    exponent: float = Field(0.5, ge=0, le=1.5)
    width_min: float = Field(0.05, ge=0.03, le=4)
    width_max: float = Field(2, ge=0.03, le=4)
    width_steps: int = Field(12, ge=2, le=24)
    split_steps: int = Field(9, ge=2, le=24)

    @model_validator(mode='after')
    def split_data(self):
        if abs(self.train_start - self.holdout_start) < self.n:
            raise ValueError('Training and holdout windows must be disjoint.')
        if self.width_max <= self.width_min:
            raise ValueError('width_max must exceed width_min.')
        if self.split_steps >= self.n:
            raise ValueError('split_steps must be smaller than n.')
        return self

class ExplicitSpec(Bounded):
    module: Literal['explicit'] = 'explicit'
    a: float = Field(0.015, ge=0.002, le=0.2)
    b_min: float = Field(0, ge=0, le=7)
    b_max: float = Field(5, ge=0, le=7)
    focus_b: float = Field(2.302585092994046, ge=0, le=7)
    samples: int = Field(81, ge=8, le=161)
    prime_cutoff: int = Field(5000, ge=10, le=100000)
    zero_count: int = Field(24, ge=2, le=64)
    band_first: int = Field(1, ge=1, le=64)
    band_last: int = Field(8, ge=1, le=64)
    gamma_cutoff: float = Field(100, ge=10, le=240)
    quadrature_order: Literal[16, 24, 32] = 24
    dps: int = Field(30, ge=20, le=60)

    @model_validator(mode='after')
    def domain(self):
        if self.b_max <= self.b_min:
            raise ValueError('b_max must exceed b_min.')
        if not self.b_min <= self.focus_b <= self.b_max:
            raise ValueError('focus_b must lie in the plotted b window.')
        if not self.band_first <= self.band_last <= self.zero_count:
            raise ValueError('The selected zero band must lie inside 1..zero_count.')
        return self

class RefineSpec(Bounded):
    module: Literal['refine'] = 'refine'
    function: Literal['zeta', 'eta', 'xi', 'beta', 'chi3'] = 'zeta'
    real: str = Field('0.5', pattern=r'^-?\d{1,4}(\.\d{1,100})?$', max_length=106)
    imag: str = Field('14.134725141734693790457251983562', pattern=r'^-?\d{1,4}(\.\d{1,100})?$', max_length=106)
    dps: int = Field(60, ge=30, le=120)
    backend: Literal['mpmath', 'flint'] = 'mpmath'

    @model_validator(mode='after')
    def domain(self):
        if not -4 <= Decimal(self.real) <= 4 or abs(Decimal(self.imag)) > 1000:
            raise ValueError('Point refinement supports -4 <= Re(s) <= 4 and |Im(s)| <= 1000.')
        return self

class FamilySpec(Bounded):
    module: Literal['family'] = 'family'
    discriminants: list[Literal[-4, -3, 5, 8, -7, -8, 12, 13, -11, 17]] = Field(default_factory=lambda: [-4, -3, 5], min_length=1, max_length=6)
    multiplier: Literal[1, 2, 3, 4] = 1
    sigma: float = Field(0.5, ge=0.25, le=2)
    t_min: float = Field(0, ge=0, le=100)
    t_max: float = Field(40, ge=0, le=100)
    samples: int = Field(96, ge=16, le=192)
    dps: int = Field(25, ge=20, le=50)

    @model_validator(mode='after')
    def unique(self):
        if len(set(self.discriminants)) != len(self.discriminants):
            raise ValueError('Each discriminant must be unique.')
        if self.t_max <= self.t_min:
            raise ValueError('t_max must exceed t_min.')
        return self

class HierarchySpec(Bounded):
    module: Literal['hierarchy'] = 'hierarchy'
    limit: int = Field(20000, ge=100, le=200000)
    depth: int = Field(3, ge=1, le=4)
    alpha: float = Field(0.5, ge=0.25, le=2)
    buckets: int = Field(360, ge=16, le=1024)

NewSpec = Annotated[CancellationSpec | SweepSpec | ExplicitSpec | RefineSpec | FamilySpec | HierarchySpec, Field(discriminator='module')]
ADAPTER = TypeAdapter(NewSpec)
NEW_MODULES = {'cancellation', 'sweep', 'explicit', 'refine', 'family', 'hierarchy'}
MODELS = [CancellationSpec, SweepSpec, ExplicitSpec, RefineSpec, FamilySpec, HierarchySpec]
