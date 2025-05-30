from bs4 import BeautifulSoup
from collections import Counter
import statistics
import random

# HTML CONTENT 
html_content = """
<html>
<head><title>Our Python Class exam</title></head>
<body>
<h3>TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK</h3>
<table>
    <thead><th>DAY</th><th>COLOURS</th></thead>
    <tbody>
    <tr><td>MONDAY</td><td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td></tr>
    <tr><td>TUESDAY</td><td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td></tr>
    <tr><td>WEDNESDAY</td><td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td></tr>
    <tr><td>THURSDAY</td><td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td></tr>
    <tr><td>FRIDAY</td><td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td></tr>
    </tbody>
</table>
</body>
</html>
"""

#STEP 1: Extract Colors from HTML
soup = BeautifulSoup(html_content, 'html.parser')
rows = soup.find_all('tr')[1:]  # Skip header row

colors_raw = []
for row in rows:
    tds = row.find_all('td')
    if len(tds) > 1:
        colors = tds[1].text.strip().split(',')
        colors = [c.strip().upper() for c in colors]
        colors_raw.extend(colors)

#STEP 2: Normalize Colors
normalized_colors = []
for color in colors_raw:
    if color == "BLEW":
        normalized_colors.append("BLUE")
    elif color == "ARSH":
        continue  # Skip invalid entry
    else:
        normalized_colors.append(color)

#STEP 3: Count Colors
color_counts = Counter(normalized_colors)

#STEP 4: Statistical Calculations
try:
    mean_color = "Mean is not applicable to categorical data like colors."
    median_color = statistics.median(sorted(normalized_colors))
    mode_color = color_counts.most_common(1)[0][0]
    variance = statistics.variance(color_counts.values())
    prob_red = color_counts.get("RED", 0) / len(normalized_colors)
except Exception as e:
    print("Error in statistical calculation:", e)

#STEP 5: Output Results
print("\U0001F3A8 Color Frequency:", dict(color_counts))
print("1. Mean Color:", mean_color)
print("2. Most Worn Color (Mode):", mode_color)
print("3. Median Color:", median_color)
print("4. Variance:", variance)
print("5. Probability of picking RED randomly: {:.2%}".format(prob_red))

#STEP 6: Save to Mock Database Function
def save_to_mock_database(color_counts):
    print("(Mock) Saving to database...")
    for color, freq in color_counts.items():
        print(f"Inserted: {color} -> {freq}")
    print("(Mock) Save complete.")

# Uncomment below to simulate database save
# save_to_mock_database(color_counts)

#STEP 7: Recursive Search
def recursive_search(lst, target, index=0):
    if index >= len(lst):
        return False
    if lst[index] == target:
        return True
    return recursive_search(lst, target, index + 1)

#STEP 8: Generate Random 4-digit Binary and Convert to Decimal
def binary_to_decimal():
    binary = ''.join(random.choices(['0', '1'], k=4))
    decimal = int(binary, 2)
    print(f"Binary: {binary} -> Decimal: {decimal}")
    return binary, decimal

#STEP 9: Sum First 50 Fibonacci Numbers
def sum_fibonacci(n=50):
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    total = sum(fib)
    print(f"Sum of first {n} Fibonacci numbers: {total}")
    return total


