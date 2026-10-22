/*
 * Directed MPFR producer for the X-9502 zeta-screw Toeplitz control.
 *
 * Exact parameters:
 *   h = log(2)/3,
 *   n = 53,
 *   b_j = BNUM[j] / 2^24.
 *
 * At t_k=k*h, a prime power q is present exactly when q^3 <= 2^k.
 * Therefore every threshold decision is made by integer arithmetic.  The
 * producer evaluates Psi(kh) with outward MPFR rounding, reconstructs the
 * zero-sum FIR difference vector and its autocorrelations from the frozen
 * integers, and emits a directed Rayleigh interval.
 *
 * This is a positive control, not an RH proof.  It excludes only this exact
 * finite vector.  A strict negative result would still require independent
 * analytic-normalization review and independent directed reproduction.
 */

#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <openssl/sha.h>

#if defined(__has_include)
#  if __has_include(<mpfr.h>)
#    include <mpfr.h>
#    define RIEMANN_HAVE_MPFR_HEADER 1
#  endif
#endif

#ifndef RIEMANN_HAVE_MPFR_HEADER
/*
 * Minimal ABI declarations for the project container, which supplies the
 * MPFR runtime but not the development header.  Production builds should use
 * the official mpfr.h.  This fallback is valid only when the runtime ABI uses
 * the standard GMP limb and LP64 MPFR layout.
 */
#  include <gmp.h>
typedef long mpfr_prec_t;
typedef long mpfr_exp_t;
typedef int mpfr_sign_t;
typedef struct {
    mpfr_prec_t _mpfr_prec;
    mpfr_sign_t _mpfr_sign;
    mpfr_exp_t _mpfr_exp;
    mp_limb_t *_mpfr_d;
} __mpfr_struct;
typedef __mpfr_struct mpfr_t[1];
typedef __mpfr_struct *mpfr_ptr;
typedef const __mpfr_struct *mpfr_srcptr;
enum {
    MPFR_RNDN = 0,
    MPFR_RNDZ = 1,
    MPFR_RNDU = 2,
    MPFR_RNDD = 3,
    MPFR_RNDA = 4,
    MPFR_RNDF = 5
};
extern void mpfr_init2(mpfr_ptr, mpfr_prec_t);
extern void mpfr_clear(mpfr_ptr);
extern int mpfr_set(mpfr_ptr, mpfr_srcptr, int);
extern int mpfr_set_ui(mpfr_ptr, unsigned long, int);
extern int mpfr_set_si(mpfr_ptr, long, int);
extern void mpfr_set_zero(mpfr_ptr, int);
extern int mpfr_add(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, int);
extern int mpfr_sub(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, int);
extern int mpfr_neg(mpfr_ptr, mpfr_srcptr, int);
extern int mpfr_mul(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, int);
extern int mpfr_mul_ui(mpfr_ptr, mpfr_srcptr, unsigned long, int);
extern int mpfr_mul_si(mpfr_ptr, mpfr_srcptr, long, int);
extern int mpfr_div(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, int);
extern int mpfr_div_ui(mpfr_ptr, mpfr_srcptr, unsigned long, int);
extern int mpfr_div_2ui(mpfr_ptr, mpfr_srcptr, unsigned long, int);
extern int mpfr_log(mpfr_ptr, mpfr_srcptr, int);
extern int mpfr_exp(mpfr_ptr, mpfr_srcptr, int);
extern int mpfr_sqrt(mpfr_ptr, mpfr_srcptr, int);
extern int mpfr_const_pi(mpfr_ptr, int);
extern int mpfr_const_euler(mpfr_ptr, int);
extern int mpfr_const_catalan(mpfr_ptr, int);
extern int mpfr_const_log2(mpfr_ptr, int);
extern int mpfr_cmp(mpfr_srcptr, mpfr_srcptr);
extern int mpfr_cmp_ui(mpfr_srcptr, unsigned long);
extern int mpfr_printf(const char *, ...);
#endif

#define MATRIX_SIZE 53
#define STEP_DENOMINATOR 3
#define VECTOR_DENOMINATOR_POWER 24
#define SMOOTH_SERIES_TERMS 512
#define PRIME_CUTOFF 208063ULL

typedef struct {
    mpfr_t lo;
    mpfr_t hi;
} interval;

static mpfr_prec_t g_precision;

static const long BNUM[MATRIX_SIZE] = {
    106102L, 221836L, 325480L, 480921L, 625575L, 752703L,
    910718L, 1094731L, 1269522L, 1475676L, 1673192L, 1854308L,
    2046207L, 2221746L, 2381750L, 2554396L, 2711898L, 2834737L,
    2955457L, 3057472L, 3143391L, 3240134L, 3312969L, 3371409L,
    3438048L, 3462946L, 3463878L, 3462946L, 3438048L, 3371409L,
    3312969L, 3240134L, 3143391L, 3057472L, 2955457L, 2834737L,
    2711898L, 2554396L, 2381750L, 2221746L, 2046207L, 1854308L,
    1673192L, 1475676L, 1269522L, 1094731L, 910718L, 752703L,
    625575L, 480921L, 325480L, 221836L, 106102L
};

static void interval_init(interval *x) {
    mpfr_init2(x->lo, g_precision);
    mpfr_init2(x->hi, g_precision);
    mpfr_set_zero(x->lo, 1);
    mpfr_set_zero(x->hi, 1);
}

static void interval_clear(interval *x) {
    mpfr_clear(x->lo);
    mpfr_clear(x->hi);
}

static void interval_set(interval *result, const interval *source) {
    mpfr_set(result->lo, source->lo, MPFR_RNDD);
    mpfr_set(result->hi, source->hi, MPFR_RNDU);
}

static void interval_set_ui(interval *result, unsigned long value) {
    mpfr_set_ui(result->lo, value, MPFR_RNDD);
    mpfr_set_ui(result->hi, value, MPFR_RNDU);
}

static void interval_add(
    interval *result,
    const interval *left,
    const interval *right
) {
    mpfr_add(result->lo, left->lo, right->lo, MPFR_RNDD);
    mpfr_add(result->hi, left->hi, right->hi, MPFR_RNDU);
}

static void interval_sub(
    interval *result,
    const interval *left,
    const interval *right
) {
    mpfr_sub(result->lo, left->lo, right->hi, MPFR_RNDD);
    mpfr_sub(result->hi, left->hi, right->lo, MPFR_RNDU);
}

static void interval_neg(interval *result, const interval *value) {
    mpfr_neg(result->lo, value->hi, MPFR_RNDD);
    mpfr_neg(result->hi, value->lo, MPFR_RNDU);
}

static void choose_lower(mpfr_ptr target, mpfr_srcptr candidate) {
    if (mpfr_cmp(candidate, target) < 0) {
        mpfr_set(target, candidate, MPFR_RNDD);
    }
}

static void choose_upper(mpfr_ptr target, mpfr_srcptr candidate) {
    if (mpfr_cmp(candidate, target) > 0) {
        mpfr_set(target, candidate, MPFR_RNDU);
    }
}

static void interval_mul(
    interval *result,
    const interval *left,
    const interval *right
) {
    mpfr_t product;
    mpfr_init2(product, g_precision);

    mpfr_mul(result->lo, left->lo, right->lo, MPFR_RNDD);
    mpfr_mul(product, left->lo, right->hi, MPFR_RNDD);
    choose_lower(result->lo, product);
    mpfr_mul(product, left->hi, right->lo, MPFR_RNDD);
    choose_lower(result->lo, product);
    mpfr_mul(product, left->hi, right->hi, MPFR_RNDD);
    choose_lower(result->lo, product);

    mpfr_mul(result->hi, left->lo, right->lo, MPFR_RNDU);
    mpfr_mul(product, left->lo, right->hi, MPFR_RNDU);
    choose_upper(result->hi, product);
    mpfr_mul(product, left->hi, right->lo, MPFR_RNDU);
    choose_upper(result->hi, product);
    mpfr_mul(product, left->hi, right->hi, MPFR_RNDU);
    choose_upper(result->hi, product);

    mpfr_clear(product);
}

static void interval_mul_ui(
    interval *result,
    const interval *value,
    unsigned long multiplier
) {
    mpfr_mul_ui(result->lo, value->lo, multiplier, MPFR_RNDD);
    mpfr_mul_ui(result->hi, value->hi, multiplier, MPFR_RNDU);
}

static void interval_div_ui(
    interval *result,
    const interval *value,
    unsigned long divisor
) {
    mpfr_div_ui(result->lo, value->lo, divisor, MPFR_RNDD);
    mpfr_div_ui(result->hi, value->hi, divisor, MPFR_RNDU);
}

static void interval_div_positive(
    interval *result,
    const interval *numerator,
    const interval *positive_denominator
) {
    mpfr_div(
        result->lo,
        numerator->lo,
        positive_denominator->hi,
        MPFR_RNDD
    );
    mpfr_div(
        result->hi,
        numerator->hi,
        positive_denominator->lo,
        MPFR_RNDU
    );
}

static void interval_log(interval *result, const interval *value) {
    mpfr_log(result->lo, value->lo, MPFR_RNDD);
    mpfr_log(result->hi, value->hi, MPFR_RNDU);
}

static void interval_sqrt(interval *result, const interval *value) {
    mpfr_sqrt(result->lo, value->lo, MPFR_RNDD);
    mpfr_sqrt(result->hi, value->hi, MPFR_RNDU);
}

static void interval_exp(interval *result, const interval *value) {
    mpfr_exp(result->lo, value->lo, MPFR_RNDD);
    mpfr_exp(result->hi, value->hi, MPFR_RNDU);
}

static __uint128_t integer_power(uint64_t base, int exponent) {
    __uint128_t result = 1;
    for (int index = 0; index < exponent; ++index) {
        result *= base;
    }
    return result;
}

static int ceil_log2_power(uint64_t value, int exponent) {
    __uint128_t powered = integer_power(value, exponent);
    int floor_log = 0;
    __uint128_t cursor = powered;
    while (cursor >>= 1) {
        ++floor_log;
    }
    return powered == (((__uint128_t)1) << floor_log)
        ? floor_log
        : floor_log + 1;
}

static void build_constants(
    interval *log2_value,
    interval *b_constant,
    interval *c_constant
) {
    interval pi;
    interval euler;
    interval catalan;
    interval log_pi;
    interval temporary;
    interval temporary_2;
    interval three_log2;

    interval_init(&pi);
    interval_init(&euler);
    interval_init(&catalan);
    interval_init(&log_pi);
    interval_init(&temporary);
    interval_init(&temporary_2);
    interval_init(&three_log2);

    mpfr_const_log2(log2_value->lo, MPFR_RNDD);
    mpfr_const_log2(log2_value->hi, MPFR_RNDU);
    mpfr_const_pi(pi.lo, MPFR_RNDD);
    mpfr_const_pi(pi.hi, MPFR_RNDU);
    mpfr_const_euler(euler.lo, MPFR_RNDD);
    mpfr_const_euler(euler.hi, MPFR_RNDU);
    mpfr_const_catalan(catalan.lo, MPFR_RNDD);
    mpfr_const_catalan(catalan.hi, MPFR_RNDU);
    interval_log(&log_pi, &pi);

    /* psi(1/4) = -EulerGamma - pi/2 - 3 log(2). */
    /* B = (psi(1/4)-log(pi))/2. */
    interval_div_ui(&temporary, &pi, 2);
    interval_mul_ui(&three_log2, log2_value, 3);
    interval_add(&temporary_2, &euler, &temporary);
    interval_add(&temporary, &temporary_2, &three_log2);
    interval_add(&temporary_2, &temporary, &log_pi);
    interval_neg(&temporary, &temporary_2);
    interval_div_ui(b_constant, &temporary, 2);

    /* C = pi^2 + 8 Catalan. */
    interval_mul(&temporary, &pi, &pi);
    interval_mul_ui(&temporary_2, &catalan, 8);
    interval_add(c_constant, &temporary, &temporary_2);

    interval_clear(&pi);
    interval_clear(&euler);
    interval_clear(&catalan);
    interval_clear(&log_pi);
    interval_clear(&temporary);
    interval_clear(&temporary_2);
    interval_clear(&three_log2);
}

static void evaluate_smooth_a(
    interval *output,
    const interval *t,
    const interval *b_constant,
    const interval *c_constant
) {
    interval half_t;
    interval exponential;
    interval leading;
    interval b_times_t;
    interval c_over_four;
    interval finite_sum;
    interval n_times_t;
    interval negative_n_times_t;
    interval exponential_term;
    interval term;
    interval first_omitted;
    interval ratio;
    interval one;
    interval denominator;
    interval tail;
    interval temporary;
    interval temporary_2;

    interval_init(&half_t);
    interval_init(&exponential);
    interval_init(&leading);
    interval_init(&b_times_t);
    interval_init(&c_over_four);
    interval_init(&finite_sum);
    interval_init(&n_times_t);
    interval_init(&negative_n_times_t);
    interval_init(&exponential_term);
    interval_init(&term);
    interval_init(&first_omitted);
    interval_init(&ratio);
    interval_init(&one);
    interval_init(&denominator);
    interval_init(&tail);
    interval_init(&temporary);
    interval_init(&temporary_2);

    interval_set_ui(&finite_sum, 0);
    interval_div_ui(&half_t, t, 2);
    interval_exp(&exponential, &half_t);
    interval_set_ui(&temporary, 2);
    interval_sub(&temporary_2, &exponential, &temporary);
    interval_mul_ui(&leading, &temporary_2, 4);
    interval_mul(&b_times_t, b_constant, t);
    interval_div_ui(&c_over_four, c_constant, 4);

    for (int index = 1; index <= SMOOTH_SERIES_TERMS; ++index) {
        const unsigned long denominator_index = 4UL * (unsigned long)index + 1UL;
        interval_mul_ui(&n_times_t, t, denominator_index);
        interval_div_ui(&temporary, &n_times_t, 2);
        interval_neg(&negative_n_times_t, &temporary);
        interval_exp(&exponential_term, &negative_n_times_t);
        interval_div_ui(
            &term,
            &exponential_term,
            denominator_index * denominator_index
        );
        interval_add(&temporary, &finite_sum, &term);
        interval_set(&finite_sum, &temporary);
    }

    {
        const unsigned long first_index =
            4UL * (SMOOTH_SERIES_TERMS + 1UL) + 1UL;
        interval_mul_ui(&n_times_t, t, first_index);
        interval_div_ui(&temporary, &n_times_t, 2);
        interval_neg(&negative_n_times_t, &temporary);
        interval_exp(&exponential_term, &negative_n_times_t);
        interval_div_ui(
            &first_omitted,
            &exponential_term,
            first_index * first_index
        );
    }

    /* Consecutive positive terms have ratio <= exp(-2t). */
    interval_mul_ui(&temporary, t, 2);
    interval_neg(&negative_n_times_t, &temporary);
    interval_exp(&ratio, &negative_n_times_t);
    interval_set_ui(&one, 1);
    interval_sub(&denominator, &one, &ratio);
    interval_div_positive(&tail, &first_omitted, &denominator);

    interval_add(&temporary, &leading, &b_times_t);
    interval_add(&temporary_2, &temporary, &c_over_four);

    /* A = leading + B t + C/4 - 4 * positive_series. */
    mpfr_add(temporary.lo, finite_sum.hi, tail.hi, MPFR_RNDU);
    mpfr_mul_ui(temporary.lo, temporary.lo, 4, MPFR_RNDU);
    mpfr_sub(output->lo, temporary_2.lo, temporary.lo, MPFR_RNDD);

    /* Omitting the positive tail gives a valid upper bound. */
    mpfr_mul_ui(temporary.lo, finite_sum.lo, 4, MPFR_RNDD);
    mpfr_sub(output->hi, temporary_2.hi, temporary.lo, MPFR_RNDU);

    interval_clear(&half_t);
    interval_clear(&exponential);
    interval_clear(&leading);
    interval_clear(&b_times_t);
    interval_clear(&c_over_four);
    interval_clear(&finite_sum);
    interval_clear(&n_times_t);
    interval_clear(&negative_n_times_t);
    interval_clear(&exponential_term);
    interval_clear(&term);
    interval_clear(&first_omitted);
    interval_clear(&ratio);
    interval_clear(&one);
    interval_clear(&denominator);
    interval_clear(&tail);
    interval_clear(&temporary);
    interval_clear(&temporary_2);
}

static void sha_u64_be(SHA256_CTX *context, uint64_t value) {
    unsigned char bytes[8];
    for (int index = 7; index >= 0; --index) {
        bytes[index] = (unsigned char)(value & 255U);
        value >>= 8;
    }
    SHA256_Update(context, bytes, sizeof(bytes));
}

static void sha_u32_be(SHA256_CTX *context, uint32_t value) {
    unsigned char bytes[4];
    for (int index = 3; index >= 0; --index) {
        bytes[index] = (unsigned char)(value & 255U);
        value >>= 8;
    }
    SHA256_Update(context, bytes, sizeof(bytes));
}

int main(int argc, char **argv) {
    g_precision = argc > 1 ? strtol(argv[1], NULL, 10) : 192;
    if (g_precision < 64) {
        fprintf(stderr, "precision must be at least 64 bits\n");
        return 2;
    }

    if (
        integer_power(PRIME_CUTOFF, STEP_DENOMINATOR)
            > (((__uint128_t)1) << MATRIX_SIZE)
        || integer_power(PRIME_CUTOFF + 1, STEP_DENOMINATOR)
            <= (((__uint128_t)1) << MATRIX_SIZE)
    ) {
        fprintf(stderr, "hard-coded prime cutoff is inconsistent\n");
        return 3;
    }

    long long difference[MATRIX_SIZE + 1];
    long long autocorrelation[MATRIX_SIZE];
    difference[0] = BNUM[0];
    for (int index = 1; index < MATRIX_SIZE; ++index) {
        difference[index] = BNUM[index] - BNUM[index - 1];
    }
    difference[MATRIX_SIZE] = -BNUM[MATRIX_SIZE - 1];

    long long difference_sum = 0;
    for (int index = 0; index <= MATRIX_SIZE; ++index) {
        difference_sum += difference[index];
    }
    if (difference_sum != 0) {
        fprintf(stderr, "difference vector is not zero-sum\n");
        return 4;
    }

    for (int lag = 1; lag <= MATRIX_SIZE; ++lag) {
        __int128 total = 0;
        for (int index = 0; index <= MATRIX_SIZE - lag; ++index) {
            total += (__int128)difference[index] * difference[index + lag];
        }
        if (total > INT64_MAX || total < INT64_MIN) {
            fprintf(stderr, "autocorrelation overflow\n");
            return 5;
        }
        autocorrelation[lag - 1] = (long long)total;
    }

    uint8_t *prime = malloc(PRIME_CUTOFF + 1);
    if (prime == NULL) {
        fprintf(stderr, "unable to allocate sieve\n");
        return 6;
    }
    memset(prime, 1, PRIME_CUTOFF + 1);
    prime[0] = 0;
    prime[1] = 0;
    for (uint64_t p = 2; p * p <= PRIME_CUTOFF; ++p) {
        if (!prime[p]) {
            continue;
        }
        for (uint64_t composite = p * p; composite <= PRIME_CUTOFF; composite += p) {
            prime[composite] = 0;
        }
    }

    interval log2_value;
    interval b_constant;
    interval c_constant;
    interval step;
    interval bucket_p0[MATRIX_SIZE + 1];
    interval bucket_p1[MATRIX_SIZE + 1];
    interval prefix_p0[MATRIX_SIZE + 1];
    interval prefix_p1[MATRIX_SIZE + 1];
    interval psi[MATRIX_SIZE + 1];

    interval_init(&log2_value);
    interval_init(&b_constant);
    interval_init(&c_constant);
    interval_init(&step);
    for (int index = 0; index <= MATRIX_SIZE; ++index) {
        interval_init(&bucket_p0[index]);
        interval_init(&bucket_p1[index]);
        interval_init(&prefix_p0[index]);
        interval_init(&prefix_p1[index]);
        interval_init(&psi[index]);
    }

    build_constants(&log2_value, &b_constant, &c_constant);
    interval_div_ui(&step, &log2_value, STEP_DENOMINATOR);

    interval p_interval;
    interval log_p;
    interval q_interval;
    interval sqrt_q;
    interval weight;
    interval log_q;
    interval weighted_log_q;
    interval temporary;
    interval_init(&p_interval);
    interval_init(&log_p);
    interval_init(&q_interval);
    interval_init(&sqrt_q);
    interval_init(&weight);
    interval_init(&log_q);
    interval_init(&weighted_log_q);
    interval_init(&temporary);

    uint64_t prime_count = 0;
    uint64_t prime_power_count = 0;
    SHA256_CTX manifest_context;
    SHA256_Init(&manifest_context);

    for (uint64_t p = 2; p <= PRIME_CUTOFF; ++p) {
        if (!prime[p]) {
            continue;
        }
        ++prime_count;
        interval_set_ui(&p_interval, (unsigned long)p);
        interval_log(&log_p, &p_interval);

        uint64_t q = p;
        unsigned long exponent = 1;
        while (q <= PRIME_CUTOFF) {
            const int bucket = ceil_log2_power(q, STEP_DENOMINATOR);
            if (bucket < 1 || bucket > MATRIX_SIZE) {
                fprintf(stderr, "prime-power bucket out of range\n");
                return 7;
            }

            interval_set_ui(&q_interval, (unsigned long)q);
            interval_sqrt(&sqrt_q, &q_interval);
            interval_div_positive(&weight, &log_p, &sqrt_q);
            interval_mul_ui(&log_q, &log_p, exponent);
            interval_mul(&weighted_log_q, &weight, &log_q);

            interval_add(&temporary, &bucket_p0[bucket], &weight);
            interval_set(&bucket_p0[bucket], &temporary);
            interval_add(&temporary, &bucket_p1[bucket], &weighted_log_q);
            interval_set(&bucket_p1[bucket], &temporary);

            sha_u64_be(&manifest_context, q);
            sha_u64_be(&manifest_context, p);
            sha_u32_be(&manifest_context, (uint32_t)exponent);
            ++prime_power_count;

            if (q > PRIME_CUTOFF / p) {
                break;
            }
            q *= p;
            ++exponent;
        }
    }

    unsigned char manifest_digest[SHA256_DIGEST_LENGTH];
    char manifest_hex[2 * SHA256_DIGEST_LENGTH + 1];
    SHA256_Final(manifest_digest, &manifest_context);
    for (int index = 0; index < SHA256_DIGEST_LENGTH; ++index) {
        sprintf(manifest_hex + 2 * index, "%02x", manifest_digest[index]);
    }
    manifest_hex[2 * SHA256_DIGEST_LENGTH] = '\0';

    interval_set_ui(&prefix_p0[0], 0);
    interval_set_ui(&prefix_p1[0], 0);
    interval_set_ui(&psi[0], 0);

    for (int k = 1; k <= MATRIX_SIZE; ++k) {
        interval_add(&prefix_p0[k], &prefix_p0[k - 1], &bucket_p0[k]);
        interval_add(&prefix_p1[k], &prefix_p1[k - 1], &bucket_p1[k]);

        interval t;
        interval smooth;
        interval t_times_p0;
        interval_init(&t);
        interval_init(&smooth);
        interval_init(&t_times_p0);

        interval_mul_ui(&t, &step, (unsigned long)k);
        evaluate_smooth_a(&smooth, &t, &b_constant, &c_constant);
        interval_mul(&t_times_p0, &t, &prefix_p0[k]);

        mpfr_sub(psi[k].lo, smooth.lo, t_times_p0.hi, MPFR_RNDD);
        mpfr_add(psi[k].lo, psi[k].lo, prefix_p1[k].lo, MPFR_RNDD);
        mpfr_sub(psi[k].hi, smooth.hi, t_times_p0.lo, MPFR_RNDU);
        mpfr_add(psi[k].hi, psi[k].hi, prefix_p1[k].hi, MPFR_RNDU);

        interval_clear(&t);
        interval_clear(&smooth);
        interval_clear(&t_times_p0);
    }

    mpfr_t rayleigh_lo;
    mpfr_t rayleigh_hi;
    mpfr_t term_lo;
    mpfr_t term_hi;
    mpfr_init2(rayleigh_lo, g_precision);
    mpfr_init2(rayleigh_hi, g_precision);
    mpfr_init2(term_lo, g_precision);
    mpfr_init2(term_hi, g_precision);
    mpfr_set_zero(rayleigh_lo, 1);
    mpfr_set_zero(rayleigh_hi, 1);

    for (int k = 1; k <= MATRIX_SIZE; ++k) {
        const long coefficient = -2L * autocorrelation[k - 1];
        if (coefficient >= 0) {
            mpfr_mul_si(term_lo, psi[k].lo, coefficient, MPFR_RNDD);
            mpfr_mul_si(term_hi, psi[k].hi, coefficient, MPFR_RNDU);
        } else {
            mpfr_mul_si(term_lo, psi[k].hi, coefficient, MPFR_RNDD);
            mpfr_mul_si(term_hi, psi[k].lo, coefficient, MPFR_RNDU);
        }
        mpfr_add(rayleigh_lo, rayleigh_lo, term_lo, MPFR_RNDD);
        mpfr_add(rayleigh_hi, rayleigh_hi, term_hi, MPFR_RNDU);
    }
    mpfr_div_2ui(
        rayleigh_lo,
        rayleigh_lo,
        2 * VECTOR_DENOMINATOR_POWER,
        MPFR_RNDD
    );
    mpfr_div_2ui(
        rayleigh_hi,
        rayleigh_hi,
        2 * VECTOR_DENOMINATOR_POWER,
        MPFR_RNDU
    );

    printf("{\n");
    printf("  \"schema\": \"riemann.screw.toeplitz-control.v1\",\n");
    printf("  \"classification\": \"DIRECTED_POSITIVE_CONTROL\",\n");
    printf("  \"normalization\": \"D-9501\",\n");
    printf("  \"filter_theorem\": \"L-9504\",\n");
    printf("  \"precision_bits\": %ld,\n", g_precision);
    printf("  \"prime_cutoff\": %llu,\n", (unsigned long long)PRIME_CUTOFF);
    printf("  \"prime_count\": %llu,\n", (unsigned long long)prime_count);
    printf(
        "  \"prime_power_count\": %llu,\n",
        (unsigned long long)prime_power_count
    );
    printf(
        "  \"manifest_order\": "
        "\"prime-major: p ascending, exponent ascending\",\n"
    );
    printf(
        "  \"manifest_row_encoding\": "
        "\"q:u64be || p:u64be || exponent:u32be\",\n"
    );
    printf("  \"manifest_sha256\": \"%s\",\n", manifest_hex);
    printf(
        "  \"step\": {\"kind\":\"symbolic-log-ratio\","
        "\"p\":2,\"denominator\":3},\n"
    );
    printf(
        "  \"threshold_rule\": \"q^3 <= 2^k at t=k*log(2)/3\",\n"
    );
    printf("  \"matrix_size\": %d,\n", MATRIX_SIZE);
    printf(
        "  \"vector_denominator_power\": %d,\n",
        VECTOR_DENOMINATOR_POWER
    );
    printf("  \"smooth_series_terms\": %d,\n", SMOOTH_SERIES_TERMS);
    printf(
        "  \"strict_positive\": %s,\n",
        mpfr_cmp_ui(rayleigh_lo, 0) > 0 ? "true" : "false"
    );

    printf("  \"b_numerators\": [");
    for (int index = 0; index < MATRIX_SIZE; ++index) {
        printf("%s%ld", index ? "," : "", BNUM[index]);
    }
    printf("],\n");

    printf("  \"rayleigh_interval\": [\n    \"");
    mpfr_printf("%.90RDe", rayleigh_lo);
    printf("\",\n    \"");
    mpfr_printf("%.90RUe", rayleigh_hi);
    printf("\"\n  ],\n");

    printf("  \"psi_intervals\": [\n");
    for (int k = 1; k <= MATRIX_SIZE; ++k) {
        printf("    {\"k\":%d,\"lo\":\"", k);
        mpfr_printf("%.82RDe", psi[k].lo);
        printf("\",\"hi\":\"");
        mpfr_printf("%.82RUe", psi[k].hi);
        printf("\"}%s\n", k == MATRIX_SIZE ? "" : ",");
    }
    printf("  ]\n}\n");

    free(prime);
    interval_clear(&p_interval);
    interval_clear(&log_p);
    interval_clear(&q_interval);
    interval_clear(&sqrt_q);
    interval_clear(&weight);
    interval_clear(&log_q);
    interval_clear(&weighted_log_q);
    interval_clear(&temporary);
    interval_clear(&log2_value);
    interval_clear(&b_constant);
    interval_clear(&c_constant);
    interval_clear(&step);
    for (int index = 0; index <= MATRIX_SIZE; ++index) {
        interval_clear(&bucket_p0[index]);
        interval_clear(&bucket_p1[index]);
        interval_clear(&prefix_p0[index]);
        interval_clear(&prefix_p1[index]);
        interval_clear(&psi[index]);
    }
    mpfr_clear(rayleigh_lo);
    mpfr_clear(rayleigh_hi);
    mpfr_clear(term_lo);
    mpfr_clear(term_hi);
    return 0;
}
