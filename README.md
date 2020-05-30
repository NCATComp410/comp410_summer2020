# NC A&T COMP410 Summer Session Project
Preparing unstructured data for deep feature synthesis
## Installation
* Anaconda environment is highly recommended.  Download the version appropriate for your system [here](https://www.anaconda.com/products/individual)
* This project is currently based on Python 3.8 - here is a [link](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) to the Anaconda getting started guide. Note that the Anaconda Navigator [GUI](https://docs.anaconda.com/anaconda/navigator/getting-started) can be used instead of CLI.
  * Open a conda shell
    * conda update conda 
    * conda create --name py38 python=3.8
  * Activate your new venv
    * conda activate py38
  * Install jupyterlab if you want (optional)
    * conda install jupyterlab==1.2.6
  * Clone this project and cd to your clone
    * cd to directory you want to put this in 
    * git clone (project URL above - Green clone button)
    * cd comp410_summer2020
  * Install requirements
    * python -m pip install -r requirements.txt
  * python demo.py 
    * Downloads necessary data
    * Runs a quick demo
* Testing
  * conda install pytest-cov
  * cd dfstools
  * pytest --cov=dfstools
## Pull Request Requirements
* All pull requests much attach output from pytest showing all test cases passed along with the coverage report or pull request will be rejected

