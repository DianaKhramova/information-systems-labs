$(document).ready(function(){
    $('.one-post').hover(
        function(event) {
            // наведение
            $(event.currentTarget).find('.one-post-shadow').animate({opacity: 0.1}, 300);
        },
        function(event) {
            // уход курсора
            $(event.currentTarget).find('.one-post-shadow').animate({opacity: 0}, 300);
        }
    );
    $('.header img').hover(
        function() {
            $(this).animate({width: '338px'}, 200); // увеличиваем на 20px
        },
        function() {
            $(this).animate({width: '318px'}, 200); // возвращаем исходный размер
        }
    );
}
);
