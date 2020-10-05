### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
A: PostgreSQL is an open source ORDBMS (object-relational database management system). In an RDBMS, we think of the data as being stored in tables. Some of these tables have relationships to each other. SQL is the language we use to communicate with PostgreSQL.

- What is the difference between SQL and PostgreSQL? 
A: PostgreSQL is the database engine. To communicate with it, we use the PostgreSQL variant of SQL (structured query language). There are many versions of SQL, and PostgreSQL uses just one of them, but it is one that closely follows the SQL standard.

- In `psql`, how do you connect to a database?
A: Once in the psql shell, to connect to a database, run `\c database_name`.  Alternatively, before entering the psql shell, it's possible to open psql and specify the database to open at the same time: `psql database_name`.

- What is the difference between `HAVING` and `WHERE`?
A: `HAVING` and `WHERE` are used in SQL to filter the data returned from a database query. `WHERE` filters at the individual records level. `HAVING` filters grouped data.

- What is the difference between an `INNER` and `OUTER` join?
A: An inner join query returns the records that have data in all the tables in the join. As a result, all rows returned will have data coming from all the tables in the query. 
An outer join query returns records that may or may not all have data coming from all tables in the join. 

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
A: In a query involving two tables, we select `FROM` a table (call it the 'left-side table') and then join another table (call it the 'right-side table'). In the result of a left join, all the rows from the 'left' table will be represented and only the data from the 'right' table that matches those rows will be included. The opposite is true in a right join: all the rows from the 'right' table will be represented and only the data that matches from the 'left' table will be returned.

- What is an ORM? What do they do?
A: An ORM is an object-relational mapping software package. An ORM translates between the relational data in our database and the OOP way that we represent those data in our server language.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
A: 
* Requests from the client side (using AJAX) can be faster, because the browser talks directly to the API without going through the server.
* Requests using AJAX are not secure; API keys and passwords are discoverable.  We can secure the API key or password by sending a request from the server instead. 
* More broadly speaking, requests from the browser are completely visible to anyone who is looking; they generate headers that we can view using the Dev Tools.  Reqests coming from the server are not visible.
* If the data returned from the request will be stored in the database, the server will have to handle the data anyway, so it makes sense to send the request from the server rather than the browser.
* Requests from the browser to an API will commonly be blocked, because of a same-origin policy. Requests from a server shouldn't violate the same-origin policy.

Note to Michael: I still can't figure out what a same-origin policy is exactly. What are the two things that must have the same origin? We should talk about this. Some examples would help. 

- What is CSRF? What is the purpose of the CSRF token?
A: CSRF stands for cross-site request forgery. A CSRF event happens when a bad actor sends form data to our form from another site. Without a CSRF token, our site would not be able to tell if the incoming data is from our form or some other form.
To address this, WTForms generates a CSRF token and puts it in the HTML as a hidden field.  When the form is submitted, the server can check for the presence of the token and authenticate it to validate that the data being sent came from the form on our site.

- What is the purpose of `form.hidden_tag()`?
A: When included on a form, this method allows us to add a hidden form field that includes a CSRF token to a form to be sent with the form data when it is submitted. The server checks to make sure the token is valid before processing the submitted data from the form.