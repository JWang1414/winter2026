Here, we discuss web deployment.
# IP Address
Production servers need an IP address for people to connect to. Generally, we used static IP addresses, which are fixed, and required to setup load balancers and gateways.

Dynamic IPs are most often used for end-user devices like laptops.

Modern backends are often ephemeral, and so started on demand by cloud service providers, instead of staying around forever.
# Domain Name
For people to connect to your IP address, you will need a domain name. You purchase one of these from the domain name registrar.

There are a few common DNS records
- A records map domain names to an IPv4 address
- AAAA records map a domain name to an IPv6 address
- CNAME records map a domain name to another domain name
- MX records direct emails to a mail server
# Web Hosting
There are a few approaches to web hosted. The rarest is dedicated, on-site hosting. This is essentially dedicating a physics server for your website. This can be particularly limiting, because it is challenging to scale, and difficult to maintain uptime.

It is most often in the modern day to use cloud hosting services. Either IaaS or PaaS. These being infrastructure and platform as a service respectively. Notable, IaaS gives you control over the runtime, middleware, and operating system, which PaaS does not.
# IaaS Deployment
We manage Node.js applications using the PM2 process manager. It is basically an init system, allowing automatic restarts, automatic startups, and clustering.
- Clustering is the process of creating multiple instances of an application across multiple CPU cores

Once you've deployed onto IaaS, you deploy your React project by configuring your web server.

This web server acts as a reverse proxy.

After the config file for your web server is complete, you just need to add it as a symlink to the nginx enabled sites to begin hosting.

To host with HTTPS, you need to have an SSL certificate.
