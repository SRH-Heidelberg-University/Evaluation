# Evaluation Metrics
We created RAGAS (Retrieval Augmented Generation Assessment), a framework for evaluating retrieval augmented generation (RAG) pipelines for both Mistral 7B and LLAMA 13B.

# Getting Started
To Evaluate these models follow the below instructions,

### Prerequisites
- **Anaconda**: Download and install Anaconda from the [official Anaconda website](https://www.anaconda.com/products/individual).

### Setup Instructions

#### Step 1: Clone the Repository
Use the following command to clone the Mistral repository :
```bash
git clone 
```

#### Step 2: Create a Conda Environment
Navigate to the project directory and use Python 3.8 to build a new Conda environment called `evalenv`
```bash
conda create -n evalenv python=3.8 -y
```
Activate the environment:
```bash
conda activate nenv
```

#### Step 3: Install Dependencies
Install the required Python packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```


### Step 4: Run the evaluations python files
Run the `mistral_with_ragas.py` file to evaluate mistral model's output and
Run the `llama_with_ragas.py` file to evaluate mistral model's output

`Already, the ouput of these files are saved in Excel files ``mistral_consfinal.xlsx`` and ``llama.xlsx`` for Mistral and LLAMA respectively.`



### Step 5: Visulaisation
Run the `mistral_plot.py` and `llama_plot.py` files for visualizing the metrics of Mistral and LLAMA respectively.



### Tech Stack:
- Python: Core programming language



### Acknowledgments
Special thanks to SRH Heidelberg for supporting this project.
