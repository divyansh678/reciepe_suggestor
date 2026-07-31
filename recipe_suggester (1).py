"""
Recipe Suggestion Based on Ingredients
----------------------------------------
Suggests recipes you can make from a list of ingredients you have on hand.
Uses simple set-matching (no ML needed) and ranks recipes by how many of
their required ingredients you already have.
"""

# ---------------------------------------------------------------------------
# 1. A small built-in recipe database (name -> set of required ingredients)
#    Extend this with more recipes, or load from a CSV/JSON file for a
#    bigger database.
# ---------------------------------------------------------------------------
RECIPES = {
    "Scrambled Eggs": {"eggs", "butter", "salt", "pepper", "milk"},
    "Grilled Cheese Sandwich": {"bread", "cheese", "butter"},
    "Tomato Pasta": {"pasta", "tomato", "garlic", "olive oil", "salt"},
    "Pancakes": {"flour", "eggs", "milk", "sugar", "baking powder"},
    "Vegetable Stir Fry": {"broccoli", "carrot", "soy sauce", "garlic", "oil"},
    "Chicken Salad": {"chicken", "lettuce", "tomato", "olive oil", "salt"},
    "Fruit Smoothie": {"banana", "milk", "honey", "ice"},
    "Guacamole": {"avocado", "lime", "salt", "onion", "tomato"},
    "Cheese Omelette": {"eggs", "cheese", "butter", "salt", "pepper"},
    "Garlic Bread": {"bread", "butter", "garlic", "parsley"},
}


def suggest_recipes(available_ingredients, min_match_ratio=0.0):
    """
    Rank recipes by how well they match the available ingredients.

    Returns a list of tuples: (recipe_name, matched, missing, match_ratio)
    sorted by match_ratio descending (best matches first).
    """
    available = {ing.strip().lower() for ing in available_ingredients}
    results = []

    for recipe_name, required in RECIPES.items():
        matched = required & available
        missing = required - available
        match_ratio = len(matched) / len(required)

        if match_ratio >= min_match_ratio:
            results.append((recipe_name, matched, missing, match_ratio))

    results.sort(key=lambda r: r[3], reverse=True)
    return results


def print_suggestions(available_ingredients, top_n=5):
    results = suggest_recipes(available_ingredients)
    print(f"Ingredients on hand: {', '.join(available_ingredients)}\n")
    print(f"Top {top_n} recipe matches:\n")

    for name, matched, missing, ratio in results[:top_n]:
        status = "✅ Ready to cook!" if not missing else f"🛒 Missing: {', '.join(sorted(missing))}"
        print(f"  {name}  ({ratio*100:.0f}% match)")
        print(f"    Have: {', '.join(sorted(matched)) if matched else '(none)'}")
        print(f"    {status}\n")


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    my_ingredients = ["eggs", "cheese", "butter", "salt", "pepper", "bread", "garlic"]
    print_suggestions(my_ingredients, top_n=5)

    print("-" * 50)
    print("Try changing 'my_ingredients' above to see different suggestions.")
