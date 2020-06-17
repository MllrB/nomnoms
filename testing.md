# MLLRB NomNoms Recipe Sharing Application
## Testing Documentation

- [Functionality Testing](#Functionality-Testing)
    - [Navbar Links](#Navbar-Links)
        - [Desktop + Laptop Devices](#Desktop-+-Laptop-Devices)
        - [Mobile Devices](#Mobile-Devices)
    - [Navbar Search Field](#Navbar-Search-Field)
    - [Footer Links](#Footer-Links)
    - [Homepage](#Homepage)
    - [Browse Recipes](#Browse-Recipes)
        - [Mobile devices](#Browse-Recipes-Mobile-devices)
    - [Individual Recipe page](#Individual-Recipe-page)
    - [Add Recipe](#Add-Recipe)
    - [Edit Recipe](#Edit-Recipe)
        - [Edit Recipe Bugs](#Edit-Recipe-Bugs)
    - [Remove Recipe](#Remove-Recipe)
    - [Remove Recipe Bugs](#Remove-Recipe-Bugs)
- [Styling Testing](#Styling-Testing)
-[Python Code Validation](#Python-Code-Validation)

### Functionality Testing

#### Navbar Links
###### Desktop + Laptop Devices
1. Test: Clicking the logo.
    * Method: 
        - Navigate away from the homepage and click the logo
    * Expected result: 
        - The user should be returned to the homepage from any other page on the website.
        - URL: `http://ci-ms3-nomnoms.herokuapp.com/home`
    * Result:
        - Clicking the logo returns the user to the homepage
        - URL: `http://ci-ms3-nomnoms.herokuapp.com/home`

2. Test: Clicking the "Browse Recipes" link.
    * Method: 
        - From all pages on the website, click the 'Browse Recipes' link 
    * Expected result: 
        - The user should be directed to the browse recipes page from any other page on the website.
        - URL: `http://ci-ms3-nomnoms.herokuapp.com/browse_recipes`
    * Result:
        - Clicking 'Browse Recipes' link directs the user to the correct URL from all pages
        - URL: `http://ci-ms3-nomnoms.herokuapp.com/browse_recipes`

3. Test: Clicking the "Add a recipe" link.
    * Method: 
        - From all pages on the website, click the 'Add a recipe' link 
    * Expected result: 
        - The user should be directed to the create recipe page from any other page on the website.
        - URL: `http://ci-ms3-nomnoms.herokuapp.com/create_recipe`
    * Result:
        - Clicking 'Add a recipe' link directs the user to the correct URL from all pages
        - URL: `http://ci-ms3-nomnoms.herokuapp.com/create_recipe`
    
4. Test: Clicking the "Edit your recipes" link.
    * Method: 
        - From all pages on the website, click the 'Edit your recipes' link 
    * Expected result: 
        - The user should be directed to the edit recipe page from any other page on the website.
        - URL: `http://ci-ms3-nomnoms.herokuapp.com/edit_recipe`
    * Result:
        - Clicking 'Edit your recipes' link directs the user to the correct URL from all pages
        - URL: `http://ci-ms3-nomnoms.herokuapp.com/edit_recipe`

5. Test: Clicking the "Remove a recipe" link.
    * Method: 
        - From all pages on the website, click the 'Remove a recipe' link 
    * Expected result: 
        - The user should be directed to the remove recipe page from any other page on the website.
        - URL: `http://ci-ms3-nomnoms.herokuapp.com/remove_recipe`
    * Result:
        - Clicking 'Remove a recipe' link directs the user to the correct URL from all pages
        - URL: `http://ci-ms3-nomnoms.herokuapp.com/remove_recipe`

------------
###### Mobile Devices
6. Test: Clicking the menu (burger) button.
    * Method: 
        - Press the menu button
    * Expected result: 
        - Side navigation panel should be triggered, slide out from the left and contain all the same links as the navbar on desktop/laptop devices + a search field
    * Result:
        - Side navigation slides out from the left and contains all the same links as in the navbar on desktop/laptop devices and the search field.

7. Test: Repeat Test 1 above for mobile device.
    * Method: 
        - Navigate away from the homepage and press the logo
    * Expected result: 
        - The user should be returned to the homepage from any other page on the website.
    * Result:
        - Clicking the logo returns the user to the homepage

8. Test: Repeat tests 2 through 5 above from the side navigation panel on a mobile device.
    * Expected result: 
        - Identical behaviour as for tests 2 through 5 above.
    * Result:
        - Identical behaviour as for tests 2 through 5 above.
------------------
#### Navbar Search Field
1. Test: Using the search input in the navbar to view relevant recipes for desktop + laptop devices.
    * Method:
        - Using the following search terms test that the search bar is returning relevant results.
            - Search Term: Pizza : to test that the recipe title is being searched.
            - Search Term: water : to test that ingredients are being searched.
            - Search Term: Sauce : to test that categories are being searched and that words within categories are being searched.
            - Search Term: vegetarian : to test that dietary information is being searched.
            - Search Term: brunch : to test that meal types are being searched.
            - Search Term: piZzA : to test that the search is not case sensitive.
    * Expected result:
        - Browse Recipes page is displayed with relevant results.
        - Recipe title is being searched.
        - Ingredients are being searched.
        - Categories are being searched.
        - Dietary information is being searched.
        - Meal types are being searched.
        - Search is not case sensitive.
    * Results: (At time of writing)
        - Browse Recipes page is displayed with relevant results.
        - 'Pizza' returns one match with Pizza in the title, test passed.
        - 'water' returns 3 matches with water listed as an ingredient, test passed. 
        - 'Sauce' returns 4 matches each with a category of 'Basics (Dough, sauces etc)', test passed.
        - 'vegetarian' returns 13 matches each with vegetarian listed in their dietary information, test passed.
        - 'brunch' returns 2 matches with brunch listed as a meal type, test passed.
        - 'piZzA' returns one match with 'Pizza' in the title, test passed.

2. Test: Repeat test 1 above from side navigation panel on mobile devices.
    * Expected result:
        - Identical to test for desktop/laptop devices.
    * Result:
        - Identical to test for desktop/laptop devices.

#### Footer Links
1. Test: Click 'home' link.
    * Expected result:
        - User is directed to the homepage.
    * Result:
        - User is directed to the homepage.

2. Test: Click 'browse' link.
    * Expected result:
        - User is directed to the browse recipes page.
    * Result:
        - User is directed to the browse recipes page.

3. Test: Click 'add' link.
    * Expected result:
        - User is directed to the create recipe page.
    * Result:
        - User is directed to the create recipe page.

4. Test: Click 'edit' link.
    * Expected result:
        - User is directed to the edit recipe page.
    * Result:
        - User is directed to the edit recipe page.

5. Test: Click 'remove' link.
    * Expected result:
        - User is directed to the remove recipe page.
    * Result:
        - User is directed to the remove recipe page.

6. Test: Click 'mllrb.com' link.
    * Expected result:
        - User is directed away from the site to my `http://www.mllrb.com` site.
    * Result:
        - User is directed away from the site to my `http://www.mllrb.com` site.

7. Test: Click '`https://fshoq.com`' link.
    * Expected result:
        - User is directed away from the site to my `https://fshoq.com` site.
    * Result:
        - User is directed away from the site to my `https://fshoq.com` site.

8. Test: Repeat tests 1 through 7 on mobile device.
    * Expected results:
        - Identical to tests 1 through 7 above.
    * Results:
        - Identical to tests 1 through 7 above.


#### Homepage
Link: [Homepage](http://ci-ms3-nomnoms.herokuapp.com/home)

1. Test: Clicking/pressing the 'Browse Recipes' link on the homepage card.
    * Expected result:
        - User is directed to the browse recipes page.
    * Result:
        - User is directed to the browse recipes page.

2. Test: Clicking/pressing the 'Add Recipes' link on the homepage card.
    * Expected result:
        - User is directed to the add recipes page.
    * Result:
        - User is directed to the add recipes page.

3. Test: Clicking/pressing the 'Edit Your Recipes' link on the homepage card.
    * Expected result:
        - User is directed to the edit recipes page.
    * Result:
        - User is directed to the edit recipes page.

#### Browse Recipes
Link: [Browse Recipes](http://ci-ms3-nomnoms.herokuapp.com/browse_recipes)

1. Test: Click on card image to reveal dietary info.
    * Expected Result:
        - Clicking on a card image reveals dietary info pertinent to that recipe.
    * Result:
        - On click of card image, dietary info is revealed.
        - Example: Clicking on the image for 'Pizza Dough for 2' reveals dietary info of Omnivorous, Vegetarian, Dairy free and Nut free.

2. Test: Click on card image to be directed to the relevant recipe page.
    * Expected Result:
        - Clicking on a card link directs the user to the recipe page for the clicked recipe card.
    * Result:
        - On click of card link, redirects to the recipe page for the recipe on the card clicked.
        - Example: Clicking on the image for 'Raita' redirects to http://ci-ms3-nomnoms.herokuapp.com/show_recipe/5ee4ac21af7d43b3a211b012

3. Test: Filter button returns pertinantly filtered results and work in combination with each other.
    * Method: 
        1. Select savoury from categories, vegetarian from dietary info and dinner from meal types.
        2. Select only savoury from categories.
        3. Select only vegetarian from dietary info.
        4. Select only dinner from meal types.
        5. Select savoury from categories and vegtarian from dietary info.
        6. Select savoury from categories and dinner from meal types.
        7. Select vegetarian from dietary info and dinner from meal types.
        8. Select brunch from meal types.
    * Expected Results: 
        - Each attempt should show a varying numbers of matched recipes if they are filtering alone and in combination.
    * Results: (At time of writing)
        1. Savoury + Vegetarian + Dinner -> 3 matches.
        2. Savoury -> 5 matches.
        3. Vegetarian -> 13 matches.
        4. Dinner -> 6 matches.
        5. Savoury + Vegetarian -> 4 matches.
        6. Savoury + dinner -> 4 matches (with 1 different recipe to matches found in 5 above).
        7. Vegetarian + dinner -> 5 matches.
        8. Brunch -> 2 matches.

4. Test: Search works correctly.
    * Method:
        - Repeat search test for navbar search (Test 1). They use the same function so should operate the same.
    * Expected Results: 
        - Identical to navbar search tests.
    * Results: (At time of writing)
        - Identical to navbar search tests.

##### Browse Recipes Mobile devices
5. Test: Search and filter column on smaller screens should be replaced by a 'Search/Filter' button (the button is transparent) which should trigger a side navigation panel containing the same search and filter options as above.
    * Expected Results: 
        - On smaller screens search and filter column is replaced by a button.
        - The button triggers a side navigation panel containing search and filter options.
        - Search and filter function correctly
    * Results: 
        - On smaller screens search and filter column is replaced by a button.
        - The button triggers a side navigation panel containing search and filter options.
        - I used the same set of criteria as in Test 3 of this section and got the same results.


#### Individual Recipe page
To navigate to an individual recipe page you must first select a recipe by searching or via the browse recipes page.

1. Test: Individual Recipes are displaying correctly with the correct information.
    * Method:
        - Select and navigate to Chickpea and Spinach curry from the browse recipe page.
    * Expected Results: 
        - The Chickpea and Spinach curry recipe is displayed on it's own page.
        - The Ingredients tab contains only ingredients.
        - The Steps tab displays only steps (scrollable).
        - Add a Recipe button directs the user to the add recipes page.
        - Browse Recipes button brings the user to the browse recipes page.
    * Results: 
        - The Chickpea and Spinach curry recipe is displayed on it's own page.
        - The Ingredients tab contains only ingredients.
        - The Steps tab displays only steps (scrollable).
        - Add a Recipe button directs the user to the add recipes page.
        - Browse Recipes button brings the user to the browse recipes page.


#### Add Recipe
Link: [Add Recipe](https://ci-ms3-nomnoms.herokuapp.com/create_recipe)
1. Test: Name and Pin must be required.
    * Method: 
        - Add an ingredient/step or try to save the recipe without first entering a name and pin.
    * Expected Result:
        - No ingredient or step will be added and the user will be promtped to enter the required fields.
        - Recipe cannot be saved and the user will be promtped to enter the required fields.
    * Result:
        - No ingredient or step was added and I was promtped to enter the required fields.
        - Recipe was not saved and I was promtped to enter the required fields.

2. Test: Adding an ingredient preserves the already entered information.
    * Method: 
        - Add name, pin, title, category, dietary info, meal type, img url and then add an ingredient.
    * Expected Result:
        - All information already entered is preserved and displayed for the user.
    * Result:
        - All information already entered is preserved and displayed for the user.

3. Test: Adding a step preserves the already entered information.
    * Method: 
        - After running test 2, add a step.
    * Expected Result:
        - All information already entered is preserved and displayed for the user.
    * Result:
        - All information already entered is preserved and displayed for the user.
4. Test: Information can be edited and will be preserved.
    * Method: 
        - After running test 3, edit the step, ingredient, title, name, category and image url, then add a step or ingredient.
    * Expected Result:
        - All edited information is preserved and displayed for the user along with the new step/ingredient.
    * Result:
        - All edited information is preserved and displayed for the user along with the new step/ingredient. 
5. Test: Deleting an ingredient.
    * Method: 
        - With 2 ingredients added, edit any information in any form input then delete an ingredient.
    * Expected Result:
        - All edited information is preserved and displayed for the user minus the deleted ingredient.
    * Result:
        - All edited information is preserved and displayed for the user minus the deleted ingredient.
6. Test: Saving the recipe.
    * Method: 
        - With some information added to the form, click the save recipe button.
    * Expected Result:
        - The user is redirected to a confirmation page.
        - The new recipe is visible in the browse recipes page with all information preserved.
        - The recipe is now a new document in the database.
    * Result:
        - I was redirected to a confirmation page.
        - The new recipe is visible in the browse recipes page with all information preserved.
        - The recipe is now a new document in the database.

#### Edit Recipe
Link: [Edit your recipes](https://ci-ms3-nomnoms.herokuapp.com/edit_recipe)

1. Test: The recipe protection in place is working correctly.
    * Method: 
        - Having added a dummy recipe via add a recipe using the user name 'Test' and pin code of '2222'...
            1. Try the wrong pin code first. Eg. User name of 'Test' and pin code of '3333'.
            2. Try the wrong user name second. Eg. User name of 'Spongebob' and pin code of '2222'.
            3. Try the correct combination of user name and pin code.
    * Expected Result:
        1. A message is displayed on the page stating "Sorry! No recipe was found with that name and pin number combination".
        2. A message is displayed on the page stating "Sorry! No recipe was found with that name and pin number combination".
        3. The user is directed to the choose recipe to edit page and a list of relevant recipes is displayed.
    * Result:
        1. A message is displayed on the page stating "Sorry! No recipe was found with that name and pin number combination".
        2. A message is displayed on the page stating "Sorry! No recipe was found with that name and pin number combination".
        3. I was directed to the choose recipe to edit page and a list my recipes is displayed.

2. Test: Recipes are displaying relevant information in a collapsible header and body. 
    * Method: 
        - Click on the collapsible and check the correct title, image, ingredients and steps are displayed. Header only on smaller mobile devices.
    * Expected Result:
        - Each recipe has the correct information associated with it.
        - The collapsible body does not trigger on smaller mobile devices.
    * Result:
        - Each recipe has the correct information associated with it.
        - The collapsible body does not trigger on smaller mobile devices.

3. Test: Clicking the edit button for a recipe.
    * Expected Result:
        - The recipe clicked is displayed in a form format on a new page.
        - The recipe information is correct.
    * Result:
        - The recipe clicked is displayed in a form format on a new page.
        - The recipe information is correct.

4. Test: The add ingredient button functions correctly. 
    * Method: 
        - Add an ingredient.
    * Expected Result:
        - A new ingredient has been added.
    * Result:
        - The page reloads and a new ingredient has been added.

5. Test: The delete ingredient buttons function correctly. 
    * Method: 
        - Delete an ingredient.
    * Expected Result:
        - The ingredient has been deleted.
    * Result:
        - The page reloads and the deleted ingredient has been removed.

6. Test: The add step button functions correctly. 
    * Method: 
        - Add a step.
    * Expected Result:
        - A new step has been added.
    * Result:
        - The page reloads and a new step has been added.

7. Test: Leaving a step blank removes the step and the recipe saves correctly.
    * Method: 
        - Add an ingredient. Change the title, category, dietary info, meal type and image url. Remove all text from a step textarea and click save recipe.
    * Expected Result:
        - The user is redirected to the recipes that they could edit with the user name and pin code entered previously.
        - The recipe is displayed with updated information.
        - The database entry for the edited recipe has been updated.
    * Result:
        - I was redirected to the recipes that I can edit with the user name and pin code entered previously.
        - The recipe was displayed with updated information.
        - The database entry for the edited recipe was updated.

##### Edit Recipe Bugs:
I discovered a few bugs in this section of testing. 
* Adding an ingredient or step updates the database immediately so this new information is stored without the user clicking the save button.
* Adding a step or adding/deleting an ingredient overwrites any other edited information so that when the page reloads, that edited information is lost.
    * Given a more distant deadline, I would re-write the update_recipe function to use the session object in a similar manner to my add_recipe function so that updates aren't written to the database until the user presses save and so that all the buttons on the page update the session recipe object.

#### Remove Recipe
Link: [Remove a recipe](http://ci-ms3-nomnoms.herokuapp.com/remove_recipe)
1. Test: The recipe protection in place is working correctly.
    * Method: 
        - Repeating Test 1 from edit recipes, this page is essentially the same.
        - Having added a dummy recipe via add a recipe using the user name 'Test' and pin code of '2222'...
            1. Try the wrong pin code first. Eg. User name of 'Test' and pin code of '3333'.
            2. Try the wrong user name second. Eg. User name of 'Spongebob' and pin code of '2222'.
            3. Try the correct combination of user name and pin code.
    * Expected Result:
        1. A message is displayed on the page stating "Sorry! No recipe was found with that name and pin number combination".
        2. A message is displayed on the page stating "Sorry! No recipe was found with that name and pin number combination".
        3. The user is directed to the choose recipe to remove page and a list of relevant recipes is displayed.
    * Result:
        1. A message is displayed on the page stating "Sorry! No recipe was found with that name and pin number combination".
        2. A message is displayed on the page stating "Sorry! No recipe was found with that name and pin number combination".
        3. I was directed to the choose recipe to remove page and a list my recipes is displayed.

2. Test: The delete button.
    * Method: 
        - Clicking on the delete button for the recipe I wish to delete.
    * Expected Result:
        - A modal with a warning method is loaded. The modal has two buttons, one to cancel and one to confirm deletion.
    * Result:
        - A modal with a warning method was loaded. The modal had two buttons, one to cancel and one to confirm deletion.

3. Test: The modal buttons.
    * Method: 
        - Clicking on the cancel button first.
        - Go again and click the delete button.
    * Expected Result:
        - Clicking cancel closes the modal without redirecting.
        - Clicking delete closes the modal and redirects the user to a page displaying a success message.
    * Result:
        - Clicking cancel closed the modal without redirecting.
        - Clicking delete closed the modal and redirected me to a page displaying a success message.

##### Remove Recipe Bugs:
I came across one particularly beguiling bug whilst test this process. If for some reason the user clicks the browser's back button, the previous page is loaded and the deleted recipe is still there. If at this point the user clicked delete on the recipe that was already deleted then the application would crash when attempting to remove a document that didn't exist anymore. The find_recipes_for_removal function relies on a form post to display the recipes that can be deleted at which point it checks the database for the relevant recipe documents so the bug was not due to the form being resubmitted. The only thing I can think of is that the page was being loaded from the browser cache.
- The fix: 
    - My fix for this was to put some protection in place in the delete_recipe function that first checks if such a document exists before passing a success message to the confirmation page. If the recipe doesn't exist the function passes a message stating that the recipe had already been deleted. This works to prevent a crash and I hope that the navigation buttons I put in place are enough to dissuade the user from using the browser's back button.

### Styling Testing
I used Google Chrome developer tools for the majority of the development process. 
I tested my styling across multiple browsers - Chrome, Firefox, Edge and Opera. I also tested on an android smartphone. I haven't had access to any apple devices in order to properly test.

All MaterializeCSS components I have used in the application tested fine for all the above browsers - sidenavs, collapsibles, cards and tabs.
All my media breaks appear to be working correctly.

### Python Code Validation
Code checked and passed with [pep8online](http://pep8online.com/)

![alt text](/static/img/pep8.png "pep8online")
