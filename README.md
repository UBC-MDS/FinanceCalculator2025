# **Finance Calculator**

## Project Summary

**financecalculator** is a Python package for calculating Financial Services specifically for loans or investment scenarios.
This package serves as a convenient tool for managing personal finances, offering functionalities such as Periodic Payment(PMT) Calculation, Future Value(FV) Calculation, Present Value(PV) Calculation, and Frequency(N) Calculation.

## Contributors

Chaoyu Ou(Shell-human)

Meagan Gardner(meagangardner)

Ziming Fang(ethanfang08)

Zoe Ren(sgdkd)

## Installation

```bash
$ pip install financecalculator
```

## Package Content

This package offers four functions: PMT Calculation, FV Calculation, PV Calculation, N Calculation.

### Functions:

1. PMT Calculation

2. FV Calculation

3. PV Calculation

    ```present_value(principal, annual_rate, n_periods, contribution=0)```

    Calculates the present value of an investment or loan, accounting for optional contributions.

4. N Calculation

    ```n_periods(principal, annual_rate, future_value, contribution=0)```

    Calculates the number of periods (in months) needed to reach a specified future value.

### Common Parameters:

```principal``` *(float)*: The initial investment or loan amount.

```annual_rate``` *(float)*: Annual interest rate (as a percentage, e.g., 5 for 5%).

```n_periods``` *(int)*: Total number of periods (in months).

```contribution``` *(float, optional)*: Payment made per period (monthly contributions). Defaults to 0 if not provided.

## Python Ecosystem

The financial calculator project situates itself within the Python ecosystem as a learning-oriented initiative aimed at developing practical skills in financial computation and programming. While the Python ecosystem already includes robust packages and applications like [Loan Calculator](https://github.com/yanomateus/loan-calculator) and [Financial Calculator App](https://github.com/dilumdesilva/Financial-Calculator-App), this project serves as a valuable hands-on exercise for those seeking to deepen their understanding of financial concepts and Python development.

## Usage

- TODO

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`financecalculator` was created by Meagan Gardner. It is licensed under the terms of the MIT license.

## Credits

`financecalculator` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
