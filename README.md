# Bullet it


## Multipage CRUD Application

This website is designed as to provide users with a bullet journal inspired CRUD application for organising and tracking all aspects of their daily lives.

The main purpose of this site is to enable the user to easily record and store notes, tasks and events occurring in their daily lives in an organised way. The application design makes use of terms native to the Bullet Journaling process such as "Collections" which would be a term akin to categories in todo applications and "Future Log" - here a user can view what tasks or events are/have occurred on a 12 monthly basis. 

The application also gives a nod to the popular bullet journaling process by allowing users to tag list items with convenient bullet/icons which can be recognised at a glance once familiarity is obtained. The user can reach a handy key for these (stored on the "Index" page) from all pages of the application.  

All in all a very useful application inspired by the immensely popular act of bullet journaling. This application could be the perfect companion for an organised life!

## Live Demo

Follow this link to view deployed version of this website https://data-centric-nikral-bullet-it.herokuapp.com/


## UX

#### 1. Initial Planning 

The planning commenced with pen and paper brainstorming and some competitor analysis. Here ideas for a twist on a regular todo app were considered. Bullet journaling is a widely used and fast trending practice of using a notebook to organise and track all aspects of a busy life. I viewed many videos along with a Ted talk by the founder of this concept and decided to explore this as a theme for my data centric project. Competitor analysis was then carried out on some todo list applications for mobile and desktop. Other mobile and desktop application interfaces were also reviewed using resources such as Pinterest and Dribble for guidance on usability. One of the challenges of this development was to create an application with good functionality while also fitting this into a simple interface which is easy to use and respponsive for using on mobile devices. 

#### 2. User Stories

From here I decided to complete some user stories before commencing wireframing. This helped me to think through the user journey and design a good site map and navigation path. 

The following is a list of some user stories:

 - As a user of a planner application, I need to be able to login/sign up quickly when I land on the site's homepage, this will ensure that I see the content is relevant to me.
 - As a user seeking an application to store to do lists, I want to be have quick access to view my lists and also add items quickly on the go, this will help me not to forget anything and ensure that everything that I think of is recorded.
 - As a user seeking to store items on the go, I would like to be able to adjust details of these list items with ease so that information is accurate and up to date.
 - As a user looking to schedule events and tasks, I would like to be able to view all items together in one place in the context of a calendar, this will help me visualise my time. 
 - As a user simply wanting to store a note, I require a way of marking an item as a note so that I know that it is simply that and not an event or task.
 - As a user who wants to defer a task to the following months, I would like a way of doing this easily when looking at my calendar, so that nothing gets left behind.
 - As a user of an organisation application, I would like to be able to easily and clearly mark tasks or events as done in order to visualise my progress.

#### 3. Wireframes

After the initial planning stage, I developed these wireframes using [Balsamiq](https://www.balsamiq.com "Balsamiq Homepage"). At this point I fine tuned down my features and layout. There were some cosmetic adjustments during the development process but on a whole the original mockups were followed quite closely. All wireframes have been included in a file labelled [wireframes](wireframes/) for project review.

#### 4. Database Schema Design

Using a MongoDB, a non-relational database required a lot of forward planning and mapping out of how I would go about designing my databse in a way that would work for my application model. As I planned on having multiple user functionality, thought needed to be given on how to best store this data. After mapping a few options out on paper, it was decided to go with a schema where each user was a "collection" in MongoDB terms and then each category of list groups was a "document" and so with a mongo assigned ID. Within this document I store a list of items belonging to the category in question. As I required each item to have various properties, one of the challenges was to generate and store an ID for each item created in order to allow manipulation and viewing of all data properties.
An illustration of the database schema design has been included in a file labelled [db schema design](db schema design/) for project review.

#### 5. Overall Look and Feel

As this is functional application where people want to clear their heads and organise their life, it needed a clean and simple interface. After some research I found the best option was to use Google's Materialize framework for some of the visual features. This provides the application with responsiveness and a clean flow when navigating around the site. I chose purple and white as my base colours for the site using variations of this throughout including a linear gradient at the top of each application page to create clean, stylish and readable headings. This colour provides a strong contrast to the white and gives a feeling of energy and warmth which are feelings which one would appreciate when organising their life. 

### Features

- This is a multipage application website built using Google's Materialize framework for responsive layout and navigation. 
- There is a simple homepage enlightening the user about Bullet Journaling and its origin. Here there is also a simple login/signup interface. Once logged in there is a clean navigation menu and path for users to follow to allow them to commence organising and tracking their lives. 
- The user can create, read, update, and delete all items and cartegories with ease.
- In addition to storing lists the user can add bullets/icons to denote firstly whether the item is a todo, event or just simply a note. 
- A due date, important tag and allocation to a calendar or in bullet journaling terms a "Future Log" month can also be set when adding a list item. 
- A user can then view all of his/her items on the "Future Log"/calendar and if they so wish, assign any items which were not previously assigned a month. 
- Finally, in the Future Log the user has the option of pushing an item forward to the next month if not complete/obsolete and also can mark items as done from this page. 

#### Future Development

- The login/sign up functionality may be developed in the future to include password authentication.
- There may also be scope to develop a "Monthly Log" where users can view a monthly calendar to view their tasks.

### Technologies Used

- HTML5 
- CSS3 - Along with using CSS for styling this was also used to create the linear gradient added to the tops of the application pages.
- [Materialize](https://materializecss.com/ "Materialize Homepage")  - used for responsive layout, clean navigation and list layout.
- JavaScript & [Jquery](https://jquery.com/Jquery "Jquery Homepage")  - Used for the typewriter effect on the desktop view for the homepage. Materialize also uses these for some of its navigation features e.g. accoridons and side navigation for mobile devices.
- Python 3 - a Python file named "app.py" renders the html templates for this CRUD application and builds a web server using Flask PyMongo to interact with MongoDB.
- [Flask Framework](http://flask.pocoo.org/ "Flask Homepage") - a Python micro-framework that was used to serve the data and render the HTML pages for this application.
- [MongoDB](https://www.mongodb.com/ "MongoDB Homepage") -NoSQL database that converts and presents data in JSON format.

## Testing & Deployment

### Testing

- Manual testing was carried out on this site. Some of the items found include:
  - All form fields were tested to see what what happen if left blank, in some cases this caused issues. To resolve this I put in a "required" tag against relevant fields.
  - The username at log in accepted both uppercase and lowercase which may lead to user confusion/duplication. I resolved this by forcing all usernames to be lowercase.
  - All aspects of CRUD functionality was tested to ensure that the correct database records were updated.
  - All links were tested to ensure that they functioned as expected
  - I tested to see if both the experience for a new user and a user with a lot of data performed as expected
  - I was originally storing some of the icons as their Unicode value, but discovered that this did not work as expected on Mac devices. I since updated the code to store strings in the database, which triggers display of font awesome icons instead.
-  The only issues arising from the CSS code assessment from the official [Jigsaw Validator](https://jigsaw.w3.org/css-validator/ "Jigsaw Validator Homepage") are those contained in the Materialize CSS file linked to my project which is out of my control.
- [Cross Browser Testing](https://crossbrowsertesting.com/ "Cross Browser Testing Homepage")  was used to ensure that the site has been tested for viewing support across the following browsers:
  - Google Chrome
  - Opera
  - Microsoft Edge
  - Internet Explorer 11
  - Mozilla Firefox
  - Safari
- Responsiveness has also been tested across multiple devices through the use of Google Dev Tools and also using the following resources:
  - [Responsinator](http://www.responsinator.com/ "Responsinator Homepage")
  - [Google Resizer](https://material.io/tools/resizer/ "Google Resizer Homepage")
  - [Mobile Test](http://mobiletest.me/ "Mobile test Homepage")
- Along with the emulator tests above, the site has been tested on my own phone along with other physical devices to ensure all looks and works as it should. 

#### Known Bugs

- It appears that Internet Explorer 11 does not support certain aspects of the Materialize framework used for some features of this application. This is something I intend to look at further in the future. However, after reasearching the user stats IE11 ranks relatively low.

### Deployment

The site has been deployed to be hosted on Heroku. (please see the live link above). The requirements.txt contains all of the dependencies required to run the app. The Procfile communicates to Heroku how to run the app. The server used for hosting the dataset is [mLab](https://mlab.com  "mLab Homepage") MongoDB. The environment variables obtained here are stored in Heroku config vars.

### Installation

If you wish to clone this project, follow the below instructions. In developing this project I used Cloud9. I recommend that this is used for cloning and the following instructions have been made with this in mind. If you are using a different editor you may need to look at its documentation for your terminal commands.

1. Please note that access keys for MongoDB are hidden and tied to my account, you will need to obtain your own connection. [mLab](https://mlab.com  "mLab Homepage") was used for this project.
2. If you wish to use the Cloud 9 code editor click here https://c9.io
3. Proceed to the folder which you want to store the cloned project and in your terminal & type: `$ git clone https://github.com/nikralave/data_centric_project_stream_three_bullet_it.git`
4. Install the project dependancies: `$ sudo pip3 install -r requirements.txt`
5. When done cut ties with my github: `$ git remote rm origin`


## Credits 

#### Media

I would like to acknowledge the following media source:

- The photo used on this homepage was obtained from the stock photo site such [Pexels](https://www.pexels.com/ "Pexels").



