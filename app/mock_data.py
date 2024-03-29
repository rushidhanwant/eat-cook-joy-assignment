import json

from fastapi import HTTPException

from app.schemas.request import RecipeData


def mock_scraper(link: str):
    raise HTTPException(status_code=200, detail={
        "author": "Erin Clarke",
        "canonical_url": "https://www.wellplated.com/korean-beef-bowl/",
        "category": "Korean",
    })


def mock_scraper_response(link: str):
    raise HTTPException(status_code=200, detail={
    "author": "Erin Clarke",
    "canonical_url": "https://www.wellplated.com/korean-beef-bowl/",
    "category": "Korean",
    "cuisine": "Main",
    "description": "Quick and healthy Korean beef bowl — ready in 20 minutes and made with simple ingredients! Serve with rice and veggies for easy dinners or meal prep!",
    "host": "wellplated.com",
    "image": "https://www.wellplated.com/wp-content/uploads/2020/03/Korean-Beef-Bowl.jpg",
    "ingredient_groups": [
        {
            "ingredients": [
                "1 pound lean ground beef ((I used 93% lean))",
                "3 tablespoons low sodium soy sauce (plus additional to taste, divided)",
                "1 1/4 cups minced scallions (both green and white parts (from about 1 small bundle), divided)",
                "1 tablespoon minced garlic (about 3 cloves)",
                "2 tablespoons rice vinegar",
                "2 tablespoons honey",
                "2 tablespoons minced or finely grated fresh ginger",
                "1/4 teaspoon red pepper flakes (plus additional to taste)",
                "1 tablespoon sesame oil (plus additional to tase)",
                "Cooked brown rice (quinoa, or cauliflower rice)",
                "1 1/2 cups shredded carrots (see recipe notes to pickle them for an upgrade)",
                "Thinly sliced seedless cucumbers (Persian-style or English/hot house)",
                "Toasted sesame seeds"
            ],
            "purpose": "null"
        }
    ],
    "ingredients": [
        "1 pound lean ground beef ((I used 93% lean))",
        "3 tablespoons low sodium soy sauce (plus additional to taste, divided)",
        "1 1/4 cups minced scallions (both green and white parts (from about 1 small bundle), divided)",
        "1 tablespoon minced garlic (about 3 cloves)",
        "2 tablespoons rice vinegar",
        "2 tablespoons honey",
        "2 tablespoons minced or finely grated fresh ginger",
        "1/4 teaspoon red pepper flakes (plus additional to taste)",
        "1 tablespoon sesame oil (plus additional to tase)",
        "Cooked brown rice (quinoa, or cauliflower rice)",
        "1 1/2 cups shredded carrots (see recipe notes to pickle them for an upgrade)",
        "Thinly sliced seedless cucumbers (Persian-style or English/hot house)",
        "Toasted sesame seeds"
    ],
    "instructions": "Pickle the carrots and/or cucumbers if desired (see recipe notes—I highly recommend).\nBrown\nIn a large skillet, brown the beef over medium-high heat, breaking it into small pieces, until it is browned and cooked through, about 5 or so minutes. When the beef is about halfway finished cooking, add 1 tablespoon of the soy sauce and 2/3 of the scallions. Once the beef is completely browned, stir in the garlic and cook 30 seconds.\nStir\nWhile the beef cooks, in a small bowl, stir together the rice vinegar, honey, ginger, red pepper flakes, and remaining soy sauce.\nPour over the browned beef. Stir and cook for 2 minutes. Remove from the heat, then stir in the sesame oil. Sprinkle the remaining green onion over the top. Taste and add extra soy sauce or red pepper flakes as desired (I added a bit more of each).\nServe the beef hot, over rice, topped generously with the carrots, cucumber, and sesame seeds.",
    "instructions_list": [
        "Pickle the carrots and/or cucumbers if desired (see recipe notes—I highly recommend).",
        "Brown",
        "In a large skillet, brown the beef over medium-high heat, breaking it into small pieces, until it is browned and cooked through, about 5 or so minutes. When the beef is about halfway finished cooking, add 1 tablespoon of the soy sauce and 2/3 of the scallions. Once the beef is completely browned, stir in the garlic and cook 30 seconds.",
        "Stir",
        "While the beef cooks, in a small bowl, stir together the rice vinegar, honey, ginger, red pepper flakes, and remaining soy sauce.",
        "Pour over the browned beef. Stir and cook for 2 minutes. Remove from the heat, then stir in the sesame oil. Sprinkle the remaining green onion over the top. Taste and add extra soy sauce or red pepper flakes as desired (I added a bit more of each).",
        "Serve the beef hot, over rice, topped generously with the carrots, cucumber, and sesame seeds."
    ],
    "language": "en-US",
    "nutrients": {
        "servingSize": "1 (of 4); heaping 3/4 cup",
        "calories": "303 kcal",
        "carbohydrateContent": "17 g",
        "proteinContent": "24 g",
        "fatContent": "15 g",
        "saturatedFatContent": "5 g",
        "cholesterolContent": "74 mg",
        "fiberContent": "2 g",
        "sugarContent": "12 g"
    },
    "ratings": 4.87,
    "site_name": "Well Plated by Erin",
    "title": "Korean Beef Bowl",
    "total_time": 20,
    "yields": "4 servings"
})

def mock_suggestion_data():
    return {
    "scaled_recipe": {
        "content": "Scaled Ingredients for 9 people:\n\n['2.25 pounds lean ground beef ((I used 93% lean))', '6 tablespoons low sodium soy sauce (plus additional to taste, divided)', '2.25 cups minced scallions (both green and white parts (from about 2 small bundles), divided)', '3 tablespoons minced garlic (about 9 cloves)', '6 tablespoons rice vinegar', '6 tablespoons honey', '6 tablespoons minced or finely grated fresh ginger', '3/4 teaspoon red pepper flakes (plus additional to taste)', '3 tablespoons sesame oil (plus additional to taste)', 'Cooked brown rice (quinoa, or cauliflower rice)', '3.75 cups shredded carrots (see recipe notes to pickle them for an upgrade)', 'Thinly sliced seedless cucumbers (Persian-style or English/hot house)', 'Toasted sesame seeds']",
        "additional_kwargs": {},
        "type": "ai",
        "example": "false"
    },
    "suggested_menu": {
        "content": "Based on the given ingredients and servings, here is a suggested menu:\n\n1. Ground Beef Stir-Fry\n   Ingredients:\n   - 2.25 pounds lean ground beef\n   - 6 tablespoons low sodium soy sauce (plus additional to taste, divided)\n   - 1.5 cups minced scallions (both green and white parts, divided)\n   - 1 tablespoon minced garlic (about 3 cloves)\n   - 2 tablespoons rice vinegar\n   - 2 tablespoons honey\n   - 2 tablespoons minced or finely grated fresh ginger\n   - 1/4 teaspoon red pepper flakes (plus additional to taste)\n   - 1 tablespoon sesame oil (plus additional to taste)\n   - Cooked brown rice (quinoa, or cauliflower rice)\n   \n   Instructions:\n   1. Heat sesame oil in a large skillet over medium heat.\n   2. Add ground beef and cook until browned and cooked through. Drain any excess fat.\n   3. In a small bowl, whisk together soy sauce, rice vinegar, honey, ginger, garlic, and red pepper flakes.\n   4. Pour the sauce over the cooked ground beef and stir to combine.\n   5. Add half of the minced scallions and cook for an additional 2 minutes.\n   6. Serve the stir-fry over cooked brown rice, quinoa, or cauliflower rice.\n   7. Garnish with remaining minced scallions and toasted sesame seeds.\n\n2. Asian Slaw\n   Ingredients:\n   - 3.75 cups shredded carrots\n   - 1 cup thinly sliced seedless cucumbers (Persian-style or English/hot house)\n   - 1/4 cup minced scallions (green parts)\n   - 2 tablespoons rice vinegar\n   - 1 tablespoon low sodium soy sauce\n   - 1 tablespoon honey\n   - 1 tablespoon sesame oil\n   - 1/4 teaspoon red pepper flakes (optional)\n   \n   Instructions:\n   1. In a large bowl, combine shredded carrots, sliced cucumbers, and minced scallions.\n   2. In a small bowl, whisk together rice vinegar, soy sauce, honey, sesame oil, and red pepper flakes (if using).\n   3. Pour the dressing over the vegetable mixture and toss to coat evenly.\n   4. Let the slaw sit for at least 10 minutes to allow the flavors to meld.\n   5. Serve as a side dish or as a topping for the ground beef stir-fry.\n\n3. Pickled Carrots\n   Ingredients:\n   - 3.75 cups shredded carrots\n   - 2 cups rice vinegar\n   - 1 cup water\n   - 1/4 cup granulated sugar\n   - 1 tablespoon salt\n   \n   Instructions:\n   1. In a small saucepan, combine rice vinegar, water, sugar, and salt.\n   2. Heat over medium heat until the sugar and salt have dissolved.\n   3. Place the shredded carrots in a large jar or container.\n   4. Pour the hot vinegar mixture over the carrots, ensuring they are fully submerged.\n   5. Let the carrots pickle in the refrigerator for at least 1 hour, or up to overnight.\n   6. Drain the pickled carrots before using them in the Asian slaw or as a topping for other dishes.\n\nEnjoy your meal!",
        "additional_kwargs": {},
        "type": "ai",
        "example": "false"
    }
}


def mock_suggestion_response(payload):
    raise HTTPException(status_code=200, detail={
    "scaled_recipe": {
        "content": "Scaled Ingredients for 9 people:\n\n['2.25 pounds lean ground beef ((I used 93% lean))', '6 tablespoons low sodium soy sauce (plus additional to taste, divided)', '2.25 cups minced scallions (both green and white parts (from about 2 small bundles), divided)', '3 tablespoons minced garlic (about 9 cloves)', '6 tablespoons rice vinegar', '6 tablespoons honey', '6 tablespoons minced or finely grated fresh ginger', '3/4 teaspoon red pepper flakes (plus additional to taste)', '3 tablespoons sesame oil (plus additional to taste)', 'Cooked brown rice (quinoa, or cauliflower rice)', '3.75 cups shredded carrots (see recipe notes to pickle them for an upgrade)', 'Thinly sliced seedless cucumbers (Persian-style or English/hot house)', 'Toasted sesame seeds']",
        "additional_kwargs": {},
        "type": "ai",
        "example": "false"
    },
    "suggested_menu": {
        "content": "Based on the given ingredients and servings, here is a suggested menu:\n\n1. Ground Beef Stir-Fry\n   Ingredients:\n   - 2.25 pounds lean ground beef\n   - 6 tablespoons low sodium soy sauce (plus additional to taste, divided)\n   - 1.5 cups minced scallions (both green and white parts, divided)\n   - 1 tablespoon minced garlic (about 3 cloves)\n   - 2 tablespoons rice vinegar\n   - 2 tablespoons honey\n   - 2 tablespoons minced or finely grated fresh ginger\n   - 1/4 teaspoon red pepper flakes (plus additional to taste)\n   - 1 tablespoon sesame oil (plus additional to taste)\n   - Cooked brown rice (quinoa, or cauliflower rice)\n   \n   Instructions:\n   1. Heat sesame oil in a large skillet over medium heat.\n   2. Add ground beef and cook until browned and cooked through. Drain any excess fat.\n   3. In a small bowl, whisk together soy sauce, rice vinegar, honey, ginger, garlic, and red pepper flakes.\n   4. Pour the sauce over the cooked ground beef and stir to combine.\n   5. Add half of the minced scallions and cook for an additional 2 minutes.\n   6. Serve the stir-fry over cooked brown rice, quinoa, or cauliflower rice.\n   7. Garnish with remaining minced scallions and toasted sesame seeds.\n\n2. Asian Slaw\n   Ingredients:\n   - 3.75 cups shredded carrots\n   - 1 cup thinly sliced seedless cucumbers (Persian-style or English/hot house)\n   - 1/4 cup minced scallions (green parts)\n   - 2 tablespoons rice vinegar\n   - 1 tablespoon low sodium soy sauce\n   - 1 tablespoon honey\n   - 1 tablespoon sesame oil\n   - 1/4 teaspoon red pepper flakes (optional)\n   \n   Instructions:\n   1. In a large bowl, combine shredded carrots, sliced cucumbers, and minced scallions.\n   2. In a small bowl, whisk together rice vinegar, soy sauce, honey, sesame oil, and red pepper flakes (if using).\n   3. Pour the dressing over the vegetable mixture and toss to coat evenly.\n   4. Let the slaw sit for at least 10 minutes to allow the flavors to meld.\n   5. Serve as a side dish or as a topping for the ground beef stir-fry.\n\n3. Pickled Carrots\n   Ingredients:\n   - 3.75 cups shredded carrots\n   - 2 cups rice vinegar\n   - 1 cup water\n   - 1/4 cup granulated sugar\n   - 1 tablespoon salt\n   \n   Instructions:\n   1. In a small saucepan, combine rice vinegar, water, sugar, and salt.\n   2. Heat over medium heat until the sugar and salt have dissolved.\n   3. Place the shredded carrots in a large jar or container.\n   4. Pour the hot vinegar mixture over the carrots, ensuring they are fully submerged.\n   5. Let the carrots pickle in the refrigerator for at least 1 hour, or up to overnight.\n   6. Drain the pickled carrots before using them in the Asian slaw or as a topping for other dishes.\n\nEnjoy your meal!",
        "additional_kwargs": {},
        "type": "ai",
        "example": "false"
    }
})