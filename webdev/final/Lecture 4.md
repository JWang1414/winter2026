The back-end of a web site focuses on the data access, data storage, and business logic. It is part of the server. It is also the focus of this lecture.
# Web Server
The technology responsible for listening on a specific port, and then handling the incoming connections. It can generate responses, fetch files, and act as a proxy.
# Forward Proxy
Sits in front of client devices, before Internet access.

Forward proxies are the local connects you use to connect to the internet. They can be used to monitor content, hide your IP address, and sometimes circumvent regional restrictions.
# Reverse Proxy
Sits in front of origin server, after Internet access.

Responsible for caching content for a distant web server, a front for security purposes, and provide load balancing.
# Web Server Architecture
Single-threaded servers run on just one thread. They handle requests one at a time, and if a new request arrives, it must wait until the current one is done.

Multi-threaded servers create a new thread every time to handle a request. So there is a thread for each request. This means there's less waiting, but creating threads is very expensive.

It is more often that we use multi-threaded servers with a thread pool. That is, there is some static number of threads available, and whenever a request is made, it is passed off to one of those existing threads.
- If all the threads get filled up, presumably you have to wait, but this is still much faster

However, now a new issue arises. Your threads will likely spend a lot of time waiting for the database's response. This is a bottleneck to overcome.

One method of circumventing this is using an event driven web server. In this case, one thread can handle numerous requests, and each request is broken up to several sub parts.

For example, a thread can accept, read, and process a request. But, while that request is still being processed, accept another one and read it as well. So, while it's waiting for the database to respond, it covers some ground.

This sort of event driven framework is what is used by Nginx.
# Common Gateway Interface
Allows web server to run an external program to process requests. Separates web server from web application.

As long as a language can understand HTTP, it can be used in the back-end. However, most web languages are interpreted for a number of reasons:
- Portable to numerous operating systems
- Code doesn't need to be compiled
- Slow, but the bottleneck is the network speed anyways
# Runtime Environment
The runtime environment is the hardware and software infrastructure for running your code. It isn't your language. A few examples include CPython, Node, and PHP interpreter.
# Full Stack Framework
Historically, the front-end and back-end were coupled together. In the modern day, however, we separate the front-end and back-end to separate the logic.

This also enables the use of one back-end with numerous front-ends.
# Web API
API (application programming interface). The way in which applications communicate with each other. For web applications, this is HTTP requests.

The front-end and back-end typically communicate with each other using JSON.
# REST API
Representation State Transfer. It is a style with a set of constraints and principles.
1. Uses HTTP verbs to define operations on resources
2. Resources should be nouns identified through URIs
	1. Perform CRUD operations on resources
3. Requires stateless client-server communication
4. REST defines method semantics that enable caching and retries
	1. GET requests cannot modify data
5. Client interacts with the system only through the API interface