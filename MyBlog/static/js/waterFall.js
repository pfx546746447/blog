/**
 * Created by user on 17-10-10.
 */
var data = [{
    "src":"blackwhite.jpg",
    "title":"blackwhite"
},{
    "src":"google.jpg",
    "title":"google"
},{
    "src":"htc.jpg",
    "title":"htc"
},{
    "src":"htc2.jpg",
    "title":"htc2"
},{
    "src":"iphone.jpg",
    "title":"iphone"
},{
    "src":"iphone5.jpg",
    "title":"iphone5"
},{
    "src":"iphone5s.jpg",
    "title":"iphone5s"
},{
    "src":"iphone6.jpg",
    "title":"iphone6"
},{
    "src":"iphone6plus.jpg",
    "title":"iphone6plus"
},{
    "src":"mobile.jpg",
    "title":"mobile"
},{
    "src":"sumsung.jpg",
    "title":"sumsung"
},{
    "src":"xiaomi4.jpg",
    "title":"xiaomi4"
}];

function getIndex(minHeight, boxesHeight) {
    for (index in boxesHeight) {
        if (boxesHeight[index] == minHeight)
            return index
    }
}

function waterFall(wrap, boxes) {
    var boxWidth = boxes.eq(0).width() + 40;
    var windowWidth = $(window).width();
    var colNum = Math.floor(windowWidth / boxWidth);

    wrap.width(boxWidth * colNum);

    var boxesHeight = new Array();

    for (var i = 0; i < boxes.length; i++) {
        if (i < colNum) {
            boxesHeight[i] = boxes.eq(i).height() + 40;
        } else {
            var minHeight = Math.min.apply(null, boxesHeight);
            var minIndex = getIndex(minHeight, boxesHeight);
            var leftValue = boxes.eq(minIndex).position().left;
            boxes.eq(i).css({
                'position': 'absolute',
                'top': minHeight,
                'left': leftValue,
                'opacity':0
            }).stop().animate({
                'opacity':1
            },1000);

            boxesHeight[minIndex] += boxes.eq(i).height()+40;
        }
    }
}

var appendBox = function(wrap,boxes){
    for (var i = 0; i < data.length;i++){
        wrap.append('<div><img src="../../media/phone/'+ data[i].src +'" alt=""><a href="">'+ data[i].title +'</a></div>')
    }

};

$(function () {
    var wrap = $('#wrap');
    var boxes = wrap.children('div');
    waterFall(wrap,boxes);

    $(this).scroll(function(event){
        appendBox(wrap,boxes);
    })
});