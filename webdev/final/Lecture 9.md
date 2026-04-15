# Rendering Patterns
Describe how a website is rendered. Each with their own pros and cons

1. Server-side rendering (SSR)

Consists of a back-end server sending a number of static files. Separate requests are used for each static file, and the browser rendered the HTML, CSS, and scripts

The simple web pages make them fast, accessible, and have very good search engine optimization.

However, it comes at the cost of a higher server load, and requires common full reloads.

2. Client-side rendering (CSR)

In this case the browser loads a minimal HTML page, and than the rest of the content is rendered with JS. The web page essentially loads just one time. Requests and rendering is handled by Ajax in the background.

In this case, only the relevant portions of a page are updates, and the dynamic load time is improved. However, it has poor search engine optimization, and often less accessible.

One other method is the multi-page application. Which uses full page navigation, but each individual page has CSR

Single page applications, which heavily rely on CSR, are build using front-end frameworks like React, Angular, and Vue.
# Hybrid Approach
Pre-rendering consists of static site generation. Once the static HTML is delivered, it is hydrated with attached client-side JS. These applications are typically made with hybrid rendering frameworks like Next.js, Nuxt.js etc.
# React JS
React essentially re-rendered only when something changes.

It accomplishes thing by using a virtual DOM, a lightweight representation of the UI, and synced with the real DOM. A comparison between the virtual and real DOM reveals the elements that have updated, and exclusively those elements are updated.

React is written in JSX, a combination of HTML and JS. it must be compiled to JS using Babel JS.
# React Components
These are either functions that return a JSX element, or a class that extends `React.Component`. Building components makes your elements reusable. 

To distinguish from HTML elements, React components must be capitalized.
# Components and Props
Props are read-only arguments passed into React components via a dictionary. Their syntax is a little strange, here's an example: `<Text value="Hello" />`. The string passed in as `value` is the prop.

Importantly, note that styles and classes use JS names, as opposed to the HTML/CSS names you might be used to.

Elements that have been created in a loop must have a `key` prop. This prop is used by React to determine which element to re-render, so it can avoid rendering the entire list.
# Hooks
Hooks enable state and lifecycle features for functional components. States being the data that changes over time, and a lifecycle describing the stages a component goes through during its existence.

They are yet another tool used to help reduce how much re-rendering must happen on a website.