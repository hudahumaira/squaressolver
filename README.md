# Square Solver

I got completely hooked on playing the word squares game — so I decided to write a solver that uses a dictionary and Trie + DFS algorithm in Python !

This solver loads a dictonary from a file, constructs a Trie for prefix lookup, and uses depth-first search with backtracking to explore every path on a 4x4 board. It outputs all valid words (4-11 letter) found, grouped by length of the words.

## Learning Goals
- Implement a Trie
- Apply DFS with backtracking to traverse a grid
- Prune search space using prefix checks

## Running
1. Run the solver:
   ```bash
   python solver.py

Link to the game: https://squares.org
