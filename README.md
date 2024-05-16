# Sequence Alignment Using Dynamic Programming and Divide and Conquer

## Overview
This project implements two solutions for the Sequence Alignment problem:
1. Basic version using Dynamic Programming (DP)
2. Memory-efficient version that combines DP with Divide-and-Conquer

The project aims to align two sequences of symbols (A, C, G, T) by minimizing the cost of alignment, which includes gap penalties and mismatch costs.

## Project Description

### Problem Review
Given two strings `X` and `Y`, where `X` consists of symbols `x1, x2, ..., xm` and `Y` consists of symbols `y1, y2, ..., yn`, the goal is to find the optimal alignment between these strings. The alignment cost includes:
1. **Gap Penalty (δ)**: A fixed cost for each unmatched position.
2. **Mismatch Costs (αpq)**: Costs for matching different symbols `p` and `q`.

The task is to implement the basic DP solution and a memory-efficient version, run them on provided test sets, and compare their performance.

### Input String Generator
The input strings are generated from a base string and a series of steps that iteratively insert copies of the string within itself at specified indices.

### Delta and Alpha Values
- Gap Penalty (δ): 30
- Mismatch Costs:
  - A: [0, 110, 48, 94]
  - C: [110, 0, 118, 48]
  - G: [48, 118, 0, 110]
  - T: [94, 48, 110, 0]

## Implementation Details
### Basic Algorithm
Uses a dynamic programming approach to compute the optimal alignment cost and sequences.

### Memory-efficient Algorithm
Combines dynamic programming with divide-and-conquer to reduce memory usage while maintaining the correctness of the alignment.

## How to Run
### Prerequisites

- Python 3.x
- Required Python packages: `psutil`

### Running the Basic Algorithm
```sh
./basic.sh input.txt output.txt
```
Running the Memory-efficient Algorithm
```
./efficient.sh input.txt output.txt
```
Results

[Summary.pdf](https://github.com/darshanrao/CSCI-Algo-Sequence-Alignment/blob/main/Summary.pdf) file with:

- Data points output table generated from provided input files.
- Line graphs comparing CPU time and memory usage vs. problem size for both solutions.
- Insights and observations from the results.


# Contributors
- <a href="https://github.com/Darshan120501" >Darshan Rao</a><br>
- <a href="https://github.com/rahulanilnair">Rahul Nair</a><br>
- <a href="https://github.com/shardul-datar">Shardul Datar</a><br>
