The separation of concerns essentially tells us that we should differentiate our files between structure and meaning, and presentation and visual style. These two are done by HTML and CSS, respectively.

There a numerous benefits to this approach, including consistency, accessibility, improved performance, and compatibility.
# Cascading Style Sheet
This is the "CSS" responsible for describing the presentation of markup languages.

Can be specified inline, applying to just a single element, or with a CSS rule.

Generally speaking, CSS rules are written in another file.

- The "cascading" in CSS means that multiple rules can affect the same element.

Less specific rules are overridden by more specific rules. They are in this order:
1. Order of appearance, later is better
2. Elements and pseudo-elements
3. Classes, pseudo-classes, and attribute selectors
4. IDs
5. Inline style
6. Important rules
# Units
Absolute units include centimetres, inches, pixels etc. These are typically not used in web development.

Typically, relative units like rem, em, vh, % and fr are preferred
 - rem is the root element's font size, and em is the parent element's font size
 - vh and vw are the viewport's height and width