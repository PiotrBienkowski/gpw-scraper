# GPW Scraper
This tool is designed for scraping and processing data from the GPW

## Installation

To get started, clone the repository to your local machine using the following command:

```
git clone <repo_link>
```

Next, you'll need to set up a .env file in the root directory of the project. This file should contain essential environment variables. Here is an example of what it might look like:

```
FILENAME=data.txt
URL=https://www.gpw.pl/archiwum-notowan-full?type=10&date=11-03-2024
```
After setting up the .env file, install the required libraries by running:

```
pip3 install -r requirements.txt
```

## Usage
To run the GPW Scraper, execute main.py with the following command:
```
python3 main.py
```
If you encounter any errors during the first attempt, try running the command a few more times ;) 


## Output
After the program is executed, it will create a file with the prefix 'out_data':
```
out_data*.txt
```