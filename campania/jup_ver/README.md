# Quant Reentry Projects  
_A portfolio of guided, high-signal model development & validation exercises._

## ✅ Objective  
This repo is designed to support reentry into Quantitative Analyst roles, especially in **Model Development** and **Model Validation** for Investment Banking, Asset Management, or Wealth Management. It emphasizes *active skill reconstruction* through projects with minimal passive reading.

---

## 📁 Project Structure

### [`01_lombard_model_reconstruction/`](./01_lombard_model_reconstruction/)
Rebuild a simplified version of a Lombard Lending Exposure model. Treat it as a baseline model dev project.

- `data/`: Sample CSV input data (generated or dummy).
- `notebooks/`: Model dev notebook explaining each step.
- `model/`: Python scripts for modeling logic.
- `reports/`: Draft model development report (PDF or Markdown).
- `tests/`: Unit tests for model pipeline.
- `README.md`: Project summary and usage guide.

---

### [`02_model_validation_simulation/`](./02_model_validation_simulation/)
Use the Lombard model from project 01 as a case study. Perform key validation tasks.

- `validation_checks/`: Scripts for benchmarking, conceptual review, and backtesting.
- `reports/`: Draft validation memo and PDF summary.
- `README.md`: What was validated, how, and key findings.

---

### [`03_pd_model_retail_credit/`](./03_pd_model_retail_credit/)
Build a logistic/XGBoost-based Probability of Default (PD) model for a retail loan dataset.

- `data/`: Raw and processed input data.
- `notebooks/`: End-to-end modeling notebook.
- `model/`: Scripts for model pipeline and scorecard generation.
- `evaluation/`: Metrics, charts, and plots.
- `reports/`: Model development report tailored to governance.
- `README.md`: Summary, approach, and instructions.

---

### [`04_auto_validation_toolkit/`](./04_auto_validation_toolkit/)
Reusable validation code: PSI, AUC drift, macro shocks, and score stability.

- `checks/`: Validation scripts (Python, modular).
- `sample_data/`: Example model output snapshots.
- `README.md`: What each script does and how to run them.

---

### [`05_portfolio_repositioning/`](./05_portfolio_repositioning/)
Optional creative exercises: reposition models for Asset Management or SaaS.

- `asset_mgmt_model/`: Factor model or liquidity model.
- `saas_churn_model/`: Client downgrade risk model.
- `README.md`: Explain repositioning logic and adaptations.

---

## 🧩 Getting Started

```bash
git clone https://github.com/yourusername/quant-reentry-projects.git
cd quant-reentry-projects
