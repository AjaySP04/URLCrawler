from urllib.request import urlopen
from .link_finder import LinkFinder
from .url_crawl import *

class Spider(object):
	"""Class Spider : """

	#: class variables to be shared among all instances.
	project_name = ''
	base_url = ''
	domain_name = ''
	queue_file = ''
	crawled_file = ''
	queue = set()
	crawled = set()

	def __init__(self, project_name = '', base_url = '', domain_name = ''):
		
		Spider.project_name = project_name
		Spider.base_url = base_url
		Spider.domain_name = domain_name
		Spider.queue_file = os.path.join(MASTER_FOLDER_LOCATION, Spider.project_name, 'queue.txt')
		Spider.crawled_file = os.path.join(MASTER_FOLDER_LOCATION, Spider.project_name, 'crawled.txt')
		self.boot()
		self.crawl_page('First spider', Spider.base_url)

	@staticmethod
	def boot():
		"""Boot up the initial spider for crawling."""
		create_project_url_dir(Spider.project_name)
		create_url_data(Spider.project_name, Spider.base_url)
		Spider.queue = file_to_set(Spider.queue_file)
		Spider.crawled = file_to_set(Spider.crawled_file)

	@staticmethod
	def crawl_page(thread_name='', page_url=''):
		""""""
		if page_url not in Spider.crawled:
			print(thread_name + " now crawling " + page_url)
			print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
			Spider.add_links_to_queue(Spider.gather_link(page_url))
			Spider.queue.remove(page_url)
			Spider.crawled.add(page_url)
			Spider.update_files()
	
	@staticmethod
	def add_links_to_queue(links = None):
		""""""
		for url in links:
			if url in Spider.queue:
				continue
			if url in Spider.crawled:
				continue
			if Spider.domain_name not in url:
				continue
			Spider.queue.add(url)

	@staticmethod
	def gather_link(page_url=''):

		html_string = ''
		try:
			response = urlopen(page_url)
			if response.getheader('content-type').split(";")[0] == 'text/html':
				html_bytes = response.read()
				html_string = html_bytes.decode('utf-8')
				finder = LinkFinder(Spider.base_url, page_url)
				finder.feed(html_string)
			return finder.page_links()
		except Exception as e:
			print("Error: Cannot crawl the page. Message: {}".format(e))
			return set()

	@staticmethod
	def update_files():
		set_to_file(Spider.queue, Spider.queue_file)
		set_to_file(Spider.crawled, Spider.crawled_file)


def main():
	project_name =  input("Enter project name : ")
	url_subject = "https://twitter.com/"
	domain = 'twitter'

	spider1  = Spider(project_name, url_subject, domain)
	print(spider1.queue)

if __name__ == '__main__':
	main()
