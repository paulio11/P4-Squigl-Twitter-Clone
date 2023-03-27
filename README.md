# Squigl
[Link to live site](http://squigl.herokuapp.com/)

![Squigl on multiple devicies](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-hero.png)

## Contents 

1. [Introduction](#introduction)
2. [Project Planning](#project-planning)
    1. [Github Project](#github-project)
    2. [Database Schema](#database-schema)
    3. [Epics and User Stories](#epics-and-user-stories)
    4. [Timeboxing](#timeboxing)
3. [User Experience](#user-experience)
    1. [Wireframes](#wireframes)
    2. [Design Choices](#design-choices)
        1. [Typography](#typography)
        2. [Images](#images)
        3. [Colour Scheme](#colour-scheme)
        4. [Layout](#layout)
4. [Features](#features)
    1. [Site Wide Features](#site-wide-features)
    2. [Specific Pages](#specific-pages)
    3. [Unimplemented Features](#unimplemented-features)
5. [Bugs and Fixes](#bugs-and-fixes)
6. [Technologies](#technologies)
    1. [Main Languages Used](#main-languages-used)
    2. [Frameworks](#frameworks)
    3. [Libraries](#libraries)
    4. [Software and Other](#software-and-other)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Credits](#credits)
    1. [Code](#code)
    2. [Text](#text)
    3. [Images](#images-1)
    4. [Acknowledgements](#acknowledgements)

## Introduction
Squigl is a Twitter clone, a social network built using the Django framework. Deployed to Gitpod.  

This is the fourth milestone project required to complete my Diploma in Full Stack Software Development at [Code Institute](https://codeinstitute.net/). I was required to build a Full-Stack site based on business logic used to control a centrally-owned dataset. With an authentication mechanism that provides role-based access to the site's data. This was achieved using HTML, CSS, JavaScript, Python and the Django framework paired with a relational database.  

The name comes from the use of ~ in front of usernames, used here in a similar fashion to @username tags on Twitter. The tilde symbol is on the same keyboard key as # (on a UK keyboard) so it was a natural pairing for me. Its appearance as a squiggly line inspired the project’s name.  

The idea behind Squigl was to create an alternative to Twitter. I started on this project during the beginning of the recent Elon Musk Twitter drama. Basing this project on a pre-existing website helped aid planning early on, establishing expected goals and requirements for end users.  

Squigl allows users to post short posts on their customizable profile pages. Follow other users, like, and comment on posts. Send private messages to each other. Be notified when they are mentioned. See popular trending topics or search for users and posts by a phrase keyword.

[Back to top 🔺](#squigl)

## Project Planning

### GitHub Project
The GitHub project board feature was used to keep track of what I was working on and what still needed to be done. I created a user story for each feature and moved them when necessary throughout the development of the site.

![Github Project Board](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-project-board.png)

### Database Schema
The models required for this project are:

 - **Post** - for user posts.
 - **Reply** - for replies to the posts.
 - **Message** - for private messaging between users
 - **CustomUser** - my custom user model which includes additional fields for a user to customize their profile.
 
![Database Schema](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-schema.png)

#### CustomUser Model

| Name | Type | Details | Notes |
|--|--|--|--|
| id | Primary Key | unique |
| username | CharField | unique, max_length=20, validators=[alphanumeric] | Used by the user to login and for their url, therefor it has to be unique. Alphanumeric validator ensures that user tagging works as punctuation breaks the script. |
| email | EmailField | unique | Used when a user attempts to reset their password. |
| name | CharField | max_length=30 | Included a max length so it doesn't break the size of html elements. |
| avatar | ResizedImageField | blank=True, upload_to='avatars/', size=[150, 150], crop=['middle', 'center'], force_format='WEBP' | The user's avatar is displayed as a small square. Cropped and resized to keep the file size low and the aspect ratio correct. |
| profile_background | ResizedImageField | blank=True, upload_to='backgrounds/', size=[600, 200], crop=['middle', 'center'], force_format='WEBP' | Cropped and resized to keep the file size low and the aspect ratio correct. |
| about | CharField | max_length=200, blank=true | Text to display on a user's profile. |
| website | CharField | max_length=50, blank=true | A website link to display on a user's profile. |
| verified | BooleanField | default=False | Text to display on a user's profile. |
| following | ManyToManyField | to self (CustomUser), blank=true | A list of followed users. |
| strikes | IntegerField | default=0 | Number of strikes gained, for moderation. |

#### Post Model

| Name | Type | Details | Notes |
|--|--|--|--|
| id | Primary Key | unique |
| user | Foreign Key | to CustomUser | The author of the post. |
| date | DateTimeField | auto_now_add=True | Date of post, automatically added on creation. |
| post | TextField | max_length=400 | Text content of the post. |
| image | ResizedImageField | blank=True, upload_to='post-images/', size=[600, None], force_format='WEBP' | Optional image for post. Cropped to a width of 600px and converted to WEBP. |
| link | CharField | max_length=50, blank=True | Optional website link. |
| likes | ManyToManyField | to CustomUser, blank=True | A list of users that liked the post. |
| repost_post | ForeignKey | to self (Post), blank=True | If this post is a repost this is the original post. |
| reported | ManyToManyField | to CustomUser, blank=True | A list of user that have reported the post (for moderation). |
| read | ManyToManyField | to CustomUser, blank=True | A list of users that have marked the post read (for mentions). |

#### Reply Model

| Name | Type | Details | Notes |
|--|--|--|--|
| id | Primary Key | unique |
| user | Foreign Key | to CustomUser | The author of the reply. |
| post | Foreign Key | to Post | The parent post of the reply. |
| date | DateTimeField | auto_now_add=True | Date of reply, automatically added on creation. |
| reply | TextField | max_length=400 | Text content of the reply. |
| hidden | BooleanField | default=False | The author of the parent post can hide inappropriate  replies. |
| reported | ManyToManyField | to CustomUser, blank=True | A list of user that have reported the reply (for moderation).|
| read | ManyToManyField | to CustomUser, blank=True | A list of users that have marked the reply read (for mentions). |

#### Message Model

| Name | Type | Details | Notes |
|--|--|--|--|
| id | Primary Key | unique |
| sender | Foreign Key| to CustomUser | The user sending the message. |
| recipient | Foreign Key | to CustomUser | The user receiving the message. |
| date | DateTimeField | auto_now_add=True | Date of message, automatically added on creation. |
| message | TextField | max_length=400 | Text content of the message. |
| sender_del | BooleanField | default=False | True if the sender has deleted the message. |
| recipient_del | BooleanField | default=False | True if the recipient  has deleted the message. |
| read | BooleanField | default=False | A user can mark a message as read, to remove it from unread messages. |
| reported | BooleanField | default=False | A user can report a message (for moderation). |

 ### Epics and User Stories
There will be three types of users visiting Squigl. A **new** or **logged out user**, a **registered user**, and **moderators**. User stories were logged as issues on GitHub to track them throughout the project - [Project Issues](https://github.com/paulio11/project-4/issues?q=is:issue%20is:closed%20sort:created-asc). They were subject to manual testing at the end of the project to determine if I was successful with my objectives.

#### Epic - New or Logged Out Users
| User Story | Achieved? |
|--|--|
|As a new user I can **sign up** so that I can have my own account and use the full feature set of the website|✓|
|As a logged out user I can **sign in** so that I can return to my account|✓|
|As a logged out user I can **search squigl** so that I can find users, posts and replies that I am looking for|✓|

#### Epic - A registered user can view a feed of posts from followed users

| User Story | Achieved? |
|--|--|
|As a user I can **view my feed** so that I can see my own posts and posts of users I follow|✓|
|As a user I can **follow or unfollow other users** so that their posts appear in my feed|✓|

#### Epic - A registered user can customize their profile

| User Story | Achieved? |
|--|--|
|As a user I can **upload an avatar** so that it can represent me as a user|✓|
|As a user I can **add a link to my profile** so that I can share something important to me or another website relevant to my account|✓|
|As a user I can **add a short description to my profile** so that other users can find out more about me|✓|
|As a user I can **add an image as a background to my profile** so that I can further customize my profile|✓|

#### Epic - A registered user can create new posts and manage their posts

| User Story | Achieved? |
|--|--|
|As a user I can **create a new post** so that I can share something with my followers|✓|
|As a user I can **add an image to my post** so that I can share an image with my followers|✓|
|As a user I can **add a link to a website to my post** so that I can share a website with my followers|✓|
|As a user I can **like my own or someone else's post** so that I can show my support|✓|
|As a user I can **delete my own posts** so that I can remove them from my profile if necessary|✓|
|As a user I can **edit my posts** so that I can change them if necessary|✓|

#### Epic - A registered user can reply to posts and manage their replies
| User Story | Achieved? |
|--|--|
|As a user I can **add a reply to my own posts or someone else's** so that I can start or add to a conversation related to the post|✓|
|As a user I can **edit my replies** so that I can change what I said or fix a mistake|✓|
|As a user I can **delete my replies** so that I can remove them if I want|✓|
|As a user I can **hide a reply to my post** so that it can be hidden from other users if inappropriate or irrelevant|✓|

#### Epic - A registered user can privately message other registered users
| User Story | Achieved? |
|--|--|
|As a user I can **send a private message to another user** so that we can have a private conversation|✓|
|As a user I can **have a message inbox** so that I can read my private messages|✓|
|As a user I can **reply to my private messages** so that I can quickly respond to the sender and keep a conversation going|✓|
|As a user I can **delete a message** so that I keep my inbox clear and/or remove no longer useful messages|✓|

#### Epic - A registered user can report inappropriate content
| User Story | Achieved? |
|--|--|
|As a user I can **report a post** so that moderators are notified of inappropriate content|✓|
|As a user I can **report a reply** so that moderators are notified of inappropriate content|✓|
|As a user I can **report a message** so that moderators are notified of inappropriate content|✓|

#### Epic - A registered user can keep their account secure
| User Story | Achieved? |
|--|--|
|As a user I can **log out** so that my account remains secure and private when not in use|✓|
|As a user I can **delete my account** so that I can leave the website and remove all my content|✓|
|As a user I can **change my password** so that my account can remain secure|✓|
|As a user I can **reset my password** so that I can still log in if I have forgotten my password|✓|

#### Epic - A registered user be part of a conversation
| User Story | Achieved? |
|--|--|
|As a user I can **search squigl** so that I can find users, posts and replies that I am looking for|✓|
|As a user I can **repost another user's post** so that I can share it with my own followers|✓|
|As a user I can **create a hashtag in my posts and replies** so that I can be part of a larger conversation and contribute to trending topics|✓|
|As a user I can **tag other users in my posts, replies and messages** so that I can link directly to their profile|✓|
|As a user I can **see trending hashtags** so that I am aware of current popular topics of conversation|✓|

#### Epic - Moderation
| User Story | Achieved? |
|--|--|
|As a moderator I can **see reported items** so that I can act upon them|✓|
|As a moderator I can **delete or mark okay a reported item** so that it can either be deleted or removed from the reported items list where appropriate|✓|
|As a moderator I can **message users** so that we can talk to them with clearly labeled official messages|✓|
|As a moderator I can **see a list of users with strikes** so that troublesome users are clearly viewable and action can be take if necessary|✓|
|As a moderator I can **ban or unban a user** so that they can be banned or unbanned if necessary|✓|

### Timeboxing

Using MoSCoW prioritisation I categorised the features needed to meet the requirements of the user stories into the following categories:

#### Must Do

The final version of Squigl must be able to do the following:
- User signup
- User login
- Make new posts
- View posts
- Edit posts
- Delete posts

This would produce the **minimal viable product**.

#### Should Do

A more fully featured product would contain these features:
- Search
- Replying to posts
- Reading replies
- Editing replies
- Deleting replies
- Post liking
- Follow and unfollow users
- User settings

#### Could Do

And if there is extra time before then end these features could be included:
- User profile customisation
- User to user private messaging
- Notifications

An early version of Squigl would contain the following - every **must do** feature, from **should do**: post replying, user following, and from **could do:** user profile customisation (time permitting). Futher features can be added in later versions.

Fortunately due to the length of this project I was able to produce every feature.

[Back to top 🔺](#squigl)

## User Experience

### Wireframes

[Balsamiq for Desktop](https://balsamiq.com/wireframes/) was used ahead of development to plan the basic skeleton of all pages. You can download my wireframes file [here](https://github.com/paulio11/project-4/blob/main/documentation/squigl-wireframes.bmpr).

<details>
    <summary><strong>Feed page wireframe</strong></summary>
    <img src="https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/wf-feed.png">
</details>

<details>
    <summary><strong>Post page wireframe</strong></summary>
    <img src="https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/wf-post.png">
</details>

<details>
    <summary><strong>New post form wireframe</strong></summary>
    <img src="https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/wf-newpost.png">
</details>

<details>
    <summary><strong>User page wireframe</strong></summary>
    <img src="https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/wf-user.png">
</details>

<details>
    <summary><strong>Search page wireframe</strong></summary>
    <img src="https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/wf-search.png">
</details>

<details>
    <summary><strong>Mobile wireframe</strong></summary>
    <img src="https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/wf-mobile.png">
</details>

### Design Choices

#### Typography

Fonts are imported from [Google Fonts](https://fonts.google.com/). The font used for the website logo and some usernames is [Fredoka One](https://fonts.google.com/specimen/Fredoka+One). To keep visual clutter to a minimum only two fonts are used. Fredoka One for elements that are important to the current page, and for the rest of the content the default bootstrap font is used. Simply increasing the font-weight creates enough contrast between titles and body text.

![Squigl logo](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-logo.png)

#### Images

The only images used on the website are those **added by users**. These include profile backgrounds, user avatars and images shared in posts. This keeps the focus where it should be - on the user generated content. A placeholder image is used in cases where a user has not yet uploaded an avatar.

![Placeholder avatar](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-avatar.png)

#### Colour Scheme

Squigl uses a restrained colour-scheme. The design focuses mainly on off black text on a white background. The main content column is highlighted by a grey gradient background to draw user's eyes to the middle of the page. Colour mostly comes from the content added by users. 

The colours used in the site logo represent two of the main pillars of squigl - users and trending topics. The letter "i" coloured goldenrod represents the users, as the "i" looks like a person and the colour is also used for the *verified tick* next to usernames. The indigo ~ is the same colour used for hashtags.

![Colour palette](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-colours.png)

#### Layout

In desktop view the website is structured into three columns. The first being for navigation, the centre for the main content, and the right sidebar is for extra content. The centre column is the largest to highlight it's importance and draw the eye.

For smaller screens such as mobile the navigation shrinks and the right side bar hides - keeping focus on the centre column. The menu will include links to the Trending Hashtags and the Who To Follow pages when the right sidebar is hidden due to screen size.

<details>
    <summary><strong>Desktop layout</strong></summary>
    <img src="https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-desktop.png">
</details>

<details>
    <summary><strong>Small desktop layout</strong></summary>
    <img src="https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-desktop-small.png">
</details>

<details>
    <summary><strong>Tablet layout</strong></summary>
    <img src="https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-tablet.png">
</details>

<details>
    <summary><strong>Mobile layout</strong></summary>
    <img src="https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-mobile.png">
</details>

[Back to top 🔺](#squigl)

## Features

### Site-wide features

#### Header

- The header featured on every page is made of three parts. The site logo, a search box, and the logged in user's info. 
- The logo returns a logged in user to their feed.
- Having search in the header encourages users to explore squigl. 
- The user info links the user to their page and helps show that the user is signed in.

![Header](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-header.png)

#### Navigation

- The user will navigate to all the main pages of the site using the menu in the left sidebar. Depending on the status of the current user this menu changes. 
- A logged out or new user will see the options to login and sign up. 
- A logged in user will see the full list of menu options. 
- A moderator will see two further options, one for the Django admin and another for the moderation tools.
- Labels are removed from the menu at lower screen widths, on mobile this is then replaced with an expandable hamburger menu.
- If the logged in user has any unread mentions or messages the relevant menu link is highlighted and includes a count.

<details>
    <summary><strong>Logged out navigation</strong></summary>
    <img src="https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-loggedout-nav.png">
</details>

<details>
    <summary><strong>Full desktop navigation</strong></summary>
    <img src="https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-fullnav.png">
</details>

<details>
    <summary><strong>Portrait tablet navigation</strong></summary>
    <img src="https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-tablet-nav.png">
</details>

<details>
    <summary><strong>Expanded mobile navigation</strong></summary>
    <img src="https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-mobile-nav.png">
</details>

#### Scroll To Top Button

- A back to top button appears when scrolling below the header to further assist navigation. 
- The JavaScript code that makes this work can be found in [this file](https://github.com/paulio11/project-4/blob/main/static/js/script.js).

#### Centre Column

- The centre column houses the main content on every page, and is the only column to remain visible at every screen size.

#### Sidebar

- On the majority of pages the sidebar will show a list of recent trending hashtags and a random list of unfollowed users.
- On the post page the user will find the reply form here.

#### User Tagging

- User's can mention/tag other users in their posts, replies and messages by using ~ in front of their username.
- This functionality is made possible using JavaScript, the code that makes this work can be found in [templates/base.html](https://github.com/paulio11/project-4/blob/main/templates/base.html).
- This code is included in the html file because it requires django template tags to function. 

#### Hashtags

- Users can include hashtags in their posts and replies by using # in front of the desired keyword.
- This functionality is made possible using JavaScript, the code that makes this work can be found in [templates/base.html](https://github.com/paulio11/project-4/blob/main/templates/base.html).
- This code is included in the html file because it requires django template tags to function. 

**Example of a post with a tagged user and hashtags:**

![A post containing user tags and hashtags](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-hash-tag.png)

#### Trending Hashtags

- JavaScript looks for a hidden `<div>` containing the last 100 posts that include `#` or in other words, a hashtag.
- The hashtag form inner html is extracted, the number of occurrences are counted, then sorted by value.
- Finally keys from this created JavaScript object are appended into the page html.
- The code that makes this work can be found in [this file](https://github.com/paulio11/project-4/blob/main/static/js/script.js).

![Trending Hashtags](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-trending.png)

#### Modals
Modals are used where it's possible to make permanent irreversible changes. Giving the user a chance to reconsider.
- Deleting a post
- Deleting a reply
- Deleting a message
- Reporting a post
- Reporting a reply
- Reporting a message
- Moderator functions
- Account deletion

**Modal example:**

![Modal example](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-modal.png)

#### Django Messages
Django messages are implemented to provide the user confirmation of their actions.

### Specific pages

#### Error pages

- There are error pages for error [404](https://github.com/paulio11/project-4/blob/main/templates/404.html), [500](https://github.com/paulio11/project-4/blob/main/templates/500.html), and a [third one](https://github.com/paulio11/project-4/blob/main/templates/error.html) for squigl specific error messages.
- A bootstrap alert is used to display the relevant error message.
- A button using JavaScript can send the user back one page if they want.
- Custom error messages are sent to the page from the relevant `views.py` file, often the else result of an if statement.

```
else:
        e = 'You can not delete this post because you are not the author.'
        return render(request, 'error.html', {'e': e})
```
**Error 404 example:**

![Error display](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-error.png)

#### Login and Sign up

- The default django login and sign up forms are used. Using [accounts/forms.py](https://github.com/paulio11/project-4/blob/main/accounts/forms.py) I have added placeholder text to the html inputs to assist the user when signing up.
- In my CustomUser model I made email a requirement, this is so the user can reset their password, and this is reflected while signing up.
- The login page includes a link to password reset.
- Login is required for most of the functionality. A `@login_required` decorator is used where possible. In cases where this is not an alert will notify the user.
- A logged out user will be redirected to the login page if they attempt any of these actions:
    - Change account settings such as password
    - View, send, mark read, delete, report or reply to messages
    - Any moderation only action
    - View feed
    - Make a new post
    - Repost a post
    - Report a post
    - Follow or unfollow a suer
    - View mentions
    - Mark posts and replies as read

**New user sign up form**

![User sign up form](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-signup.png)

#### Feed
- The home page for a logged in user.
- The feed displays a timeline of all the user's post and the posts of followed users.
- If there are no posts to display the user is encouraged to find users to follow.
- 20 posts are shown at a time, with pagination at the bottom so the user can navigate further into the timeline.
```
def feed(request):
    following = request.user.following
    posts = Post.objects.filter(
        Q(user__in=following.all()) | Q(user=request.user))
    paginator = Paginator(posts, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'social/feed.html', {
        'post_count': posts.count(),
        'page_obj': page_obj,
    })
```

**An example feed:**

![Feed](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-feed.png)

#### Search

- All users can search squigl.
- The user input in the search form is used to filter through posts, replies, and users.
- Results can be filtered using the navigation below the page title.
- The number of results in each category are displayed.
- Replies shown in search results contain a link to the post they are a part of.
```
def search(request):
    if request.method == 'POST':
        query = request.POST['query'].strip().lower()
        users = CustomUser.objects.filter(
            Q(username__icontains=query) | Q(name__icontains=query)).order_by(
                'username')
        posts = Post.objects.filter(
            post__icontains=query).order_by('-date')
        replies = Reply.objects.filter(
            reply__icontains=query).exclude(hidden=True).order_by('-date')
        return render(request, 'social/search.html', {
            'query': query,
            'posts': posts,
            'users': users,
            'replies': replies,
        })
    else:
        return render(request, 'social/search.html')
```

**Searching for users example:**

![User search](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-search-users.png)

**Searching for posts example:**

![Post search](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-search-posts.png)

#### User Page

- Every user that signs up has a profile page.
- This is where a user's posts will be shown regardless of if you follow them or not.
- Includes buttons to **Message** and **Follow/Unfollow** the user.
- If this is the logged in user's page then a **Edit Profile** button is shown instead.
- The user can choose to upload and display an avatar, a profile background image, a short description about themselves, change their profile name, and add a link to a website.
- User stats are also shown: Number of followers, number of users they are following, and number of posts.
- Like the Feed page, user posts are paginated.
```
def user(request, user):
    queryset = CustomUser.objects
    user = get_object_or_404(queryset, username=user)
    posts = Post.objects.filter(user_id=user.id).order_by('-date')
    following = False
    paginator = Paginator(posts, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.user.is_authenticated:
        if request.user.following.filter(id=user.id):
            following = True
    return render(request, 'social/user.html', {
        'user': user,
        'page_obj': page_obj,
        'post_count': posts.count(),
        'following': following,
    })
```

**User page example:**

![User page](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-user.png)

#### New Post

- Placeholder text is included to guide a user when making a new post. You can see the code [here](https://github.com/paulio11/project-4/blob/main/social/forms.py).
- A user has the option to include an image and/or a link to a website.
- Using the [django-reszied](https://pypi.org/project/django-resized/) package images are scaled to a width of 600px, this ensures images being shared with users of the website are not a large file size. This also has hosting benefits as well. Images are stored on [Cloudinary](https://cloudinary.com/).
- Once the form is submitted the user is redirected to the page for that post. 

```
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post', post.id)
    else:
        return render(request, 'new/new-post.html', {'form': PostForm()})
```
**New post form:**

![New post form](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-newpost.png)

#### Post Page

- Each post has its own page, this can be accessed by clicking the post timestamp or permalink in the footer.
- On the post page a user can read and post their own replies.
- The date of the post is represented in a few ways.
    - If the post is less than a minute old it shows as "Now".
    - If the post is less than 24 hours old then "X hours ago" is shown.
    - If the post is greater than 24 hours old then the published date will be shown.
- Each post shows a like count, reply count, repost count and a menu with further options. These are also shown wherever a post is displayed (feed, user page and search results).
- If the logged in user has replied and/or liked a post the relevant icons will be filled in.
- Clicking the repost icon or count will let the user repost the post by including it in a post of their own.
- A user can like a post without the need for a page reload thanks to Ajax. This code can be found [here](https://github.com/paulio11/project-4/blob/main/templates/templates/post-template.html).
- Each post contains a drop down menu which includes the option to **Report** the post and a **Permalink**. If the logged in user is the author of the post, they will also see the **Edit/Delete** option. 
- Each reply contains a button to **Report** the reply. If the logged in user is the author of the reply, they will also see the **Edit/Delete** option.

```
def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    replies = Reply.objects.filter(post_id=post_id).order_by('-date')
    if request.method == 'POST':
        form = ReplyForm(data=request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        return render(request, 'social/post.html', {
            'post': post,
            'replies': replies,
            'form': ReplyForm(),
        })
```

**An example of a post with replies:**

![New post form](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-post.png)

#### Mentions

- If a user is mentioned in a public post or reply they will be notified of this by an unread mention count in the menu.
- A user can view these posts and replies on their Mentions page.
- Posts and replies are excluded if the logged in user exists in their **read** `ManyToManyField`.
- Posts and replies can be marked as **Read** to clear the notification, and be excluded in the future.

```
def mentions(request):
    posts = Post.objects.filter(post__icontains=request.user).exclude(
        read=request.user).order_by('-date')
    replies = Reply.objects.filter(reply__icontains=request.user).exclude(
        hidden=True).exclude(read=request.user).order_by('-date')
    return render(request, 'social/mentions.html', {
        'posts': posts,
        'replies': replies,
    })
```

**An example of a user's mentions:**

![User mentions](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-mentions.png)

#### Messages

- Two logged in users can privately message each other.
- A user can either be messaged using the **Message** button on their user page, or by replying to a message they have previously sent.
- As with mentions above, a user is notified of any unread messages with a count in the menu.
- A user can view unread, read and sent messages using the message page navigation.
- Each message has a drop down menu with the options **Mark Read**, **Reply**, **Report**, and **Delete**.
- If a sent message has been read by the recipient, the sender is notified.
- Messages from website moderators (django staff role) are labeled.
- A user can chose to delete a message. The message remains in the database until both the sender and recipient have both chosen to delete it.

```
def messages(request):
    unread_messages = Message.objects.filter(
        recipient=request.user).filter(read=False).order_by('-date')
    messages = Message.objects.filter(
        recipient=request.user).filter(read=True).exclude(
            recipient_del=True).order_by('-date')
    sent_messages = Message.objects.filter(
        sender=request.user).exclude(sender_del=True).order_by('-date')
    return render(request, 'dm/messages.html', {
        'unread_messages': unread_messages,
        'messages': messages,
        'sent_messages': sent_messages})
```

**Example unread messages:**

![Unread messages](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-unread-messages.png)

**Example sent messages:**

![Sent messages](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-sent-messages.png)

#### Moderation

- Squigl moderators have access to the moderation page.
- Posts, replies and messages reported by users can be viewed here by moderators.
- A moderator can decide whether to ignore a report and mark the content as okay, or if necessary delete the content which will remove it and give the author a strike.
- Users with strikes can be viewed and messaged and banned or unbanned if necessary.
- All tables can be sorted by clicking on a column header. The code for this can be found [here](https://github.com/paulio11/project-4/blob/main/static/js/script.js).

```
def moderation(request):
    if request.user.is_staff:
        reported_posts = Post.objects.annotate(
            nreports=Count('reported')).filter(nreports__gt=0)
        reported_replies = Reply.objects.annotate(
            nreports=Count('reported')).filter(nreports__gt=0)
        reported_messages = Message.objects.filter(reported=True)
        users = CustomUser.objects.filter(strikes__gt=0).order_by('-strikes')
        return render(
            request,
            'moderation/moderation.html', {
                'reported_posts': reported_posts,
                'reported_replies': reported_replies,
                'reported_messages': reported_messages,
                'users': users,
                })
    else:
        e = 'Only Squigl moderators can view this page.'
        return render(request, 'error.html', {'e': e})
```

**Example reported posts:**

![Sent messages](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-mod-posts.png)

**Example reported post modal:**

![Sent messages](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-mod-modal.png)

**Example naughty users list:**

![Sent messages](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-mod-users.png)

### Unimplemented Features

If possible I would have liked to have implemented the following features:
- A dark mode theme.
- The ability to post other media such as videos including YouTube embeds.
- A server side trending hashtags list. The current implementation is built with JavaScript that runs client side.
- Improvements to the user pages, including a gallery of their shared images, and a list of their liked posts.
- Reposts would notify the author of the original post.
- Further styling. In my opinion this still looks too much like a Bootstrap website, even though there are almost 700 lines of CSS code!
- Inline private messaging. Replies to messages appearing as a conversation thread instead of individual separate messages.
- Some form of indication that a post or reply has been updated by the author.
- URLs shown as part of a post or on a user profile automatically converted into a working link without the need for a user to include "http://" etc.


[Back to top 🔺](#squigl)

## Bugs and Fixes

A lot of bug fixes relate to features that are no longer a part of this project so they are not documented. They are still visible via commits with the **Fix** preset. There are currently no known unfixed bugs.

|Bug|Cause|Fixed?|
|--|--|--|
|Sign page up not working|Incorrect url in view, using 'accounts' where the included default django view requires 'registration'|✓|
|Avatar in header displaying incorrectly|Wrong class applied to element|✓|
|Reply form not working|Missing `data=request.POST` parameter|✓|
|Incorrect display of 'Follower' and 'Followers' on user page|Incorrect comparison operator in django html tag|✓|
|Followers count not working|ManyToManyField in CustomUser model had a relation ship with the wrong model|✓|
|New reposts not linking to original post|`old_post` variable assignment outside of if statement|✓|
|EditProfile success url broken|Unnecessary `request.user` in kwargs|✓|
|Change password field missing on change password page|Hide password div javascript running on every page|✓|
|Hide reply not working|Missing `save()` reply function in view|✓|
|Reply indicator in post footer not working|Missing `request.user` from if statement|✓|
|User links and hashtags not working in reposts|Incorrect class on element|✓|
|HTML table sorting not functioning|Incorrect url value in javascript if statement|✓|
|Mentions notification in menu not functioning|Incorrect value in if statement|✓|
|CollectStatic failing|Missing `STATICFILES_STORAGE` variable in settings.py|✓|
|Suggested users showing when not logged in|Beginning of if statement on the wrong line|✓|
|Error page not shown when attempting to delete a message when not a moderator|Incorrect file path in render request|✓|

[Back to top 🔺](#squigl)

## Technologies

### Main Languages Used

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [HTML5](https://en.wikipedia.org/wiki/HTML)
    - The HTML is found in the [templates directory](https://github.com/paulio11/project-4/tree/main/templates).
- [CSS3](https://en.wikipedia.org/wiki/CSS)
    - You can see all my CSS [here](https://github.com/paulio11/project-4/blob/main/static/css/style.css).
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - The majority of my JavaScript is [here](https://github.com/paulio11/project-4/blob/main/static/js/script.js).
    - Hashtag and user tagging functionality can be found [here](https://github.com/paulio11/project-4/blob/main/templates/base.html).

### Frameworks

- [Bootstrap](https://getbootstrap.com/) - A frontend toolkit.
- [Django](https://www.djangoproject.com/) - A high-level Python web framework.

### Libraries

- [jQuery](https://jquery.com/) - A fast, small, and feature-rich JavaScript library.
- [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/) - A bootstrap5 template pack for django-crispy-forms. Includes [django-crispy-forms](https://pypi.org/project/django-crispy-forms/).
- [dj-database-url](https://pypi.org/project/dj-database-url/) - Enables the use of database URLS in Django.
- [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) - A Django package that provides Cloudinary storages for both media and static files as well as management commands for removing unnecessary files.
- [django-resized](https://pypi.org/project/django-resized/) - Used to resize images uploaded by the user.
- [gunicorn](https://pypi.org/project/gunicorn/) - Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX.
- [oauthlib](https://pypi.org/project/oauthlib/) - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic.
- [Pillow](https://pypi.org/project/Pillow/) - A Python Imaging Library that adds image processing capabilities to your Python interpreter.
- [psycopg2](https://pypi.org/project/psycopg2/) - Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
- [PyJWT](https://pypi.org/project/PyJWT/) - JSON Web Token implementation in Python.
- [pytz](https://pypi.org/project/pytz/) - Allows accurate and cross platform timezone calculations using Python 2.4 or higher.
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) - OAuthlib authentication support for Requests.
- [sqlparse](https://pypi.org/project/sqlparse/) - sqlparse is a non-validating SQL parser for Python.
- [Coverage](https://pypi.org/project/coverage/) - To check full for automated test coverage.
- [model-bakery](https://pypi.org/project/model-bakery/) - To create database objects for testing.

### Software and Other

- [ElephantSQL](https://www.elephantsql.com/) - Hosting of the PostgreSQL database used by squigl.
- [Balsamiq](https://balsamiq.com/) - For the creation of my wireframes during the planning stages.
- [GitHub](https://github.com/) - Repository hosting, commit history and project management with user stories. 
- [Heroku](https://heroku.com/) - Squigl is deployed to Heroku.
- [Gitpod](https://www.gitpod.io/) - Used to write code and commit to GitHub.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - For testing of site performance and used to check if the website meets accessibility guidelines.
- [Favicon.io](https://favicon.io/) - Creation of the favicon from an image.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Used to debug and test website responsiveness.
- [Cloudinary](https://cloudinary.com/) - Hosting of images and other static files such as CSS and JS.
- [Font Awesome](https://fontawesome.com/) - Source of icons used in the menu and in posts/replies/messages.
- [Google Fonts](https://fonts.google.com/) - Fonts imported from Google Fonts, see Typography section above.
- [W3C Markup Validation Service](https://validator.w3.org/) - Used to validate HTML code.
- [Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used to validate CSS code.
- [JSHint JavaScript Code Quality Tool](https://jshint.com/) - Used to validate JavaScript code.
- [CI Python Linter](https://pep8ci.herokuapp.com/) - Used to validate my Python code.
- [Am I Responsive](https://ui.dev/amiresponsive) - Used to create the hero image at the top of this readme.

[Back to top 🔺](#squigl)

## Testing
Testing information can be found [here](https://github.com/paulio11/project-4/blob/main/TESTING.md).

[Back to top 🔺](#squigl)

## Deployment
Deployment steps can be found [here](https://github.com/paulio11/project-4/blob/main/DEPLOYMENT.md).

[Back to top 🔺](#squigl)

## Credits

### Code

- Code to make sure usernames are alphanumeric from [StackOverflow](https://stackoverflow.com/questions/17165147/how-can-i-make-a-django-form-field-contain-only-alphanumeric-characters).
- CSS for reply speech bubbles from [Codepen](https://codepen.io/rikschennink/pen/mjywQb).
- JavaScript to count occurrences  of hashtags from [StackOverflow](https://stackoverflow.com/questions/14914046/counting-occurrences-of-a-word-in-a-string-javascript).
- Code to strip irrelevant time since information from post dates from [StackOverflow](https://stackoverflow.com/questions/6481788/format-of-timesince-filter).
- JavaScript to sort HTML tables from [StackOverflow](https://stackoverflow.com/questions/3160277/jquery-table-sort).
- Scroll to Top button code from [W3 Schools](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp)

### Text

- Profile descriptions and posts from real life companies/individuals are taken from their respective Twitter profiles.

### Images

- Icons from [Font Awesome](https://fontawesome.com/).
- User avatars and profile backgrounds from real life companies/individuals are taken from their respective Twitter profiles.

### Acknowledgements

Thanks again to my mentor [Oluwaseun Owonikoko](https://github.com/seunkoko) and the [Code Institute](https://codeinstitute.net/) students from class June 2022 for their help, testing and suggestions throughout the project.

[Back to top 🔺](#squigl)