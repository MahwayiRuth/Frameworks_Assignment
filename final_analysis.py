import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter

# Load data
df = pd.read_csv('/storage/emulated/0/Download/metadata_cleaned.csv')

# Create output text file
results = []
results.append("="*60 + "\n")
results.append("COVID-19 RESEARCH ANALYSIS - FINAL RESULTS\n")
results.append("="*60 + "\n\n")

# Analysis 1: Papers by year
results.append("1. PUBLICATIONS BY YEAR:\n")
papers_by_year = df['year'].value_counts().sort_index()
for year, count in papers_by_year.items():
    results.append(f"   {int(year)}: {count} papers\n")

# Analysis 2: Top journals
results.append("\n2. TOP 10 JOURNALS:\n")
top_journals = df['journal'].value_counts().head(10)
for i, (journal, count) in enumerate(top_journals.items(), 1):
    results.append(f"   {i:2d}. {journal}: {count} papers\n")

# Analysis 3: Word frequency
results.append("\n3. MOST FREQUENT WORDS IN TITLES:\n")
all_titles = ' '.join(df['title'].dropna().astype(str))
words = all_titles.lower().split()
stop_words = {'a', 'the', 'and', 'of', 'in', 'to', 'for', 'with', 'on', 'at', 'by', 'from', 'as', 'is', 'an'}
filtered = [w for w in words if w not in stop_words and len(w) > 3]
word_freq = Counter(filtered).most_common(15)
for i, (word, count) in enumerate(word_freq, 1):
    results.append(f"   {i:2d}. {word}: {count} times\n")

# Analysis 4: Source distribution
results.append("\n4. PAPERS BY SOURCE:\n")
source_counts = df['source_x'].value_counts()
for source, count in source_counts.items():
    pct = count/len(df)*100
    results.append(f"   {source}: {count} papers ({pct:.1f}%)\n")

results.append("\n" + "="*60 + "\n")
results.append(f"Total papers analyzed: {len(df)}\n")
results.append(f"Date range: {int(df['year'].min())}-{int(df['year'].max())}\n")
results.append("="*60 + "\n")

# Save results
with open('/storage/emulated/0/Download/ANALYSIS_RESULTS.txt', 'w') as f:
    f.writelines(results)

# Create visualizations
# Viz 1: Timeline
plt.figure(figsize=(10, 6))
papers_by_year.plot(kind='bar', color='steelblue')
plt.title('COVID-19 Publications by Year', fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Number of Papers')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('/storage/emulated/0/Download/chart_timeline.png', dpi=150)
plt.close()

# Viz 2: Top journals
plt.figure(figsize=(10, 6))
top_journals.head(8).plot(kind='barh', color='coral')
plt.title('Top Journals', fontsize=14, fontweight='bold')
plt.xlabel('Number of Papers')
plt.tight_layout()
plt.savefig('/storage/emulated/0/Download/chart_journals.png', dpi=150)
plt.close()

# Viz 3: Word frequency
plt.figure(figsize=(10, 6))
words_list = [w[0] for w in word_freq[:10]]
counts_list = [w[1] for w in word_freq[:10]]
plt.barh(words_list, counts_list, color='green')
plt.title('Most Frequent Words in Titles', fontsize=14, fontweight='bold')
plt.xlabel('Frequency')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('/storage/emulated/0/Download/chart_words.png', dpi=150)
plt.close()

# Viz 4: Source pie chart
plt.figure(figsize=(8, 8))
source_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribution by Source', fontsize=14, fontweight='bold')
plt.ylabel('')
plt.tight_layout()
plt.savefig('/storage/emulated/0/Download/chart_sources.png', dpi=150)
plt.close()

# Success marker
with open('/storage/emulated/0/Download/SUCCESS.txt', 'w') as f:
    f.write("Analysis complete!\n")
    f.write("Check your Downloads folder for:\n")
    f.write("- ANALYSIS_RESULTS.txt\n")
    f.write("- chart_timeline.png\n")
    f.write("- chart_journals.png\n")
    f.write("- chart_words.png\n")
    f.write("- chart_sources.png\n")