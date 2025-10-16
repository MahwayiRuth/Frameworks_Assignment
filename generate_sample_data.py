import pandas as pd
import random
from datetime import datetime, timedelta

print("Generating CORD-19 sample dataset...")
print("="*60)

# Sample data for realistic generation
journals = [
    'Nature', 'Science', 'The Lancet', 'JAMA', 'BMJ', 
    'New England Journal of Medicine', 'Cell', 'PLOS ONE',
    'Journal of Virology', 'Emerging Infectious Diseases',
    'Clinical Infectious Diseases', 'Vaccine', 'Virology',
    'Journal of Medical Virology', 'Nature Medicine'
]

sources = [
    'PMC', 'Medline', 'WHO', 'bioRxiv', 'medRxiv', 
    'arXiv', 'CZI', 'Elsevier', 'Springer'
]

title_keywords = [
    'COVID-19', 'SARS-CoV-2', 'coronavirus', 'pandemic',
    'viral infection', 'respiratory disease', 'vaccine',
    'treatment', 'transmission', 'diagnosis', 'clinical',
    'epidemiology', 'public health', 'immunity', 'outbreak'
]

abstract_templates = [
    "This study investigates the {topic} in patients with COVID-19. We analyzed {n} cases and found significant results regarding {finding}.",
    "Background: Understanding {topic} is crucial for pandemic response. Methods: We conducted a {study_type} study with {n} participants. Results: Our findings suggest {finding}.",
    "The {topic} of SARS-CoV-2 remains poorly understood. This research examines {n} samples to elucidate {finding}.",
    "Objective: To assess {topic} during the COVID-19 pandemic. We present data from {n} cases showing {finding}.",
]

topics = [
    'viral transmission dynamics', 'vaccine efficacy', 'immune response',
    'clinical outcomes', 'diagnostic methods', 'therapeutic interventions',
    'epidemiological patterns', 'disease severity', 'prevention strategies'
]

findings = [
    'improved patient outcomes', 'significant correlations', 
    'novel insights into disease progression', 'effective prevention measures',
    'important implications for treatment', 'critical factors affecting recovery'
]

study_types = ['retrospective', 'prospective', 'cross-sectional', 'cohort', 'case-control']

# Generate authors
def generate_authors():
    first_names = ['John', 'Mary', 'David', 'Sarah', 'Michael', 'Emily', 'James', 'Lisa', 'Robert', 'Jennifer']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
    num_authors = random.randint(2, 8)
    authors = []
    for _ in range(num_authors):
        first = random.choice(first_names)
        last = random.choice(last_names)
        authors.append(f"{last}, {first}")
    return '; '.join(authors)

# Generate title
def generate_title():
    keyword1 = random.choice(title_keywords)
    keyword2 = random.choice(title_keywords)
    templates = [
        f"{keyword1}: A Study of {keyword2}",
        f"Analysis of {keyword1} and {keyword2}",
        f"{keyword1} in the Context of {keyword2}",
        f"Understanding {keyword1}: Implications for {keyword2}",
        f"{keyword1} and {keyword2}: A Comprehensive Review"
    ]
    return random.choice(templates)

# Generate abstract
def generate_abstract():
    template = random.choice(abstract_templates)
    return template.format(
        topic=random.choice(topics),
        n=random.randint(50, 5000),
        finding=random.choice(findings),
        study_type=random.choice(study_types)
    )

# Generate dates between 2019 and 2023
def generate_date():
    start_date = datetime(2019, 12, 1)
    end_date = datetime(2023, 12, 31)
    time_between = end_date - start_date
    days_between = time_between.days
    random_days = random.randrange(days_between)
    return (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

# Generate the dataset
print("Creating records...")
num_records = 1000  # Generate 1000 sample papers

data = {
    'cord_uid': [f'uid_{i:06d}' for i in range(num_records)],
    'sha': [f'sha_{random.randint(100000, 999999)}' for _ in range(num_records)],
    'source_x': [random.choice(sources) for _ in range(num_records)],
    'title': [generate_title() for _ in range(num_records)],
    'doi': [f'10.{random.randint(1000, 9999)}/covid.{i}' for i in range(num_records)],
    'pmcid': [f'PMC{random.randint(1000000, 9999999)}' if random.random() > 0.3 else None for _ in range(num_records)],
    'pubmed_id': [random.randint(10000000, 99999999) if random.random() > 0.2 else None for _ in range(num_records)],
    'license': [random.choice(['cc-by', 'cc-by-nc', 'cc0', 'no-cc']) for _ in range(num_records)],
    'abstract': [generate_abstract() for _ in range(num_records)],
    'publish_time': [generate_date() for _ in range(num_records)],
    'authors': [generate_authors() for _ in range(num_records)],
    'journal': [random.choice(journals) for _ in range(num_records)],
    'url': [f'https://doi.org/10.{random.randint(1000, 9999)}/covid.{i}' for i in range(num_records)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Add some missing values to make it realistic
for col in ['pmcid', 'pubmed_id', 'abstract']:
    missing_indices = random.sample(range(num_records), k=int(num_records * 0.15))
    df.loc[missing_indices, col] = None

# Save to CSV
output_path = '/storage/emulated/0/Download/metadata.csv'
df.to_csv(output_path, index=False)

print(f"✓ Generated {num_records} sample records")
print(f"✓ Saved to: {output_path}")
print("\nDataset preview:")
print(df.head())
print("\nDataset info:")
print(f"  Shape: {df.shape}")
print(f"  Columns: {list(df.columns)}")
print("\n" + "="*60)
print("✓ Sample data generation complete!")
print("You can now use this file for your analysis.")