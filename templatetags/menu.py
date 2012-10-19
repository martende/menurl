from django import template
import datetime

from menurl.urlresolvers import MenuURLPattern,populate_menu,reverse_menu
from django.core.urlresolvers import reverse


register = template.Library()

#@register.simple_tag(takes_context=True)
@register.inclusion_tag('menu.html',takes_context=True)
def menu(context,name='main'):
	try:
		ap=context['request'].path
		user = context['request'].user
	except KeyError:
		# pleaase make context request visible
		ap="/"
		user = ""
	active_node = reverse_menu(ap)
	els = populate_menu(name)
	m = []
	for e in els.values():
		m.append({
			'title':e.title,
			'active': e.name == active_node,
			'url': reverse(e.name),
			'icon':e.icon,
		})
	print "A"
	return {
		'menu':m,
		'user':user
	}
