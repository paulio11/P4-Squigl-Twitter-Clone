// Follow user button
$('#follow-btn:contains(Following)').mouseenter(function () {
    $(this).removeClass('btn-dark').addClass('btn-danger').text('Unfollow');
}).mouseleave(function () {
    $(this).removeClass('btn-danger').addClass('btn-dark').text('Following');
})