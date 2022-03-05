branch 5.2-submission - 

I wasn't able to complete this project in windows, I will come back to investigate it.  I ran the project on an AWS instance and was able to complete the work there.

 I was able to get the services running on windows, but starting the service like this:

$ ADMIN_USER=admin ADMIN_PASSWORD=admin docker-compose up -d

I can not get logged into grafana with "admin/admin".   I do get the login screen.  I even logged into the running docker container and successfully changed the password with the grafana-cli utility, but still couldn't login in the grafana screen.

When I ran it on AWS, I was able to login to both.      The login was over http, I think it would improve the liveProject to make that https (maybe that is in a future lesson)

