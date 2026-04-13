TCP/IP are the protocols that provide reliable end-to-end communication between two applications on different computers

HTTP(S) is the protocol for the delivery of contents on the web.
# TCP/IP
IP is the "internet protocol". Each computer on a network is given a unique IP address.

It's responsible for sending data/packets, and routing it to the destination computer.
- It's pretty unreliable though, and packets can be corrupted

TCP is the transmission control protocol. It enables multiple virtual connections to share a single IP address. Each connection is identified with a port number.

Makes connections reliable by ensuring the correct ordering of packets, detecting corruption, and sending an acknowledgement.
# Domains
Provide an easier method of remembering addresses. Furthermore, since domains can be tied to numerous addresses before being resolved, it makes it easier to migrate servers, or use numerous servers.

Essentially, a domain name is mapped to an IP address. This is called resolving the domain.

Resolving is done by a DNS server. Where DNS means domain name system. The DNS server is manually configured by the system administrator, or automatically configured.
# HTTP
Hypertext Transfer Protocol. Responsible for distribution hypertext documents.
- Built on-top of TCP/IP
- HTTP is human readable, but HTTPS is encrypted

HTTP messages are composed of requests and responses.

Requests are composed of a method, path, header, and body. Responses are composed of a response code, header, and body.
# Uniform Resource Locator
These are URLs. They are strings that reference web resources. Some characters are not safe in documents, and so URLs must be encoded.
# Stateless Protocol
HTTP servers do not remember previous interactions.

A stateful server, on the other hand, reacts differently to the same input.

Stateful servers need to keep a lot of information. They are challenging to scale, and hard to implement. Stateless servers are simple and easy to scale.

Generally speaking, the server will ask the user to save a cookie. This cookie is responsible for remembering the previous session state.