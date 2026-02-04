# AMD Patient Education Analytics Platform

**End-to-end ETL pipeline, predictive modeling, and interactive Streamlit dashboard for analyzing ophthalmic patient education effectiveness and feedback.**

This project analyzes synthetic data from patient education modules on Age-related Macular Degeneration (AMD). It demonstrates how data pipelines and ML can improve clinical workflows by quantifying quiz score improvements, identifying demographic drivers, and visualizing patient feedback.

Built as part of research at the Wilmer Eye Institute (Johns Hopkins Medicine). Real patient data is never included—only synthetic datasets for demonstration and reproducibility.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-FF4B4B)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of Contents
- [Features](#features)
- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Key Insights & Results](#key-insights--results)
- [Data Disclaimer](#data-disclaimer)
- [Project Structure](#project-structure)
- [License](#license)
- [Contact](#contact)

## Features
- Full ETL pipeline: data ingestion, cleaning, and SQLite integration
- Demographic breakdowns (age, gender, disease stage) and cohort analysis
- Predictive modeling of post-quiz score improvements
- Interactive Streamlit dashboard with:
  - Dynamic filters (demographics, disease type)
  - Visualizations: bar charts, histograms, scatter plots (Plotly)
  - Word clouds and sentiment analysis on patient feedback
- Reproducible exploratory data analysis (EDA) in Jupyter notebook

## Project Overview
Patient education is critical in ophthalmology, yet understanding varies widely. This project processes quiz responses and feedback from AMD education modules to:
- Measure knowledge gains pre- vs. post-education
- Build a simple predictive model (e.g., regression/classification) to forecast improvement based on demographics
- Provide clinicians with interactive insights via dashboards

Goal: Support data-driven enhancements to patient education delivery while maintaining full HIPAA/IRB compliance (using only synthetic data).

## Tech Stack
- **Core Language**: Python
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly, Matplotlib, Seaborn, WordCloud
- **Dashboard**: Streamlit
- **Database/Storage**: SQLite
- **Modeling/EDA**: Scikit-learn (if used), Jupyter Notebook

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Matt-Vierheller/AMD-education-data-analysis.git
   cd AMD-education-data-analysis
