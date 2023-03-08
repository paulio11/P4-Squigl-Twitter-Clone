var href = window.location.href;

// Follow user button
if (href.indexOf('/u/') > -1){
    $('#follow-btn:contains(Following)').hover(function () {
        $(this).removeClass('btn-dark').addClass('btn-danger').text('Unfollow');
    }, function () {
        $(this).removeClass('btn-danger').addClass('btn-dark').text('Following');
    });
};

// Refresh feed icon spin
if (href.indexOf('/feed/') > -1){
    $('#feed-link').hover(function () {
        $('#feed-icon').addClass('fa-spin');
    }, function () {
        $('#feed-icon').removeClass('fa-spin');
    });
};

// Hide password div on edit profile page
if(href.indexOf('/accounts/edit-profile/') > -1){
    $('#div_id_password').css("display", "none");
};

// Trending hashtags
// Find .hidden-post class and take hashtag(s) out, then into a string
var hash_str = ''
$('.hidden-post').each(function () {
    var hashtag = $(this).find('form');
    hashtag = hashtag.text().replaceAll('#', ' ')
    hash_str = hash_str.concat(hashtag)
});
// Split the hashtag string into an array
var split = hash_str.trimStart().split(' ');
// Count occurrences of hashtags in array
var obj = {};
for (var x = 0; x < split.length; x++) {
    if (obj[split[x]] === undefined) {
        obj[split[x]] = 1;
    } else {
        obj[split[x]]++;
    }
};
// Sort new object by key value
var sorted_obj = Object.entries(obj).sort((a,b) => b[1]-a[1])
// Object keys and value into html to display on page (up to 10)
var trending_ul = $('#trending-ul'), container;
for (var key in sorted_obj){
    if (key == 10) {
        break;
    } else {
        container = $('<li class="list-group-item hashtag-li"></li>');
        trending_ul.append(container);
        container.append('<span>#' + sorted_obj[key][0] + '</span');
        container.append('<span>' + sorted_obj[key][1] + '</span');
    };
}; 
