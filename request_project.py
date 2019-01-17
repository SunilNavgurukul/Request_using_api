import requests
import json
import os

saral_url=("http://saral.navgurukul.org/api/courses")
def request_api(url):
	if os.path.exists('courses.json'):
		print("It is from your file courses.json")
	else:
		page = requests.get(url)
		with open('courses.json','w') as file1:
			raw = json.dumps(page.text)
			file1.write(raw)
			file1.close()

	file2 = open('courses.json')
	a = file2.read()
	b = json.loads(a)
	c = json.loads(b)
	courses_list = c["availableCourses"]
	i=0
	while i<len(courses_list):
		course_name = courses_list[i]['name']
		course_id = courses_list[i]['id']
		i+=1
		print(i,course_name)
	user_input=int(input("In which code you wants to Enroll:- "))
	print("")
	print("This is your Enroll course list")
	print("")
	user_input-=1
	file_name = "course_topic//Topic%s.json"%(user_input)
	print('course id',courses_list[user_input]['id'],'and course name',courses_list[user_input]['name'])
	courses_api="http://saral.navgurukul.org/api/courses/%s/exercises"%(courses_list[user_input]['id'])
	id=courses_list[user_input]['id']
	course_request=requests.get(courses_api)
	convert=course_request.json()
	v=convert['data']
	for i in range(0,len(v)):
		print(i+1,v[i]['name'])

	user_input2=int(input("In which page you want to visit:-  "))
	slug=v[user_input2-1]['slug']
	print("")
	print("Topic Name and content")
	print("")

	slug_make = "http://saral.navgurukul.org/api/courses/%d/exercise/getBySlug?slug=%s"%(id,slug)
	course_api_slug=requests.get(slug_make)
	raw = course_api_slug.json()
	Topic_id=raw['content']
	Topic_name=raw['name']
	print(Topic_name,Topic_id)

request_api(saral_url)
