## Recipes 4 U ##
<br>

This Django project is a reccipe sharing blog intended for food lovers where users can upload, comment and like other recipes. Users can also view recipes posted by other users which they can try. Like a regular blog only registered users can post, comment on or like other recipies . Registered users will also have the ability to edit or remove their previous posts. 

## Post responsive images here

Link to site.

## UI/UX ##

The overall desing is kept simple as users are encouraged to post images to go with their recipes . Research has shown that people eat with their eyes so to speak so distractions were kep to a minium.

The layout of the site is standard for a blog site with clear descriptive navigational links. 

The site features are standard and expected for a blog site. 

**Agile**

The agile approach was employed in designing and constructing this project, from the outset of planning to the completion of development. To facilitate the process, I established a GitHub project and adopted the Kanban board methodology to divide project components into user stories and feasible tasks.

For a comprehensive view of all user stories please refer to the linked project [Project Kanban Board](https://github.com/users/oconnorian3/projects/10) . Additionally, each story has been assigned a label that indicates its level of significance in the site's overall functionality and acceptance.

## Wireframe

Below are some basic Wireframes done up before the project started.

*When a user is NOT logged in*

![](static/images/wireframe_loggedout.png)

*When a user IS logged in*

![](static/images/wireframe_loggedin.png)

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
    * Register and establish their account
    * Create and upload their own recipes
    * Like and comment on recipes
    * Fill out a contact form

* The website must provide the admin with the ability to:
    * Approve comments    
    * Filter through recipes, comments, and users to manage the site effectively    

## Scope ##

This section outlines the functions and features included in the project scope. The project was designed with minimal functionality in mind, which means that most of the features included are basic requirements. For instance, user sign up and login functionality had to be implemented, along with basic CRUD operations for authenticated users. For a detailed explanation of all the existing features, please refer to the Existing Features **Add Link** section. The Future Features section discusses potential features that were deemed unnecessary at this point in time, despite being within the project's possible scope.

## Structure ##

 The site's layout is based on a simple blog design that is commonly used by many other blogs online. With this structure, users can easily access the site, browse receipes , leave a message and login/register so they can upload their own recipes and comment on other recipes.

 ## Skeleton ##

 Wireframes were made using Lucid. Plsease click [here](#Wireframe) to view Wireframes. 

 ## Surface ##

 This pertains to the visual design aspect and how to effectively convey the desired emotions and effects. For a more comprehensive understanding of planning for the surface plane please see below.

**Colour Scheme**

A white background (#FFF) for all pages and posts was chosen throughout the site. A white background allows the images to standout which is the intention here. 

The colour (#d62b70) was used for most (not all) other areas of the site as this colour is the main colour used in the logo and using this colour throughout helps tie the design of the site in together. 

![](static/images/colour_displayed_in_readme.png)

**Fonts**

Fill in later

**Images and Logos/Icons**

The custom logo was used using the Logo Generator Looka. The post imagery will be determined by whatever image the post creator decides to publish. A default image will be put in place should the user not upload an image. The social icons and comment/like icons are taken from Font Awesome.

## Features ##

**Navigation**

 * Navigation bar with logo and links
 * Different links visible for authenticated and unauthenticated users
 * Links change from **add colour** to **add colour** when you hover over them
 * Responsive menu which collapes into a burger on small to medium screens
 * Brief description on the far right, explaining what the site is about

**Add Imagery**

**Landing Page**

 * The landing page itself will immediately display the most recent ** posts.
 * The landing pagge will display both the headers and footer with easibly identifiable links to helo the user navigate throughout the site
 * Pagnation has been implekllented on the site so the user can scrool to the next set of posts using the "next" link
 * When a user is logged in the home page will display different links as seen in the images below

**Add Imagery**

**Post View For Non Logged In Users**

 * Recipe title and image viewble at the top of the post view page
 * Author's name and publish date viewable under title and image
 * Recipe content  
 * Number of likes and comments ( Non logged in users cannot contribute to this)
 * User can view approvded comments

**Add Imagery**

**Post View For Logged In Users**

 * Recipe title and image viewble at the top of the post view page
 * Author's name and publish date viewable under title and image
 * Recipe content
 * Number of likes and comments, user can click on the heart to add a like
 * Option to edit/remove a post if the user created that post. When clicking delete the user is prompted with the message *Are you sure you want to delete the following recipe?* which helps prevent users mistakinly deleteing posts.
 * Option to submit a comment and view other comments. Test must be added or else the comment will not submit.

**Add Imagery**

**Contact US**

 * This is a simple form which allows user contact the site admins directly. The form will not submit unless all fields are filled out. THer email field requires a valid email.

**Add Imagery**

**Register/Sign UP**

 * Allows user to create account
 * Fields include Username, Email (optional), Password and Password confirmation
 * Has an embeeded link which takes the user back to the login page should they need to

**Add Imagery**

**Login**

 * Login form asking for username and password of signed up user
 * Includes "Remember me" checkbox option
 * Has an embeeded link which takes the user back to the register page should they need to

**Add Imagery**

**Logout (For Authenticated Users Only)**

 * Seperate page prompts user to confirm action to sign out

**Add Imagery**

**Create Post (For Authenticated Users Only)**

 * Allows a user to create a post
 * Has a title , slug , and a body field. All fields must be filled out for the post to create. The body field allows users to format and style their text and also allows them to add images which will display in the body of the post only
 * User must select the author field and whether they just want a draft of the blog or actually publish it
 * User can submit an image aswell which will display as the main image for the post. If no image is selected a default place holder will be used
