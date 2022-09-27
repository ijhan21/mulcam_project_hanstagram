$("#button_feed_list").click(function (){
    $('#feed_list').css({
        display : 'flex'
    });
    $('#like_feed_list').css({
        display : 'none'
    });
    $('#bookmark_feed_list').css({
        display : 'none'
    });
});
$("#button_feed_like_list").click(function (){
    $('#feed_list').css({
        display : 'none'
    });
    $('#like_feed_list').css({
        display : 'flex'
    });
    $('#bookmark_feed_list').css({
        display : 'none'
    });
});
$("#button_feed_bookmark_list").click(function (){
    $('#feed_list').css({
        display : 'none'
    });
    $('#like_feed_list').css({
        display : 'none'
    });
    $('#bookmark_feed_list').css({
        display : 'flex'
    });
});



$(".modal_close").click(function () {
    $('#first_modal').css({
        display: 'none'
    });
    $('#second_modal').css({
        display: 'none'
    });
});

let files;

$('#nav_bar_add_box').click(function () {
    $('#first_modal').css({
        display: 'flex'
    });

    $(document.body).css({
        overflow: 'hidden'
    });

});

$('#feed_create_button').click(function () {
    alert("공유하기 눌렀다.");

    let file = files[0];
    let image = files[0].name;
    let content = $('#input_feed_content').val();

    let fd = new FormData();

    fd.append('file', file);
    fd.append('image', image);
    fd.append('content', content);

    $.ajax({
        url: "/content/upload",
        data: fd,
        method: "POST",
        processData: false,
        contentType: false,
        success: function (data) {
            console.log("성공");
        },
        error: function (request, status, error) {
            console.log("에러");
        },
        complete: function () {
            console.log("완료");
            location.replace("/main");
        }
    });
});

$('.img_upload_space')
    .on("dragover", dragOver)
    .on("dragleave", dragOver)
    .on("drop", uploadFiles);

function dragOver(e) {
    e.stopPropagation();
    e.preventDefault();

    if (e.type == "dragover") {
        $(e.target).css({
            "background-color": "black",
            "outline-offset": "-20px"
        });
    } else {
        $(e.target).css({
            "outline-offset": "-10px"
        });
    }
}

function uploadFiles(e) {
    e.stopPropagation();
    e.preventDefault();

    e.dataTransfer = e.originalEvent.dataTransfer; //2
    files = e.target.files || e.dataTransfer.files;
    console.log("뭔가 파일을 올렸네??" + files[0].name);
    if (files.length > 1) {
        alert('하나만 올려라.');
        return;
    }

    if (files[0].type.match(/image.*/)) {

        $('#first_modal').css({
            display: 'none'
        });
        $('#second_modal').css({
            display: 'flex'
        });

        $('.img_upload_space').css({
            "background-image": "url(" + window.URL.createObjectURL(files[0]) + ")",
            "outline": "none",
            "background-size": "100%",
            "background-repeat": "no-repeat",
            "background-position": "center"
        });
    } else {
        alert('이미지가 아닙니다.');
        return;
    }

}

$('#button_profile_upload').click(function (){
    $('#input_fileupload').click();
});

function profile_upload(){
    let file = $('#input_fileupload')[0].files[0];

    let email = "{{ user.email }}";

    let fd = new FormData();

    fd.append('file', file);
    fd.append('email', email);

    $.ajax({
        url: "/user/profile/upload",
        data: fd,
        method: "POST",
        processData: false,
        contentType: false,
        success: function (data) {
            console.log("성공");
        },
        error: function (request, status, error) {
            console.log("에러");
        },
        complete: function () {
            console.log("완료");
            location.replace("/content/profile");
        }
    });

}