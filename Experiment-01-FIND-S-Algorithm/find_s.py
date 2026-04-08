import pandas as pd

def find_s_algorithm(csv_file):
    data = pd.read_csv(csv_file)

    attributes = data.columns[:-1]
    target = data.columns[-1]

    hypothesis = ['0'] * len(attributes)  

    print("Initial Hypothesis:", hypothesis)

    for index, row in data.iterrows():
        if row[target] == 'Yes':
            print(f"\nProcessing positive example {index + 1}:")
            print(list(row[attributes]))

            for i in range(len(hypothesis)):
                if hypothesis[i] == '0':
                    hypothesis[i] = row[attributes[i]]
                elif hypothesis[i] != row[attributes[i]]:
                    hypothesis[i] = '?'

            print("Updated Hypothesis:", hypothesis)

    return hypothesis


final_hypothesis = find_s_algorithm("Training_Data.csv")

print("\nFinal Most Specific Hypothesis:")
print(final_hypothesis)