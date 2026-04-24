import pandas as pd

# Step 1: Extract (student data)
data = {
    "name": ["Navitha", "Nancy", "Naina", None],
    "skills": ["Python, SQL", "Communication, Sales", "AI, Python", "Java"],
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Step 2: Transform (clean data)
df = df.dropna()

# Step 3: Career mapping logic
def assign_career(skills):
    if "Python" in skills or "AI" in skills:
        return "Data Engineer / AI Engineer"
    elif "Sales" in skills:
        return "Business Analyst / Sales Manager"
    else:
        return "Software Engineer"

df["recommended_career"] = df["skills"].apply(assign_career)

print("\nProcessed Data:")
print(df)

# Step 4: Save result
df.to_csv("career_output.csv", index=False)

print("\nFinal Output Saved!")
