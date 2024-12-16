# Cap Gemini Technical Test

## Project Structure
This repository structure:
- `/data`: Contains datasets (raw and processed).
  - `/raw`: Holds unprocessed data files.
  - `/processed`: Stores cleaned and transformed data.
- `/notebooks`: Jupyter notebooks for analysis and modeling.
- `/src`: Source code modules for reusable functions and pipelines.
- `/tests`: Unit tests for validating the code.
- `/docs`: Documentation files, optional for generating with MkDocs.

## Environment Setup and Usage
This project is built and managed using Poetry for dependency management. The main analysis is explained in the Analysis.ipynb notebook. To reproduce and run the notebook follow the steps below to set up the environment.

1. Prerequisites
Ensure the following tools are installed on your system:

- Python 3.11 or above
- Poetry (installation guide: https://python-poetry.org/docs/#installation)

2. Setting Up the Environment
- Clone the repository (in the terminal):
  git clone <https://github.com/farukyasarphd/classification_loan_acceptance.git>
  cd classification_loan_acceptance
- Install dependencies using Poetry (in the terminal):
  poetry install
- Activate the virtual environment (in the terminal):
  poetry shell

3. Running the Notebook
- Start Jupyter Notebook (in the terminal):
  jupyter notebook
- Open the analysis notebook in your browser and run the cells.


