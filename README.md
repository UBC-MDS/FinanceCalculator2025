# **Finance Calculator**

------------------------------------------------------------------------

<img src="https://github.com/UBC-MDS/FinanceCalculator/blob/main/img/finance-calculator-200px.png">

## Project Summary

**financecalculator** is a Python package for calculating financial metrics specifically designed for loans or investment scenarios.\
This package serves as a convenient tool for managing personal finances, offering functionalities such as Periodic Payment (contribution) Calculation, Future Value (FV) Calculation, Present Value (PV) Calculation, and Frequency (N) Calculation.

------------------------------------------------------------------------

## Contributors

-   Chaoyu Ou [Shell-human](https://github.com/Shell-human)
-   Meagan Gardner [meagangardner](https://github.com/meagangardner)
-   Ziming Fang [ethanfang08](https://github.com/ethanfang08)
-   Zoe Ren [sgdkd](https://github.com/sgdkd)

------------------------------------------------------------------------

## Installation

``` bash
$ pip install financecalculator
```

------------------------------------------------------------------------

## Package Content

This package offers four key functions:

### **Functions:**

1.  **contribution Calculation**

    ``` python
    calculate_contribution(principal, future_value, annual_rate, n_periods)
    ```

    Calculates the periodic payment (contribution) required to pay off a loan or reach a specified future value over a given number of periods.

2.  **FV Calculation**

    ``` python
    future_value(principal, annual_rate, n_periods, contribution=0)
    ```

    Calculates the future value of an investment or loan, factoring in optional periodic contributions.

3.  **PV Calculation**

    ``` python
    present_value(principal, annual_rate, n_periods, contribution=0)
    ```

    Calculates the present value of an investment or loan, considering optional monthly contributions.

4.  **N Calculation**

    ``` python
    n_periods(principal, annual_rate, future_value, contribution=0)
    ```

    Calculates the number of periods (in months) required to reach a specified future value, given an initial principal, an annual interest rate, and optional monthly contributions.

------------------------------------------------------------------------

### **Common Parameters:**

-   **`principal`** *(float)*:\
    The initial investment or loan amount (also known as Present Value in financial terms).

-   **`future_value`** *(float)*:\
    The desired amount at the end of the calculation period (e.g., remaining loan balance or target savings).

-   **`annual_rate`** *(float)*:\
    Annual interest rate expressed as a percentage (e.g., 5 for 5%).

-   **`n_periods`** *(int)*:\
    Total number of periods (typically in months) over which the calculation will be performed.

-   **`contribution`** *(float, optional)*:\
    The amount paid or contributed per period (e.g., monthly contributions). Defaults to 0 if not provided.

------------------------------------------------------------------------

## Python Ecosystem

The financial calculator project situates itself within the Python ecosystem as a learning-oriented initiative aimed at developing practical skills in financial computation and programming. While the Python ecosystem already includes robust packages and applications like [Loan Calculator](https://github.com/yanomateus/loan-calculator) and [Financial Calculator App](https://github.com/dilumdesilva/Financial-Calculator-App), this project differentiates itself by offering an accessible, user-friendly tools that simplifies core financial concepts. With intuitive function names like calculate_contribution, future_value, and present_value, it allows users — especially beginners and students — to quickly grasp the essentials without needing to understand complex financial formulas. This project also serves as a hands-on exercise for those eager to deepen their understanding of both finance and Python programming, making it a valuable resource for anyone looking to deepen their understanding of financial concepts and Python development.

------------------------------------------------------------------------

## Usage

The `financecalculator` package allows users to perform essential financial calculations conveniently. Below are some examples of how to use this package:

``` python
from financecalculator import calculate_contribution, future_value, present_value, n_periods

# Calculate periodic payments for a loan
payment = calculate_contribution(principal=20000, future_value=0, annual_rate=5, n_periods=24)

# Calculate future value of an investment
fv = future_value(principal=5000, annual_rate=7, n_periods=36, contribution=200)

# Calculate present value for a target amount
pv = present_value(principal=0, annual_rate=4, n_periods=12, contribution=500)

# Calculate the number of months to reach a goal
months = n_periods(principal=10000, annual_rate=6, future_value=50000, contribution=300)
```

------------------------------------------------------------------------

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

------------------------------------------------------------------------

## License

`financecalculator` was created by Meagan Gardner, Zoe Ren, Ziming Fang, and Chaoyu Ou. It is licensed under the terms of the MIT license.

------------------------------------------------------------------------

## Credits

`financecalculator` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
