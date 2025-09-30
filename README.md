# Telecom Customer Churn Prediction

## Project Overview
In the telecommunications industry, competition is intense.
Customers have many options, and switching providers is easy.
For companies, keeping existing customers is often cheaper than acquiring new ones - which makes customer retention a critical business priority. 

**Goals:**
- Predict churn probability for each customer.
- Identify the strongest churn drivers.
- Recommend business strategies to improve retention.

- ## Dataset
The project uses 5 relational tables:
- **Demographics**: Age, gender, dependents, etc.
- **Location**: Country, state, city, etc.
- **Population**: Zip-code and population.
- **Services**: Subscribed services.
- **Status**: Satisfaction score, customer status, churn label, etc.

## Environment & Setup
### Python Environment
- Use **Conda** to ensure all teammates have the same environment.
- Python version: 3.11

### Required Packages
- pandas (data manipulation)
- openpyxl (Excel reading)
- jupyter (notebooks)
- ipykernel (VS Code kernel integration)

### Setup Instructions
1. Install Miniconda or Anaconda if not already installed:
   - [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
   - [Anaconda](https://www.anaconda.com/products/distribution)

2. Clone the repository and navigate to the project folder:
    git clone https://github.com/dianagvmes/telco_churn_project.git
    cd telco_churn_project

3. Create the Conda environment from environment.yml:
    conda env create -f environment.yml
    conda activate telco_churn

4. Make the environment available as a VS Code kernel:
    python -m ipykernel install --user --name telco_churn --display-name "Telco Churn"

5. Updating / Synchronizing the Environment
    If environment.yml changes:
    conda env update -f environment.yml
    conda activate telco_churn

6. Verify Setup
    Open a notebook (.ipynb) in VS Code
    Select Telco Churn kernel
    Run:
        import pandas as pd
        import openpyxl

        print("Kernel is working!") 