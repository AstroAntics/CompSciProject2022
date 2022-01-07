$(document).ready(function() {
    console.log("Page loaded successfully.")

    // google maps page: show location of restaurants near user on homepage
//    make_restaurant_map()

//    $("#restaurant_location_map").append(mapsFrame)

    // create restaurant map using api key
//    function make_restaurant_map(api_key) {
//        console.log("Creating Google Maps page.")
//        var mapsFrame = document.createElement('iframe');
//        $("mapsFrame").attr({
//            "width": '650px',
//            "height": '450px',
//            "style": "border: 0",
//            "loading": "lazy",
//            "src": "https://www.google.com/maps/embed/v1/place?key=" + api_key + "&q=Space+Needle,Seattle+WA"
//        });
//
//        return mapsFrame
//    }

$('#dropdownMenu1').click(function (e) {
    e.preventDefault();
    console.log(e);

//    _children = $('#dropdownMenu1').children();
//    console.log(_children)

    _restaurantsDropdown =  $('#restaurantsDropdown');
//    console.log(_restaurantsDropdown)
    _restaurantChildren = _restaurantsDropdown.children();
    _restaurantChildren.parent().attr('style' , 'display: block');
//    console.log(_restaurantChildren);
//     _restaurantChildren.attr('display' , 'block');
})

});