- Re-taking some notes on lectures so that I can remember them a little better
# Common Gateway Interface
It is the interface that allows a web server to run an external program to process the requests. This way you can separate the web server and web application from each other.

Web applications use the web servers to generate dynamic content.

Note that web applications can be written in compiled or interpreted programs, but typically interpreted programs are preferred because they are easily portable, very flexible, and easy to use. Most importantly, the speed bottleneck of website is network speed, rarely ever the speed of the programming language.
# Runtime Environment
The hardware and software infrastructure used for running the code, as opposed to the code itself. For example, your PC and CPython make up a Python runtime environment. Node.js makes up a Javascript runtime environment, and it's out choice for web development.
# Backend Frameworks
Libraries on the server-side we use to help build a web application. A few popular examples are ExpressJS, Django, and Ruby on Rails.

Before the 2010s, we typically used libraries that did backend and frontend work. However, this design causes coupling of the back and frontends. In more modern websites the back and front ends are typically decoupled from one another. Furthermore, this helps to enable the use of multiple frontends, so we can change website behaviour on different devices.
# Web API
Stands for application programming interface, it is the way applications communicate with each other. Web applications communicate with HTTP requests. The front and backends communicate with each other using Json.
# REST API
Representation state transfer. REST describes a particular architectural style with a set of constraints and principles
1. Use HTTP verbs to define operations
	1. So actions and occurrences
2. Resources should be nouns identified through URIs
	1. We perform CRUD operations on resources
3. Stateless client-server communication, as opposed to stateful
4. Defines method semantics that enable caching and retries.
	1. For example, GET requests cannot modify any data
5. Client must interact through the system through exclusively the API interface

For example, lets say you are building an API endpoint for transferring money across bank accounts.

Using the endpoints `/transfer` or `/create` are not good because those are verbs, and resources must be a noun. Instead use `/transaction/42` where the transaction is the resource, and this value increments for every new transaction.

- **There's an exercise for this one I should do if I have time**
# Start New Project
- I'm pretty used to package managers, so I shouldn't struggle with `npm`

Packages for a project are installed locally, and the dependency tree is tracked inside `package.json`
- Should be checked into your repo
 
You can create a `package.json` with `npm init` and install things with `npm install`.
- And npm has no default output like a super chud pm

Run the server locally with `node --watch server.js` where the `watch` flag allows the server to restart whenever changes are made to `server.js`.
# Route Handler
Handles HTTP requests for a specific URL path. For example, `app.get("/hello", (req, ...))`. GET is the HTTP method, `/hello` is the endpoint, and the function inside is the request handler.

Req is the request object, and res is the response object.

Acting on the response object, you can `.send` an HTTP response, report a `.status`, send a `.json` response, and a few other things, like redirection, downloads, or end the response.

Sometimes, parts of the URL can be dynamic. These can be captured and used by the request handler. For example, if you have `/users/123` you might try something like `/users/:userId` to claim 123 as the ID of your user. These captured parameters are stored in `req.params`.

Express.js routes as handled from top to bottom (including middleware), so you should try to handle specific routes first, and then general routes last.

For example:
```js
app.get("/users/", (req, res) => res.send("My User"));
app.get("/users/:id/", (req, res) => res.send(`User ID: ${req.params.id}`));
app.get("/users/all/", (req, res) => res.send("All users"));
```
For the URL `/users/all` `/users/:id` will run because it is listed first.
# Organizing Routes
In large projects, routes are typically organized inside a routes folder.

A few notes here:
- Store subsets of routes in appropriated named files
- Create a Router object in these files. Use it instead of app
- Import the routes file in the main server file, use the Router in there.
	- You need to explicitly declare this

If you need to handle multiple CRUD operations as the same method, you can use the `router.route` method to accomplish this. Simply chain them all together.
# Middleware
Functions that modify the request or response. Allows for separation of concern. You may for example have a middleware that logs data, or parse Json requests, or does basic auth.
# Event Loop
JS runs in a single thread, and uses an event loop to provide the illusion of multiple running threads.

New events are pushed into the event queue, and the event loop constantly checks for new events to execute their callback

Oftentimes, because of these callbacks, we need to nest code, resulting in unmaintainable codebases. An alternative to callbacks is instead to use Promises. They are pushed into the event queue, and then handled later when it is done.

Promises have a pending state, resolved state, and rejected state.

Although promises are much better, typically it is more standardized to use `async` functions and `await` for functions that require being pushed into the event queue.
# Database
For persistent storage, we need a database to store our data. Relational databases use SQL, and non-relational databases do not use SQL. Unfortunately for us, direct database is use can be complex, and typically needs knowledge in SQL.

Instead, we will use object relational mappers, an ORM. They provide an abstraction for the underlying database and so we can interface with it directly in whatever languages we are used to. Method called are translated to queries, and results are encapsulated in objects.

ORMs are known for their simplicity and flexibility, however they are quite slow. Therefore, they are typically used for prototyping. Once a project gets large enough, and stable enough, the ORM is swapped out for a custom made interface.

