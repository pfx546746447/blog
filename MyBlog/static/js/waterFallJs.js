/**
 * Created by user on 17-10-10.
 */
function getIndex(minHeight, boxesHeight) {
    for (i in boxesHeight) {
        if (boxesHeight[i] == minHeight)
            return i
    }
}

function waterFallJs(wrap, boxes) {
    var boxWidth = boxes[0].clientWidth + 20;
    var windowWidth = document.body.clientWidth;
    var col = Math.floor(windowWidth / boxWidth);

    wrap.style.width = boxWidth* col;

    var boxesHeight = new Array();

    for(var i = 0;i<boxes.length;i++){
        if (i < col){
            boxesHeight[i] = boxes[i].clientHeight + 20;
        }else {
            var minHeight = Math.min.apply(null,boxesHeight);
            var minIndex = getIndex(minHeight,boxesHeight);
            var leftValue = boxes[minIndex].offsetLeft -10;
            boxes[i].style.position = 'absolute';
            boxes[i].style.top = minHeight + 'px';
            boxes[i].style.left = leftValue + 'px';

            boxesHeight[minHeight] += boxes[i].clientHeight + 20;
        }
    }
}


window.onload = function () {
    var wrap = document.getElementById('wrap');
    var boxes = wrap.getElementsByTagName('div');
    waterFallJs(wrap, boxes);
};