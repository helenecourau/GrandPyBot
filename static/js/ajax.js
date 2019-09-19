$(document).ready(function() {

	$('form').on('submit', function(event) {
		$('#errorAlert').hide();
		loader()
		$.ajax({
			data : {
				question : $('#questionInput').val(),
			},
			type : 'POST',
			url : '/process'
		})

		.done(function(data) {
			clean()
			if (data.error) {
				$('#errorAlert').text(data.error).show();
			} else {
				if (data.lat!==0) {
					var lat = data.lat;
					var lng = data.lng;
					var adress = data.adress;
					initMap(lat, lng);
					insertAdress(adress);
				}
				if (data.title.length!==0 && data.lat===0){
					$('#sentencePlace').append("<div id=\"errorMap\"> Saperlipopette, je n'ai aucune idée d'où c'est ! Mais j'ai une petite anecdote à ce propos.</div>")
				}
				if (data.title.length!==0 && data.lat!==0) {
					var random_sentence = data.random_sentence;
					insertSentence(random_sentence);
				}
				if (data.title.length!==0) {
					var title = data.title;
					var description = data.description;
                	var url = data.url;
					insertWiki(title, description, url);
				}	
				if (data.title.length===0 && data.lat!==0){
					$('#sentencePlace').append("<div id=\"errorWiki\">Par ma barbe, ça me dit rien mais j'ai l'adresse! </div>")
				}
				if (data.title.length===0 && data.lat===0) {
					$('#sentencePlace').append("<div id=\"errorAll\">Boudiou, je suis tout déboussolé ! J'en ai aucune idée. Repose ta question s'il te plaît.</div>")
				}	
			}
		$('#loaderImp').remove();

		});

		event.preventDefault();

	});

});