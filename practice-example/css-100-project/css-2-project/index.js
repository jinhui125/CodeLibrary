$('.menu_icon').bind('click', function () {
    $(this).toggleClass('active')
    $(this).find('div').removeClass('no_animation')
})