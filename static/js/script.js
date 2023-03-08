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

// 0 minutes ago span change
$('.timesince').each(function () {
    if ($(this).html() == '0&nbsp;minutes ago') {
        $(this).html('Now');
    };
});

// Hide password div on edit profile page
if(href.indexOf('/accounts/edit-profile/') > -1){
    $('#div_id_password').css("display", "none");
};

// Trending hashtags
// Find .hidden-post class, extract hashtag(s), place into a string
var hash_str = ''
$('.hidden-post').each(function () {
    var hashtag = $(this).find('form');
    hashtag = hashtag.text().replaceAll('#', ' ')
    hash_str = hash_str.concat(hashtag.toLowerCase())
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
        container.append('<span>#' + sorted_obj[key][0] + '</span>');
        container.append('<span class="badge text-bg-dark">' + sorted_obj[key][1] + '</span>');
    };
}; 

// Table sorting
if (href.indexOf('/mod/') > -1){
    $('th').click(function(){
        var table = $(this).parents('table').eq(0)
        var rows = table.find('tr:gt(0)').toArray().sort(comparer($(this).index()))
        this.asc = !this.asc
        if (!this.asc){rows = rows.reverse()}
        for (var i = 0; i < rows.length; i++){table.append(rows[i])}
    })
    function comparer(index) {
        return function(a, b) {
            var valA = getCellValue(a, index), valB = getCellValue(b, index)
            return $.isNumeric(valA) && $.isNumeric(valB) ? valA - valB : valA.toString().localeCompare(valB)
        }
    }
    function getCellValue(row, index){ return $(row).children('td').eq(index).text() }
}

//Scroll to top button
let topButton = document.getElementById('top-button');
window.onscroll = function () {
    scrollFunction();
};

/**
 * Shows or hides scroll to top button based on scrolled distance from top of page.
 */
function scrollFunction() {
    if (document.body.scrollTop > 64 || document.documentElement.scrollTop > 64) {
        //if user scrolls below header (64px).
        topButton.style.display = 'block';
    } else {
        topButton.style.display = 'none';
    }
}

document.getElementById('top-button').addEventListener('click', toTop);

/**
 * Scrolls page back to top.
 */
function toTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}