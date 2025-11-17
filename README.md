
# Task_08_Bias_Detection  
Bias Detection in LLM Data Narratives  
Syracuse University – Research Task 08

## Overview
This repository contains a complete controlled experiment designed to detect potential biases in Large Language Model (LLM) data narratives. The experiment uses the Syracuse Women’s Lacrosse 2025 anonymized dataset and evaluates three bias hypotheses:

- **H1: Framing Bias** (positive vs. negative framing)
- **H2: Identity Bias** (anonymous vs. “first-year” labeling)
- **H3: Confirmation Bias** (neutral vs. underperformance-primed prompts)

Two LLMs were tested:
- **Gemini Advanced** (simulated experimental data provided)
- **Claude-style model** (simulated but realistic outputs)

Each model received all **6 prompt conditions**, with **4 runs each for Gemini** and **1 run each for Claude**.

## Repository Structure
Task_08_Bias_Detection/
│
├── README.md
├── REPORT.md
├── requirements.txt
│
├── prompts/
│ ├── H1_positive.txt
│ ├── H1_negative.txt
│ ├── H2_anonymous.txt
│ ├── H2_named.txt
│ ├── H3_neutral.txt
│ ├── H3_underperformance.txt
│
├── code/
│ ├── experiment_design.py
│ ├── run_experiment.py
│ ├── analyze_bias.py
│ ├── validate_claims.py
│
├── results/
│ ├── gemini/
│ │ ├── H1_pos.json
│ │ ├── H1_neg.json
│ │ ├── H2_anon.json
│ │ ├── H2_risk.json
│ │ ├── H3_neutral.json
│ │ ├── H3_underperf.json
│ │
│ ├── claude/
│ ├── H1_pos.json
│ ├── H1_neg.json
│ ├── H2_anon.json
│ ├── H2_named.json
│ ├── H3_neutral.json
│ ├── H3_underperf.json
│
└── analysis/
├── sentiment_summary.csv
├── recommendation_counts.csv
├── statistical_tests.txt
├── hallucination_flags.csv
├── bias_visualizations.md
