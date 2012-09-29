python django small menu creator simple shortcuts for menu creating menu as url element

usage

## settings.py

	INSTALLED_APPS = (
		...
		'menurl',
		...
	)
	
## urls.py
	...

	from menurl.urlresolvers import menu
	
	....
	
	urlpatterns = patterns(
		'',
		....
		menu(r'^search$', 'mfg.views.searchroute' ,name='search',title= _(u'Search Rides')),
		....
		menu(r'^user/rating$', 'mfg.views.add_route' ,name='profile-rating',title= _(u'Feedback received'),menu='user',icon='ico32x32_yfeedbak.gif'),
		
		
## any template
	{% load menu %}
	
	...
	
	<ul class="nav">{% menu %}</ul>
	...
	
	<ul class="subnav nav nav-pills">
	{% menu "user" %}
	</ul>


## template menu.html

	{% for el in menu %}
		<li {%if el.active %}class="active"{% endif %}>
		<a href="{{el.url}}">{%if el.icon == "profile" %}
		{%if user.profile.avatar %}
		<img src="{% thumbnail user.profile.avatar 30x30 %}" width="18" height="18">
		{%else%}
		<img src="{{user.profile.anon_sex_avatar30x30}}" width="18" height="18">
		{%endif%}
		{%else%}
		{%if el.icon %}
		<img src="/static/images/icons/{{el.icon}}" width="18" height="18">
		{%endif%}
		{%endif%}
		<span>{{ el.title }}</span>
		</a>
		</li>
	{% endfor %}
