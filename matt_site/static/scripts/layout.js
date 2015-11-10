$(document).ready(function () {
    stretchContent();
    $(window).resize(stretchContent);
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
