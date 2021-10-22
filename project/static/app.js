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


//Jquery ajax
$(document).ready(function() {
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
			$('#validateError').text('Please provide a valid Udemy course link').show();
				
		}
		e.preventDefault();
	});
});