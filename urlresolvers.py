from django.core.urlresolvers import RegexURLPattern,RegexURLResolver
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse,get_resolver,get_urlconf
from django.utils.datastructures import SortedDict
from django.utils.regex_helper import normalize
from django.core.urlresolvers import resolve,reverse

class MenuURLPattern(RegexURLPattern):
	def __init__(self, regex, callback, default_args=None, name=None,title = None,menu='main',icon=None):
		if not title:
			raise ImproperlyConfigured('Empty Title in Menu (for pattern %r)' % regex)
		self.title = title
		if not menu:
			self.menu = 'main'
		else:
			self.menu = menu
		self.icon = icon
		super(MenuURLPattern,self).__init__( regex, callback, default_args, name)

_menu_lookups = {}

def reverse_menu(path):
	r = resolve(path)
	return r.url_name
	
def populate_menu(name):
	global _menu_lookups
	if name in _menu_lookups:
		return _menu_lookups[name]
	else:
		urlconf = get_urlconf()
		r = get_resolver(urlconf)
		_menu_lookups[name] = _populate_menu(r,name)
	return _menu_lookups[name]

def _populate_menu(r,name):
	lookups = SortedDict()
	for pattern in (r.url_patterns):
		# MenuURLPattern exportet as appname.projname - isinstance not work
		if type(pattern).__name__ == "MenuURLPattern" and pattern.menu == name:
			lookups[pattern.name]=pattern
		elif isinstance(pattern, RegexURLResolver):
			lookups.update(_populate_menu(pattern,name))

	return lookups


def menu(regex, view, kwargs=None, name=None, prefix='',title=None,menu=None,icon=None):
	if isinstance(view, (list,tuple)):
		# For include(...) processing.
		urlconf_module, app_name, namespace = view
		r = MenuURLPattern(regex, urlconf_module, kwargs, app_name=app_name, namespace=namespace,title=title,menu=menu,icon=icon)
	else:
		if isinstance(view, basestring):
			if not view:
				raise ImproperlyConfigured('Empty URL pattern view name not permitted (for pattern %r)' % regex)
			if prefix:
				view = prefix + '.' + view
		r = MenuURLPattern(regex, view, kwargs, name,title=title,menu=menu,icon=icon)
	return r

