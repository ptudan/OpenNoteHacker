class PageResult:
	
	def __init__(self, name, link, page, index, description):
		self.name = name
		self.link = link
		self.page = page
		self.index = index
		self.description = description
		self.internal_links = []

	def add_result_to_internal(self, new_page_result):
		self.internal_links.append(new_page_result)