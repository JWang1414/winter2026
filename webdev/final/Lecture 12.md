# Web Security
The particular goals of web security are: confidentiality, integrity, and availability.
# Security Terms
A vulnerability is a flaw in a system.

A threat is the potential to exploit a vulnerability, like a hacker.

And an attack is the actual exploit used to cause harm.
# Key Strategies
- Properly sanitizing all possible inputs
- Authentication, identifying and verifying users
- Placing expiration times on tokens or sessions
- Including 2FA
- Lock account after failed attempts
- Implementing a strong password policy.
# Cross Site Scripting
Attacks where JS is run on the victim's browser.

Reflected attacks are attacks that are run immediately, and returned by a server-side script

Persistent attacks are stored on the target server, and affects anyone who accesses the data.

One example of a reflected XSS attack might be abuse a vulnerability in a search query. If somebody is fooled into clicking a malicious link using the query, then they could steal our data.

A persistent XSS attack could be a malicious social media post that has a hidden piece of JS inside. Anybody visiting this page will be affected by the attack.
# Same Origin Policy
A policy introduced by Netscape in an attempt to prevent the data from one website being accessed by another.

If you have a website that has numerous origin points, you would need to setup cross-origin resource sharing (CORS) to bypass the policy.
- The browser is responsible for enforcing CORS rules, not the web server.

Notably, XSS attacks are not mitigated by SOP, because they typically originate from the correct server.

We can really just use input sanitization, input encoding, secure cookies etc.
# Cross-Site Request Forgery
Tricks an authenticated user into performing unintended actions.

This happens if, for example, a user logs into an important account, before clicking a link to a malicious website. Because they have already logged into this account, a form from the malicious website using the correct credentials appears legitimate.

We prevent this from happening using CSRF tokens. These are randomized tokens that are generated with every HTML form. Without the correct token, the form is rejected. CSRF tokens change very frequently, and without knowing the signing key, are very challenging to figure out.

Another common defense is the is the use of same site cookies. Which prevents cookies that are sent from different sites.
# DNS Poisoning
Occurs in the case of a compromised DNS server. This allows a hacker to direct any domains to a malicious version of the same website, in an attempt to steal your information.

The defense we use here is HTTPS. It is responsible for verifying the server's cryptographic identity, not just the IP.