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

	def diag_print(self):
		print("Title: " + str(self.name)) # The title of the link
		print("URL: " + str(self.link)) # The external link
		print("Description: " + str(self.description)) # The description of the link
		print("Page: " + str(self.page)) # What page this result was on (When searching more than one page)
		print("Index: " + str(self.index)) # What index on this page it was on
		print("Internal links: " + str(internal_links)) # all links contained on the page