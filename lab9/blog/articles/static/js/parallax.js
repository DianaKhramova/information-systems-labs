$(document).ready(function(){
    var yPosition;
    var scrolled = 0;
    var $parallaxElements = $('.icons-for-parallax img');
    var $logo = $('.header .logo');

    $(window).scroll(function() {
        scrolled = $(window).scrollTop();
        for (var i = 0; i < $parallaxElements.length; i++) {
            // скорость перемещения зависит от номера элемента (i+1) и коэффициента 0.15
            yPosition = scrolled * 0.15 * (i + 1);
            $parallaxElements.eq(i).css({ top: yPosition });
        }
        var logoMove = scrolled * 0.8;
        $logo.css({ top: logoMove });
    });
});