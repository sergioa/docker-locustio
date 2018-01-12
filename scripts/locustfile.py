from locust import HttpLocust, TaskSet, task

HOST='http://sweng_loadtest.emea.roche.com:8080'


class PractitionerTaskSet(TaskSet):
    @task
    def get_practitioners(self):
        self.client.get('/UserManagement/Practitioner')


class UserManagement(HttpLocust):
    task_set = PractitionerTaskSet
    host = HOST
    min_wait = 5000
    max_wait = 15000


if __name__ == '__main__':
    UserManagement().run()
