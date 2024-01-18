$(document).ready(function () {
    $("#search-input").on("input", function () {
        var searchTerm = $(this).val().toLowerCase();

        $(".carde").each(function () {
            var cardTitle = $(this).find(".card-title").text().toLowerCase();
            if (cardTitle.includes(searchTerm)) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });
});