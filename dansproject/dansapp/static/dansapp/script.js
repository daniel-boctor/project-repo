document.addEventListener('DOMContentLoaded', function() {

    document.querySelectorAll('.nav-link').forEach(function(nav_link) {
        if (nav_link.getAttribute("href") === window.location.pathname) {
            //nav_link.setAttribute("class", "nav-link active");
            nav_link.className += " active";
            nav_link.setAttribute("aria-current", "page");
            nav_link.style.textDecoration = "underline"; 
        }
    });

    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl)
    })
});