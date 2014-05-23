function search () {
		var keyword = $("input[name='keyword']").val();
		$.getJSON('twitsearch?keywords='+keyword, '', function(myTweets) {
			var i, k, tweet, text, where, n;
			for (n=0;n <= 1; ++n) {
				where = $('#_tweets').find('._row'+(n+1));
				where.html('');
				for (i=n*3;i < (n+1)*3; ++i) {
					tweet = myTweets[i];
					text = '<div class="col-md-4">' +
						'<p>$full_name @$screen_name</p>' +
						'<p>$text</p>' +
						'<p>$url</p>' +
						'<p>$created_at</p>' +
						'</div>';
					for (k in tweet) {
						text = text.replace("$"+k, tweet[k]);
					}
					where.append(text);
				}
			}
		});
	}

$(function() {
	$('.btn').on('click', search);
	$('#_search_text').keypress(function(event){
		if (event.which === 13)
			search();
	});
});







