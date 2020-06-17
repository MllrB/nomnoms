# NomNoms 
##### A Recipe Sharing Web App by MllrB
##### Developed for CodeInstute Milestone Project 3 - Data Centric Development

NomNoms is a website for creating and sharing recipes.
 - Browse other user's recipes.
 - Add recipes.
 - Edit recipes you created.
 - Delete recipes you created.

You can visit the deployed web app via:
- [Heroku](https://ci-ms3-nomnoms.herokuapp.com/home)

Files and code can be found in my GitHub repository:
- [GitHub Repository](https://github.com/MllrB/nomnoms)

_//NomNoms was developed for educational purposes. Recipes are open for anyone to browse and add. There is no user authenication. I'll do my best to moderate but am not responsible for content at any given time._

![alt text](/static/img/nomnoms.png "NomNoms")

## Contents
- [UX](#UX)
    - [Project Goals](#Project-Goals)
    - [User Stories](#User-Stories)
    - [Design Choices](#Design-Choices)
    - [Fonts](#Fonts)
- [Technologies Used](#Technologies-Used)
    - [Languages](#Languages)
    - [Libraries/Tools](#Libraries/Tools)
    - [Applications](#Applications)
- [Testing and Bugs](#Testing-and-Bugs)
- [Deployment](#Deployment)
    - [Heroku Deployment](#Heroku-Deployment)
    - [Cloning my NomNoms Repository](#Cloning-my-NomNoms-Repository)
- [Acknowledgements](#Acknowledgements)

## UX

### Project Goals
For this project I needed to familiarise myself with technologies and frameworks new to me, Python, Flask, MongoDB and Heroku. Using these technologies I intended to create a recipe sharing web application that would allow users to create, update and delete their own recipes and to find recipes created by other users. 

#### User Stories
1. As a user I would like to find recipes to prepare myself.
    * To achieve this I made a "browse recipes" page with search and filtering options. 
    * The search allows the user to find recipes from keywords in the recipe title, ingredients, category(sweet, savoury, basics, drinks), dietary information (vegetarian, dairy free, nut free etc...) and meal types (breakfast, lunch, dinner etc...).
    * The user can also fileter recipes by category, dietary information and meal types or a combination of all three
    * On desktop/laptop devices, the search and filter functionalities are displayed on the page. On mobile devices the search and filter functionalities are accessible via a side navigation panel triggered by a button on the page
    * Each recipe can be viewed on it's own page by selecting "show recipe" from the browse recipes page

2. As a user I would like to easily access the list of ingredients while following the steps for a recipe.
    * One of the common complaints I heard about recipe websites in general is the need to constantly scroll up and down the page to switch between ingredients and steps. To address this, I decided to use tabs; A tab for ingredients and a tab for steps which allows the user to easily switch between the two.
    * I also included a scroll bar for the steps tab so that the available tabs would always be visible even if the list of steps is long. As a bonus, this method also preserves the user's position in the steps list. That is, if a user is a few steps in and needs to switch to the ingredients tab, when they switch back to the steps tab they will see the step they were previously on.
    

3. As a user I would like the ability to add my own recipes
    * The user can add recipes via the add recipes links in the navigation bar, a homepage card and buttons on the recipe pages and after the user has added or removed a recipe.
    * Adding a recipe is quite form heavy so in order to make this process more user friendly I tried to make the form as dynamic as I could. To achieve this dynamic behaviour, I used the Flask session object.
        * The session object is initialised with an empty recipe object that can be updated as the user inputs information. This initialisation occurs when the homepage loads and a check is made on the add recipe page to ensure it exists, which it might not if for example the user navigated directly to the add recipe page from a link external to the website or if the user deletes their recent browser cache.
        * Every time the user presses a button on the add recipes page a form is submitted and the session object is updated with the new information. The page is then reloaded and displays the new information that had just previously been entered by the user. To make this as dynamic as possible:
            * When a new ingredient is added, changes made to any existing information are logged to the session recipe object.
            * When a new step is added, changes made to any existing information are logged to the session recipe object.
            * When the save recipe button is clicked, change made to any existing information are first logged to the session recipe object before being inserted as a new document in the database.

4. As a user I would like to be able to correct any mistakes I make when adding a recipe.
    * The user can edit any of the recipes they have added via the edit recipes links in the navbar or on the homepage.
    * In order to prevent users from editing other user's recipes, the user must first provide a combination of the name and pin/password they used when creating the recipe.
    * Exclduing the user's name or pin, the user can edit all recipe information in any of their recipes.

5. As a user I would like to update my recipes.
    * As above (4), exclduing the user's name or pin, the user can edit all recipe information in any of their recipes.

6. As a user I would like the ability to remove a recipe.
    * Using the same name and pin protection as used for editing, the user can delete/remove any of their recipes. 
    * In order to prevent accidental deletion, I included a modal used as an extra step that the user must pass before the recipe is deleted. This modal simply asks the user to confirm or cancel the deletion of the recipe.

7. As a user I would like to upload my own photos to accompany my recipes.
    * This is currently beyond the scope of this project as the images would require storage, but this is a feature I would like to introduce in a later version. To allow the user to attach images to their recipes, my workaround is to allow the user to save an image URL as part of their recipe(s).

##### User Stories for later versions

8. As a user I would like to 
    * build a collection of favourite recipes.
    * follow other users who's recipes I like or have add to my favourites.
    * build a shopping list from by selecting recipes I want to try.
    * maintain a "pantry" so that ingredients that I already have don't appear in my shopping list.
    * leave feedback and ratings for recipes that I have tried.
        * Without user authentication, I am unable to deliver these options in a satisfactory and user friendly manner. I would need to ask for a pin and name each time the user tried to access any of these options which would leave scope for bad user experience, for example, through typos or by having to click too many buttons to achieve their goals. With this in mind, I thought it best to leave these for a later version.


#### Design Choices

I wanted my design to reflect the appearance of a traditional recipe notebook. The background images used are photographs of my own notebook. On the add, edit, remove and recipe pages, the background image includes a spine to further present the appearance of a notebook. On the home page, the browse recipes page, cards and sidenav the bacckground image is a section of notebook paper. For mobile devices, I used the notebook paper image across the site as the spine caused legibility issues on smaller screens. I wanted my font choices to give the impression that the recipes were handwritten. I chose the text colours used with a similar goal in mind.

##### Fonts
My choice of fonts:

* Logo: [Google Fonts: Swanky and Moo Moo](https://fonts.google.com/specimen/Swanky+and+Moo+Moo)
    * Font name aside, the whimsy this font presented was the main driver in my decision to use it for the logo. I felt it perfectly matched the whimsical nature of my choice of project/application name. I would have also used it for my navigation links too but it was slightly less suitable at smaller text sizes than the "Indie Flower" font I used instead.

* Navbar Fonts: [Google Fonts: Indie Flower](https://fonts.google.com/specimen/Indie+Flower)
    * I chose this font for it's handwritten look and used it only in the navigation bar. 

* Main body, buttons, labels, links and cards: [Google Fonts: Gaegu](https://fonts.google.com/specimen/Gaegu)
    * This was the most appealing font to me due to it's appearance on the notepaper backround images. I felt it was the most suited to the design aesthetic I have attemted to achieve and as such I have used it all over the site. I intentionally used both capitalised and fully lowercase/uppercase sentences with this font to further reinforce the idea of the recipes being handwritten.


## Technologies Used

#### Languages
* HTML
* CSS
* jQuery
* Python
* Jinja

#### Libraries/Tools
* jQuery
* MaterializeCSS
* Google Fonts
* Git

#### Applications
* Visual Studio Code
* GitHub
* Heroku
* MongoDB
* Adobe Photoshop
* MS Powerpoint
* CPanel

## Testing and Bugs

View the testing documentation in the [testing.md file](testing.md)

## Deployment
This project has been deployed using Heroku. 

#### Heroku Deployment 
- [Heroku Deployment](http://ci-ms3-nomnoms.herokuapp.com/home)

After logging into my Heroku dashboard via [Heroku's login page](https://id.heroku.com/login), I selected "Create new app" from the dropdown menu at the top right of the dashboard. I typed in my project name and selected Europe as my region. The deployment method was set to Heroku Git by default so I left that as is. I then navigated to the Settings tab and clicked "Reveal Config Vars". From here I set the IP and PORT variables, the MONGO_URI varibale to allow connection to my database and also a SECRET_KEY to allow the app to use the Flask session object.
From the command line, I initialised a git repository and established a connection to Heroku using the "heroku git:remote -a " command with my application name. I created a requirements file using the pip freeze command and also created a Procfile. I encountered a problem with the creation of the Procfile which appeared to be a result of the filenaming conventions employed by Windows 10. As a workaround, I copied the Procfile text, deleted the inital Procfile i had created and using the Notepad++ text editor, I created a new file, pasted in the Procfile contents and saved it as a "Procfile" with no file extension. This solved the issue of Heroku reading my initial Procfile. I then started the Heroku Dynos from the command line using the "heroku ps:scale web=1" command. Once ready, I pushed my git commits to Heroku using the "git push heroku master" command.

I also created a repository for my code on [GitHub](https://github.com/MllrB/nomnoms) and connected my heroku application to this repository.

#### Cloning my NomNoms Repository
Should you wish to clone this repository you can do so by:
1. Navigate to my [NomNom repository](https://github.com/MllrB/nomnoms).
2. Click the green "Clone or Download" button on the right side of the repository.
3. Copy the URL displayed `(https://github.com/MllrB/nomnoms.git)`.
4. You will need to have Git installed on your system, if you don't, you can find out how [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
5. Open a terminal window and navigate to the folder where you wish to clone this repository.
6. Initialise Git for this folder by typing "git init".
7. Type "git clone " followed by the URL you copied on step 3. It should look like this...
    - `git clone https://github.com/MllrB/nomnoms.git`

## Acknowledgements

* All background images used on the site are my own.
* Homepage card images are courtesy of [fshoq.com](https://fshoq.com)
* Homepage 'Fried Egg' image provided by [freestockphotos.biz](http://www.freestockphotos.biz/stockphoto/11438)
* Image used as default image for recipes from [pikrepo.com](https://www.pikrepo.com/fyxnv/illustration-of-person-holding-sign-with-images-of-healthy-food)
* Image URLS provided by users are outside my current control. This project is for my educational purposes only and not for profit. If you wish for credit to be attributed for an image, please contact me via mllrb.dev@gmail.com 
* Fonts provided by [Google Fonts](https://fonts.google.com).


------------






