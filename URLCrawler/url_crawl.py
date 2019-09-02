import os

"""
URL Crawl will crawl the websites to find the links within web page which
will be stored in a seperate folder path given by the user.

- created by : Ajay Singh Parmar
- date : Sept 02, 2019.
- Project Type : Open Source. 
"""
MASTER_FOLDER_LOCATION = 'Projects'  #: master location for all project folders. 

def write_file(file_path = '', data = ''):
	"""
	write file using usrl provided and data that need to be entered.
	"""
	file = open(file_path, 'w')
	file.write(data)
	file.close()


def append_to_file(file_path = '', data = ''):
	"""
	Append data to the file.
	"""
	with open(file_path, 'a') as file:
		file.write(data + "\n")


def delete_file_data(file_path = ''):
	"""
	Delete all the data from the file.
	"""
	with open(file_path, 'w') as file:
		pass #: do nothing

def file_to_set(file_path = ""):
	"""
	"""
	results = set()
	with open(file_path, 'rt') as file:
		for line in file:
			results.add(line.replace('\n',''))
	return results


def set_to_file(links = None, file_path=""):
	"""
	"""
	delete_file_data(file_path)
	for link in links:
		append_to_file(file_path, link)


def create_project_url_dir (input_directory = None):
	"""
	Method will create project directory for web page thats crawled by the crawler.
	"""

	directory = os.path.join(MASTER_FOLDER_LOCATION, input_directory)  #: directory creating to location 

	if not os.path.exists(directory):  #: if project directory exists or not.
		print("creating project folder ...")
		os.makedirs(directory)  #: making project directory.
	else:
		print("project folder already exists.")


def create_url_data(project_name = '', base_url = ''):
	"""
	Method creates the files for crawling using base url and project name.
	It creates 2 files one for queued url and another for keeping track of crawled ones.
	Files will only be created if they does not exist already.
	"""
	file_path_queued = os.path.join(MASTER_FOLDER_LOCATION, project_name, 'queue.txt')  #: file to store the queue of url to be crawled.
	file_path_crawled = os.path.join(MASTER_FOLDER_LOCATION, project_name, 'crawled.txt')  #: file to store crawled url list.
	if not os.path.isfile(file_path_queued):
		print("creating 'queue.txt' file for the the project.")
		write_file(file_path_queued, base_url)  #: base url as first data for atleast one unique url.
	else:
		print("queue file already exists.")
	if not os.path.isfile(file_path_crawled):																																																																																																																	
		print("creating 'crawled.txt' file for the the project.")
		write_file(file_path_crawled, '')  #: empty data as in begining there will be no crawled data.
	else:
		print("crawled file already exists.")
	

if __name__=='__main__':
	"""
	Main - entry point for function to be called.
	"""
	project_name =  input("Enter project name : ")  #: input directory name that you want to specify.
	create_project_url_dir(project_name)  #: will create project folder in ".Projects/<project_name>".

	url_subject = "https://twitter.com/"
	create_url_data(project_name, url_subject)
