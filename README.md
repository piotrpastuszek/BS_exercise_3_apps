# BS_exercise_3_apps

APP's made for DevOps School.

APP 1 - reading json file - if file has correct form, app posting it to RabbitMQ queue, if not app return 400 Bad Request error
App 2 - listening on RabbitMQ queue, consuming messages and passing it to Redis data base with TTL 60s.
App 3 - printing out number of objects stored in Redis 
