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

![alt text](/static/img/nomnoms.png "Movie Buff Preview")

## Contents
- [UX](#UX)
    - [Project Goals](#Project-Goals)
    - [My Goals](#My-Goals)
    - [User Stories](#User-Stories)
    - [Design Choices](#Design-Choices)
    - [Fonts](#Fonts)
- [Wireframes](#Wireframes)
- [Technologies Used](#Technologies-Used)
    - [Languages](#Languages)
    - [Libraries/Tools](#Libraries/Tools)
    - [Applications](#Applications)
- [Testing and Bugs](#Testing-and-Bugs)
- [Deployment](#Deployment)
    - [GitHub Deployment](#GitHub-Deployment)
    - [Cloning my MovieBuff Repository](#Cloning-my-MovieBuff-Repository)
    - [Mllrb.com Deployment](#Mllrb.com-Deployment)
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
            * Changes to steps are logged when the user updates a step

4. As a user I would like to be shown my score at the end of each game and where my score ranks against previous attempts.
    * A current score and leaderboard is displayed at the end of every round for each game type and mode.
    * The leaderboards are seperated by each game type and each mode within the game types.
    * The leaderboard scores are persistent but only per session. A page refresh will reset the top scores. Ideally I would prefer the scores to be persistent per user, however, limitations in my knowledge of how to achieve this and time constraints have prevented me from implementing this for this current version.

5. As a user I would like to see variation in the questions posed.
    * I tried to achieve this by shuffling the data set for each game attempt and each round within a game attempt. The player will not be presented with the same correct answer twice in the same round with one caveat... in survival mode and in the unlikely event that the player succeeds in answering all of the available questions correctly, the data set will reset.
    * If the same correct answers are displayed in subsequent game attempts, they, at least, will not be displayed in the same order and will have different preceding and succeeding questions.


#### Design Choices

In general, people watch movies in darkened environments whether that be in a theatre or at home. With that in mind, I decided to use a dark background image and for the headings and titles to be slightly dimmed. This decision has the added bonus of directing the user's attention to the game rather than the background or titles.

In a nod to The Movie DB who provide the data that powers the game free of charge, I decided to use similar (but not the same) colors to their logo's primary and secondary colors. I re-colored the background image with a dark blue overlay similar to that of their secondary logo color and the game buttons are styled with a similar color to their primary logo color. 

##### Fonts
My choice of fonts were made with the movie industry in mind.

* Titles: [Google Fonts: Monoton](https://fonts.google.com/specimen/Monoton)
    * This font reminded me of early cinema movie poster styles.

* Buttons, tooltips and actor/character names: [Google Fonts: Special Elite](https://fonts.google.com/specimen/Special+Elite)
    * I chose this font for it's typewriter feel and it's similarity to Courier New which is traditionally used for movie/screenplay scripts.

* Leaderboard Scores: [Google Fonts: Bungee Inline](https://fonts.google.com/specimen/Bungee+Inline)
    * I feel that this font falls somewhere between the movie and game styles and is complimentary to the Monoton font used for the titles and for this reason, I used it only for the leaderboard.

## Wireframes
I first scribbled out my basic idea on paper and then used Microsoft Powerpoint to produce a digital version. [View the pdf version](Assets/Media/moviebuff-wireframes.pdf)

The idea and design were always intended for a landscape viewing aspect and as such, rather than implementing a different design for mobile devices, I decided to implement a disclaimer prior to loading which encourages the user to switch to a landscape view and which would only display when the screen height is greater than it's width.

For the most part, I stuck to the wireframe design with the exception of the leaderboard screen. Initially my design would only show the players score at the end of each game, however, as development progressed I decided that it was necessary and desirable to also show the current top scores.

## Technologies Used

#### Languages
* HTML
* CSS
* Javascript

#### Libraries/Tools
* jQuery
* Bootstrap
* FontAwesome
* Google Fonts
* Git
* Jasmine

#### Applications
* Visual Studio Code
* GitHub
* Adobe Photoshop
* MS Powerpoint
* CPanel

## Testing and Bugs

View the testing documentation in the [testing.md file](testing.md)

## Deployment
This project has been deployed both on GitHub Pages and on my personal domain.

#### GitHub Deployment 
- [GitHub Pages Site](https://mllrb.github.io/MovieBuff/index.html)

First, I navigated to my [MovieBuff Repository](https://github.com/MllrB/MovieBuff) on the GitHub site.
The default tab selected is the Code tab so from here I selected the Settings tab. I scrolled down the page until I came to the "GitHub Pages" section from where I selected Master Branch as the source. I left the Theme Chooser empty. 

_Note: Although I own a custom domain, owing to the time constraints for the completion of this project and my current lack of knowledge regarding the process, I decided against serving my custom domain from GitHub Pages. This is something I intend to rectify when time is not against me._

#### Cloning my MovieBuff Repository
Should you wish to clone this repository you can do so by:
1. Navigate to my [MovieBuff Repository](https://github.com/MllrB/MovieBuff).
2. Click the green "Clone or Download" button on the right side of the repository.
3. Copy the URL displayed `(https://github.com/MllrB/MovieBuff.git)`.
4. You will need to have Git installed on your system, if you don't, you can find out how [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
5. Open a terminal window and navigate to the folder where you wish to clone this repository.
6. Initialise Git for this folder by typing "git init".
7. Type "git clone " followed by the URL you copied on step 3. It should look like this...
    - `git clone https://github.com/MllrB/MovieBuff.git`

#### Mllrb.com Deployment 
- [mllrb.com/MovieBuff](http://mllrb.com/MovieBuff/index.html) 

After purchasing the domain from letshost.ie I gained access to their cPanel via the services menu. From here I opened their file manager which allowed me to create the various folders associated with the site. The folders had to be created within the public_html folder already present for the domain. Also, a pre-installed php file which displayed a letshost welcome screen needed to be removed.

Folders: 
* MovieBuff
    * Assets
        * css
        * js
        * Media

Once I had created these folders, I uploaded the various application files into their appropriate folders - all accomplished using the cPanel file manager application.

![alt text](Assets/Media/cPanel.png "File Manager example")

For simplicity and to avoid creating any unnecessary bugs, the folder names & structure and file names contained within each folder are identical to that of my GitHub repository with the exception of the Jasmine folder, jasmine test files and jasmine.html file which I deemed unnecessary for this avenue of deployment.

## Acknowledgements

* All data powering the game is provided by [the Movie DB](https://www.themoviedb.org/)
* The Movie DB logo also provided by [the Movie DB](https://www.themoviedb.org/)
* Actor and Movie images hosted by [the Movie DB](https://www.themoviedb.org/)
* GoldenGlobeAwards trophy image from [goldenglobes.com](https://www.goldenglobes.com/trophy-images) and unedited as stipulated (image resized to allow quick loading)
* Loading gif from [gifer.com](https://gifer.com/en/3GFW), edited by me to provide transparency
* Background image courtesy of [creativecommons.org](https://creativecommons.org/publicdomain/zero/1.0/deed.en) via [piqsels.com](https://www.piqsels.com/en/public-domain-photo-jtzfm). Edited by me.
* Fonts provided by [Google Fonts](https://fonts.google.com).
* getRandomIntInclusive function code snippet from [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random)
* Array shuffling code snippet from [adamkhoury](http://www.developphp.com/video/JavaScript/Memory-Game-Programming-Tutorial)


------------
## Finally...
...I really hope you enjoyed the game :)






