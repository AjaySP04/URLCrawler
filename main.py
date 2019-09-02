import threading
from queue import Queue 
from URLCrawler.spider import Spider
from URLCrawler.domain import *
from URLCrawler.url_crawl import *

job_queue = Queue()

def create_jobs(job_queue=None, queue_file=''):
	""""""
	if job_queue is not None or queue_file != '':
		for link in file_to_set(queue_file):
			job_queue.put(link)
		job_queue.join()
		crawl(queue_file)

def crawl(job_queue=None, queue_file=''):
	""""""
	queued_links = file_to_set(queue_file)
	if len(queued_links) > 0:
		print(str(len(queued_links)) + ' link in the queue.')
		create_jobs(job_queue, queue_file)

def create_workers(num_of_thread=0):
	""""""
	for _ in range(num_of_thread):
		t = threading.Thread(target=work)
		t.daemon = True
		t.start()

def work(queue=job_queue):
	""""""
	while(True):
		url = queue.get()
		Spider.crawl_page(threading.current_thread().name, url)
		queue.task_done()

def main():
	some_url = "https://hub.docker.com/"
	HOMEPAGE = input("Please provide page url to crawl : ")
	if HOMEPAGE.strip() == '':
		print("Please enter homepage url to begin crawling.")
		HOMEPAGE = some_url

	DOMAIN_NAME = get_domain_name(HOMEPAGE)
	PROJECT_NAME = input("Enter project name : ")
	if PROJECT_NAME.strip() == '':
		PROJECT_NAME = DOMAIN_NAME.split('.')[0]
	QUEUE_FILE = os.path.join(MASTER_FOLDER_LOCATION, PROJECT_NAME, 'queue.txt')
	CRAWLED_FILE = os.path.join(MASTER_FOLDER_LOCATION, PROJECT_NAME, 'crawled.txt')
	NUMBER_OF_THREAD = 8

	Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

	create_workers(NUMBER_OF_THREAD)
	crawl(job_queue, QUEUE_FILE)


if __name__ == '__main__':
	main()
