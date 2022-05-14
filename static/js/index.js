


let picture = document.querySelector('.slideshow');

picture.onclick = function(){
    let mySrc = picture.getAttribute('src');

    if (mySrc === "static/images/slideshow/fleet.jpeg"){
        picture.setAttribute('src', "static/images/slideshow/takeoff.jpeg");
    } else if (mySrc === "static/images/slideshow/takeoff.jpeg"){
        picture.setAttribute('src', "static/images/slideshow/sky.jpeg");
    } else {
        picture.setAttribute('src', "static/images/slideshow/fleet.jpeg");
    }
}