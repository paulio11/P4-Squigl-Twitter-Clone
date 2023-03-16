# Testing

## Validation
You can see the changes I made to make the pages error free in these commits: [1](), [2]().

### CSS & JavaScript
|File|Result|
|--|--|
|[style.css](https://github.com/paulio11/project-4/blob/main/static/css/style.css)|✓ *|
|[script.js](https://github.com/paulio11/project-4/blob/main/static/js/script.js)|✓|
|[Like post script](#)|✓|
|[base.html script](#)|✓|

*8 warnings, all related to the various avatar styles having matching background and border colours. This was intended so that avatars with transparency look good against a user's profile background.

### HTML
Due to many pages requiring login, HTML was tested using **text input** instead of **address**. I copied a rendered page's source code and pasted it into the validator.

|Page|Result|Notes|
|--|--|--|
|Feed|✓|No errors or warnings to show|
|Trending Hashtags|✓|No errors or warnings to show|
|Users to follow list|✓|No errors or warnings to show|
|Mentions|✓|No errors or warnings to show|
|Mentions with no mentions|✓|No errors or warnings to show|
|Messages|✓|No errors or warnings to show|
|Messages with no messages|✓|No errors or warnings to show|
|Post with replies|✓|No errors or warnings to show|
|Post with no replies|✓|No errors or warnings to show|
|Post with repost|✓|No errors or warnings to show|
|Search with results|✓|No errors or warnings to show|
|Search with no results|✓|No errors or warnings to show|
|User profile with posts|✓|No errors or warnings to show|
|User profile with no posts|✓|No errors or warnings to show|
|New post|✓|No errors or warnings to show|
|New repost|✓|No errors or warnings to show|
|Edit post|✓|No errors or warnings to show|
|Edit reply|✓|No errors or warnings to show|
|Send message|✓|No errors or warnings to show|
|Settings|✓|No errors or warnings to show|
|Change password|✓|No errors or warnings to show|
|Reset password - complete|✓|No errors or warnings to show|
|Reset password - confirm|✓|No errors or warnings to show|
|Reset password - done|✓|No errors or warnings to show|
|Reset password - form|✓|No errors or warnings to show|
|Login|✓|No errors or warnings to show|
|Sign up|✓|No errors or warnings to show|

## Automated Testing
I created automated tests for the following:

### Django Project Tests ([squigl/tests.py](#))

|Test|Expected Result|Result|
|--|--|--|
|debug_is_false|False|✓|
|secret_key_strength|Pass|✓|

### Social App Tests ([social/tests.py](#))

#### Testing urls go to correct view ([TestURLs](#)):

|Test Name|URL Example|Expected View|Result|
|--|--|--|--|
|test_feed|`/feed/`|feed|✓|
|test_search|`/search/`|search|✓|
|test_post|`/p/99`|post|✓|
|test_edit_post|`/edit-post/99`|edit_post|✓|
|test_delete_post|`/delete-post/99`|delete_post|✓|
|test_like_post|`/like-post/99`|like_post|✓|
|test_repost_post|`/repost/99`|repost|✓|
|test_report_post|`/like-post/99`|report_post|✓|
|test_edit_reply|`/edit-reply/21`|edit_reply|✓|
|test_delete_reply|`/delete-reply/21`|delete_reply|✓|
|test_report_reply|`/report-reply/21`|report_reply|✓|
|test_user|`/u/testuser`|user|✓|
|test_follow_user|`/follow/testuser`|follow|✓|
|test_mentions|`/mentions/`|mentions|✓|
|test_mark_read_mentions|`/mentions/read/`|mark_read|✓|
|test_trending_list|`/trending/`|trending|✓|
|test_user_list|`/user-list/`|user_list|✓|

#### Testing the reverse of above ([TestReverseURLs](#)):

|Test Name|View Name|Expected URL|Result|
|--|--|--|--|
|test_feed|feed|`/feed/`|✓|
|test_search|search|`/search/`|✓|
|test_post|post|`/p/99`|✓|
|test_edit_post|edit_post|`/edit-post/99`|✓|
|test_delete_post|delete_post|`/delete-post/99`|✓|
|test_like_post|like_post|`/like-post/99`|✓|
|test_repost_post|repost|`/repost/99`|✓|
|test_report_post|report_post|`/like-post/99`|✓|
|test_edit_reply|edit_reply|`/edit-reply/21`|✓|
|test_delete_reply|delete_reply|`/delete-reply/21`|✓|
|test_report_reply|report_reply|`/report-reply/21`|✓|
|test_user|user|`/u/testuser`|✓|
|test_follow_user|follow|`/follow/testuser`|✓|
|test_mentions|mentions|`/mentions/`|✓|
|test_mark_read_mentions|mark_read|`/mentions/read/`|✓|
|test_trending_list|trending|`/trending/`|✓|
|test_user_list|user_list|`/user-list/`|✓|

#### Testing the Post model ([TestPostModel](#)):

|Test Name|Test Action|Expected Result|Result|
|--|--|--|--|
|test_str|Compare strings|Post: ID, by: username|✓|
|test_post_has_user|Check user is not none|Post has user|✓|
|test_post_has_date|Check date is not none|Post has date|✓|
|test_post_has_post|Check post is not none|Post has post|✓|
|test_like_count|Add two users to likes field|Likes equal to 2|✓|
|test_reply_count|Add two replies to post|Replies equal to 2|✓|
|test_repost|Create new post that reposts post|New post has old post in repost field|✓|
|test_read|Add two users into read field|Read count equal to 2|✓|
|test_report|Add two users into report field|Report count equal to 2|✓|
|test_post_length|Count generated post length|Length less than 400|✓|
|test_link_length|Count generated link length|Length less than 50|✓|

#### Testing the Reply model ([TestReplyModel](#)):

|Test Name|Test Action|Expected Result|Result|
|--|--|--|--|
|test_str|Compare strings|Reply: ID, for: ID, by: username|✓|
|test_reply_has_user|Check user is not none|Reply has user|✓|
|test_reply_has_date|Check date is not none|Reply has date|✓|
|test_reply_has_post|Check reply is not none|Reply has reply|✓|
|test_reply_not_hidden|Assert False on hidden field|Hidden is False|✓|
|test_reply_report|Add two users into report field|Report count equal to 2|✓|
|test_reply_read|Add two users into read field|Read count equal to 2|✓|
|test_reply_length|Count generated reply length|Length less than 400|✓|

#### Testing login required views ([TestLoginRequiredViews](#)):

- Some views skipped due to requiring a `csrf_token`. These were manually tested.
- Response code 302 indicates a redirect to the login page.

|Test Name|Test Action|Expected Code|Result|
|--|--|--|--|
|test_feed|Compare response code|302|✓|
|test_feed_logged_in|Log in testuser, compare response code|200|✓|
|test_new_post|Compare response code|302|✓|
|test_new_post_logged_in|Log in testuser, compare response code|200|✓|
|test_repost|Compare response code|302|✓|
|test_repost_logged_in|Log in testuser, compare response code|200|✓|
|test_report_post|Compare response code|302|✓|
|test_follow_user|Compare response code|302|✓|
|test_mentions|Compare response code|302|✓|
|test_mentions_logged_in|Log in testuser, compare response code|200|✓|
|test_mark_read|Compare response code|302|✓|
|test_mark_read_logged_in|Log in testuser, compare response code|200|✓|
