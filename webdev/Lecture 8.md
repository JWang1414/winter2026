# Aggregate Query
A method of making a calculation to retrieve a singe result across many records. This might be a count of records, or an average over a particular field.
```js
const result = await prisma.order.aggregate({
	_avg: { totalPrice: true },
	_sum: { totalPrice: true },
		where: {
		isPaid: true
	}
});
```
To count the number of records, instead use the count method,
```js
const result = await prisma.order.count();
```
An aggregate field on the other hand is a computed field returned inside a select query:
```js
const users = await prisma.user.findMany({
	select: {
		id: true,
		name: true,
		_count: {
			select: {
				posts: true
		}
	}
}
});
```
So here we are selecting all the users, and then counting the number of posts they have.
- Specifically, we select the `id`, `name` and `_count` values.
# Real-Time Communication
HTTP is always initiated by the client, that is, they need to send a request to receive a response. Because the server cannot push data to clients directly, we cannot have real-time features sent to users.

We need bidirectional communication. For this we use Socket.io, which provides event-based bidirectional communication.

The client and the server maintain a persistent connection, and both sides may emit and receive events.
- Outside of initialization, the code on both programs is very similar

Both Socket.io and Express use port 3000, but they can still be run at the same time.

A *room* is a logical group of sockets, managed by the server. 
# Third-Party API Integrations
There are plenty of challenging things to implement that we might want to use. We should be using third-party services so we don't need to build something from scratch.

A number of common 3rd party apps are:
- Google maps
- OpenWeatherMap
- SMS or email APIs
- Payments
# Client-Side JavaScript
Going back to the front-end, we can see how to use JS on the client-side.

Syntax is identical, but there are a few important global variables to work with:
- `window`
	- Represents the browser window
- `document`
	- Represents the document object model, and allows interaction with HTML elements
- `location`
	- Contains information about the current URL
- `alert`, `confirm`, `prompt`
	- Displays dialog boxes to the user
- `localStorage`, `sessionStorage`
	- Provides persistent storage across sessions or page reloads
# Document Object Model (DOM)
JS can be placed into HTML in a few different ways
1. Inline
2. External JS file
3. As an event attribute
	1. In particular, doing this allows us to run JS code specifically when an event occurs, like a form being submitted

When a page is loaded, the browser creates the DOM tree of the page. Each element is called a DOM node.
- The HTML tag is the root node, and is the ancestor of all nodes

Scripts access the DOM elements through `document`, which recall is a global variable with a number of methods.
![[Pasted image 20260307173955.png]]
Here is an example of a DOM tree
- The HTML node is missing here

Using `document` we can do things like get elements, or select queries.
- Look ups can be done by id, class names, and tag names
- Query selectors instead filter by the CSS selectors

Every DOM nodes has references to related nodes. These come in the form of things like `firstChild`, `parentNode`, `nextSibling`, `childNodes` etc.

We can manipulate elements using JS. For example, changing the style, class name, and the content inside.
```js
let body = document.body;
body.innerHTML = "<h3>hello!</h3>";
h3 = document.getElementsByTagName("h3");
h3.style.color = "green";
h3.setAttribute("class", "title");
console.log(h3.getAttribute("style"));
```
# Event
JS is an event driven programming language. These events can be monitored by the browser, so we can react and change things according to user input.

There are two main event types. Document and element events.

Document events
- Occurs to the entire page
- Eg: `onload`, `onkeydown`, `onkeyup`
- By convention, scripts should exclusively run after the `onload` event, so contents will be completely loaded prior to running a script
	- That is, our JS code should run as an event after `onload`

Element events
- Occurs to a specific element, typically of a specific type of element
- E.g., `onclick`, `onmouseover`, `ondrag`, `oncopy`, `onfocus`, `onselect`, `onsubmit`
# Event Listener
There are two ways to add an event listener function
1. Set the event property of a DOM element to a function
```js
h1 = document.getElementsById("page-title");
h1.onclick = function() {
	this.innerHTML = "you just clicked on me!";
};
```
2. Set the event attribute of an HTML element to a function
```js
<script>
	function h3click(h3){
		h3.style.color = "blue";
	}
</script>
...
<h3 onclick="h3click(this)" onmouseover="console.log(new Date())"></h3>
```
