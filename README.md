## Recipes 4 U ##
<br>

This Django project is a recipe sharing blog intended for food lovers where users can upload, comment and like other recipes. Users can also view recipes posted by other users which they can try. Like a regular blog only registered users can post, comment on or like other recipes . Registered users will also have the ability to edit or remove their previous posts. 

![](images/responsive-screenshot.png)

[Link to site](https://recipesforu.herokuapp.com)

## UI/UX ##

The overall design is kept simple as users are encouraged to post images to go with their recipes . Research has shown that people eat with their eyes so to speak so distractions were kept to a minimum.

The layout of the site is standard for a blog site with clear descriptive navigational links. 

The site features are standard and expected for a blog site. 

**Agile**

The agile approach was employed in designing and constructing this project, from the outset of planning to the completion of development. To facilitate the process, I established a GitHub project and adopted the Kanban board methodology to divide project components into user stories and feasible tasks.

For a comprehensive view of all user stories please refer to the linked project [Project Kanban Board](https://github.com/users/oconnorian3/projects/10) . Additionally, each story has been assigned a label that indicates its level of significance in the site's overall functionality and acceptance.

## Wireframe

Below are some basic Wireframes done up before the project started.

*When a user is NOT logged in*

![](images/wireframe_loggedout.png)

*When a user IS logged in*

![](images/wireframe_loggedin.png)

## Development Planes ##

In order to develop an engaging and all-encompassing website, I conducted research on other food-related websites. This enabled me to identify and incorporate appropriate features and functionalities that aligned with my project, as well as determine a suitable color palette for the project.

## Strategy ##

**Site Goals**

The primary objective for the website was to establish a platform that users could effortlessly navigate and engage with, not only to upload their own recipes but also to interact with other members. My vision was to build a community where individuals could freely submit their favorite recipes and explore new ones.

The website caters to the following target groups:

* User Roles:
    * Standard User
    * Administrator

* Demographics:
    * Individuals passionate about food
    * Those seeking to broaden their culinary horizons
    * Cooking enthusiasts     

* The website must provide the user with the ability to:
    * Browse through recipes
    * Register an account
    * Create and upload their own recipes
    * Like and comment on recipes
    * Fill out a contact form

* The website must provide the admin with the ability to:
    * Approve comments    
    * Filter through recipes, comments, and users to manage the site effectively    

## Scope ##

This section outlines the functions and features included in the project scope. The project was designed with minimal functionality in mind, which means that most of the features included are basic requirements. For instance, user sign up and login functionality had to be implemented, along with basic CRUD operations for authenticated users. The Future Features section discusses potential features that were deemed unnecessary at this point in time, despite being within the project's possible scope.

## Structure ##

 The site's layout is based on a simple blog design that is commonly used by many other blogs online. With this structure, users can easily access the site, browse recipes , leave a message and login/register so they can upload their own recipes and comment on other recipes.

 ## Skeleton ##

 Wireframes were made using Lucid. Please click [here](#Wireframe) to view Wireframes. 

 ## Surface ##

 This pertains to the visual design aspect and how to effectively convey the desired emotions and effects. For a more comprehensive understanding of planning for the surface plane please see below.

**Colour Scheme**

A white background (#FFF) for all pages and posts was chosen throughout the site. A white background allows the images to standout which is the intention here. 

The colour (#d62b70) was used for most other areas of the site as this colour is the main colour used in the logo and using this colour throughout helps tie the design of the site in together. 

![](images/colour_displayed_in_readme.png)

**Fonts**

The Google Font *Frank Ruhl Libre* was used for most of the headings and Serif as a backup font.

**Images and Logos/Icons**

The custom logo was used using the Logo Generator Looka. The post imagery will be determined by whatever image the post creator decides to publish. A default image will be put in place should the user not upload an image. The social icons and comment/like icons are taken from Font Awesome.

## Features ##

**Navigation**

 * Navigation bar with logo and links
 * Different links visible for authenticated and unauthenticated users
 * Links change from Grey to pink when you hover over them
 * Responsive menu which collapes into a burger on small to medium screens
 * Brief description on the far right, explaining what the site is about

![](/images/navigation.png)

**Landing Page**

 * The landing page itself will immediately display the most recent 6 posts.
 * The landing pagge will display both the headers and footer with easily identifiable links to help the user navigate throughout the site
 * Pagination has been implemented on the site so the user can scroll to the next set of posts using the "next" link
 * When a user is logged in the home page will display different links as seen in the images below

**Create Post View For Non Logged In Users**

 * Recipe title and image viewable at the top of the post view page
 * Author's name and publish date viewable under title and image
 * Recipe content  
 * Number of likes and comments ( Non logged in users cannot contribute to this)
 * User can view approved comments

![](/images/create_post.png)

**Post View For Logged In Users**

 * Recipe title and image viewable at the top of the post view page
 * Author's name and publish date viewable under title and image
 * Recipe content
 * Number of likes and comments, user can click on the heart to add a like
 * Option to edit/remove a post if the user created that post. When clicking delete the user is prompted with the message *Are you sure you want to delete the following recipe?* which helps prevent users mistakenly deleting posts.
 * Option to submit a comment and view other comments. Text must be added or else the comment will not submit.

![](/images/post-view.png)

**Contact US**

 * This is a simple form which allows the user contact the site admins directly. The form will not submit unless all fields are filled out. The email field requires a valid email.

![](/images/contact-us.png)

**Register/Sign UP**

 * Allows user to create account
 * Fields include Username, Email (optional), Password and Password confirmation
 * Has an embedded link which takes the user back to the login page should they need to

![](/images/sign-up.png)

**Login**

 * Login form asking for username and password of signed up user
 * Includes "Remember me" checkbox option
 * Has an embedded link which takes the user back to the register page should they need to

![](/images/sign-in.png)

**Logout (For Authenticated Users Only)**

 * Separate page prompts user to confirm action to sign out

![](/images/sign-out.png)

**Create Post (For Authenticated Users Only)**

 * Allows a user to create a post
 * Has a title , slug , and a body field. All fields must be filled out for the post to create. The body field allows users to format and style their text and also allows them to add images which will display in the body of the post only
 * User can submit an image aswell which will display as the main image for the post. If no image is selected a default place holder will be used

![](/images/create-post-view.png)

**Edit Recipe (For Authenticated Users Only)**

 * Pre-populates all post content
 * User can update any field and change image
 * All fields are required and submission will not succeed unless form is completed

![](/images/edit-post.png)

**Delete Recipes (For Authenticated Users Only)**

 * Renders seperate page that prompts user to confirm action to delete recipe
 * Refuses access to delete if recipe was not posted by the user

![](/images/delete-post.png)

![](/images/custom-403.png)

## Oppurtunities For Future Features ##

Features I would have like to add but could not due to various contraints

 * Allow users create profiles so they can add extra features such as create drafts
 * Add catergories and a search bar
 * Links which allows users easily share various posts on their social media


## Database Models ##

## Database Flowchart ##

![](/images/erd.png)

I used Lucid to design the Database models. 

![](images/database_models.png)

The Post & Content models are based on the Django tutorial walkthrough project by Code Institute. The project required one custom model (the contact model) . This model was designed for the contact form. 

## CRUD ##

The project's design process was centered around the CRUD principle, which stands for Create, Read, Update, and Delete.

 * Create: An authenticated user can create and save a post entry.
 * Read: A user can browse and read their own and other users' post entries.
 * Update: An authenticated user can edit and update their own saved entries.
 * Delete: An authenticated user can delete their own saved entries.

## Technologies Used ##

**Main Languages Used**

 * HTML5
 * CSS3
 * Python

**Hosting and Work**

 * Lucid (Wireframe and DB model Diagrams)
 * GitHub (Version Control)
 * GitPod (IDE)
 * Heroku (Hosting site)
 * Cloudinary (Static Files)

**Python Libraries**

 * PyJWT (Python library that provides a way to encode and decode JSON Web Tokens (JWTs). JWT is a compact, URL-safe means of representing claims to be transferred between two parties. It can be used for authentication and authorization purposes in web applications )
 * Gunicorn (Python HTTP server for WSGI applications)
 * pyscopg2 (PostgreSQL Database adapter)

 **Django Libraries**

 * django-allauth (User authentication)
 * django-crispy-forms (Control rendering behaviour of Django forms)
 * Summernote (Summernote is a free and open-source WYSIWYG (What You See Is What You Get) text editor for web pages. It provides an easy-to-use interface for editing and formatting text, allowing users to create and publish rich content without having to write HTML code manually)
 * django-bootstrap4 (A third-party package for Django web framework that provides integration with the popular front-end framework Bootstrap 4. It allows developers to easily use Bootstrap's styling and components in their Django templates, without having to write the HTML and CSS code manually)
 * whitenoise ( Helps with static files on Heroku)

**Database**

 * ElephantSQL (PostgreSQL database hosting)

 ## Testing ##

 ## User Stories ##

  * As a First time user I want to be able to easily identify what the app is for
    * Result Passed - Logo , additional Nav text and rendered posts make this clear

  * As a User I can view posts so that I can click on one to read
    * Result Passed - You can view each and its title when visiting the site

  * As a User I can click on a post so that I can read the full post
    * Result Passed - Clicking on any post title allows you read full post

  * As a User / Admin I can view the amount of upvotes/likes so that I can see which posts are most popular
    *  Result Passed - Users can easily view the amount of likes located under each post   

  * As a User / Admin I can view comments on an individual post so that I can read what's been said
    * Result Passed - When clicking on a post a user can view all approved comments

  * As a User I can comment on a post so that I can get involved
    * Result Passed - All logged in users can leave comments which display one approved 

  * As a user I can like any post so that I can share my approval
    * Result Passed - Logged in users can like posts

  * As a Site Admin I can Approve/Disapprove Comments so that I can filter out objectionable comments
    * Result Passed - Admins can approve/disapprove comments 

  * As a Site User I can look through a paginated list of recipes so that I can select a recipe that looks good to make.
    *  Result Passed - Once a page has reached 6 posts a new page will be created which can be navigated to.  

  * As a Site Admin I can create, read, update and delete post so that I can manage my content
    * Result Passed -  Registered users are able to create, read , edit and delete all posts

  * As a Site User I can sign In and out my account so that I can protect my account when I am not using it
    * Result Passed - The login link allows a user to sign in 

  * As a user I can create an account so that I can manage all my posts
    * Result Passed - The Register Link allows users create an account so rthey can create a post and also edit and delete it

## Manual Testing ##

  * All Nav bar links redirect you to correct page
  * All footer links redirect you to correct page
  * All post titles redirect you to the recipe post
  * The logout and create post links only show for logged in users
  * The register and login links only show for logged out users
  * The contact forms will not send unless all info is entered, will insist on a valid email and admins can view all contact form submissions.
  * The edit and delete buttons only show on a post for logged in users and both work. 
  * Only the post creator can delete and edit their own submissions
  * Users who try and edit/delete posts they did not create get a custom 403
  * When users try and delete a post they are prompted with a screen to ensure they want to do it
  * If a user does not submit an image when creating a post the placeholder image loads as expected
  * The login and logout buttons work as expected
  * Creating a new user works when selecting the register link
  * Only logged in users can comment and the comment submission form only loads for logged in users
  * The home page and all inner pages are responsive for all screen types.


**Lighthouse**

![](/images/lighthouse.png)

**Validators**

**HTML**

[Home Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Frecipesforu.herokuapp.com%2F) **Passed**

[Login](https://validator.w3.org/nu/?doc=https%3A%2F%2Frecipesforu.herokuapp.com%2Faccounts%2Flogin%2F) **Passed**

[Logout](https://validator.w3.org/nu/?doc=https%3A%2F%2Frecipesforu.herokuapp.com%2Faccounts%2Flogout%2F) **Passed**

[Register](https://recipesforu.herokuapp.com/accounts/signup/) **Passed**

[Contact US](https://validator.w3.org/nu/?doc=https%3A%2F%2Frecipesforu.herokuapp.com%2Fcontact%2F) **Passed**

**CSS**

[Home Page](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Frecipesforu.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) **Passed**

[Login](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Frecipesforu.herokuapp.com%2Faccounts%2Flogin%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) **Passed**

[Logout](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Frecipesforu.herokuapp.com%2Faccounts%2Flogout%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) **Passed**

[Register](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Frecipesforu.herokuapp.com%2Faccounts%2Fsignup%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) **Passed**

[Contact Us](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Frecipesforu.herokuapp.com%2Fcontact%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) **Passed**

Python files were tested using [this validator](https://pep8ci.herokuapp.com/)

    Blog - admin.py - All clear
    Blog - apps.py - All Clear
    Blog - forms.py - All clear
    Blog - models.py - All clear
    Recipes4u - urls.py - All clear
    Blog - views.py - All Clear
    Recipes - settings.py - All clear except for 4 lines which are too long and I could not shorten
    Blog - urls.py - All clear

**Browser Testing**

Site renders correctly on Chrome, Firefox and Safari


 ## Deployment ##

 This project was deployed using Heroku, Cloudinary, ElephantSQL

 The following steps describe the required libraries to ensure successful deployment on Heroku.

 * Install Gunicorn (server used to run Django on Heroku): pip3 install django gunicorn
 * Install pyscopg2 (connects to PostgreSQL): pip 3 install dj_database_url pyscopg2
 * Install Cloudinary (host static files and images): pip3 install dj3-cloudinary-storage

**Creating the Heroku App**

 * Log into Heroku and go to the Dashboard
 * Click New and select Create new app from the drop-down
 * Name app appropriately and choose relevant region, then click Create App

**Create PostgreSQL database using ElephantSQL**

Creating a database accessible by Heroku is essential, as the database provided by Django cannot be accessed by a deployed Heroku app.


 * Log into ElephantSQL and go to Dashboard
 * Click Create New Instance
 * Set up a plan by providing a Name (project name) and select a Plan (for this project the free plan "Tiny Turtle" was chosen). Tags are optional.
 * Click Select Region and choose appropriate Data center
 * Click Review, check all details and click Create Instance
 * Return to Dashboard on click on the name of the newly created instance
 * Copy the database URL from the details section

**Update Settings**

 * Add the following code at the top of `settings.py` to connect Django project to env.py:

 ```
   import os
  import dj_database_url
  if os.path.isfile('env.py'):
      import env
 ```
 * Remove insecure secret key provide by Django in settings.py and refer to variable in env.py instead `(SECRET_KEY = os.environ.get('SECRET_KEY'))`
 * To connect to new database, replace provided DATABASE variable with

```
 DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```
* Save and migrate all changes made

**Connecting Heroku to Database**

* In Heroku dashboard, go to Settings tab
* Add three new config vars `DATABASE_URL (value is database URL)`, `SECRET_KEY (value is secret key string)` and `PORT (value "8000")`

**Connect to Cloudinary**

* In Cloudinary dashboard, copy API Environment variable
* In env.py file, add new variable `os.environ["CLOUDINARY_URL"] = "<copied_variable"` and remove `CLOUDINARY_URL=` from the variable string
* Add same variable value as new Heroku config var named `CLOUDINARY_URL`
* In settings.py, in `INSTALLED_APPS `list, above `django.contrib.staticfiles` add `cloudinary_storage`, below add cloudinary
* To define Cloudinary as static file storage add the following to settings.py

```
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```
**Allow Heroku as host**

 * In settings.py add

```
ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']
```

## Sources Credits ##

 * Used AI Logo Geneartor Looka to create Logo
 * The masthead and author banner code was taken from the walk through Django project 
 * Code for the custom 403 page was taken from W3Schools
 * Images taken from [](pexels.com)
 * Recipes were taken from various food sites