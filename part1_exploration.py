import sys
print("Starting script...")
sys.stdout.flush()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")

print("="*60)
print("PART 1: DATA LOADING AND BASIC EXPLORATION")
print("="*60)

# Load the data
file_path = '/storage/emulated/0/Download/metadata.csv'

print("\n[1] Loading data...")
try:
    df = pd.read_csv(file_path)
    print(f"    ✓ Data loaded successfully!")
    print(f"    ✓ Shape: {df.shape[0]} rows × {df.shape[1]} columns")
except Exception as e:
    print(f"    ✗ ERROR: {e}")
    exit()

# Display first few rows
print("\n" + "="*60)
print("[2] FIRST 5 ROWS:")
print("="*60)
print(df.head())

# Check DataFrame dimensions
print("\n" + "="*60)
print("[3] DATASET DIMENSIONS:")
print("="*60)
print(f"    Total rows: {df.shape[0]:,}")
print(f"    Total columns: {df.shape[1]}")
print(f"    Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

# Check data types
print("\n" + "="*60)
print("[4] COLUMN DATA TYPES:")
print("="*60)
print(df.dtypes)

# Check for missing values
print("\n" + "="*60)
print("[5] MISSING VALUES ANALYSIS:")
print("="*60)
missing_values = df.isnull().sum()
missing_pct = (missing_values / len(df)) * 100
missing_df = pd.DataFrame({
    'Missing_Count': missing_values,
    'Missing_Percent': missing_pct
})
missing_df = missing_df[missing_df['Missing_Count'] > 0].sort_values('Missing_Count', ascending=False)

if len(missing_df) > 0:
    print("\n    Columns with missing values:")
    for idx, row in missing_df.iterrows():
        print(f"    {idx:20s}: {int(row['Missing_Count']):5d} ({row['Missing_Percent']:.1f}%)")
else:
    print("    ✓ No missing values found!")

# Basic statistics
print("\n" + "="*60)
print("[6] TEXT COLUMNS ANALYSIS:")
print("="*60)

# Title analysis
if 'title' in df.columns:
    valid_titles = df['title'].dropna()
    print(f"    Title column:")
    print(f"      - Valid entries: {len(valid_titles)}")
    print(f"      - Average length: {valid_titles.str.len().mean():.0f} characters")
    print(f"      - Shortest: {valid_titles.str.len().min()} characters")
    print(f"      - Longest: {valid_titles.str.len().max()} characters")

# Abstract analysis
if 'abstract' in df.columns:
    valid_abstracts = df['abstract'].dropna()
    print(f"\n    Abstract column:")
    print(f"      - Valid entries: {len(valid_abstracts)}")
    print(f"      - Average length: {valid_abstracts.str.len().mean():.0f} characters")
    print(f"      - Shortest: {valid_abstracts.str.len().min()} characters")
    print(f"      - Longest: {valid_abstracts.str.len().max()} characters")

# Journal analysis
if 'journal' in df.columns:
    print(f"\n    Journal column:")
    print(f"      - Valid entries: {df['journal'].notna().sum()}")
    print(f"      - Unique journals: {df['journal'].nunique()}")
    print(f"\n    Top 5 journals:")
    top_journals = df['journal'].value_counts().head()
    for journal, count in top_journals.items():
        print(f"        {journal}: {count} papers")

# Source analysis
if 'source_x' in df.columns:
    print(f"\n    Source column:")
    print(f"      - Unique sources: {df['source_x'].nunique()}")
    print(f"\n    Papers by source:")
    source_counts = df['source_x'].value_counts()
    for source, count in source_counts.items():
        print(f"        {source}: {count} papers")

# All column names
print("\n" + "="*60)
print("[7] ALL COLUMN NAMES:")
print("="*60)
for i, col in enumerate(df.columns, 1):
    non_null = df[col].notna().sum()
    print(f"    {i:2d}. {col:20s} ({non_null:,} non-null)")

print("\n" + "="*60)
print("✓ PART 1 COMPLETE!")
print("="*60)
print("\nKey findings:")
print(f"  • Total papers analyzed: {len(df):,}")
print(f"  • Unique journals: {df['journal'].nunique() if 'journal' in df.columns else 'N/A'}")
print(f"  • Date range: {df['publish_time'].min()} to {df['publish_time'].max()}" if 'publish_time' in df.columns else "")
print("\nNext: Run Part 2 for data cleaning!")
input("\n\nPress Enter to exit...")