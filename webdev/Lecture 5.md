Recall that last time we stopped while discussing web servers.
# Common Gateway Interface
Allow web servers to run external programs to process requests.

Help to separate the web server from the web application, to the application can use any web server.

A number of standard gateway interfaces are:
- Web server gateway interface: Python
- Rack: Ruby
- JavaScript gateway interface: JS

Typically, interpreted languages are used in web programming, because most servers are bottlenecked by the network, as opposed to the code execution.
- RAM access is $10^{6}$ faster than network access
- It is easier to edit and change interpreted languages
# Runtime Environment
The hardware and software infrastructure for running code.
- CPython is the interpreted for Python, for example

For our purposes, we will be using Node.js
## Backend Frameworks
Server-side libraries to help build a web application. Helps to avoid building everything from scratch.

Some examples include Django for Python, ExpressJS for JS, and Ruby on Rails.
# Early Web Architecture
![[Pasted image 20260203152335.png]]
Before the 2010s application servers typically returned HTML content back to the client.

This version is called the full stack framework because the libraries are attempting to do the front and backend work at the same time.
- This coupling results in a poor separation of duty
- Dedicated frontend frameworks like React do not work in this paradigm
![[Pasted image 20260203152827.png]]
In the modern day we typically use one backend with multiple frontends.
# Web API
These are the method services uses to communicate to each other.
- API stands for application programming interface

Web applications use HTTP requests, backend is responsible for data retrieval and manipulations, so we need to use something for the front and backend to communicate.

Typically, we use JSON, JavaScript Object Notation. It is the most popular standard for backend responses.
# REST API
Representation State Transfer. It is a architectural style with a set of constraints and principles.
1. Uses HTTP verbs to define operations on resources
2. Resources should be nouns identified through URIs
	1. Only CRUD operations: Create, Retrieve, Update, Delete
3. Stateless client-server communication
4. REST defines method semantics that enable caching and retries
	1. GET requests must not modify data, which allows responses to be safely cached
5. Client interacts with the system only through the API interface

Example:
Transferring money across accounts

Lets say we have some endpoint like `/accounts/transfer` or `/transaction/create`. Well neither of these are REST because both of these are verbs.

The proper method is to use `/transaction/`, `/transaction/42/` and then use POST to create an object, PUT to request to update an object etc.
# Node.js Project
ExpressJS is just a package library, so we can use `npm` to install it.

So, how do we keep track of numerous projects?

`package.json`
- Tracks the libraries for your project
- Should be check into your repository

You can create a `package.json` with `npm init -y`
## Setup Express.js
Just run `npm install express`

Create a barebones server file like this:
```js
const express = require('express');
const app = express();

const port = 8000;
app.listen(port, () => {
	console.log(`Server started on port ${port}`);
});
```
And then run the server locally `node --watch server.js`
# Route Handler
Responsible for handling HTTP requests for a specific set of URL paths
```js
app.get("/hello", (req, res) => {
	res.send("Hello, world!");
});
```

In this case we have the handler on the `/hello` endpoint. The request handler is some function that typically takes the request and the response.
## Response Object
Include a number of methods like `send`, `status`, `redirect`, `json`, `download`, `end` and so on.
## Route Parameters
Parts of a URL can be dynamic like `/users/123/` where that last portion might be changed. The route parameters can be captured and used in a request handler like: `/users/:userId/`

Captures parameters are stored in `req.params`
```js
const userId = req.params.userId;
```

In larger projects, we may have hundreds of routes we would like to organize. Conventionally, we use a routes folder to manage this.
- You accomplish this by creating a router object inside a routes file, and then import the routes file

Inside the main server we might have:
```js
const express = require("express");
const app = express();

// Import the user routes
const userRoutes = require(
"./routes/users");
// Mount the user routes at `/users`

app.use("/users", userRoutes);
app.listen(3000);
```

Where the routes file is:
```js
const express = require("express");
const router = express.Router();

router.get("/", (req, res) => {
	res.send("List of users");
});

router.get("/:id", (req, res) => {
	res.send(`User ID: ${req.params.id}`);
});

router.post("/", (req, res) => {
	res.send("User created");
});

module.exports = router;
```

We can also handle numerous methods for each API endpoint by defining them in groups:
```js
router.route("/:id")
	.get((req, res) => {
		res.send(`Fetching user with ID: ${req.params.id}`);
	})
	.put((req, res) => {
		res.send(`Updating user with ID: ${req.params.id}`);
	})
	.delete((req, res) => {
		res.send(`Deleting user with ID: ${req.params.id}`);
	});
```
# Middleware
A function we use to modify the request or response. It allows a separation of concern that can be used for things like authentication, logging, error handling etc. Typically used to handle general concerns as opposed to specific ones.
# Template Languages
Adds imperative programming features to making HTML files. Enables dynamic content injection, it is typically used in server-side rendering and email templating.

You just need to install some template language like EJS `npm install ejs`, set EJS as the template engine, and call the render method with data.
