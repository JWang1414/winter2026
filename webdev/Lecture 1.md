Lets begin with the end user perspective for the use of a website. Whenever you access a website, what happens is:
- You attempt to access some address
- Your browser sends a request to the server on your behalf
- The server processes your request, and responds with a web page

So what is the world wide web made of?

Well, the internet is effectively an interconnected network of computers, which communicate with each other using a set of protocols. Often TCP/IP and HTTP/HTTPS.

TCP/IP includes the end-to-end communication between two applications

HTTP/HTTPS is the delivery protocol for the web.
# Internet Protocol
All computers have a unique IP address. This protocol facilitates the routes of data from and to the destination computers, typically sent in bunches called *packets*.
- Packets are routed through a number of middle-men. Sometimes, you might have a packet that two different routes. This is an example of duplication

Unfortunately, it's not the most reliable. Packets can bet lost, reordered, duplicated, or corrupted. There are two versions of IP, IPv4 and IPv6, which use 32-bit addresses and 128-bit addresses, respectively.
# Transmission Control Protocol
Allows multiple virtual connections to share a single IP address using port numbers.

Helps to make connections reliable by using:
1. Sequence numbers. Ensuring the correct ordering of packets
2. Data checksum. Detecting packet corruption
3. Acknowledgement. Sending a message for each successfully received packet

![[Pasted image 20260106154021.png]]
An example of two computers communicating with each other
# Domains
Allow us to use another way to access websites. We no longer need to remember IP addresses, and it lets us move websites elsewhere
- This arises because IP addresses are associated with locations. And so if we swap the host server, we need to change the IP address. A domain solves this issue
- Some websites are hosted on numerous machines

Domains map their names into IP addresses. This translation is called *resolving* a domain name
- Imagine a phone book
- google.com $\to$ 142.251.41.78

But, this still doesn't answer the question: How do we find the Domain name system (DNS) server?
- Well, they can be assigned by the system administrator
- Typically they are configured when a computer connects to the Internet
# Hypertext Transfer Protocol
HTTP servers typically listen on port 80, and HTTPS listen on port 443. They are protocols for distributing and accessing hypertext documents
- HTTP is plain text, and HTTPS is encrypted
- Holy terrible idea
![[Pasted image 20260106155823.png]]
Example HTTP message
![[Pasted image 20260106160015.png]]
List of some common HTTP methods

- There's also a list of possible response codes, but I won't write them here
# Uniform Resource Locator
A string reference for a web resource, formatted as hyperlinks
- Composed of a protocol, domain name, and resource name
- For example: `https`, `utoronto.ca`, and `current-students`

Some characters are unsafe in URLs, like the space, which must be represented as `%20`
# Stateless/ful Protocol
HTTP is a stateless protocol, that is, it does not remember your previous interaction with their clients. Stateful servers react differently to the same input, based on the state of the connection.

An online banking service, for example, must remember if you have logged into an account. The stateless server essentially gives a cookie to the client to be passed back later, so it can remind the server of the previous step.

Stateful servers are much the same thing. Stateful servers remember information about sessions. They are more complicated to implement, and a server crash can potentially result in the loss of session states. Furthermore, as there is an increased number of users, the amount of data you need to save increases.

Stateless servers, however, are easier to design, and easier to scale and optimize. Of course, you need cookies for anybody to remember anything. So there are pros and cons to both approaches.
# Markup Languages
Languages that provide control over the organization of document content. Includes Markdown, LaTeX, and SGML, the precursor to HTML and XML.

SGML is a declarative language that exclusively described document structure, without touching upon presentation, which is typically handled by the browser.
# Hypertext Markup Language
HTML emphasizes the structural semantics of elements, described within tags
```
<img src="portait.jpg" alt="me">
```

There are two types of elements, regular and void elements. Regular elements have a closing tag, and can include nested elements. Void elements have no closing tag, and therefore cannot nest anything.

![[Pasted image 20260106163032.png]]
Here is an example HTML file

Notice that everything must begin with an `<html>` tag. Everything else is composed of a head and body tag.
- The head portion is not shown, it specifies information about the document

HTML also has a whole thing called attributes. A few examples include `id` and `class`.

Some characters must be escaped using HTML entities. For example, > becomes `&gt`.

You can organize elements with the `<div>` and `<span>` tags, which are block level and inline elements, respectively. That is, `<div>` shows up on a new line.