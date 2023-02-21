// validate the URI
function validateInput(linkStr){
	var reg=/https:\/\/www\.udemy\.com\/course\/[^\/]+\//;
	if (linkStr.match(reg)){	
		matches=linkStr.match(reg)
		return matches[0]
	}else{
		return null;
	}

}


// copy html text to clipboard
function copyToClipboard(passEle) {
	document.getElementById("copyBtn").innerText="Copied!";
	var copyText = document.getElementById(passEle);
	copyText.select();
	copyText.setSelectionRange(0, 99999); 
	navigator.clipboard.writeText(copyText.value);
}
//copy string to clipboard
function copySyllabus(text) {
	navigator.clipboard.writeText(text);
}


// clearButton
function clearContent(){
	$('#markdownArea').text("");
	$('#collapseExample').text("");
}


$(document).ready(function() {
	$('form').on('submit', function(e) {
		$("#copyBtn").text('Copy')
		var converter = new showdown.Converter();
		var inputValue=$("#linkInput").val();
		var inputValue=validateInput(inputValue);
		if (inputValue!==null){
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
	$(".searchcopyBtn").click(function(){
		currLink=$(this).parent().prev().find('a:first').attr('href');
		curr_id=this.id
		req=$.ajax(
			{
				data:{
					link:currLink,
				},
				type:'POST',
				url:'/getsyllabus',
			})
		req.done(function(data){	
			copySyllabus(data.syllabus);
			$(".searchcopyBtn").text("Copy");
			$("#"+curr_id).text("Copied!");
		});

	})


});

