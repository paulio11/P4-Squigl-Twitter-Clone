# Testing

## Contents

1. [Validation](#validation)
2. [Automated Testing](#automated-testing)
3. [Browser Validation](#browser-testing)
4. [Lighthouse Results](#lighthouse-results)
5. [User Stories](#user-stories)

## Validation
You can see the changes I made to make the pages error free in these commits: [1](https://github.com/paulio11/project-4/commit/5576d642edf0307751bedf8fe2495476df2b8b62), [2](https://github.com/paulio11/project-4/commit/3ecc8493b64dc6579d071d7707c6f821dd47b27a).

### CSS ([Jigsaw CSS Validation](https://jigsaw.w3.org/css-validator/)) & JavaScript ([JSHint](https://jshint.com/))
|File|Result|Screenshot|
|--|--|--|
|[style.css](https://github.com/paulio11/project-4/blob/main/static/css/style.css)|✓ *|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/stylecss.JPG)
|[script.js](https://github.com/paulio11/project-4/blob/main/static/js/script.js)|✓|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/scriptjs.JPG)
|[Like post script](https://github.com/paulio11/project-4/blob/main/templates/templates/post-template.html)|✓|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/likejs.JPG)
|[base.html script](https://github.com/paulio11/project-4/blob/main/templates/base.html)|✓|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/basehtmljs.JPG)

*8 warnings, all related to the various avatar styles having matching background and border colours. This was intended so that avatars with transparency look good against a user's profile background.

JavaScript code in base.html was tested manually.

### HTML ([W3C Markup Validation](https://validator.w3.org/))
Due to many pages requiring login, HTML was tested using **text input** instead of **address**. I copied a rendered page's source code and pasted it into the validator.

|Page|Result|Notes|Results|
|--|--|--|--|
|Feed|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Trending Hashtags|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Users to follow list|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Mentions|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Mentions with no mentions|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Messages|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Messages with no messages|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Post with replies|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Post with no replies|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Post with repost|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Search with results|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Search with no results|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|User profile with posts|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|User profile with no posts|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|New post|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|New repost|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Edit post|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Edit reply|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Send message|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Settings|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Change password|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Reset password - complete|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Reset password - confirm|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Reset password - done|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Reset password - form|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Login|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Sign up|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)
|Home|✓|No errors or warnings to show|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/noerrorhtml.JPG)

### Python ([CI Python Linter](https://pep8ci.herokuapp.com/))
All python files with code written by myself were run through the CI Python Linter. These are the results.

|File|Result|Notes|Screenshot|
|--|--|--|--|
|[accounts/admin.py](https://github.com/paulio11/project-4/blob/main/accounts/admin.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/accounts-admin.JPG)
|[accounts/forms.py](https://github.com/paulio11/project-4/blob/main/accounts/forms.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/accounts-forms.JPG)
|[accounts/models.py](https://github.com/paulio11/project-4/blob/main/accounts/models.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/accounts-model.JPG)
|[accounts/tests.py](https://github.com/paulio11/project-4/blob/main/accounts/tests.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/accounts-tests.JPG)
|[accounts/urls.py](https://github.com/paulio11/project-4/blob/main/accounts/urls.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/accounts-urls.JPG)
|[accounts/views.py](https://github.com/paulio11/project-4/blob/main/accounts/views.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/accounts-view.JPG)
|[dm/templatetags/dm_extras.py](https://github.com/paulio11/project-4/blob/main/dm/templatetags/dm_extras.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/dm-extras.JPG)
|[dm/admin.py](https://github.com/paulio11/project-4/blob/main/dm/admin.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/dm-admin.JPG)
|[dm/forms.py](https://github.com/paulio11/project-4/blob/main/dm/forms.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/dm-forms.JPG)
|[dm/models.py](https://github.com/paulio11/project-4/blob/main/dm/models.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/dm-models.JPG)
|[dm/tests.py](https://github.com/paulio11/project-4/blob/main/dm/tests.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/dm-tests.JPG)
|[dm/urls.py](https://github.com/paulio11/project-4/blob/main/dm/urls.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/dm-urls.JPG)
|[dm/views.py](https://github.com/paulio11/project-4/blob/main/dm/views.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/dm-views.JPG)
|[moderation/templatetags/dm_extras.py](https://github.com/paulio11/project-4/blob/main/moderation/templatetags/dm_extras.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/mod-extras.JPG)
|[moderation/tests.py](https://github.com/paulio11/project-4/blob/main/moderation/tests.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/mod-tests.JPG)
|[moderation/urls.py](https://github.com/paulio11/project-4/blob/main/moderation/urls.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/mod-urls.JPG)
|[moderation/views.py](https://github.com/paulio11/project-4/blob/main/moderation/views.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/mod-views.JPG)
|[social/templatetags/dm_extras.py](https://github.com/paulio11/project-4/blob/main/social/templatetags/dm_extras.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/social-extras.JPG)
|[social/admin.py](https://github.com/paulio11/project-4/blob/main/social/admin.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/social-admin.JPG)
|[social/forms.py](https://github.com/paulio11/project-4/blob/main/social/forms.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/social-forms.JPG)
|[social/models.py](https://github.com/paulio11/project-4/blob/main/social/models.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/social-models.JPG)
|[social/tests.py](https://github.com/paulio11/project-4/blob/main/social/tests.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/social-tests.JPG)
|[social/urls.py](https://github.com/paulio11/project-4/blob/main/social/urls.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/social-urls.JPG)
|[social/views.py](https://github.com/paulio11/project-4/blob/main/social/views.py)|✓|All clear, no errors found|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/testing/social-views.JPG)

[Back to top 🔺](#testing)

## Automated Testing
My goal for automated testing was to reach 100% coverage using the Python library [Coverage](https://pypi.org/project/coverage/). **100% coverage was achieved** excluding `manage.py` as this is built in django code. I further developed each test to cover things such as testing for login requirements and changes to the database. **See each test file for full list of things tested for**. 

<details>
    <summary><strong>Coverage Report</strong></summary>
    <img src="https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-coverage-report.png">
</details>

<details>
    <summary><strong>Terminal Test Output</strong></summary>
    <img src="https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/readme-test-results.png">
</details>
<br>

**The following tests are carried out:**

### [accounts.tests.py](https://github.com/paulio11/project-4/blob/main/accounts/tests.py)

| Name                 | Testing For                      | Result |
| -------------------- | -------------------------------- | ------ |
| **CustomUserModelTests** |||
| test_followers_count | User has 2 followers|✓|
| test_following_count | User is following 2|✓|
| **EditProfileTests**|
| test_success_url| Correct success url|✓|
| **ChangePasswordTests**|||
| test_post| Password changed|✓|
| test_get| Correct template|✓|
| **DeleteAccountTests**|
| test_post| Account deleted, user count is 0|✓|
| test_error|User has permission, correct template, correct error message|✓|

### [dm.tests.py](https://github.com/paulio11/project-4/blob/main/dm/tests.py)

|Name|Testing For|Result|
|--|--|--|
|**MessageModelTests**|||
|test_str|String is correct|✓|
|**MessagesTests**|||
|test_login_requirement|Login required to see messages, redirects to login|✓|
|test_render|Correct template|✓|
|**SendMessageTests**|||
|test_login_required|Login required to send message, redirects to login|✓|
|test_post|Message created, correct redirect|✓|
|test_get|Correct template, contains recipient name|✓|
|**SendReplyTests**|||
|test_login_required|Login required to send reply, redirects to login|✓|
|test_post|Message created, correct redirect|✓|
|test_get|Correct template, contains send reply to recipient|✓|
|test_error|User has permission, correct template, correct error message|✓|
|**MarkReadTests**|||
|test_login_required|Login required to mark read, redirects to login|✓|
|test_mark_read|Message is marked read, correct redirect|✓|
|test_error|User has permission, correct template, correct error message|✓|
|**DeleteMessageTests**|||
|test_login_required|Login required to delete message, redirects to login|✓|
|test_sender_delete|Set true, correct redirect|✓|
|test_recipient_delete|Set true, correct redirect|✓|
|test_delete|Message is deleted|✓|
|test_error|User has permission, correct template, correct error message|✓|
|**ReportMessageTests**|||
|test_login_required|Login required to report message, redirects to login|✓|
|test_report|Message reported, correct redirect|✓|
|test_error|User has permission, correct template, correct error message|✓|

### [moderation.tests.py](https://github.com/paulio11/project-4/blob/main/moderation/tests.py)

|Name|Testing For|Result|
|--|--|--|
|**ModCountTests**|||
|test_mod_count|mod_count() works|✓|
|**ModerationTests**|||
|test_login_required|Login required to see mod page, redirects to login|✓|
|test_login_as_normal_user|Normal user gets error message|✓|
|test_moderation|Logged in moderator can see correct page|✓|
|**ModDeletePostTests**|||
|test_login_required|Login required to delete post, redirects to login|✓|
|test_login_as_normal_user|Normal user gets error message|✓|
|test_mod_delete|Post is deleted, user gets a strike, correct redirect|✓|
|**ModDeleteReplyTests**|||
|test_login_required|Login required to delete reply, redirects to login|✓|
|test_login_as_normal_user|Normal user gets error message|✓|
|test_mod_delete|Reply is deleted, user gets a strike, correct redirect|✓|
|**ModDeleteMessageTests**|||
|test_login_required|Login required to delete message, redirects to login|✓|
|test_login_as_normal_user|Normal user gets error message|✓|
|test_mod_delete|Message is deleted, user gets a strike, correct redirect|✓|
|**PostIsOkayTests**|||
|test_login_required|Login required to okay post, redirects to login|✓|
|test_login_as_normal_user|Normal user gets error message|✓|
|test_post_okay|Post report count is 0, correct redirect|✓|
|**ReplyIsOkayTests**|||
|test_login_required|Login required to okay reply, redirects to login|✓|
|test_login_as_normal_user|Normal user gets error message|✓|
|test_reply_okay|Reply report count is 0, correct redirect|✓|
|**MessageIsOkayTests**|||
|test_login_required|Login required to okay message, redirects to login|✓|
|test_login_as_normal_user|Normal user gets error message|✓|
|test_message_okay|Message reported is False, correct redirect|✓|
|**BanUserTests**|||
|test_login_required|Login required to ban/unban user, redirects to login|✓|
|test_login_as_normal_user|Normal user gets error message|✓|
|test_ban_user|User active is False, correct redirect|✓|
|test_unban_user|User active is True, correct redirect|✓|

### [social.tests.py](https://github.com/paulio11/project-4/blob/main/social/tests.py)

|Name|Testing For|Result|
|--|--|--|
|**PostModelTests**|||
|test_str|String is correct|✓|
|test_like_count|like_count() works|✓|
|test_reply_count|reply_count() works|✓|
|test_repost_count|repost_count() works|✓|
|test_reported_count|reported_count() works|✓|
|test_time_check|Post is less than 24hrs old so time_check() is True|✓|
|test_time_check_2|Post is more than 24hrs old so time_check() is False|✓|
|**ReplyModelTests**|||
|test_str|String is correct|✓|
|test_reported_count|reported_count() works|✓|
|test_time_check|Reply is less than 24hrs old so time_check() is True|✓|
|test_time_check_2|Reply is more than 24hrs old so time_check() is False|✓|
|**UserHasRepliedTagTests**|||
|test_replies_gte_1|True if user has replied to post|✓|
|test_replies_0|False if user has replied to post|✓|
|**StringFilterTests**|||
|test_upto|upto template tag works|✓|
|**HomeTests**|||
|test_logged_in|Logged in user redirected to feed|✓|
|test_logged_out|Home page shown|✓|
|**FeedTests**|||
|test_login_required|Login required to see feed, redirects to login|✓|
|test_render|Correct template used|✓|
|**SearchTests**|||
|test_post|Correct template used, shows search query|✓|
|test_get|Correct template used|✓|
|**PostTests**|||
|test_get|Correct template used, page shows: post, reply, form1 and form 2, login to reply message|✓|
|test_post_reply_form_1|Form1 functions, reply is created, redirect correct, reply shown|✓|
|test_post_reply_form_2|Form2 functions, reply is created, redirect correct, reply shown|✓|
|**UserTests**|||
|test_render|Correct template used, shows user's posts|✓|
|test_when_following|Follow button text is 'Following'|✓|
|test_when_not_following|Follow button text is 'Follow'|✓|
|**NewPostTests**|||
|test_login_required|Login required to make new post, redirects to login|✓|
|test_get|Correct template used, contains form|✓|
|test_post|New post created, correct redirect|✓|
|**RepostTests**|||
|test_login_required|Login required to make repost, redirects to login|✓|
|test_get|Correct template used, contains form, shows old post|✓|
|test_post|Repost post created, correct redirect, old post has repost count of 1|✓|
|**EditPostTests**|||
|test_get|Correct template used, permission error shown|✓|
|test_get_as_author|Correct template used, correct redirect|✓|
|test_post|Correct redirect, post is edited|✓|
|**EditReplyTests**|||
|test_get|Correct template used, permission error shown|✓|
|test_get_as_author|Correct template used, correct redirect|✓|
|test_post|Correct redirect, reply is edited|✓|
|**DeletePostTests**|||
|test_delete|Correct template used, permission error shown|✓|
|test_delete_as_author|Correct redirect, post is deleted|✓|
|**DeleteReplyTests**|||
|test_delete|Correct template used, permission error shown|✓|
|test_delete_as_author|Correct redirect, reply is deleted|✓|
|**LikePostTests**|||
|test_like|Like count increases|✓|
|test_unlike|Like count decreases|✓|
|**ReportPostTests**|
|test_login_required|Login required to report post, redirects to login|✓|
|test_report|Correct redirect, post reported count increases|✓|
|**ReportReplyTests**|
|test_login_required|Login required to report reply, redirects to login|✓|
|test_report|Correct redirect, reply reported count increases|✓|
|**FollowTests**|||
|test_login_required|Login required to follow, redirects to login|✓|
|test_follow|Correct redirect, user follow count increases, followed user followers count increases|✓|
|test_unfollow|Correct redirect, user follow count decreases, followed user followers count decreases|✓|
|**MentionsTest**|||
|test_login_required|Login required to use mentions page, redirects to login|✓|
|test_mark_read|Correct redirect, post/reply marked as read|✓|
|**SideTests**|||
|test_trending|Correct template used|✓|
|test_user_list|Correct template used|✓|
|test_ulist_login_required|Login required to view user list, redirects to login|✓|

[Back to top 🔺](#testing)

## Browser Testing

|Browser|Screenshot|
|--|--|
|Google Chrome|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/browser-chrome.jpg)|
|Edge|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/browser-edge.jpg)|
|Safari|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/browser-safari.png)|
|Mobile Safari (iOS)|[Screenshot](https://raw.githubusercontent.com/paulio11/project-4/main/documentation/images/browser-mobile-safari.png)|

[Back to top 🔺](#testing)

## Lighthouse Results

All possible pages were checked using Lighthouse in desktop mode. Any unresolved issues were left as such because they are either out of my control (response times etc) or intensional. Results were not recorded as screenshots as due to variations. These are the results I found at time of submission(your own results may vary based on page content at the time of testing):

|Page|Performance|Accessibility|Best Practices|SEO|
|--|--|--|--|--|
|Feed|87|99|100|100|
|Trending Hashtags|100|98|100|100|
|Users to follow list|99|98|100|100|
|Mentions|100|97|100|100|
|Mentions with no mentions|99|98|100|100|
|Messages|99|99|100|100|
|Messages with no messages|100|99|100|100|
|Post with replies|100|98|100|100|
|Post with no replies|100|98|100|100|
|Post with repost|92|98|100|100|
|Search with results|100|98|100|100|
|Search with no results|99|98|100|100|
|User profile with posts|97|98|100|100|
|User profile with no posts|100|96|100|100|
|New post|100|98|100|100|
|New repost|92|98|100|100|
|Edit post|100|98|100|100|
|Edit reply|99|98|100|100|
|Send message|100|98|100|100|
|Settings|99|98|100|100|
|Change password|100|98|100|100|
|Reset password - complete|100|100|100|100|
|Reset password - confirm|100|100|100|100|
|Reset password - done|100|100|100|100|
|Reset password - form|100|100|100|100|
|Login|100|100|100|100|
|Sign up|100|100|100|100|
|Home|100|98|100|100|

[Back to top 🔺](#testing)

## User Stories

All user stories were achieved during development and were subject to manual user testing. You can see a list of all user stories in my readme [here](https://github.com/paulio11/project-4#epics-and-user-stories).

[Back to top 🔺](#testing)