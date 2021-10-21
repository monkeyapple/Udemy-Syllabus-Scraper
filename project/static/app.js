$(document).ready(function() {

	$('form').on('submit', function(event) {
		var converter = new showdown.Converter(),
		req=$.ajax({
			data : {
				link : $('#linkInput').val(),
			},
			type : 'POST',
			url : '/update'
		})
		req.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#markdownArea').text(data.content);
				$('.textTitle h2').text(data.name);
				result=converter.makeHtml(data.content);
				$('#collapseExample').prepend(result);
			}
				

		});

		event.preventDefault();

	});

});
