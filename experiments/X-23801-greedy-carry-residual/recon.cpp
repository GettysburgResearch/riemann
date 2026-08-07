#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    const int X = argc > 1 ? std::atoi(argv[1]) : 1000000;

    std::vector<int> mu(X + 1), least_prime(X + 1), primes;
    mu[1] = 1;
    for (int n = 2; n <= X; ++n) {
        if (least_prime[n] == 0) {
            least_prime[n] = n;
            primes.push_back(n);
            mu[n] = -1;
        }
        for (int p : primes) {
            const long long value = 1LL * p * n;
            if (value > X) break;
            least_prime[value] = p;
            if (p == least_prime[n]) {
                mu[value] = 0;
                break;
            }
            mu[value] = -mu[n];
        }
    }

    std::vector<double> w(X + 1), u(X + 3), suffix(X + 4);
    for (int q = 1; q <= X; ++q) {
        w[q] = std::log(static_cast<double>(X) / q) / std::sqrt(q);
    }

    for (int k = 1; k <= X; ++k) {
        if (mu[k] == 0) continue;
        for (int m = 2; m <= X / k; ++m) {
            u[m] += mu[k] * w[m * k];
        }
    }

    for (int m = X; m >= 2; --m) {
        suffix[m] = suffix[m + 1] + u[m];
    }

    long long negative_count = 0;
    int first_negative = 0;
    double minimum = 1e300;
    double weighted_mass = 0.0;
    double coefficient_mass = 0.0;

    for (int j = 2; j <= X; ++j) {
        const double coefficient = (
            (j + 1.0) * (j * u[j] - (j - 2.0) * u[j + 1])
            + 2.0 * suffix[j + 2]
        ) / (j * (j - 1.0));

        if (coefficient < -1e-10) {
            ++negative_count;
            if (first_negative == 0) first_negative = j;
        }
        minimum = std::min(minimum, coefficient);
        weighted_mass += j * coefficient;
        coefficient_mass += coefficient;
    }

    std::cout << std::setprecision(17)
              << "{\n"
              << "  \"classification\": \"BINARY64_RECONNAISSANCE_ONLY\",\n"
              << "  \"xmax\": " << X << ",\n"
              << "  \"negative_count_below_minus_1e_10\": "
              << negative_count << ",\n"
              << "  \"first_negative_index\": " << first_negative << ",\n"
              << "  \"minimum_coefficient\": " << minimum << ",\n"
              << "  \"weighted_mass\": " << weighted_mass << ",\n"
              << "  \"mass_ratio_to_8_sqrt_x\": "
              << weighted_mass / (8.0 * std::sqrt(X)) << ",\n"
              << "  \"coefficient_mass\": " << coefficient_mass << "\n"
              << "}\n";
}
