# Display Property
Specifies how to render elements and/or its children
- `inline` display the element inline
- `block` display the element as a block-level element
- `none` do not display
- `inline-block` inline, but with width and height properties

You can resize elements with `width`, `height`, `max-width`, `max-height`
- Often used to resize images

Box-sizing
- Changes the behaviour of resizing
- The default, `content-box` for example, means resizing should not take border and padding into account, which can be annoying
- Often times people will use `border-box` instead like so:
```css
* { box-sizing: border-box; }
```
Which selects everything and changes the border to `border-box`
# Responsive Design
Make things look good on different aspect ratios
- Hiding things on small viewports
- Changing layouts on phone and PC

Viewport setup:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Set responsive image sizes with `width` 100%, for examplee.

You could use responsive text size like `10vw` or use the `clamp` function
- `10vw` sets the font size to 10% of the width

Historically, `float` was used to put images inline with text, but typically it's not used for design now-a-days
# Flexbox
Flexibly places items inside the parent element
- `display: flex`

`flex-direction` determines if items form a row or column. `flex-wrap` decides what happens in the case of overflow. `flex-flow` is the combination of both.

`justify-content` justifies the content to one side, or adds space between or around items.
- `space-` options use the entire width or height of the main axis

`align-items` decides where to place child elements along the cross-axis of the flex direction, and `align-content` determines where to place each flex line along the cross-axis
- The cross-axis is the axis perpendicular to the main axis. So if you had everything aligned in a row, the cross axis would be along the column

`flex-grow` determines how much a flex item with grow relative to other items. 0 means no growth, and 1 means "it will take up one share of the available free space". `flex-shrink` is the opposite
- Here is an example to see how share work. Imagine you have two items, both with one share. Then, they will equally share the remaining space on the screen. However, if one has 2 shares, and one has 1 share, then one will take double the amount of space as the other item.
# Grid Layout
2-D layout similar to a table
```css
.container { display: grid; }
```
You can specify your rows and columns like so:
```css
grid-template-rows: auto 1fr auto;
```
Which defines three rows. `fr` means that the size of this row or column show take up some shares of the remaining space.

`row`, `row-gap`, and `column-gap` specify space between rows and columns

`grid-template-areas` defines what goes inside each of the rows and columns. 
```css
grid-template-areas: 'menu top top'
					 'menu bot bot';
```
For example says the menu should take up the left side, the top bar goes on the top, and the bottom bar goes on the bottom

Grid items are direct children of a grid container. `grid-area` for example, defines which named area this item belongs to
```css
.item1 { grid-area: menu; }
```
Will move this item into the menu area.
# Media Query
Checks the capabilities of a device before CSS rules are applied. Defined by `@media` types, expressions, and CSS rules
```css
@media screen and (min-width: 480px) {
	#leftsidebar {width: 200px; float: left;}
	#main {margin-left: 216px;}
}
```

Media queries still follow specificity, so typically you will find queries at the bottom
# CSS Functions
`var()` allows you to define a custom defined variable. `url()` helps to reference a file, and `max()`, `min()` selects the maximum or minimum set of values
```css
width: max(20vw, 400px)
```
You can see here, the max of the two isn't entirely clear, but you can easily check this way

It is also possible to create animations in CSS, but we didn't go very deep into it.
# CSS Framework
CSS Libraries people use to help build their websites
- Bootstrap is the one recommended for us to use, because it is easy
# Introduction to JavaScript
Programming language used in all browsers. Used in frontend and backend development. It is a high-level, runtime interpreted scripting language
- Node.js is the most popular JavaScript engine

TypeScript is a strict superset of JavaScript, it is rising in popularity for backend development, because it is better in a number of ways.

Lots of things are roughly the same in Python and JS here are a few with just minor syntax differences:
- Variable declaration
	- Number, String, boolean variable types
- If condition comparisons are in C syntax
	- `==` and `===` in JS are NOT THE SAME
- Loops are roughly the same. `for of` loops through elements, and `for in` loops through properties
	- `Array.forEach` takes a function as an argument
- Functions can be declared anonymously and assigned to a variable or just how you would in OOB languages
	- Functions can be declared within another function
	- Can accept any number of arguments, missing arguments are `undefined`, if nothing is returned, `undefined` is returnedScope
# Scope
JavaScript defines a global, function, and block scopes. Block scopes are smaller than function scopes, for example, within an if-statement

By convention, generally everything in JS is run within a function. Global variables are discouraged
