function search () {
		var keyword = $("input[name='keyword']").val();
		$.getJSON('twitsearch?keywords='+keyword, '', function(myTweets) {
			var i, k, tweet, text;
			$('#_tweets').find('._row1').html('');
			for (i in myTweets) {
				if (i < 3) {
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
					$('#_tweets').find('._row1').append(text);
				}
			}
			$('#_tweets').find('._row2').html('');
			for (i in myTweets) {
				if (i >= 3) {
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
					$('#_tweets').find('._row2').append(text);
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







