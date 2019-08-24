# Chris' tech blog

Random thoughts and observations from my experiences as a full-stack developer


{% for post in site.posts %}
	[{{ post.title }}]({{ post.url }})
{% endfor %}