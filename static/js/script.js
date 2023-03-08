// Follow user button
$('#follow-btn:contains(Following)').hover(function () {
    $(this).removeClass('btn-dark').addClass('btn-danger').text('Unfollow');
}, function () {
    $(this).removeClass('btn-danger').addClass('btn-dark').text('Following');
})

// Refresh feed icon spin
$('#feed-link').hover(function () {
    $('#feed-icon').addClass('fa-spin');
}, function () {
    $('#feed-icon').removeClass('fa-spin');
});

// Hide password div on edit profile page
$('#div_id_password').css("display", "none");