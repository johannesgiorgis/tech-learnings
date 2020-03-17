# Chapter 12 - User Input and HTML Forms

## Get > Post > Redirect Pattern

[Wikipedia Page]

- Eliminates the weird problem where you see this form has been submitted, and you are prompted "are you sure you want to re-submit it?" when you refresh the destination page
- It is very clean, nice pattern and easy to implement in HTML and Flask

**How does it work?**

1. User requests a page on our site - they want to register -> they will do a HTTP GET /accounts/register. That page will display an HTML form.
2. User will edit the form locally and will click submit on that form.
3. POST /accounts/register back to the server
4. Save validated data to the database. 
5. Redirect user to a welcome page. 302 redirect /welcome 


[Wikipedia Page]: https://en.wikipedia.org/wiki/Post/Redirect/Get
