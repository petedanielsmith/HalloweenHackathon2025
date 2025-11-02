# Hackathon Halloween 2025

<details>
<summary>How to use this repo (Click to show)</summary>

**Make sure you have:**
- Python installed, this project used V3.12,

**From the terminal:**

Open the folder in a terminal where you want the project to be saved
#### Run git clone:
```
git clone https://github.com/petedanielsmith/HalloweenHackathon2025.git
```
#### Navigate in to the new folder:
```
cd HalloweenHackathon2025
```
#### Setup a virtual enviroment:
Create a virtual enviroment for the project.

Linux / Mac:
```
python3 -m venv .venv
source .venv/bin/activate
```
Windows CMD:
```
python3 -m venv .venv
.venv\Scripts\activate
```
Windows PowerShell:
```
python3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```
#### Install the dependancies:
This will install all the dependancies needed for the project in to the virtual enviroment if it is setup, rather than globally
```
pip install -r requirements.txt
```
#### Add `.env` file
Add a file in the root of the project called .env and add this to the file for local dev:
```
DEBUG=True
SECRET_KEY=dev-secret-key-change-this
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
```
#### Run the migration to create local db
```
python3 manage.py migrate
```
#### Create a local admin user
Run this and enter user, email and passowrds when asked
```
python manage.py createsuperuser
```
#### To launch the server
Run this and then open the url (probably http://127.0.0.1:8000/)
```
python3 manage.py runserver 
```

---

</details>



# Lost Souls
Lost Souls is a site that has been created solely with the purpose of offering top-quality experiences to a market that hasn't been addressed as of yet; the Undead. The site allows our unliving users to book an event that appeals to them, whether it's a unique possession or haunting experience, or simply a little R&R away same four walls of the user's usual crypt.

![Site view across devices](route)

The live link for "Lost Souls" can be found [HERE](https://halloween-hackathon-25.petedanielsmith.co.uk/)

## Table of Contents
+ [UX](#ux "UX")
  + [Site Purpose](#site-purpose "Site Purpose")
  + [Site Goal](#site-goal "Site Goal")
  + [Audience](#audience "Audience")
  + [Communication](#communication "Communication")
  + [Existing User Goals](#existing-user-goals "Existing User Goals")
  + [New User Goals](#new-user-goals "New User Goals")
  + [Future Goals](#future-goals "Future Goals")
+ [User Stories](#user-stories "User Stories")
  + [Admin stories](#admin-stories "Admin stories")
  + [Site User stories](#site-user-stories "Site User stories")
+ [Design](#design "Design")
  + [Colour Scheme](#colour-scheme "Colour Scheme")
  + [Imagery](#imagery "Imagery")
+ [Features](#features "Features")
  + [Existing Features](#existing-features "Existing Features")
  + [C.R.U.D](#crud "C.R.U.D")
  + [Future Implementations](#future-implementations "Future Implementations")
+ [Testing](#testing "Testing")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Responsiveness Testing](#responsiveness-testing "Responsiveness Testing")
  + [C.R.U.D. Testing](#crud-testing "C.R.U.D. Testing")
  + [Feature Testing](#feature-testing "Feature Testing")
  + [Bug Testing](#bug-testing "Bug Testing")
+ [Technologies Used](#technologies-used "Technologies Used")
  + [Main Languages Used](#main-languages-used "Main Languages Used")
  + [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used "Frameworks, Libraries & Programs Used")
  + [Databases](#databases "Databases")
  + [Installed dependencies](#installed-dependancies "Installed dependencies")
+ [Development and Deployment](#development-and-deployment "Development and Deployment")
+ [Credits](#credits "Credits")
  + [Content](#content "Content")
  + [Media](#media "Media")

## UX

### Site Purpose:
The aim of this site is to bring all undead spirits together from around the world.  It is still a rather niche market, where we hope to offer this audience something original that they wouldn't be able to find anywhere else among this mortal realm.  It also offers them the chance to interact to leave reviews based on their experiences with our service.

### Site Goal:
To propagate a variety of experiences and events our soulless companions can take full advantage of.  It aims to bring them various options to explore new haunts and/ or environments.

### Audience:
Naturally it is clearly aimed to the undead since only they can really benefit from our services, yet the living can still catch a quick preview of what's in store once they are eligible to sign up for our site.  We aim to be the first to provide this service and reunite ghouls from all different backgrounds.

### Communication:
users are provided with the possibility to review experiences and interact with one another via their reviews.

### Existing User Goals:
The endless joy of eternal scares in our ever-expanding event catalogue.

### New User Goals:
To feel welcomed by the existing community of undead users we have and explore options in the afterlife they may have never previously considered.

### Future Goals:
- We aim to build an online ouija application where many undead can taunt the living and interfere with their ceremonies, for entertainment purposes of course.
- We seek to contact other mediators around the world to help broaden our catalogue of events to choose from, appealing to different tastes our undead clients may have.

## User Stories

### Admin stories:
#### As an admin:
- As an admin I can see registered user's information on the system, preferred payment method of souls and preferences.
- As an admin I can ensure it only allows the undead to sign up and access our services.

### Site User stories:

#### Home/Events:
- [x] As a user I can enter key words in the search field so that I can filter the events that interest me.
- [x] As a user I can scroll down and switch pages to continue viewing more options.
- [x] As a living user I am restricted access to signing up for the service until I pass away.

#### Purchase feature:
- [x] As a user I can proceed to purchase an event and enter my payment details
- [x] As a user I can confirm my purchase is successful.

#### Review:
- [x] As an undead user, I can enter my review of an event I have bought and experienced.
- [x] As an undead user, I can enter my rating of the event so others may see how terrifying it is.

#### Navigation bar:
- [x] As an undead user I can always view the NavBar so that I can navigate between pages.
- [x] As an undead user I can click on the logo to return to the home page.


## Design

### Colour Scheme:

Our team have decided for this Halloween theme Hackathon to naturally go with colours that resemble our favourite holiday. 

- #0d0c13 - Typically used as background colour for the body of the page.

- #16151f - Typically used as the colour for the NavBar and the Footer of the page.

- #f6a824 - This is the colour we used for our nav-links, buttons while using a slightly lighter shade #d8900f for hover effects and button outlines.

### Imagery:

#### Logo

- PENDING

![logo](ROUTE)

#### Favicon

- This favicon was selected from [iconos8](LINK).

![Favicon](ROUTE)

#### Sign up/ Sign in image

This image was taken from [Pexels](https://www.pexels.com/@anete-lusina/) for my Sign In and Sign Up pages.

![signinup-image](src/images/signinup-pic.jpg)

#### Dice (Rating)

All the images of dice in this image were taken from [freeiconspng](https://www.freeiconspng.com/images/dice-png) for my dice rating system.  This was chosen to fit the theme of board games a little better.

![Dice](src/images/dice-all.png)

## Features

### Existing Features:

#### Home Page:

![Home page](src/images/home-page.png)

#### Navigation Bar:

##### Desktop:

![Navbar desktop](src/images/navbar.png)

##### Mobile:

-Upon clicking on the dropdown menu, options appear:

![Navbar mobile](src/images/navbar-smaller.png)

#### Games Page:

- Games appear in a list in order from latest to oldest.

![Games page](src/images/games-page.png)

#### Count features on Games Page:

-Displays total amount of likes, reviews, and average of ratings respectively.

![Count features](src/images/total-count.png)

#### Game Page:

![Game Page](src/images/game-page.png)

#### Review feature:

![Review feature](src/images/review-feature.png)

#### Like icon feature:

- Like icon highlights if previously selected by user.

![Like icon feature](src/images/like-icon.png)

#### Ratings feature:

![Ratings feature](src/images/ratings-feature.png)

#### Create Game Page:

![Create Game Page](src/images/create-game.png)

#### Search bar feature:

- Waits a couple of seconds before updating search incase user is still typing.

![Search bar feature](src/images/search-bar.png)

#### Liked page:

- Displays a list of all liked game in order from latest to oldest.

![Liked Page](src/images/liked-page.png)

#### Profile page:

![Profile Page](src/images/profile-page.png)

#### Sign in & Sign up:

##### Sign-in:

![Sign-in](src/images/sign-in.png)

##### Sign-up:

![Sign-up](src/images/sign-up.png)

#### Confirmation messages:

These were supplied by [react toastify](https://deadsimplechat.com/blog/react-toastify-the-complete-guide/#what-are-toast-notifications) to confirm each of the user's decisions throughout the App.

![Confirmation-messages](src/images/confirm-message.png)

### C.R.U.D:

#### Created Game Page:
- Once the dots to the top-right corner are clicked on, they are given the option to edit or delete the game post they've created.
- Only the owner of the Game is shown the three-dot dropdown menu with access to these options.

![CRUD - created game edit menu](src/images/create-game-edit.png)

#### Review Game Page:
- Once the dots to the top of the review are clicked on, they are given the option to edit or delete the review they've created.
- Only the owner of the review is shown the three-dot dropdown menu with access to these options.

![CRUD - Review edit menu](src/images/review-feature-menu.png)

#### Like Icon:
- The user is given the option to unlike the Game post the same way they liked it to begin with, by clicking on the icon. icon will change colour.
- Users are not given the possibility to like their own posts.

![CRUD - Like-icon](src/images/like-icon.png)

#### Ratings Game Page:
- User is given the option below their initial rating to edit and update their rating or delete it.
- Only the owner of the rating is shown these options.
- If the user chooses to update, and clicked on the 'edit' button, the six dice images will re-appear for the user to correctly update.

![CRUD - Ratings edit menu](src/images/ratings-feature-edit.png)

#### Profile Page:
- Once the dots to the top-right corner are clicked on, they are given the option to edit their profile or change either their username or password.
- Only the owner of the Game is shown the three-dot dropdown menu with access to these options.

![CRUD - Profile Page edit](src/images/profile-page-edit.png)

### Future Implementations
- Using the GameDataContext.js, we plan to add a feature to the game to display the top-rated games according to the total averages our community users have given.
- Forum for users to have more in-depth conversations and thus increase user interaction within the community.
- Nested comments within the review section to users to interact or react to each other's reviews.
- Additional app dedicated to informing our users of upcoming board-gaming events.

## Testing

### Validator Testing

- W3 HTML Validator

I ran the website through the validator and recieved no errors.
![W3 Validator HTML](src/images/w3validator-html.png).

- W3c CSS Validator

I ran the website through the validator and recieved no errors.
![W3c Validator CSS](src/images/w3cvalidator-css.png)

- I also checked each of my JS fies through [JSHint](https://jshint.com/) and found no errors in any of the files

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** |
| ----------------------------- | ----------------------- | --------------------------- | ---------- |
| Home page | lighthouse | [Acceptable scores](src/images/lighthouse.png) | ✅ |
| Liked Page| lighthouse | Acceptable scores | ✅ |
| Profile Page | lighthouse | Acceptable scores | ✅ |
| GamePage | lighthouse | Acceptable scores | ✅ |
| Sign-up page | lighthouse | Acceptable scores | ✅ |
| Sign-in page - html | lighthouse | Acceptable scores | ✅ |
| WAVE results | WAVE | [Acceptable scores](src/images/wave-results.png) | ✅ |
| Microsoft Edge browser | Launch site | Site opens without issue | ✅ |
| Google Chrome browser | Launch site | Site opens without issue | ✅ |

The results from WAVE mostly highlight that icons don't have a link when infact they are being used as a total count feature.

### Responsiveness testing

| **TEST**                      | **ACTION**              | **EXPECTATION**             | **RESULT** |
| ----------------------------- | ----------------------- | --------------------------- | ---------- |
| Games page - responsiveness    | Size site down to 320px | all elements stay on screen | ✅         |
| Games page - responsiveness    | Size site up to 1920px  | all elements stay on screen | ✅         |
| Liked page - responsiveness   | Size site down to 320px | all elements stay on screen | ✅         |
| Liked page - responsiveness   | Size site up to 1920px  | all elements stay on screen | ✅         |
| Game page - responsiveness  | Size site down to 320px | all elements stay on screen | ✅         |
| Game page - responsiveness  | Size site up to 1920px  | all elements stay on screen | ✅         |
| Profile page - responsiveness    | Size site down to 320px | all elements stay on screen | ✅         |
| Profile page - responsiveness    | Size site up to 1920px  | all elements stay on screen | ✅         |
| Sign-up page - responsiveness   | Size site down to 320px  | all elements stay on screen | ✅         |
| Sign-up page - responsiveness   | Size site up to 1920px  | all elements stay on screen | ✅         |
| Sign-in page - responsiveness | Size site down to 320px | all elements stay on screen | ✅         |
| Sign-in page - responsiveness | Size site up to 1920px  | all elements stay on screen | ✅         |

### C.R.U.D. testing

| **TEST**          | **ACTION**             | **EXPECTATION**          | **RESULT** |
| ----------------- | ---------------------- | ------------------------ | ---------- |
| New Game Post - Create     | Add new instance | Instance created         | ✅         |
| New Game Post - Read       | Retrieve all instances | Instances visible in UI  | ✅         |
| New Game Post - Update     | Modify an instance     | Mods saved & visible     | ✅         |
| New Game Post - Delete     | Delete an instance     | Instance removed | ✅         |
| Reviews - Create | Add new instance | Instance created         | ✅         |
| Reviews - Read   | Retrieve all instances | Instances visible in UI  | ✅         |
| Reviews - Update | Add new instance | Mods saved & visible     | ✅         |
| Reviews - Delete   | Retrieve all instances | Instance removed | ✅         |
| Likes - Create | Add new instance to DB | Instance created         | ✅         |
| Likes - Delete | Delete an instance     | Instance removed from UI | ✅         |
| Ratings - Create | Add new instance to DB | Instance created         | ✅         |
| Ratings - Update | Add new instance | Mods saved & visible     | ✅         |
| Ratings - Delete | Delete an instance     | Instance removed from UI | ✅         |
| User Profile - Read   | Retrieve all instances | Instances visible in UI  | ✅         |
| User Profile - Update | Add new instance | Mods saved & visible     | ✅         |

### FEATURE TESTING

| **TEST**                      | **ACTION**             | **EXPECTATION**                                           | **RESULT** |
| ----------------------------- | ---------------------- | --------------------------------------------------------- | ---------- |
| Navigation bar                | Click on nav link      | user routed to correct page                               | ✅         |
| Game Post - Create                  | Enter characters in integer field  | user given an error                            | ✅         |
| Creation/ Update submission message                  | clicked on submit/ update/ delete button  | user is informed on success                            | ✅         |
| Like button                   | Click "like"           | Post liked/unliked accordingly                            | ✅         |
| Review section                   | Written empty message           | does not submit, prompts to write a message                            | ✅         |
| Review section                   | Write message and submit           | Message submits correctly                          | ✅         |
| Review - Edit button                   | Click edit button      | user allowed to edit review only if owner                             | ✅         |
| Review - Delete button                 | Click delete button    | user allowed to delete comment only if owner                               | ✅         |
| Image updated                | Change profile & post image    | both upload successfully                                | ✅         |
| Ratings average                | multiple ratings submitted/ deleted             | Calculates total average correctly                           | ✅         |
| Infinite scroll               | created more than 10 posts and scrolled down             | Page loads more posts with no duplicates                          | ✅         |
| 'Liked' page                | like a post            | 'Liked' posts added to page                    | ✅         |
| Sign in                         | User signs in           | UI updates & user is signed in, cannot access sign in or sign up page                            | ✅         |
| Sign up                       | User signs up          | new account created for the user                          | ✅         |
| Sign out                        | User clicks sign out     | UI updates, user is signed out, user cannot create a post | ✅         |

### BUG TESTING:
1. Rating.js wouldn't correctly update the total rating average upon deleting a rating.
- I added a windows.location.reload() method so it could fetch and call the correct recalculated average.

## Technologies Used
### Main Languages Used
- HTML5
- CSS3
- Javascript
- Python

### Frameworks, Libraries & Programs Used
- [Google Fonts](https://fonts.google.com/) - for the font families: 
- [Font Awesome](fontawesome.com) - for the social network icons.
- [GitPod](https://www.gitpod.io/) - for creating html files, css stylesheet and python files.
- [GitHub](https://github.com/) - to store my repository for submission.
- Google Dev tools - to test and fix issues detected.
- [Pexels](https://www.pexels.com/) to use free image for site.
- [Iconos8](https://iconos8.es/) for favicon.
- [Free icons](https://www.freeiconspng.com/) to use free dice images for rating.
- [Balsamiq](https://balsamiq.com/) - for the wireframe mockups of my webpage.
- [Am I Responsive?](https://ui.dev/amiresponsive) - to ensure the webpage displayed well on all devices.
- [Tiny PNG](https://tinypng.com/) to compress images.
- [Django database extension](https://yathomasi.medium.com/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16) - for ERD diagrams
- [FreeLogoDesign](https://app.freelogodesign.org/)
- [Colormind.io](http://colormind.io/) to generate color palette used. 
- [react bootstrap](https://react-bootstrap.netlify.app/) for bootstrap.
- [react toastify](https://deadsimplechat.com/blog/react-toastify-the-complete-guide/#what-are-toast-notifications)

### Databases

- [PostgreSQL](https://dbs.ci-dbs.net/)

### Installed Dependencies:
- "@testing-library/jest-dom": "^5.14.1",
- "@testing-library/react": "^11.2.7",
- "@testing-library/user-event": "^12.8.3",
- "axios": "^0.21.4",
- "bootstrap": "^4.6.0",
- "jwt-decode": "^3.1.2",
- "react": "^17.0.2",
- "react-bootstrap": "^1.6.3",
- "react-dom": "^17.0.2",
- "react-infinite-scroll-component": "^6.1.0",
- "react-router-dom": "^5.3.0",
- "react-scripts": "^5.0.1",
- "react-toastify": "^9.1.3",
- "web-vitals": "^1.1.2"

## Development and Deployment

### Heroku

This site is deployed using Heroku. To deploy it from its GitHub repository to Heroku, I took the following steps:

1. Log in (or sign up) to Heroku
2. Click on the _New_ button and select _Create new app_
3. Give it a unique name and choose the region _Europe_
4. Click the *Deploy* tab, go to the _Deployment method_ section, select _GitHub_ and confirm this selection by clicking on the _Connect to Github_ button
5. Search for the repository name on github _Boardgamers_ and click the _Connect_ button
6. Inside the src folder add an api folder and create an axiosDefault.jsx
7. Add the link to the deployed version of the api as baseURL
8. Create a _Procfile_ in the root directory and add *web: npm run start*
9. In Heroku enable the automatic deploy or manually deploy the code from the main branch

To see the [view of the live site](https://boardgamers-ci-364d7fb71032.herokuapp.com/) click on the _Open app_ button in the top right corner.

### Run Locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

Install Dependencies:

```npm install```

Run Application:

```npm start```

### Development

#### Forking GitHub Repository

Forking allows you to make a copy of a chosen repository to your own GitHub account. This allows you to test and edit the project without making changes to the original. Forking is done by following these steps.

1. Whilst logged into your GitHub account, navigate to the repository you would like to fork.
2. Click on the **Fork** button at the top right of the page.
3. Choose a name to give the repository. It will be intially named as the same as the original repository.
4. Click the **Create Fork** button.

#### Cloning GitHub Repository

Cloning allows you to download a local version of a chosen repository. Cloning can be done by following these steps.

1. Whilst logged into your GitHub account, navigate to the repository you would like to clone.
2. Click the green **<> Code** button.
3. Click on the **Local** tab.
4. Select **HTTPS** and copy the url.
5. Open your chosen IDE and ensure Git is installed.
5. In your IDE terminal type **git clone (url link that you copied)** and hit enter.

## Credits

- “Moments” walkthrough: Helped me immensely with the initial setup for my project and basic functions to help me then expand and personalize with my fetures and my own apps.
- Slack community for the vast amount of support and information available to clear doubts and help with potential bugs.
- Tutor Support for their constant support with some of the questions or issues I had and the patience to make everything so clear and such a pleasant learning experience.
- CI for providing us with a GitPod that I've spent manu hours on for this project, and hopefully many more for the future implementations and improvements to be made.

### Content
- The majority of the descriptions for my Games Pages came from [BoardGameGeek](https://boardgamegeek.com/)


### Media
- [Pexels (@anete-lusina)](https://www.pexels.com/@anete-lusina/) provided me with the image for my sign up and sign in forms.
- CI for the default images for both profile and posts which has been stored in Cloudinary.
- Dice images