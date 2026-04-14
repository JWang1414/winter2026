Javascript is the most popular method of programming the front-end and back-end of websites.

There are a few main ways to run Javascript
1. Within a browser, embedded in HTML or in the browser console
2. Inside of an interpreter like Node JS

There are several ways to declare variables in Javascript. `var` creates it in function scope, and `let` creates it in block scope. This is a crucial difference that I will review shortly.

JS functions can accept any number of arguments without error. Missing arguments are given the value `undefined`, and without a return statement, functions will return `undefined`.
# Scope
The global scope consists of variables outside of any function. They can be accessed anywhere.

Function scope includes variables defined anywhere inside functions, and they're exclusive to that function.

Block scope is variables accessible inside only the block it is declared in.
# IIFE
Immediately Invoked Function Expression

These are functions are run as soon as they are defined. They were a workaround before modules for initialization logic
# Closures
Since JS is functional, functions can be defined inside another functions, and returned.

In combination with `var` and `let`, this means we must be very careful with the scope that is being used. `var`, for example, can have unexpected behaviour inside for-loops
# Arrow Function and this
Unlike regular functions, arrow functions do not have their own `this` value. So, you can use them to capture the `this` from its lexical scope.