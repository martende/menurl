from django import template
import datetime

from menurl.urlresolvers import MenuURLPattern,populate_menu,reverse_menu
from django.core.urlresolvers import reverse


register = template.Library()
 
#@register.simple_tag(takes_context=True)

@register.inclusion_tag('menu.html',takes_context=True)
def menu(context,name='main'):
	active_node = reverse_menu(context['request'].path)
	els = populate_menu(name)
	m = []
	for e in els.values():
		m.append({
			'title':e.title,
			'active': e.name == active_node,
			'url': reverse(e.name),
			'icon':e.icon,
		})

	return {
		'menu':m,
		'user':context['request'].user
	}
