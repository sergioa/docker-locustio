from locust import HttpLocust, TaskSet, task

class DeviceTaskSet(TaskSet):
    @task
    def get_devices(self):
        self.client.get('/DeviceManagement/Device')


class DeviceManagement(HttpLocust):
    task_set = DeviceTaskSet
    min_wait = 5000
    max_wait = 15000


if __name__ == '__main__':
    DeviceManagement().run()
