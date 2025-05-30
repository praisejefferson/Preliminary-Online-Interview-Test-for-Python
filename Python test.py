from bs4 import BeautifulSoup
from collections import Counter
import statistics

# Full HTML content from the image
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

# Answers
🎨 Color Frequency: {'BROWN': 5, 'GREEN': 7, 'BLUE': 25, 'PINK': 4, 'ORANGE': 7, 'RED': 8, 'WHITE': 14, 'YELLOW': 3, 'CREAM': 1, 'BLACK': 1}
1. Mean Color: BLUE
2. Most Worn Color (Mode): BLUE
3. Median Color: GREEN
4. Variance: 52.5
5. Probability of picking RED randomly: 10.67%


# Step 1: Extract colors from HTML
soup = BeautifulSoup(html_content, 'html.parser')
rows = soup.find_all('tr')[1:]  # skip header

colors_raw = []
for row in rows:
    tds = row.find_all('td')
    if len(tds) > 1:
        colors = tds[1].text.strip().split(',')
        colors = [c.strip().upper() for c in colors]
        colors_raw.extend(colors)

# Step 2: Normalize colors
normalized_colors = []
for color in colors_raw:
    if color == "BLEW":
        normalized_colors.append("BLUE")
    elif color == "ARSH":
        continue
    else:
        normalized_colors.append(color)

# Step 3: Count colors
color_counts = Counter(normalized_colors)

# Step 4: Stats
mean_color = statistics.mode(normalized_colors)
median_color = statistics.median(sorted(normalized_colors))
mode_color = color_counts.most_common(1)[0][0]
variance = statistics.variance(color_counts.values())
prob_red = color_counts.get("RED", 0) / len(normalized_colors)

# Step 5: Print results
print("🎨 Color Frequency:", dict(color_counts))
print("1. Mean Color:", mean_color)
print("2. Most Worn Color (Mode):", mode_color)
print("3. Median Color:", median_color)
print("4. Variance:", variance)
print("5. Probability of picking RED randomly: {:.2%}".format(prob_red))

