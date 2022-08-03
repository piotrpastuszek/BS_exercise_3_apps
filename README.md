# BS_exercise_3_apps

APP's made for DevOps School.

APP 1 - reading json file - if file has correct form, app posting it to RabbitMQ queue, if not app return 400 Bad Request error.

App 2 - listening on RabbitMQ queue, consuming messages and passing it to Redis data base with TTL 60s.

App 3 - printing out number of objects stored in Redis.



UPDATE - 23.07.2022

Now for each app there is Containerfile to bild images of this app's.

UPDATE - 30.07.2022

Now there is requirements.txt files to every Containerfiles

