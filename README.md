# Theory Of Computation Automata Package

# Name: Ahmed Adel Mahmoud | Section: 1

## Automata Implementations in Python For:
 1. Write a program that construct a DFA that accepts binary strings where the number
of Is is divisible by 3.

 2. Write a program that simulates a PDA to check if a string is accepted by a given
context-free language (e.g., balanced parentheses, an aⁿbⁿ).

 3. Write a program that simulates a basic single-tape Turing machine that decides the
language L = {ww | w ∈ {0,1}*} Provide a Turing machine definition in code (or file
language L
format), and run a simulator that tests acceptance.

## Usage

```bash
from Programs.DFA import DFA_Divisible_By_Three
from Programs.PDA import PDA_an_bn
from Programs.Turing_Machine import Turing_Machine


DFA_Divisible_By_Three("11010")    # Returns "Accepted"
PDA_an_bn("aabb")                  # Returns "Accepted"
TuringMachine("0101").run()        # Returns "Accepted"
```
## Running Tests
```bash
python -m pytest Tests/
```
## Python Package (toc-automata-package-a23 V0.1.0)
Link: https://test.pypi.org/project/toc-automata-package-a23/0.1.0/
### Install Package
```
pip install -i https://test.pypi.org/simple/ toc-automata-package-a23==0.1.0
```
## Installation
```bash
pip install -r requirements.txt
```
