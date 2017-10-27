/**
 * Created by user on 17-10-11.
 */
function close(){
    var close = $('.closed');
    close.click(function(){
        $('.mask').css({
            'display':'none'
        });
        $('.login').css({
            'display':'none'
        });
        $('.regist').css({
            'display':'none'
        });
        $('#regist_error').html("");
        $('#login_error').html("");
    })
}

function login(){
    $('#initLogin').click(function(){
        $('.mask').css({
            'display':'block'
        });
        $('.login').css({
            'display':'block'
        });
    })
}

function regist(){
    $('#initRegist').click(function(){
        $('.mask').css({
            'display':'block'
        });
        $('.regist').css({
            'display':'block'
        })
    })
}

$(function(){
    close();
    login();
    regist();
});