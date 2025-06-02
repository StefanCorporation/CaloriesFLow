document.addEventListener('DOMContentLoaded', function() {
    var sliders = document.querySelectorAll('.slider-range')

    sliders.forEach(function(slider) {
        var outputId = 'value' + slider.id.replace('customRange', '')
        var output = document.getElementById(outputId)

        output.innerHTML = slider.value

        slider.addEventListener('input', function() {
            output.innerHTML = this.value
        })

    })
})







// document.addEventListener('DOMContentLoaded', function() {
//     var slider = document.getElementById('customRange3');
//     var output = document.getElementById('value');

//     output.innerHTML = slider.value;

//     slider.oninput = function() {
//         output.innerHTML = this.value;
//     }
// })





