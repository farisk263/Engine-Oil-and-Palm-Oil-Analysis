# Engine Oil & Palm Oil Analysis

A collection of three independent data analysis projects covering statistical analysis, time-series analysis, and natural language processing (NLP). Each task is self-contained with its own dataset, Jupyter notebook, and documentation.

## Projects at a Glance

| Task | Topic | Techniques | Dataset |
|------|-------|------------|---------|
| [Task 1](Task_1/README.md) | Engine Oil Additive Formulations | EDA, ANOVA, PCA, K-Means, DBSCAN | `ingredient.csv` (214 rows, 9 additives) |
| [Task 2](Task_2/README.md) | Palm Oil FFB Yield Analysis | Correlation, Seasonal Decomposition, Time-Series | `palm_ffb.csv` (130 rows, 2008–2018) |
| [Task 3](Task_3/README.md) | NLP Word Probability Analysis | Text Cleaning, Word Frequency, Probability Distribution | `text.txt` (21 lines) |

## Repository Structure

```
Engine-Oil-and-Palm-Oil-Analysis/
├── environment.yml        # Conda environment (Python 3.9.5)
├── Task_1/
│   ├── README.md          # Problem statement & findings
│   ├── task_1.ipynb       # Analysis notebook
│   └── ingredient.csv     # Petrol additive formulations dataset
├── Task_2/
│   ├── README.md          # Problem statement & findings
│   ├── task_2.ipynb       # Analysis notebook
│   └── palm_ffb.csv       # Monthly palm oil yield dataset
└── Task_3/
    ├── README.md          # Problem statement & findings
    ├── task_3.ipynb       # Analysis notebook
    ├── text.txt           # Source document for NLP analysis
    └── distribution.csv   # Generated word frequency output
```

## Setup

### Prerequisites

You need **Anaconda** or **Miniconda** installed. If you don't have it, download Miniconda from [here](https://docs.conda.io/en/latest/miniconda.html).

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/farisk263/Engine-Oil-and-Palm-Oil-Analysis.git
   cd Engine-Oil-and-Palm-Oil-Analysis
   ```

2. Create and activate the conda environment:
   ```sh
   conda env create -n oil-analysis -f environment.yml
   conda activate oil-analysis
   ```

3. Launch Jupyter Notebook:
   ```sh
   jupyter notebook
   ```

4. Open the notebook for the task you want to explore (e.g., `Task_1/task_1.ipynb`).

To deactivate the environment when done:
```sh
conda deactivate
```

## Key Findings Summary

**Task 1 — Engine Oil Additives:**
- Additives A & G are strongly positively correlated (r = 0.81); A & E are negatively correlated (r = −0.54).
- PCA reduced 9 dimensions to 2 principal components (50.68% variance explained).
- K-Means identified **3 distinct formulations**; DBSCAN detected **4 clusters** (more robust to outliers).

**Task 2 — Palm Oil FFB Yield:**
- Precipitation is the strongest external driver of FFB yield (r = 0.29).
- FFB yield peaks in **October** and is lowest in **February** each year.
- A significant yield drop occurred in **2016** due to the El Niño weather phenomenon.

**Task 3 — NLP Word Probability:**
- The word *"data"* appears with the highest frequency in the source document.
- Probability distribution of word occurrences was computed per line and exported to `distribution.csv`.
