# 📝 Project Summary: Bincom ICT Color Analysis
This project analyzes the dress color preferences of Bincom ICT staff over a week, based on data provided in an HTML table.

👨‍💻 Approach
I wrote a Python script to parse the color data directly from the HTML file using BeautifulSoup. After extracting the raw color entries, I performed the following steps:

Data Cleaning: Normalized color names by fixing typos (e.g., correcting "BLEW" to "BLUE") and removing invalid entries like "ARSH".

Data Analysis: Leveraged Python’s built-in collections.Counter and statistics modules to:

Identify the most frequent color worn (mode),

Calculate the mean and median colors,

Compute the variance in color frequency,

Determine the probability of selecting RED at random from the dataset.

📄 Output
All logic and computed answers are contained in the Python file provided. The script prints the full analysis results when executed.
