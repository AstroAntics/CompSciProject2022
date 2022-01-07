$(document).ready(function() {
    console.log("Page loaded successfully.")

    $('#dropdownMenu1').click(function (e) {
        e.preventDefault();
        console.log(e);

        _restaurantsDropdown =  $('#restaurantsDropdown');
        _restaurantChildren = _restaurantsDropdown.children();
        _restaurantParent = _restaurantChildren.parent();

        // Extend or retract dropdown based on user interaction
        if (_restaurantParent.hasClass('extended')) {
            console.log("Collapsing dropdown.");
            _restaurantParent.removeClass('extended');
            _restaurantParent.attr('style' , 'display: none');
        } else {
            console.log("Extending dropdown.")
            _restaurantParent.attr('style' , 'display: inline-block');
            _restaurantParent.addClass('extended');
        }
    });
});