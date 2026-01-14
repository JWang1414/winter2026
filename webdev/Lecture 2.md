# HTML
*Semantic HTML* includes elements that convey information about what they contain, added in HTML5. They are things like `<header>`, `<footer>` etc.

Tables organize data in tables.

HTML includes unordered and ordered lists. You can also include a description list, one with key value pairs.

`<label>` can be applied to elements and input elements
# HTML Forms
Most data is sent to servers using forms. They have numerous various input elements.

Form data is typically composed of key-value pairs of input names and their values. The `<action>` attribute defines the URL of the HTTP request, and `<method>` attribute defined the HTTP method, like GET and POST queries.
# HTML Validation
There exist HTML validators that parse HTML to find issues in code. They can detect and sometimes fix issues, but this isn't an excuse to write bad code and just assume the validator will fix it.
# Cascading Style Sheet
CSS includes only the presentation and visual style of your website

Separating HTML and CSS has numerous benefits beyond organization. It improves the performance, because the two are no longer coupled together, and so aren't both reloaded. The separation of CSS also improves device compatibility, and webpage accessibility

CSS describes the presentation of document written in markup languages.

CSS properties define the style or behaviour of an element, they are the backbone of CSS. They follow `property name : propery value(s)` syntax.
# Where do we specify properties?
## Inline style
Use an attribute named `style` to define the CSS. This applied to just a single element.

Breaks the separation of responsibility.
## CSS Rules
Apply a property to one or more elements. You first select the targetted elements, and follow with the properties.
```
.danger {
	color: red;
	font-size: 14px;
	font-weight: bold;
}
```
These rules can be written in `<style>` elements or in a `.css` file.

Generally speaking we try to avoid embedding CSS in `<style>` tags.

What if we also have the following rule targeting paragraphs?
```
p {
	font-family: san-serif;
	...
}
```
If something is a paragraph with the danger class,
```
<p class="danger">This is a dangerous message</p>
```
Then both will apply. But, how do we know which has precedence?
# CSS Specificity
Larger numbers override lower numbers:
1. Order of appearance (later is better)
2. Elements and pseudo-elements
	- Example: `p, h1, ::before`
3. Classes, pseudo-classes, and attribute selectors
	- Example: `.danger, :hover, [name]`
4. IDs
	- Example: `#footer`
5. Inline style
6. !important rule
	- Example: `font-size: 1rem !important;`

Element selector syntax follows:
1. `tagname`
2. `.classname`
3. `#idname`
4. `:pseudoclass`
5. `[attribute name]`
6. `::pseudoelement`

And you can combine these things together to be more specific:
```
p.danger:hover::first-letter
```
However you cannot select two types of elements. You cannot select `p` and `a`, for example. This of this an an AND condition. You can separate selectors with a comma to obtain the OR condition, selecting all of them.

Descendant conditions allow you to select children of the current selector like
```
.center p
header nav a
form input
```
The last one for example would select all inputs within forms.

You can specify exclusively immediate children with $>$ in between:
```
form > input
footer > a:hover
```
And so the first would select only top level input elements within forms.

There is also the adjacent sibling condition, with selects the rightmost elements whose immediate previous sibling is the element on the left-hand side
```
div + p
```
Would select `p` elements that come directly after a `div` element, for example.
# Font Properties
- `color`
- `font-family`
- `font-style`
	- Normal or italic
- `font-weight`
	- Normal or bold
- `font-size`
- `text-decoration`
	- None, underline, overline etc.
- `text-align`
- `font`
	- Shorthand property. You can include multiple values here
# Units
Specify the size and length of things.

Absolute units includes:
- cm, in, px
Relative units include:
- `rem`: root element’s font-size (default is 16px)
- `em`: parent element’s font-size
- `vh, vw`: current screen’s (viewport) height or width
- `%`: a percent relative to the size of the parent element
- `fr`: fraction (of the available space)

The `calc` function allows allows you to do math on different units like
```
width: calc(100% - 100px)
```
Which is 100 px subtracting the full width of the screen/window.
# Box Model
A set of boxes that wraps around every visible HTML element
- The width and height of an element includes border, padding, and content, but not margin
![[Pasted image 20260113163016.png]]
You can change the size of these values with `margin`, `padding`, `border-width`
- 4 numbers correspond to top-right-bottom-left
- 2 numbers correspond to top & bottom, left & right
- 1 number is all edges

Margins can nave a negative value, pulling in elements. Negative values are not applicable on the rest.
# Position Property
## Static
This is the default positioning behaviour. Block-level elements are laid out top to bottom in the order they appear in the HTML
## Relative
Defined relative to the static position, where it "would have" been. Makes something "positioned"
![[Pasted image 20260113164327.png]]
Relative positioning has moved this div element down right.
## Absolute
Relative to the nearest “positioned” ancestor. In order for something to be positioned, it cannot be static, because that is the default.
- By default it will just target the screen
- Outside normal flow
![[Pasted image 20260113164813.png]]
## Fixed
Relative to the viewport, all the time. This is how people make very annoying ads!
- Outside normal flow
- If you align to the left and right, then the right alignment will be ignored. Unless you emit the "width" attribute, then it stretches out the element to cover the width of the screen
# Transform Property
Fine-grained transformation of an element. You can, for example, translate something 50px down and right, which accomplishes something very similar to the `relative` property.

Also includes `scale` and `rotate`

