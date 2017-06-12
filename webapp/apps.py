from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class SuitConfig(DjangoSuitConfig):
	menu = (
		ParentItem('Home Content', app='home_content'),
		ParentItem('Pages', app='page_content'),
		ParentItem('Navigation', app='navigation'),
		ParentItem('Site Content', children=[
			ChildItem(model='site_content.logo'),
			ChildItem(model='site_content.sociallink'),
			ChildItem(model='site_content.instagram'),
		]),
		ParentItem('Contacts', app='contact'),
		ParentItem('Site Media', children=[
			ChildItem('Files', url='fb_browse'),
		]),
		ParentItem('Account', app='account'),
		ParentItem('Users', children=[
			ChildItem(model='auth.user'),
			ChildItem('User groups', 'auth.group'),
		]),
		ParentItem('Your Account', children=[
			ChildItem('Password change', url='admin:password_change'),

		], align_right=True),
	)

	def ready(self):
		super(SuitConfig, self).ready()
