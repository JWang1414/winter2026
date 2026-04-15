Generally speaking, React applications are made inside React projects, as opposed to embedding React into HTML files as scripts.
# File Structure
While there are a few small changes, one of the main ones is file structure.

Everything used by your app is placed in the `src` folder, and anything not used by a React component is placed in the`public` folder.

Nothing gets imported to the HTML files. Static file imports should be handled by the server.

Components are typically placed in the `src/components` folder, and each component owns its own folder. The JSX file inside is called `index.jsx`, and the CSS file `style.css`
# Global State
Often times inside React projects, we find ourselves repeatedly passing down states from component to component. This is called prompt drilling.

An alternative to prompt drilling is using a global state, which is accessible anywhere in your project.

They make a component harder to reuse, but by leveraging contexts you can make particular functions available to otherwise deep components.

Typically placed inside a `contexts` folder.

Contexts are made available by wrapping a provider around the parent component. Then, any descendent components can access the context with `useContext`