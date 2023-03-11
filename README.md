# Squigl
## Contents
## Introduction
Squigl is a Twitter clone, a social network built using the Django framework. Deployed to Gitpod.  

This is the fourth milestone project required to complete my Diploma in Full Stack Software Development at The Code Institute. I was required to build a Full-Stack site based on business logic used to control a centrally-owned dataset. With an authentication mechanism that provides role-based access to the site's data. This was achieved using HTML, CSS, JavaScript, Python and the Django framework paired with a relational database.  

The name comes from the use of ~ in front of usernames, used here in a similar fashion to @username tags on Twitter. The tilde symbol is on the same keyboard key as # (on a UK keyboard) so it was a natural pairing for me. Its appearance as a squiggly line inspired the project’s name.  

The idea behind Squigl was to create an alternative to Twitter. I started on this project during the beginning of the recent Elon Musk Twitter drama. Basing this project on a pre-existing website helped aid planning early on, establishing expected goals and requirements for end users.  

Squigl allows users to post short posts on their customizable profile pages. Follow other users, like, and comment on posts. Send private messages to each other. Be notified when they are mentioned. See popular trending topics or search for users and posts by a phrase keyword.
## Project Planning
### GitHub Project
The GitHub project board feature was used to keep track of what I was working on and what still needed to be done. I created a user story for each feature and moved them when necessary throughout the development of the site. 

SCREENSHOT OF GITHUB PROJECT PAGE
### Database Schema
The models required for this project are:

 - **Post** - for user posts.
 - **Reply** - for replies to the posts.
 - **Message** - for private messaging between users
 - **CustomUser** - my custom user model which includes additional fields for a user to customise their profile.
 
 SCREENSHOT OF ERD
 ### User Stories
There will be three types of users visiting Squigl. A **new** or **logged out user**, a **registered user**, and **moderators**. User stories were logged as issues on GitHub to track them throughout the project - [Project Issues](https://github.com/paulio11/project-4/issues?q=is:issue%20is:closed%20sort:created-asc). They were subject to manual testing at the end of the project to determine if I was successful with my objectives.
#### New or Logged Out Users
| User Story |  |
|--|--|
|As a new user I can **sign up** so that I can have my own account and use the full feature set of the website|✓|
|As a logged out user I can **sign in** so that I can return to my account|✓|
|As a logged out user I can **search squigl** so that I can find users, posts and replies that I am looking for|✓|
#### Returning Users
| User Story |  |
|--|--|
|As a user I can **log out** so that my account remains secure and private when not in use|✓|
|As a user I can **view my feed** so that I can see my own posts and posts of users I follow|✓|
|As a user I can **search squigl** so that I can find users, posts and replies that I am looking for|✓|
|As a user I can **upload an avatar** so that it can represent me as a user|✓|
|As a user I can **add a link to my profile** so that I can share something important to me or another website relevant to my account|✓|
|As a user I can **add a short description to my profile** so that other users can find out more about me|✓|
|As a user I **can add an image as a background to my profile** so that I can further customise my profile|✓|
|As a user I can **follow or unfollow other users** so that their posts appear in my feed|✓|
|As a user I can **create a new post** so that I can share something with my followers|✓|
|As a user I can **add an image to my post** so that I can share an image with my followers|✓|
|As a user I can **add a link to a website to my post** so that I can share a website with my followers|✓|
|As a user I can **like my own or someone else's post** so that I can show my support|✓|
|As a user I can **delete my own posts** so that I can remove them from my profile if necessary|✓|
|As a user I can **edit my posts** so that I can change them if necessary|✓|
|As a user I can **add a reply to my own posts or someone else's** so that I can start or add to a conversation related to the post|✓|
|As a user I can **edit my replies** so that I can change what I said or fix a mistake|✓|
|As a user I can **delete my replies** so that I can remove them if I want|✓|
|As a user I can **hide a reply to my post** so that it can be hidden from other users if inappropriate or irrelevant|✓|
|As a user I can **repost another user's post** so that I can share it with my own followers|✓|
|As a user I can **tag other users in my posts, replies and messages** so that I can link directly to their profile|✓|
|As a user I can **create a hashtag in my posts and replies** so that I can be part of a larger conversation and contribute to trending topics|✓|
|As a user I can **send a private message to another user** so that we can have a private conversation|✓|
|As a user I can **have a message inbox** so that I can read my private messages|✓|
|As a user I can **reply to my private messages** so that I can quickly respond to the sender and keep a conversation going|✓|
|As a user I can **delete a message** so that I keep my inbox clear and/or remove no longer useful messages|✓|
|As a user I can **report a post, message or reply** so that moderators are notified of inappropriate content|✓|
|As a user I can **see trending hashtags** so that I am aware of current popular topics of conversation|✓|
|As a user I can **delete my account** so that I can leave the website and remove all my content|✓|
|As a user I can **change my password** so that my account can remain secure|✓|
|As a user I cant **reset my password** so that I can still log in if I have forgotten my password|✓|
#### Moderators
| User Story |  |
|--|--|
|As a moderator I can **see reported items** so that I can act upon them|✓|
|As a moderator I can **delete or mark okay a reported item** so that it can either be deleted or removed from the reported items list where appropriate|✓|
|As a moderator I can **message users** so that we can talk to them with clearly labelled official messages|✓|
|As a moderator I can **see a list of users with strikes** so that troublesome users are clearly viewable and action can be take if necessary|✓|
|As a moderator I can **ban or unban a user** so that they can be banned or unbanned if necessary|✓|
## User Experience
### Wireframes
[Balsamiq for Desktop](https://balsamiq.com/wireframes/) was used ahead of development to plan the basic skeleton of all pages. You can download my wireframes file LINK.

SCREENSHOT OF WIREFRAMES
### Design Choices
#### Typography
Fonts are imported from [Google Fonts](https://fonts.google.com/). The font used for the website logo and some usernames is [Fredoka One](https://fonts.google.com/specimen/Fredoka+One). To keep visual clutter to a minimum only two fonts are used. Fredoka One for elements that are important to the current page, and for the rest of the content the default bootstrap font is used. Simply increasing the font-weight creates enough contrast between titles and body text.

SCREENSHOT OF LOGO
#### Images
The only images used on the website are those **added by users**. These include profile backgrounds, user avatars and images shared in posts. This keeps the focus where it should be - on the user generated content. A placeholder image is used in cases where a user has not yet uploaded an avatar.

SCREENSHOT OF PLACEHOLDER AVATAR
#### Colour Scheme
Squigl uses a restrained colour-scheme. The design focuses mainly on off black text on a white background. The main content column is highlighted by a grey gradient background to draw user's eyes to the middle of the page. Colour mostly comes from the content added by users. 

The colours used in the site logo represent two of the main pillars of squigl - users and trending topics. The letter "i" coloured goldenrod represents the users, as the "i" looks like a person and the colour is also used for the *verified tick* next to usernames. The indigo ~ is the same colour used for hashtags.

SCREENSHOT OF COLOUR PALETTE
#### Layout
In desktop view the website is structured into three columns. The first being for navigation, the centre for the main content, and the right sidebar is for extra content. The centre column is the largest to highlight it's importance and draw the eye.

For smaller screens such as mobile the navigation shrinks and the right side bar hides - keeping focus on the centre column.

SCREENSHOT OF DESKTOP
SCREENSHOT OF SMALLER DESKTOP
SCREENSHOT OF TABLE
SCREENSHOT OF MOBILE
## Features
### Site-wide features
#### Header
SCREENSHOT OF HEADER
#### Navigation
SCREENSHOT OF ALL NAV MENUS
#### Centre Column
#### Sidebar
SCREENSHOT OF SIDEBAR
#### User Tagging
SCREENSHOT OF TAGGED USER
#### Hashtags
SCREENSHOT OF HASHTAGS IN A POST
### Specific pages
#### Login
SCREENSHOT OF LOGiN
#### Signup
SCREENSHOT OF SIGNUP
#### Feed
SCREENSHOT OF FEED
#### Search
SCREENSHOT OF SEARCH
#### User Page
SCREENSHOT OF USER PAGE
#### New Post
SCREENSHOT OF NEW POST FORM
#### Post Page
SCREENSHOT OF POST PAGE
#### Mentions
SCREENSHOT OF MENTIONS
#### Messages
SCREENSHOTS OF MESSAGES
#### Moderation
SCREENSHOTS OF MOD PAGE
## Technologies
### Languages
### Frameworks
### Python Libraries
### Software
## Testing
## Deployment
## Credits
### Code
### Text
### Images
### Acknowledgements
