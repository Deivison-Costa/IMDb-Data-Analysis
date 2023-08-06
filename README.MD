# IMDb Data Analysis and Visualization
This code performs data analysis and visualization of IMDb (Internet Movie Database) data using the Python programming language and some popular libraries like Pandas and Matplotlib. The code reads a GZIP-compressed IMDb dataset, cleans and preprocesses the data, and then generates various visualizations to understand and explore the dataset.

![Figure_1](https://github.com/Deivison-Costa/IMDb-Data-Analysis/assets/112001225/a34237d4-f909-477b-80e5-528c6139e241)
![Figure_2](https://github.com/Deivison-Costa/IMDb-Data-Analysis/assets/112001225/7f950999-0b40-4931-a7e6-5c74cc516239)
![Figure_3](https://github.com/Deivison-Costa/IMDb-Data-Analysis/assets/112001225/35ffaeb6-3ff0-4e15-8321-3eb1cf781e7a)

# Installation and Setup
- Clone the repository or download the source code.
- Make sure you have Python installed on your system (Python 3.6 or higher is recommended).

## Create a virtual environment (optional, but recommended):

### On Windows:
    pip install virtualenv
    virtualenv venv
    .\venv\Scripts\Activate.ps1
### On Linux:
    sudo apt-get install python3-venv
    python3 -m venv venv
    source meu_env/bin/activate

### Install the required dependencies:
    pip install pandas matplotlib

# Usage
- Download the IMDb dataset file (title.akas.tsv.gz) in the project directory.
- https://developer.imdb.com/non-commercial-datasets/
## Run the imdb_analysis.py file to start the application: 
    python imdb_analysis.py

# Code Explanation
The code imports the required libraries: pandas to handle data, matplotlib.pyplot for plotting, and gzip for reading the compressed data.

## Two main functions are defined:

- *read_imdb_data(file_path):* Reads the IMDb dataset file and loads it into a Pandas DataFrame.
- *analyze_imdb_data(df):* Performs data analysis and visualization on the DataFrame.

## The *analyze_imdb_data* function does the following:

- Cleans the data by dropping rows with missing information in the 'region' and 'language' columns.
- Computes the counts of titles by region and language, and the counts of different title types.
- Plots the top 10 regions with the most titles, top 10 languages with the most titles, and the distribution of title types.
- The main function executes the analysis by calling *read_imdb_data* to load the data and then calling *analyze_imdb_data* to perform the analysis and generate the visualizations.

# Technology Stack
- Python.
- Pandas.
- Matplotlib.
