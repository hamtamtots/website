(function ($) {

    $.fn.downify = function () {

        var showdownConverter = new showdown.Converter();

        return this.each(function () {
            $(this).html(showdownConverter.makeHtml($(this).html()));
        });

    };

}(jQuery));


(function ($) {

    $.fn.downeditor = function (options) {

        var settings = $.extend({ target: '#downeditor-target' }, options);

        var showdownConverter = new showdown.Converter();

        return this.each(function () {
            var editor = $(this);
            $(settings.target).html(showdownConverter.makeHtml(editor.val()));
            editor.keyup(function () {
                $(settings.target).html(showdownConverter.makeHtml(editor.val()));
            });
        });

    };

}(jQuery));


$(function () {
    $('.downed').downify();
});


$(function () {
    var editor = $('[data-downeditor-target]');
    var target = editor.attr('data-downeditor-target');
    editor.downeditor({ target: target });
});