// Standard-library reconnaissance scanner for L-23812.
//
// This uses long double/double arithmetic and is NOT a proof object.  It is
// intentionally separate from verify.py, which performs a modest directed
// Decimal check.
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
  if (argc < 2) {
    std::cerr << "usage: scan_large X\n";
    return 2;
  }
  const int X = std::stoi(argv[1]);

  std::vector<int8_t> mu(X + 1, 0);
  std::vector<int> primes;
  std::vector<uint8_t> composite(X + 1, 0);
  mu[1] = 1;
  for (int n = 2; n <= X; ++n) {
    if (!composite[n]) {
      primes.push_back(n);
      mu[n] = -1;
    }
    for (int p : primes) {
      const long long m = 1LL * n * p;
      if (m > X) break;
      composite[m] = 1;
      if (n % p == 0) {
        mu[m] = 0;
        break;
      }
      mu[m] = -mu[n];
    }
  }
  composite.clear();
  composite.shrink_to_fit();

  std::vector<double> U(X + 2, 0.0);
  std::vector<double> incoming(X + 1, 0.0);

  for (int k = 1; k <= X; ++k) {
    if (mu[k] == 0) continue;
    const double sign = static_cast<double>(mu[k]);
    for (int m = 1; m <= X / k; ++m) {
      const int q = k * m;
      if (q < 2) continue;
      U[m] += sign * std::log(static_cast<double>(X) / q) /
              std::sqrt(static_cast<double>(q));
    }
  }
  mu.clear();
  mu.shrink_to_fit();

  int negative_count = 0;
  int largest_negative_index = 0;
  int minimum_index = 0;
  double minimum_value = 1e300;
  long double weighted_negative_mass = 0.0L;

  for (int n = X; n >= 2; --n) {
    const double divergence = U[n] - U[n + 1];
    const double d = divergence + incoming[n];
    if (d < 0.0) {
      ++negative_count;
      largest_negative_index = std::max(largest_negative_index, n);
      weighted_negative_mass += static_cast<long double>(n) * (-d);
    }
    if (d < minimum_value) {
      minimum_value = d;
      minimum_index = n;
    }

    const int j3 = std::max(1, n / 3);
    const int j2 = std::max(1, n / 2);
    incoming[j3] += (31.0 / 32.0) * d;
    incoming[n - j3] += (31.0 / 32.0) * d;
    incoming[j2] += (1.0 / 32.0) * d;
    incoming[n - j2] += (1.0 / 32.0) * d;
  }

  std::cout << std::setprecision(17)
            << "X=" << X
            << " weights=31/32,1/32"
            << " negative_count=" << negative_count
            << " largest_negative_index=" << largest_negative_index
            << " minimum=" << minimum_value
            << " minimum_index=" << minimum_index
            << " weighted_negative_mass="
            << static_cast<double>(weighted_negative_mass)
            << " terminal_balance=" << (U[1] - U[2] + incoming[1])
            << "\n";
  return 0;
}
