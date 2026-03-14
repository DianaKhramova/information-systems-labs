var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(e) {
        var post = e.target.parentElement; // родительский .one-post
        if (post.className.indexOf("folded") === -1) {
            // сворачиваем
            post.className += " folded";
            e.target.innerHTML = "развернуть";
        } else {
            // разворачиваем
            post.className = post.className.replace(" folded", "");
            e.target.innerHTML = "свернуть";
        }
    });
}