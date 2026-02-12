# Event Loops
JavaScript uses an event-driven paradigm. The code is run in a single thread. We use event loops to provide the illusion of multiple threads.
- Events are placed inside an event queue, one that checks for new events and executes their callback

They are run synchronously, which means tasks are run one after another.
![[Pasted image 20260211180541.png]]
This is a visualization of the event loop.

Events get placed into the callback queue, and then one task will run inside of JS. This process loops until the queue is empty, where the JS engine just goes to sleep.
- This means that if there is an infinite loop inside of the JS engine, the entire tab will freeze.
# Promises
Callbacks can make code very challenging to read due to nesting.

As an alternative, we can use promises. The code inside of promises is executed immediately, and they can be asynchronously pushed to the event queue.

They are handled using the functions `resolve`, `reject`, `then`, and `catch`.
# Fetch API
Returns a promise object
```js
let request = fetch('https://api.openai.com/v1/chat/completions', {
	method: 'POST',
	data : {model: 'gpt-4', messages: ...},
});

request.then(response => response.text())
	.then(text => console.log(text));
```
Here we are making a post request, receiving another promise in the form of `response.text()`, and then logging the text from that promise.

The initial response from HTTP is a promise because sometimes the header and content can be sent as different payloads.

Generally speaking a promise has three states:
- Pending: initial state
- Resolved: when the resolve function is called
- Rejected: when the reject function is called
![[Pasted image 20260211182129.png]]
A diagram of the typical flow a promise follows.

Generally speaking, we use `catch` to handle errors. So we typically use the status codes (200, 404 etc) to determine which function to use.

```js
const add = (num1, num2) => new Promise((resolve) => resolve(num1 + num2));

add(2, 4)
	.then((result) => {
		console.log(result); return result + 10;
	})
	.then((result) => {
		console.log(result); return add(result, 2);
	})
	.then((result) => {
		console.log(result);
	})
```
This program shows us how we can chain promises together. It looks very intuitive, like one step happens after the next, but between these promises JavaScript is going to sleep and making changes in the background
- Notice that the return value is wrapped in a promise

These chains of promises are much better than callback hell! However, we are interested in trying to see if we can write this even better.
# async and await
If we have functions that use a lot of promises, we can define an asyncronous function using await operator.

Await waits for a promise to be fulfilled before continuing code.
```js
async function divide_thrice(a, b, c, d) {
	try {
		let res = await slow_divide(a, b);
		console.log("result is " + res);
		res = await slow_divide(res, c);
		console.log("result is " + res);
		res = await slow_divide(res, d);
		console.log("result is " + res);
	} catch(err) {
		console.log(err);
	}
}
```
This function essentially "unwraps" the chains promises into one block of code.
- Notice the use of `try` and `catch` to catch errors as opposed to the single `catch` operator we were originally using
# Database
Web applications need some sort of persistent storage.

Typically, people use SQL databases.

Primary databases come in two forms, relational, and non-relational. These two use SQL or don't use SQL, respectively.

- Remember to properly handle queries to avoid SQL injection!
# Object Relational Mapper
Provides and abstraction for accessing the underlying database. This helps to separate the application from the database implementation.

Advantages:
- Used in the native language, you don't need to learn SQL
- You can swap out the database easily
- Secure queries prevent attacks like SQL injection
- Easy conversion from native types to storage types
Disadvantages:
- Reduced performance
- Hiding implementation details can result in poorly designed database schema
# Designing Models
Models involve representing and storing data. It is based on the secure and efficient design of an application.

Generally speaking it should be done before any programming starts, and it can be done in any programming language or framework.
# Prisma Setup
We will be using Prisma 7 with SQLite. SQLite stores everything inside a file. It's very simple and not intended for use in production.

Prisma uses its own data definition language inside a schema file. This file essentially initializes Prisma.
```scheme
datasource db {
	provider = "sqlite"
}

generator client {
	provider = "prisma-client-js"
}

model User {
	id Int @id @default(autoincrement())
	username String @unique
	password String
	email String @unique
	firstname String @default("")
	lastname String @default("")
	createat DateTime @default(now())
}
```
This file for example tells Prisma our database provider, what client we are using, and defines the database table we are going to use.

It is possible to generate classes from the schema file using `npx prisma generate` and sync the schema to the database with `npx prisma migrate dev`.
- It is good practice to include the `--name` option when migrating the database so that you have a version name or version number

Prisma studio is a tool you can use to look at your database tables and manually modify data. You access it with `npx prisma studio`, and open it from localhost

We add model definitions and fields from our diagrams via `schema.prisma`
# Fields and Attributes
Field scalar types include things like String, Boolean, Int etc. It is possible to make something "nullable" by adding a question mark to the end like: String?
- Typically, we prefer to use a default value instead like the empty string or 0

Field attributes include `@id`, `@default`, `@unique` which tell us things like the primary key, default value etc.
# Foreign Key
Establish relationships between models.

1. One-to-Many relationships

This is when multiple objects in model A belong to a single object in model B. Use the `[]` modifier on the many side, and `@relation` on the single side

2. Many-to-Many relationships

When multiple objects in model A relate to multiple objects in model B. This is typically done by joining tables together, however Prisma does this automatically for us. Both sides should use the `[]` modifier, and `@relation("join-table-name")`

3. One-to-One relationships

Most often appear in the case of inheritance. For example: a single user has a single profile. Notate this with a `?` on the parent side, and `@relation` on the child side.

For one-to-one relationships, the foreign should be set to unique. In the case of the user and profile, this means that the userId is unique, because a profile can only be owned by a single user.
# onDelete
Defines what happens when we delete something.
- Argument optionally taken in the `@relation` field
- `@relation(fields: [authorId], references: [id], onDelete: Cascade)`

There are a few delete options,
1. Cascade
	1. All related records are also deleted
2. SetNull
	1. Related records' foreign key field is set to null
3. Restrict
	1. Prevents the deletion of a record if there are related records
4. NoAction
	1. Do nothing
# Migrations
Generally speaking, we typically assume that the state of the schema file matches the database table. However, this is not always the case; two tables can go out of sync.

Whenever our model changes, the database needs to migrate to the new state. This is done by applying the current application schema using DDL queries like CREATE, ALTER, TRUNCATE etc.

Prisma does this in two steps, it first creates the migration, and then applies it.
## Create Migration
Prisma does this by generating a list of operations required to migrate to the new state. These are tracked inside the `prisma/migrations` folder.

For example, we might have something like:
```sql
-- Rename the firstName field to givenName
ALTER TABLE "User" RENAME COLUMN "firstName" TO "givenName";

-- Create the new Profile table
CREATE TABLE "Profile" (
	"id" SERIAL PRIMARY KEY,
	"bio" TEXT NOT NULL,
	"userId" INTEGER NOT NULL UNIQUE,
	FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE
);
```
Which is a series of SQL commands Prisma is using the synchronize to the current state of the schema file.
## Applying Migrations
We can create and apply migrations using `npx prisma migrate dev`.

Prisma knows how to tell is a migration has been applied by using a special table called `_prisma_migrations` which tracks the current migrations applied to the current database. The `migrate` command applies exclusively the migrations not currently in your table.
