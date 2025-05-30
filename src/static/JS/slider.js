document.addEventListener('DOMContentLoaded', function() {
    var slider = document.getElementById('customRange3');
    var output = document.getElementById('value');

    output.innerHTML = slider.value;

    slider.oninput = function() {
        output.innerHTML = this.value;
    }
})





