#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    long double sum;
    long double correction;
} kahan_sum;

static inline void kahan_add(kahan_sum *state, long double value) {
    long double y = value - state->correction;
    long double updated = state->sum + y;
    state->correction = (updated - state->sum) - y;
    state->sum = updated;
}

static int build_mobius(int limit, int8_t *mu, uint8_t *composite) {
    memset(mu, 1, (size_t)limit + 1);
    memset(composite, 0, (size_t)limit + 1);
    mu[0] = 0;
    int prime_count = 0;
    for (int p = 2; p <= limit; ++p) {
        if (composite[p]) {
            continue;
        }
        ++prime_count;
        for (int64_t multiple = (int64_t)p * 2; multiple <= limit; multiple += p) {
            composite[multiple] = 1;
        }
        for (int64_t multiple = p; multiple <= limit; multiple += p) {
            mu[multiple] = (int8_t)(-mu[multiple]);
        }
        int64_t square = (int64_t)p * p;
        if (square <= limit) {
            for (int64_t multiple = square; multiple <= limit; multiple += square) {
                mu[multiple] = 0;
            }
        }
    }
    mu[1] = 1;
    return prime_count;
}

static inline long double row_coefficient(int n, int row, const int8_t *mu) {
    if (row == 2) {
        long double value = (n == 1 ? 1.0L : 0.0L) - (long double)mu[n];
        if ((n & 1) == 0) {
            value += 2.0L * mu[n / 2];
        }
        if (n % 3 == 0) {
            value -= mu[n / 3];
        }
        return value;
    }

    long double value = (n == 1 ? 1.0L / 3.0L : 0.0L) - (long double)mu[n] / 3.0L;
    if ((n & 1) == 0) {
        value -= (long double)mu[n / 2] / 3.0L;
    }
    if (n % 3 == 0) {
        value += (5.0L / 3.0L) * mu[n / 3];
    }
    if ((n & 3) == 0) {
        value -= mu[n / 4];
    }
    return value;
}

static int scan_row(
    int limit,
    int row,
    const int8_t *mu,
    long double *sum_history,
    long double *log_history
) {
    int history_limit = limit / 4;
    kahan_sum weighted = {0.0L, 0.0L};
    kahan_sum weighted_log = {0.0L, 0.0L};
    sum_history[0] = 0.0L;
    log_history[0] = 0.0L;

    long double minimum = 1e4000L;
    long double late_minimum = 1e4000L;
    int minimum_at = -1;
    int late_minimum_at = -1;

    for (int n = 1; n <= limit; ++n) {
        long double coefficient = row_coefficient(n, row, mu);
        long double term = coefficient / sqrtl((long double)n);
        kahan_add(&weighted, term);
        kahan_add(&weighted_log, term * logl((long double)n));

        if (n <= history_limit) {
            sum_history[n] = weighted.sum;
            log_history[n] = weighted_log.sum;
        }

        if (n >= row + 1) {
            long double full = logl((long double)n) * weighted.sum - weighted_log.sum;
            int quarter_index = n / 4;
            long double quarter = 0.0L;
            if (quarter_index >= 1) {
                quarter =
                    logl((long double)n / 4.0L) * sum_history[quarter_index]
                    - log_history[quarter_index];
            }
            long double annular = full - quarter;
            if (annular < minimum) {
                minimum = annular;
                minimum_at = n;
            }
            if (n >= 1000000 && annular < late_minimum) {
                late_minimum = annular;
                late_minimum_at = n;
            }
            if (annular < -1e-14L) {
                fprintf(stderr, "NEGATIVE row=%d X=%d value=%.21Lg\n", row, n, annular);
                return 1;
            }
        }
    }

    printf(
        "row=%d limit=%d minimum=%.21Lg at=%d late_minimum=%.21Lg at=%d PASS\n",
        row,
        limit,
        minimum,
        minimum_at,
        late_minimum,
        late_minimum_at
    );
    return 0;
}

int main(int argc, char **argv) {
    int limit = 10000000;
    if (argc > 1) {
        limit = atoi(argv[1]);
    }

    int history_limit = limit / 4;
    int8_t *mu = malloc((size_t)limit + 1);
    uint8_t *composite = malloc((size_t)limit + 1);
    long double *sum_history = malloc((size_t)(history_limit + 1) * sizeof(long double));
    long double *log_history = malloc((size_t)(history_limit + 1) * sizeof(long double));
    if (!mu || !composite || !sum_history || !log_history) {
        fprintf(stderr, "allocation failure\n");
        return 2;
    }

    int prime_count = build_mobius(limit, mu, composite);
    fprintf(stderr, "limit=%d primes=%d\n", limit, prime_count);
    free(composite);

    int status = 0;
    status |= scan_row(limit, 2, mu, sum_history, log_history);
    status |= scan_row(limit, 3, mu, sum_history, log_history);

    free(mu);
    free(sum_history);
    free(log_history);
    return status;
}
