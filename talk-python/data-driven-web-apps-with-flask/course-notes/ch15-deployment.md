# Chapter 15 - Deployment

## Deployment overview and topology

- Ubuntu 18.04 Server in the Cloud
- Nginx
    - the thing people will actually talk to
    - listens on port 80 for regular HTTP and 443 for HTTPS encrypted traffic
    - request comes here but this does not run our Python code
    - it serves up static files and delegates to the thing that runs our Python code
- uWSGI (micro WSGI)
    - Handles our Python requests
    - We don't want to just run one of them; Python has the Global Interpreter Lock (GIL) which inhibits parallelism 
    within a single process.
    - The ways people get parallelism in Python is to create multiple processes
    - This has great benefits for fail over if something goes wrong with some process running one of our requests we 
    can kill it and have other processes deal with it
    - It is not the only way to get parallelism but it is one really nice way
    - We will hav uWSGI spin off a whole bunch of itself which will actually run our Python code
    - It will host the Python runtime and it's going to launch and initiate a bunch of copies of our website running in 
    parallel.

**Flow**

1. Requests will come in, hopefully over HTTPS (you want to set up some sort of encrypted layer)
1. Once inside the server, we do a regular HTTP request over to uWSGI itself
1. uWSGI will decide which of its worker processes is ready to handle it and pass the request to it
1. uWSGI will return the response back through NGINX back out over HTTPs to the client

