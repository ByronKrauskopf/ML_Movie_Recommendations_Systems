$(document).ready(function() {

    $('html').addClass('js-enabled');

    setup_nivo_lightbox();
    setup_dense();

    $(window).load(function() {
        $(".js-preloader").fadeOut(800, function() {
            $(".js-main-container").fadeIn(800);

            setup_scrollreveal();
            setup_progress_bar_animation();
        });
    });

});