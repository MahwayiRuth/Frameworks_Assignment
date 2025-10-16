import pandas as pd
import warnings
warnings.filterwarnings('ignore')

print("="*60)
print("PART 2: DATA CLEANING AND PREPARATION")
print("="*60)

# Load data
file_path = '/storage/emulated/0/Download/metadata.csv'
print("\n[1] Loading data...")
df = pd.read_csv(file_path)
print(f"    ✓ Loaded {len(df)} rows")

# Show initial missing values
print("\n" + "="*60)
print("[2] INITIAL MISSING VALUES:")
print("="*60)
missing_before = df.isnull().sum()
for col in missing_before[missing_before > 0].index:
    print(f"    {col}: {missing_before[col]} missing ({missing_before[col]/len(df)*100:.1f}%)")

# Handle missing data
print("\n" + "="*60)
print("[3] HANDLING MISSING DATA:")
print("="*60)

# For title and abstract - remove rows where BOTH are missing
print("    • Removing rows with missing title AND abstract...")
before_count = len(df)
df = df[~(df['title'].isnull() & df['abstract'].isnull())]
removed = before_count - len(df)
print(f"      Removed {removed} rows")

# For abstract - fill missing with "No abstract available"
print("    • Filling missing abstracts...")
df['abstract'] = df['abstract'].fillna('No abstract available')

# For pmcid and pubmed_id - fill with "Unknown"
print("    • Filling missing IDs...")
df['pmcid'] = df['pmcid'].fillna('Unknown')
df['pubmed_id'] = df['pubmed_id'].fillna('Unknown')

print(f"    ✓ Cleaned dataset now has {len(df)} rows")

# Prepare data for analysis
print("\n" + "="*60)
print("[4] PREPARING DATA FOR ANALYSIS:")
print("="*60)

# Convert publish_time to datetime
print("    • Converting dates to datetime format...")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
print(f"      ✓ Converted successfully")

# Extract year from publication date
print("    • Extracting year from publication date...")
df['year'] = df['publish_time'].dt.year
print(f"      ✓ Year column created")

# Create abstract word count
print("    • Calculating abstract word counts...")
df['abstract_word_count'] = df['abstract'].str.split().str.len()
print(f"      ✓ Word count column created")
print(f"      Average: {df['abstract_word_count'].mean():.0f} words")

# Create title word count
print("    • Calculating title word counts...")
df['title_word_count'] = df['title'].str.split().str.len()
print(f"      ✓ Title word count created")
print(f"      Average: {df['title_word_count'].mean():.0f} words")

# Show final missing values
print("\n" + "="*60)
print("[5] FINAL MISSING VALUES:")
print("="*60)
missing_after = df.isnull().sum()
if missing_after.sum() == 0:
    print("    ✓ No missing values!")
else:
    for col in missing_after[missing_after > 0].index:
        print(f"    {col}: {missing_after[col]} missing")

# Save cleaned data
print("\n" + "="*60)
print("[6] SAVING CLEANED DATA:")
print("="*60)
output_path = '/storage/emulated/0/Download/metadata_cleaned.csv'
df.to_csv(output_path, index=False)
print(f"    ✓ Saved to: {output_path}")

# Summary
print("\n" + "="*60)
print("✓ PART 2 COMPLETE!")
print("="*60)
print("\nData cleaning summary:")
print(f"  • Original rows: {before_count}")
print(f"  • Final rows: {len(df)}")
print(f"  • Rows removed: {before_count - len(df)}")
print(f"  • New columns created: year, abstract_word_count, title_word_count")
print(f"  • Date range: {df['year'].min():.0f} to {df['year'].max():.0f}")
print("\nNext: Run Part 3 for analysis and visualization!")

print("\n" + "="*60)