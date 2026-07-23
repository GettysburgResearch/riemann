#include <mpfr.h>
#include <gmp.h>
#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <memory>
#include <stdexcept>
#include <string>
#include <vector>

struct Number {
    mpfr_t x;
    explicit Number(mpfr_prec_t precision) { mpfr_init2(x, precision); }
    ~Number() { mpfr_clear(x); }
    Number(const Number &) = delete;
    Number &operator=(const Number &) = delete;
};

struct Interval {
    Number lower;
    Number upper;
    explicit Interval(mpfr_prec_t precision) : lower(precision), upper(precision) {}
};

struct ComplexIntervals {
    std::vector<std::unique_ptr<Interval>> real;
    std::vector<std::unique_ptr<Interval>> imag;
};

static_assert(sizeof(unsigned long) >= 8, "producer requires a 64-bit unsigned long ABI");

static void set_unsigned(Interval &out, uint64_t value) {
    mpfr_set_ui(out.lower.x, static_cast<unsigned long>(value), MPFR_RNDD);
    mpfr_set_ui(out.upper.x, static_cast<unsigned long>(value), MPFR_RNDU);
}

static void set_zero(Interval &out) {
    mpfr_set_ui(out.lower.x, 0, MPFR_RNDN);
    mpfr_set_ui(out.upper.x, 0, MPFR_RNDN);
}

static void set_dyadic(
    Interval &out, const mpz_t numerator, unsigned long scale_bits
) {
    mpfr_set_z(out.lower.x, numerator, MPFR_RNDD);
    mpfr_div_2ui(out.lower.x, out.lower.x, scale_bits, MPFR_RNDD);
    mpfr_set_z(out.upper.x, numerator, MPFR_RNDU);
    mpfr_div_2ui(out.upper.x, out.upper.x, scale_bits, MPFR_RNDU);
}

static void copy_interval(Interval &out, const Interval &source) {
    mpfr_set(out.lower.x, source.lower.x, MPFR_RNDD);
    mpfr_set(out.upper.x, source.upper.x, MPFR_RNDU);
}

static void add_interval(
    Interval &out, const Interval &left, const Interval &right
) {
    mpfr_add(out.lower.x, left.lower.x, right.lower.x, MPFR_RNDD);
    mpfr_add(out.upper.x, left.upper.x, right.upper.x, MPFR_RNDU);
}

static void subtract_interval(
    Interval &out, const Interval &left, const Interval &right
) {
    mpfr_sub(out.lower.x, left.lower.x, right.upper.x, MPFR_RNDD);
    mpfr_sub(out.upper.x, left.upper.x, right.lower.x, MPFR_RNDU);
}

static void scale_unsigned(
    Interval &out, const Interval &source, uint64_t scalar
) {
    mpfr_mul_ui(
        out.lower.x, source.lower.x, static_cast<unsigned long>(scalar), MPFR_RNDD
    );
    mpfr_mul_ui(
        out.upper.x, source.upper.x, static_cast<unsigned long>(scalar), MPFR_RNDU
    );
}

struct Scratch {
    std::vector<std::unique_ptr<Number>> values;
    Scratch(mpfr_prec_t precision, int count = 20) {
        for (int index = 0; index < count; ++index) {
            values.emplace_back(std::make_unique<Number>(precision));
        }
    }
};

static void multiply_interval(
    Interval &out,
    const Interval &left,
    const Interval &right,
    Scratch &scratch
) {
    mpfr_mul(
        scratch.values[0]->x, left.lower.x, right.lower.x, MPFR_RNDD
    );
    mpfr_mul(
        scratch.values[1]->x, left.lower.x, right.upper.x, MPFR_RNDD
    );
    mpfr_mul(
        scratch.values[2]->x, left.upper.x, right.lower.x, MPFR_RNDD
    );
    mpfr_mul(
        scratch.values[3]->x, left.upper.x, right.upper.x, MPFR_RNDD
    );
    mpfr_set(out.lower.x, scratch.values[0]->x, MPFR_RNDD);
    for (int index = 1; index < 4; ++index) {
        if (mpfr_cmp(scratch.values[index]->x, out.lower.x) < 0) {
            mpfr_set(out.lower.x, scratch.values[index]->x, MPFR_RNDD);
        }
    }

    mpfr_mul(
        scratch.values[0]->x, left.lower.x, right.lower.x, MPFR_RNDU
    );
    mpfr_mul(
        scratch.values[1]->x, left.lower.x, right.upper.x, MPFR_RNDU
    );
    mpfr_mul(
        scratch.values[2]->x, left.upper.x, right.lower.x, MPFR_RNDU
    );
    mpfr_mul(
        scratch.values[3]->x, left.upper.x, right.upper.x, MPFR_RNDU
    );
    mpfr_set(out.upper.x, scratch.values[0]->x, MPFR_RNDU);
    for (int index = 1; index < 4; ++index) {
        if (mpfr_cmp(scratch.values[index]->x, out.upper.x) > 0) {
            mpfr_set(out.upper.x, scratch.values[index]->x, MPFR_RNDU);
        }
    }
}

static void divide_positive_interval(
    Interval &out, const Interval &numerator, const Interval &denominator
) {
    if (mpfr_cmp_ui(denominator.lower.x, 0) <= 0) {
        throw std::runtime_error("nonpositive interval divisor");
    }
    mpfr_div(
        out.lower.x, numerator.lower.x, denominator.upper.x, MPFR_RNDD
    );
    mpfr_div(
        out.upper.x, numerator.upper.x, denominator.lower.x, MPFR_RNDU
    );
}

static void hull_interval(
    Interval &out, const Interval &source, bool first_piece
) {
    if (first_piece) {
        copy_interval(out, source);
        return;
    }
    if (mpfr_cmp(source.lower.x, out.lower.x) < 0) {
        mpfr_set(out.lower.x, source.lower.x, MPFR_RNDD);
    }
    if (mpfr_cmp(source.upper.x, out.upper.x) > 0) {
        mpfr_set(out.upper.x, source.upper.x, MPFR_RNDU);
    }
}

static void clamp_unit_interval(Interval &interval) {
    if (mpfr_cmp_si(interval.lower.x, -1) < 0) {
        mpfr_set_si(interval.lower.x, -1, MPFR_RNDN);
    }
    if (mpfr_cmp_ui(interval.upper.x, 1) > 0) {
        mpfr_set_ui(interval.upper.x, 1, MPFR_RNDN);
    }
}

struct Manifest {
    int cells = 0;
    int vector_scale_bits = 0;
    int autocorrelation_scale_bits = 0;
    int cutoff_power10 = 0;
    uint64_t cutoff = 0;
    uint64_t segment_size = 0;
    uint64_t total_segments = 0;
    std::string vector_sha256;
    std::string normalization_sha256;
    std::string parameter_sha256;
    std::string carrier_numerator;
    std::string carrier_denominator;
    std::vector<std::string> autocorrelation_real;
    std::vector<std::string> autocorrelation_imag;
};

static Manifest read_manifest(const std::string &path) {
    std::ifstream input(path);
    if (!input) {
        throw std::runtime_error("cannot open manifest");
    }
    std::string magic;
    input >> magic;
    if (magic != "RIEMANN_D0801_AUTOCORRELATION_V1") {
        throw std::runtime_error("bad manifest magic");
    }

    Manifest manifest;
    std::string key;
    int autocorrelation_count = 0;
    while (input >> key) {
        if (key == "cells") {
            input >> manifest.cells;
        } else if (key == "vector_scale_bits") {
            input >> manifest.vector_scale_bits;
        } else if (key == "autocorr_scale_bits") {
            input >> manifest.autocorrelation_scale_bits;
        } else if (key == "vector_sha256") {
            input >> manifest.vector_sha256;
        } else if (key == "normalization_sha256") {
            input >> manifest.normalization_sha256;
        } else if (key == "parameter_sha256") {
            input >> manifest.parameter_sha256;
        } else if (key == "cutoff_power10") {
            input >> manifest.cutoff_power10;
        } else if (key == "cutoff") {
            input >> manifest.cutoff;
        } else if (key == "carrier_num") {
            input >> manifest.carrier_numerator;
        } else if (key == "carrier_den") {
            input >> manifest.carrier_denominator;
        } else if (key == "segment_size") {
            input >> manifest.segment_size;
        } else if (key == "total_segments") {
            input >> manifest.total_segments;
        } else if (key == "a_count") {
            input >> autocorrelation_count;
            manifest.autocorrelation_real.resize(autocorrelation_count);
            manifest.autocorrelation_imag.resize(autocorrelation_count);
        } else if (key == "a") {
            int lag = 0;
            input >> lag;
            if (lag < 0 || lag >= autocorrelation_count) {
                throw std::runtime_error("bad autocorrelation index");
            }
            input >> manifest.autocorrelation_real[lag]
                  >> manifest.autocorrelation_imag[lag];
        } else {
            throw std::runtime_error("unknown manifest key: " + key);
        }
    }

    if (
        manifest.cells < 1
        || autocorrelation_count != manifest.cells + 1
        || manifest.cutoff < 2
        || manifest.segment_size < 1
        || manifest.carrier_denominator == "0"
    ) {
        throw std::runtime_error("incomplete manifest");
    }
    if (
        manifest.normalization_sha256
        != "65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be"
    ) {
        throw std::runtime_error("normalization fingerprint mismatch");
    }
    uint64_t expected_cutoff = 1;
    for (int index = 0; index < manifest.cutoff_power10; ++index) {
        if (expected_cutoff > UINT64_MAX / 10) {
            throw std::runtime_error("cutoff overflow");
        }
        expected_cutoff *= 10;
    }
    if (expected_cutoff != manifest.cutoff) {
        throw std::runtime_error("cutoff does not match cutoff_power10");
    }
    const uint64_t expected_segments
        = (manifest.cutoff - 2) / manifest.segment_size + 1;
    if (expected_segments != manifest.total_segments) {
        throw std::runtime_error("total_segments mismatch");
    }
    return manifest;
}

static std::vector<uint32_t> simple_primes(uint64_t limit) {
    std::vector<uint8_t> mark(limit + 1, 1);
    mark[0] = 0;
    if (limit >= 1) {
        mark[1] = 0;
    }
    for (uint64_t prime = 2; prime * prime <= limit; ++prime) {
        if (mark[prime]) {
            for (
                uint64_t multiple = prime * prime;
                multiple <= limit;
                multiple += prime
            ) {
                mark[multiple] = 0;
            }
        }
    }
    std::vector<uint32_t> primes;
    for (uint64_t value = 2; value <= limit; ++value) {
        if (mark[value]) {
            primes.push_back(static_cast<uint32_t>(value));
        }
    }
    return primes;
}

static std::vector<uint64_t> segment_primes(
    uint64_t low,
    uint64_t high,
    const std::vector<uint32_t> &base_primes
) {
    std::vector<uint8_t> mark(high - low, 1);
    uint64_t root = static_cast<uint64_t>(
        std::sqrt(static_cast<long double>(high - 1))
    );
    while ((root + 1) * (root + 1) <= high - 1) {
        ++root;
    }
    while (root * root > high - 1) {
        --root;
    }
    for (uint32_t prime : base_primes) {
        if (prime > root) {
            break;
        }
        const uint64_t first = std::max<uint64_t>(
            static_cast<uint64_t>(prime) * prime,
            ((low + prime - 1) / prime) * prime
        );
        for (uint64_t multiple = first; multiple < high; multiple += prime) {
            mark[multiple - low] = 0;
        }
    }
    std::vector<uint64_t> primes;
    for (uint64_t offset = 0; offset < high - low; ++offset) {
        if (mark[offset] && low + offset >= 2) {
            primes.push_back(low + offset);
        }
    }
    return primes;
}

struct Evaluator {
    mpfr_prec_t precision;
    int cells;
    Interval pi;
    Interval log_cutoff;
    Interval carrier;
    ComplexIntervals autocorrelations;
    Scratch scratch;

    Interval prime_value;
    Interval log_prime;
    Interval log_power;
    Interval power_value;
    Interval sqrt_power;
    Interval denominator;
    Interval amplitude;
    Interval support_coordinate;
    Interval phase;
    Interval phase_radius;
    Interval cosine;
    Interval sine;
    Interval autocorrelation_real;
    Interval autocorrelation_imag;
    Interval real_factor;
    Interval term;
    Interval temporary_1;
    Interval temporary_2;
    Interval temporary_3;
    Interval temporary_4;
    Interval interpolation_fraction;
    Interval difference;

    uint64_t knot_hulls = 0;
    double maximum_phase_width = 0;

    Evaluator(const Manifest &manifest, mpfr_prec_t requested_precision)
        : precision(requested_precision),
          cells(manifest.cells),
          pi(requested_precision),
          log_cutoff(requested_precision),
          carrier(requested_precision),
          scratch(requested_precision),
          prime_value(requested_precision),
          log_prime(requested_precision),
          log_power(requested_precision),
          power_value(requested_precision),
          sqrt_power(requested_precision),
          denominator(requested_precision),
          amplitude(requested_precision),
          support_coordinate(requested_precision),
          phase(requested_precision),
          phase_radius(requested_precision),
          cosine(requested_precision),
          sine(requested_precision),
          autocorrelation_real(requested_precision),
          autocorrelation_imag(requested_precision),
          real_factor(requested_precision),
          term(requested_precision),
          temporary_1(requested_precision),
          temporary_2(requested_precision),
          temporary_3(requested_precision),
          temporary_4(requested_precision),
          interpolation_fraction(requested_precision),
          difference(requested_precision) {
        autocorrelations.real.reserve(cells + 1);
        autocorrelations.imag.reserve(cells + 1);
        for (int lag = 0; lag <= cells; ++lag) {
            autocorrelations.real.emplace_back(
                std::make_unique<Interval>(requested_precision)
            );
            autocorrelations.imag.emplace_back(
                std::make_unique<Interval>(requested_precision)
            );
            mpz_t numerator;
            mpz_init(numerator);
            mpz_set_str(
                numerator,
                manifest.autocorrelation_real[lag].c_str(),
                10
            );
            set_dyadic(
                *autocorrelations.real[lag],
                numerator,
                manifest.autocorrelation_scale_bits
            );
            mpz_set_str(
                numerator,
                manifest.autocorrelation_imag[lag].c_str(),
                10
            );
            set_dyadic(
                *autocorrelations.imag[lag],
                numerator,
                manifest.autocorrelation_scale_bits
            );
            mpz_clear(numerator);
        }

        mpfr_const_pi(pi.lower.x, MPFR_RNDD);
        mpfr_const_pi(pi.upper.x, MPFR_RNDU);

        set_unsigned(temporary_1, manifest.cutoff);
        mpfr_log(
            log_cutoff.lower.x,
            temporary_1.lower.x,
            MPFR_RNDD
        );
        mpfr_log(
            log_cutoff.upper.x,
            temporary_1.upper.x,
            MPFR_RNDU
        );

        mpz_t carrier_numerator;
        mpz_t carrier_denominator;
        mpz_init_set_str(
            carrier_numerator,
            manifest.carrier_numerator.c_str(),
            10
        );
        mpz_init_set_str(
            carrier_denominator,
            manifest.carrier_denominator.c_str(),
            10
        );
        mpfr_set_z(carrier.lower.x, carrier_numerator, MPFR_RNDD);
        mpfr_set_z(
            temporary_1.lower.x,
            carrier_denominator,
            MPFR_RNDU
        );
        mpfr_div(
            carrier.lower.x,
            carrier.lower.x,
            temporary_1.lower.x,
            MPFR_RNDD
        );
        mpfr_set_z(carrier.upper.x, carrier_numerator, MPFR_RNDU);
        mpfr_set_z(
            temporary_1.upper.x,
            carrier_denominator,
            MPFR_RNDD
        );
        mpfr_div(
            carrier.upper.x,
            carrier.upper.x,
            temporary_1.upper.x,
            MPFR_RNDU
        );
        mpz_clear(carrier_numerator);
        mpz_clear(carrier_denominator);
    }

    void interpolate_autocorrelation() {
        long first_lag = mpfr_get_si(
            support_coordinate.lower.x, MPFR_RNDD
        );
        long last_lag = mpfr_get_si(
            support_coordinate.upper.x, MPFR_RNDD
        );
        first_lag = std::max<long>(0, first_lag);
        last_lag = std::min<long>(cells, last_lag);
        bool first_piece = true;
        if (last_lag > first_lag) {
            ++knot_hulls;
        }

        for (long lag = first_lag; lag <= last_lag; ++lag) {
            if (lag >= cells) {
                set_zero(temporary_3);
                set_zero(temporary_4);
                hull_interval(
                    autocorrelation_real,
                    temporary_3,
                    first_piece
                );
                hull_interval(
                    autocorrelation_imag,
                    temporary_4,
                    first_piece
                );
                first_piece = false;
                continue;
            }

            mpfr_set(
                interpolation_fraction.lower.x,
                support_coordinate.lower.x,
                MPFR_RNDD
            );
            if (mpfr_cmp_ui(interpolation_fraction.lower.x, lag) < 0) {
                mpfr_set_ui(
                    interpolation_fraction.lower.x,
                    static_cast<unsigned long>(lag),
                    MPFR_RNDN
                );
            }
            mpfr_sub_ui(
                interpolation_fraction.lower.x,
                interpolation_fraction.lower.x,
                static_cast<unsigned long>(lag),
                MPFR_RNDD
            );

            mpfr_set(
                interpolation_fraction.upper.x,
                support_coordinate.upper.x,
                MPFR_RNDU
            );
            if (mpfr_cmp_ui(interpolation_fraction.upper.x, lag + 1) > 0) {
                mpfr_set_ui(
                    interpolation_fraction.upper.x,
                    static_cast<unsigned long>(lag + 1),
                    MPFR_RNDN
                );
            }
            mpfr_sub_ui(
                interpolation_fraction.upper.x,
                interpolation_fraction.upper.x,
                static_cast<unsigned long>(lag),
                MPFR_RNDU
            );
            if (
                mpfr_cmp(
                    interpolation_fraction.lower.x,
                    interpolation_fraction.upper.x
                ) > 0
            ) {
                continue;
            }

            subtract_interval(
                difference,
                *autocorrelations.real[lag + 1],
                *autocorrelations.real[lag]
            );
            multiply_interval(
                temporary_1,
                difference,
                interpolation_fraction,
                scratch
            );
            add_interval(
                temporary_3,
                *autocorrelations.real[lag],
                temporary_1
            );

            subtract_interval(
                difference,
                *autocorrelations.imag[lag + 1],
                *autocorrelations.imag[lag]
            );
            multiply_interval(
                temporary_1,
                difference,
                interpolation_fraction,
                scratch
            );
            add_interval(
                temporary_4,
                *autocorrelations.imag[lag],
                temporary_1
            );

            hull_interval(
                autocorrelation_real,
                temporary_3,
                first_piece
            );
            hull_interval(
                autocorrelation_imag,
                temporary_4,
                first_piece
            );
            first_piece = false;
        }

        if (first_piece) {
            set_zero(autocorrelation_real);
            set_zero(autocorrelation_imag);
        }
    }

    void evaluate(
        uint64_t prime_power,
        uint64_t base_prime,
        unsigned exponent,
        Interval &out
    ) {
        set_unsigned(prime_value, base_prime);
        mpfr_log(
            log_prime.lower.x,
            prime_value.lower.x,
            MPFR_RNDD
        );
        mpfr_log(
            log_prime.upper.x,
            prime_value.upper.x,
            MPFR_RNDU
        );
        scale_unsigned(log_power, log_prime, exponent);

        set_unsigned(power_value, prime_power);
        mpfr_sqrt(
            sqrt_power.lower.x,
            power_value.lower.x,
            MPFR_RNDD
        );
        mpfr_sqrt(
            sqrt_power.upper.x,
            power_value.upper.x,
            MPFR_RNDU
        );
        multiply_interval(denominator, pi, sqrt_power, scratch);
        divide_positive_interval(amplitude, log_prime, denominator);

        scale_unsigned(temporary_1, log_power, cells);
        divide_positive_interval(
            support_coordinate,
            temporary_1,
            log_cutoff
        );
        interpolate_autocorrelation();

        multiply_interval(phase, carrier, log_power, scratch);
        mpfr_sub(
            phase_radius.upper.x,
            phase.upper.x,
            phase.lower.x,
            MPFR_RNDU
        );
        mpfr_set_ui(phase_radius.lower.x, 0, MPFR_RNDN);
        maximum_phase_width = std::max(
            maximum_phase_width,
            mpfr_get_d(phase_radius.upper.x, MPFR_RNDU)
        );

        mpfr_cos(cosine.lower.x, phase.lower.x, MPFR_RNDD);
        mpfr_cos(cosine.upper.x, phase.lower.x, MPFR_RNDU);
        mpfr_sub(
            cosine.lower.x,
            cosine.lower.x,
            phase_radius.upper.x,
            MPFR_RNDD
        );
        mpfr_add(
            cosine.upper.x,
            cosine.upper.x,
            phase_radius.upper.x,
            MPFR_RNDU
        );
        clamp_unit_interval(cosine);

        mpfr_sin(sine.lower.x, phase.lower.x, MPFR_RNDD);
        mpfr_sin(sine.upper.x, phase.lower.x, MPFR_RNDU);
        mpfr_sub(
            sine.lower.x,
            sine.lower.x,
            phase_radius.upper.x,
            MPFR_RNDD
        );
        mpfr_add(
            sine.upper.x,
            sine.upper.x,
            phase_radius.upper.x,
            MPFR_RNDU
        );
        clamp_unit_interval(sine);

        multiply_interval(
            temporary_1,
            autocorrelation_real,
            cosine,
            scratch
        );
        multiply_interval(
            temporary_2,
            autocorrelation_imag,
            sine,
            scratch
        );
        add_interval(real_factor, temporary_1, temporary_2);
        multiply_interval(out, amplitude, real_factor, scratch);
    }
};

static std::string integer_string(const mpz_t value) {
    char *raw = mpz_get_str(nullptr, 10, value);
    std::string text(raw);
    void (*free_function)(void *, size_t);
    mp_get_memory_functions(nullptr, nullptr, &free_function);
    free_function(raw, text.size() + 1);
    return text;
}

static std::pair<std::string, std::string> rational_strings(
    mpfr_srcptr value
) {
    mpz_t numerator;
    mpz_t denominator;
    mpz_init(numerator);
    mpz_init_set_ui(denominator, 1);
    const mpfr_exp_t exponent = mpfr_get_z_2exp(numerator, value);
    if (exponent >= 0) {
        mpz_mul_2exp(numerator, numerator, exponent);
    } else {
        mpz_mul_2exp(denominator, denominator, -exponent);
    }
    const std::string numerator_text = integer_string(numerator);
    const std::string denominator_text = integer_string(denominator);
    mpz_clear(numerator);
    mpz_clear(denominator);
    return {numerator_text, denominator_text};
}

int main(int argc, char **argv) {
    try {
        std::map<std::string, std::string> options;
        bool include_higher_powers = false;
        for (int index = 1; index < argc; ++index) {
            const std::string argument = argv[index];
            if (argument == "--include-higher-powers") {
                include_higher_powers = true;
            } else if (
                argument.rfind("--", 0) == 0
                && index + 1 < argc
            ) {
                options[argument] = argv[++index];
            } else {
                throw std::runtime_error("bad argument: " + argument);
            }
        }
        auto required = [&](const std::string &key) -> std::string {
            if (!options.count(key)) {
                throw std::runtime_error("missing " + key);
            }
            return options[key];
        };

        const Manifest manifest = read_manifest(required("--manifest"));
        const uint64_t start_segment
            = std::stoull(required("--start-segment"));
        const uint64_t end_segment
            = std::stoull(required("--end-segment"));
        const mpfr_prec_t precision = std::stol(
            options.count("--precision")
                ? options["--precision"]
                : "192"
        );
        const std::string output_path = required("--output");
        if (
            !(start_segment < end_segment
              && end_segment <= manifest.total_segments)
        ) {
            throw std::runtime_error("bad segment range");
        }
        if (precision < 64 || precision > 4096) {
            throw std::runtime_error("precision must lie in [64,4096]");
        }

        Evaluator evaluator(manifest, precision);
        Interval sum(precision);
        Interval term(precision);
        set_zero(sum);

        const auto base_primes = simple_primes(
            static_cast<uint64_t>(
                std::sqrt(static_cast<long double>(manifest.cutoff))
            ) + 1
        );
        uint64_t prime_count = 0;
        uint64_t higher_power_count = 0;

        for (
            uint64_t segment = start_segment;
            segment < end_segment;
            ++segment
        ) {
            const uint64_t low
                = 2 + segment * manifest.segment_size;
            const uint64_t high = std::min<uint64_t>(
                manifest.cutoff + 1,
                low + manifest.segment_size
            );
            const auto primes = segment_primes(low, high, base_primes);
            for (uint64_t prime : primes) {
                evaluator.evaluate(prime, prime, 1, term);
                mpfr_add(
                    sum.lower.x,
                    sum.lower.x,
                    term.lower.x,
                    MPFR_RNDD
                );
                mpfr_add(
                    sum.upper.x,
                    sum.upper.x,
                    term.upper.x,
                    MPFR_RNDU
                );
            }
            prime_count += primes.size();
        }

        if (include_higher_powers) {
            for (uint32_t prime : base_primes) {
                uint64_t prime_power = static_cast<uint64_t>(prime) * prime;
                unsigned exponent = 2;
                while (prime_power <= manifest.cutoff) {
                    evaluator.evaluate(
                        prime_power,
                        prime,
                        exponent,
                        term
                    );
                    mpfr_add(
                        sum.lower.x,
                        sum.lower.x,
                        term.lower.x,
                        MPFR_RNDD
                    );
                    mpfr_add(
                        sum.upper.x,
                        sum.upper.x,
                        term.upper.x,
                        MPFR_RNDU
                    );
                    ++higher_power_count;
                    if (prime_power > manifest.cutoff / prime) {
                        break;
                    }
                    prime_power *= prime;
                    ++exponent;
                }
            }
        }

        const auto lower = rational_strings(sum.lower.x);
        const auto upper = rational_strings(sum.upper.x);
        std::ofstream output(output_path);
        if (!output) {
            throw std::runtime_error("cannot open output path");
        }
        output
            << "{\n"
            << "  \"schema\": \"riemann.piecewise-carrier-directed-shard.v1\",\n"
            << "  \"segment_start\": " << start_segment
            << ", \"segment_end\": " << end_segment << ",\n"
            << "  \"include_higher_powers\": "
            << (include_higher_powers ? "true" : "false") << ",\n"
            << "  \"prime_count\": " << prime_count
            << ", \"higher_prime_power_count\": " << higher_power_count
            << ", \"total_terms\": "
            << prime_count + higher_power_count << ",\n"
            << "  \"vector_sha256\": \"" << manifest.vector_sha256 << "\",\n"
            << "  \"parameter_sha256\": \"" << manifest.parameter_sha256 << "\",\n"
            << "  \"normalization_sha256\": \""
            << manifest.normalization_sha256 << "\",\n"
            << "  \"precision_bits\": " << precision
            << ", \"mpfr_version\": \"" << mpfr_get_version() << "\",\n"
            << "  \"phase_method\": "
            << "\"MPFR directed log/product plus correctly-rounded sin/cos "
            << "and Lipschitz phase widening\",\n"
            << "  \"knot_hulls\": " << evaluator.knot_hulls
            << ", \"maximum_phase_interval_width_upper\": "
            << std::setprecision(17) << evaluator.maximum_phase_width << ",\n"
            << "  \"prime_rayleigh_interval\": {\n"
            << "    \"lower\": {\"numerator\": " << lower.first
            << ", \"denominator\": " << lower.second << "},\n"
            << "    \"upper\": {\"numerator\": " << upper.first
            << ", \"denominator\": " << upper.second << "}\n"
            << "  }\n"
            << "}\n";
    } catch (const std::exception &error) {
        std::cerr << "error: " << error.what() << "\n";
        return 2;
    }
    return 0;
}
