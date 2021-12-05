// validate the URI
function validateInput(inputValue){
	var expression=/(https:\/\/www\.udemy\.com\/course\/[\d*\w*\-*]{1,256}\/)/gi;
	var reg=new RegExp(expression);
	if (inputValue.match(reg)){	
		return true;
	}else{
		return false;
	}
}

// copy button
function copyToClipboard() {
	document.getElementById("copyBtn").innerText="Copied!";
	var copyText = document.getElementById("markdownArea");
	copyText.select();
	copyText.setSelectionRange(0, 99999); 
	navigator.clipboard.writeText(copyText.value);
}


// clearButton
function clearContent(){
	$('#markdownArea').text("");
	$('#collapseExample').text("");
}

$(document).ready(function() {
	//Jquery ajax
	$('form').on('submit', function(e) {
		$("#copyBtn").text('Copy')
		var converter = new showdown.Converter();
		inputValue=$("#linkInput").val();
		if (validateInput(inputValue)===true){
			$('#submitButton').html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>Loading...')
			$('#validateError').hide()
			req=$.ajax({
				data : {
					link : inputValue,
				},
				type : 'POST',
				url : '/update'
				})
			req.done(function(data) {
				$('#submitButton').text('Submit');	
				$('#markdownArea').text(data.syllabus);
				$('.textTitle h2').text(data.name);
				result=converter.makeHtml(data.syllabus);
				$('#collapseExample').prepend(result);
			});	
			

		}else{
			var obj=$('#validateError').text("Valid link sample: \n https://www.udemy.com/course/100-days-of-code/ \n (Do not forget to add '/' at the end)").show();
			obj.html(obj.html().replace(/\n/g,'<br/>'));	
		}
		e.preventDefault();
	});

});

$(document).ready(function () {
    $('input:radio').change(function () {//Clicking input radio
        var radioClicked = $(this).attr('id');
        unclickRadio();
        removeActive();
        clickRadio(radioClicked);
        makeActive(radioClicked);
    });
    $(".card").click(function () {//Clicking the card
        var inputElement = $(this).find('input[type=radio]').attr('id');
        unclickRadio();
        removeActive();
        makeActive(inputElement);
        clickRadio(inputElement);
    });
});

// selectable cards
function unclickRadio() {
    $("input:radio").prop("checked", false);
}

function clickRadio(inputElement) {
    $("#" + inputElement).prop("checked", true);
}

function removeActive() {
    $(".card").removeClass("active");
}

function makeActive(element) {
    $("#" + element + "-card").addClass("active");
}