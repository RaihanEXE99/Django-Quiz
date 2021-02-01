document.getElementById('cBut').addEventListener('click', function() {
    html2canvas(document.querySelector('.Download'), {
        onrendered: function(canvas) {
            // document.body.appendChild(canvas);
          return Canvas2Image.saveAsPNG(canvas);
        }
    });
    
});