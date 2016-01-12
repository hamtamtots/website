$(document).ready(function () {
    stretchContent();
    $(window).resize(stretchContent);
    $('#dwongoose_bottom').click(scrollToTop);
});

function stretchContent() {
    headerHeight = $('header').outerHeight(true);
    footerHeight = $('footer').outerHeight(true);
    windowHeight = $(window).height();
    var height = windowHeight - headerHeight - footerHeight;
    if ($('#content').css('height') < height) {
        $('#content').css('height', height);
    }
    $('#content').css('min-height', height);
}

function scrollToTop() {
    $('html, body').animate({ scrollTop: 0 }, 'fast');
}