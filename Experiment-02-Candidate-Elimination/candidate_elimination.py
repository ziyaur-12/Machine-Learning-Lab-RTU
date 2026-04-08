import csv

def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def candidate_elimination(data):
    attributes = len(data[0]) - 1

    # Initialize S and G
    S = ['ϕ'] * attributes
    G = [['?'] * attributes]

    for row in data[1:]:
        x = row[:-1]
        label = row[-1]

        # POSITIVE EXAMPLE
        if label == 'Yes':
            # Update S
            for i in range(attributes):
                if S[i] == 'ϕ':
                    S[i] = x[i]
                elif S[i] != x[i]:
                    S[i] = '?'

            # Remove inconsistent hypotheses from G
            G = [g for g in G if all(g[i] == '?' or g[i] == S[i] for i in range(attributes))]

        # NEGATIVE EXAMPLE
        else:
            new_G = []
            for g in G:
                for i in range(attributes):
                    if g[i] == '?' and S[i] != x[i]:
                        new_hypothesis = g.copy()
                        new_hypothesis[i] = S[i]
                        if new_hypothesis not in new_G:
                            new_G.append(new_hypothesis)
            G = new_G

    return S, G

# -------- MAIN --------
data = read_csv("enjoysport.csv")
S, G = candidate_elimination(data)

print("Final Specific Hypothesis (S):")
print(S)

print("\nFinal General Hypotheses (G):")
for g in G:
    print(g)
