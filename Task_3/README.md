# NLP Word Probability Analysis

## Introduction

A paragraph of text about data analytics is provided. The goal is to perform statistical analysis on the words in the document — specifically to compute the probability of a target word appearing in each line, and to analyse the distribution of distinct word counts across lines.

This task combines basic text preprocessing with probability and frequency analysis, producing a word distribution dataset as output.

## Problem Statement

Given a paragraph of text (`text.txt`):

A) Clean and preprocess the text (remove punctuation, normalise whitespace, convert to lowercase).

B) For each line, compute the **probability** that a given word (e.g., *"data"*) appears.

C) Count the number of **distinct words** per line and produce a frequency distribution.

D) Export the distribution results to a CSV file (`distribution.csv`).

## Source Document

The input document (`text.txt`) is a 21-line passage about data analytics, covering topics such as business intelligence, exploratory data analysis (EDA), confirmatory data analysis (CDA), and qualitative vs. quantitative analysis.

## Analysis

### Data Preprocessing

Text cleaning steps applied to each line:
```python
import re, string

def clean_line(line):
    line = line.lower()
    line = re.sub(f"[{re.escape(string.punctuation)}]", "", line)
    line = re.sub(r"\s+", " ", line).strip()
    return line
```

### Word Probability per Line

For each line, the probability of a target word (e.g., *"data"*) appearing is calculated as:

```
P(word | line) = count(word in line) / total_words_in_line
```

### Distribution of Distinct Word Counts

The number of distinct (unique) words per line was counted and aggregated into a frequency distribution, which was saved to `distribution.csv`.

**Sample output (`distribution.csv`):**

| index | counts |
|-------|--------|
| 1     | 3      |
| 2     | 7      |
| ...   | ...    |

### Key Findings

- The word **"data"** is the most frequently occurring meaningful word across the document.
- Word count per line ranges from approximately 20 to 40 words, reflecting the dense, technical nature of the passage.
- The distribution of distinct words per line follows a roughly uniform pattern given the consistent paragraph style.

## Files

| File | Description |
|------|-------------|
| `task_3.ipynb` | Jupyter notebook with full analysis and code |
| `text.txt` | Source document (21 lines on data analytics) |
| `distribution.csv` | Output — word frequency distribution per line |
