# Immediately Invoked Function Expression
A JS function that runs as soon as it is defined
- Typically created anonymously, and create a private scope to avoid polluting global namespace

Originally used as a workaround before modules for initialization logic.
# Closures
The nesting of functions where the inner function as access to local variables in the outer functions
```js
function outer() {
	var b = 10;
	var c = 100;
	
	function inner() {
		var a = 20;
		console.log("a = " + a + ", b = " + b);
		a++;
		b++;
	}
	
	return inner;
}
var X = outer(); var Y = outer();
```
Something interesting to note is that the scope of `X` and `Y` will include their own `b` and `c` variables. If you call `X` twice, it will increment `b` from 10 to 11. But if you call `Y` afterwards, `b` will remain 10.

This process is called *capturing* variables.

Inside of a for-loop, `var` declares a variable once and updates its value, `let` re-declares the variable
```js
function outer() {
	let a = [];
	for (var i=1; i<=5; i++)
		a.push(function() {
			return i;
		});
	return a;
}
```
If you call every single one of these functions in `a`, you will get 6, 5 times.
# Object
Python dictionary, or a HashMap, but the key does not need to be a string

Here we may go over the difference between `null` and `undefined`. They are roughly the same thing, but `null` is typically used by programmers to denote that there is no value, but `undefined` is used in the case where an error occurred.
- This is mostly for readability purposes
# Array
Objects and arrays are mutable, but other data types are immutable.

You can unpack or *destructure* objects in the same way that you would in Python

Aliasing, deep copied, and shallow copies all exist in JS
# Class
Special function that creates an object. It has a constructor and supports inheritance, similarly to other OOP languages.
# Template Literals
The same thing as formatted strings in other languages
```js
const name = 'Alice';
const age = 25;
const greeting = `Hello, my name is ${name} and I am ${age} years old.`;
```
# Arrow Function
More concise function setting
```
(params, ...) => <expression or body here>
```
For example:
```js
function regular(a, b) { return a + b; }
```
Can be shortened to:
```js
const concise = (a, b) => a + b;
```
For a single parameter, you can drop the brackets
# Functional Programming
`foreach` does something for every element and its index
```js
var names = ["ali", "hassan", "mohammad"];
names.forEach((item, index) => console.log(index + ": " + item));
```

`map` modifies every element of an array
```js
upper = names.map(item => item.toUpperCase());
// ['ALI', 'HASSAN', 'MOHAMMAD']
```

`filter` returns a new array, keeping only the elements satisfying some condition
```js
var students = [{name: "Jay", id: 1}, {name: "Ali", id: 2}, {name: "Jay", id: 3}]
let jays = students.filter(item => item.name === "Jay");
// [{name: "Jay", id: 1}, {name: "Jay", id: 3}]
```

`reduce` returns some aggregate value after processing an array
```js
var names = ["ali", "hassan", "mohammad"];
let longest = names.reduce((acc, cur) => Math.max(cur.length, acc),
	Number.NEGATIVE_INFINITY);
// 8
```
# Arrow Function and this
Regular functions have their own `this` value, but the arrow function does not. However, we can use the arrow function to capture `this` inside of a closure
```js
const person = {
	name : 'King Bob',
	greet() {
		setTimeout(() => console.log(this.name + " says hi!"), 500);
	}
};
```
Here, we use the arrow function to capture the value of `this` from the object `person`. If we use `function ()` as opposed to `() =>` we will no longer capture the `this` from `person` and it will fail.
# Web Server
Listen for HTTP/HTTPS requests
- We will use Apache and Nginx in this course, because they are open source

They are responsible for handling incoming connections by generating a response, fetching files, and act as a proxy between the client and origin server.
- Responses make up dynamic content, and files make up static content
- Forward proxies sit in front of client devices before internet access, and reverse proxies in front of the origin server, after internet access
# Forward Proxy
Used to block or monitor content. Can improve security by hiding someone's IP address. Or you could use one to circumvent regional restrictions
# Reverse Proxy
Caches content for a potentially distance web server, acts as a front end for security purposes, and provides load balancing.

Say we have a website with numerous servers. If we have millions of requests, then we need a load balancer to distribute the concurrent request across the servers for optimal performance.

This means your website can respond to spikes in demand, it secures it from DDoS attack, and can reduce energy consumption during low traffic.
# Web Server Architecture
A single threaded server would accept some request, read it, process it, write something, and then close the process. Of course, a single threader server can handle just one connection at a time.

Multi-threaded servers would spawn a new thread every time a request is received. The main thread is exclusively responsible for accepting requests and creating new threads. This is faster, but very expensive.

One way to circumvent this is to use a thread pool. It creates a task queue, and then the threads will sit and wait until something in the task queue appears.
- After HTTP requests, typically a request to a web server is made. These types of web servers are typically blocked waiting for the database
- Apache uses this method

Event-driven web servers queues events and executes them in some order. Each request is broken up into states, and each state is processed asynchronously.
- There is no overhead from switching threads, and we can combine this with a high thread pool to utilize many physical CPU cores
- This basically means that, while Nginx is waiting, it will work on something else

**MIDTERM CONTENT ENDS HERE**
