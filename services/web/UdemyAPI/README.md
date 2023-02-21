## Welcome

This repository provides you with a simple interface to interact with the Udemy API.

All you need to do is:
 - Get an API client from [here](https://www.udemy.com/user/edit-api-clients/)
 - Then use the module :)
 - Feel free to extend or modify it as you would like to!

You can either set the udemyClientID and udemyClientSecret environment variable or specify them as keyword arguments.
All the API functions are supported with additional query parameters 

## Example
> In order to use the os environment variable defined clientID and clientSecret
```python
from udemy import *
Client = PyUdemy()
Client.get_publiccurriculumlist(courseID = "1967128",page=1)
```
> In order to specify as keyword argument the cliendID and clientSecret
```python
from udemy import *
Client = PyUdemy(clientID = '<clientID>', clientSecret = '<clientSecret>')
Client.get_courseslist()
```
