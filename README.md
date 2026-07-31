# Recipe Suggestion Based on Ingredients

Suggests recipes you can make from a list of ingredients you already have. Pure logic — no machine learning — using set matching to rank recipes by how many required ingredients you already have on hand.

## What it does

1. Stores a small built-in database of recipes, each mapped to its set of required ingredients.
2. Compares your available ingredients against each recipe's requirements.
3. Ranks recipes by **match ratio** — the percentage of required ingredients you already have.
4. Shows which ingredients you have, which you're missing, and whether you're ready to cook right now.

## Requirements

No external libraries — pure Python standard library.

## Usage

```bash
python3 recipe_suggester.py
```

Example output:

```
Ingredients on hand: eggs, cheese, butter, salt, pepper, bread, garlic

Top 5 recipe matches:

  Grilled Cheese Sandwich  (100% match)
    Have: bread, butter, cheese
    ✅ Ready to cook!

  Cheese Omelette  (100% match)
    Have: butter, cheese, eggs, pepper, salt
    ✅ Ready to cook!

  Scrambled Eggs  (80% match)
    Have: butter, eggs, pepper, salt
    🛒 Missing: milk
```

## Using it with your own ingredients

```python
from recipe_suggester import print_suggestions

my_ingredients = ["chicken", "lettuce", "tomato", "olive oil", "salt"]
print_suggestions(my_ingredients, top_n=3)
```

Or get the raw ranked results to build your own UI around:

```python
from recipe_suggester import suggest_recipes

results = suggest_recipes(["banana", "milk", "honey"])
for name, matched, missing, ratio in results:
    print(name, ratio)
```

## How it works

- Each recipe's ingredients are stored as a Python `set`.
- Your available ingredients are also converted to a set (case-insensitive, whitespace-trimmed).
- **Matched ingredients** = intersection of the two sets.
- **Missing ingredients** = required ingredients not in your set.
- **Match ratio** = `len(matched) / len(required)`, used to sort recipes best-match-first.

## Ideas for extending

- Load a much bigger recipe database from a CSV or JSON file, or pull from a public recipe API.
- Weight "core" ingredients (like the protein or main starch) more heavily than garnishes/seasonings.
- Add a `min_match_ratio` filter so only recipes you're close to being able to make show up.
- Build a simple web form where users type in ingredients and see live matches.
- Factor in quantities, not just presence/absence of an ingredient.
