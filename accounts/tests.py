from rest_framework.test import APIRequestFactory

def test_teacher_register():
    factory = APIRequestFactory()
    request = factory.post("api/users/",{
	"username" : "student1" ,
	"email" : "student1@student.com",
	"password" : "p@ssword1",
	"type": "STUDENT"},
        format='json'
    )
    assert request.status_code == 200

def test_student_register():
    factory = APIRequestFactory()
    request = factory.post("api/users/",{
	"username" : "teacher1" ,
	"email" : "teacher1@teacher.com",
	"password" : "p@ssword1",
	"type": "Teacher"},
        format='json'
    )
    assert request.status_code == 200

def test_student_login():
    factory = APIRequestFactory()
    request = factory.post("/api/token/login/",{
	"username" : "teacher1" ,
	"password" : "p@ssword1"},
        format='json'
    )
    assert request.status_code == 200

def test_teacher_login():
    factory = APIRequestFactory()
    request = factory.post("/api/token/login/",{
	"username" : "teacher1" ,
	"password" : "p@ssword1"},
        format='json'
    )
    assert request.status_code == 200

