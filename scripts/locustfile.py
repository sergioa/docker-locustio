from locust import HttpLocust, TaskSet, task


class PractitionerTaskSet(TaskSet):
    @task
    def get_practitioners(self):
        self.client.get('/UserManagement/Practitioner')


class UserManagement(HttpLocust):
    task_set = PractitionerTaskSet
    min_wait = 5000
    max_wait = 15000


if __name__ == '__main__':
    UserManagement().run()
