# Chapter 13 - Testing Web Apps

## Why write tests (web)

It helps us find bugs in our application.

In modern software engineering, we have lots of infrastructure in place to help with continuous deployment,
checking code and verifying that we don't step on each other's feet if we are working on a team.
Testing is one of the few verifications that we have that we can work with.

Continuous Integration (e.g. TeamCity, Travis CI) will automatically check out a code change and build our project.
That build will include running tests. If we don't have tests, what does a build passing really mean? So having testing
in place ensures that when our automatic build system runs, it says something about the state of our web app

## Special challenges for the web

There are some special challenges to testing web applications - they often have more dependencies and other systems
tangled up in their code than most. Let's take an example:

```python
@blueprint.route("/account/register", methods=["POST"])
@response(template_file="account/register.html")
def register_post():
    vm = RegisterViewModel()
    vm.validate()

    if vm.error:
        return vm.to_dict()
    
    try:
        user = user_service.create_user(vm.name, vm.email, vm.password)
        vm.user_session.login(user.id)
    except Exception as x:
        vm.error = f"The account could not be created: {x}"
        return vm.to_dict()

    return flask.redirect('/account')
```

- What if we want to test this behavior?
- What if we want to verify the user can register for our site if that email address is not already taken and all the 
details are filled out?

We want to test this code - what are some of the challenges?

- In `RegisterViewModel`, it imports Flask inside and goes `flask.request`. It expects implicitly request to be there,
to be setup and to have values and not be empty
- When we call `vm.validate`, we see it is going to `request.form` and getting information such as full name, email, 
etc. We need that to be correctly populated.
- In the `user_service`, it will try to create an account so it will talk to the database just as `validate` also would
 to verify an account didn't already exist. It will go to the database and maybe insert some data if it worked. It might
 also do some other kind of check as well here. Maybe it registers the user at a different API - e.g. mailing list.
- We want to be able to test in isolation. We don't want to depend on the database or a random user to get an email
 every time we run this automated test.
- When we call `login`, it working with the response object and calling `set_cookie`.
- At the end, we are doing some kind of redirect with Flask. What does that need set up to work?

So a relatively simple function has all sorts of tangled interconnections with the web framework, database, potentially
 other services like email and external APIs. How do we test this?

## 3 Types of Web Unit Tests

**View Models**

These are central to the data exchange with the user, template, view and a lot of data validation. They implicitly use
a request object. So somehow we have to provide this view model a fake request or a pre-populated request with the data
that we need it to work with. Sometimes, these view models talk to the database which might be a problem.

**View Method**

This is the actual code that has the `@app.route` dectorator or the `blueprint.route` decorator. We would like to call 
that as if it were a web request, not through the whole system, just call that function. This also works with request, 
response, database calls; it has a bunch of stuff going on working with Flask so we need to carefully spec that out or 
provide it something that will work in the way that it expects. 

**Integration**

We might also want to create the entire web application, let the register blueprint, the database init, all that kind
of stuff get up and running and then we're going to feed to the overall application a particular URL, ensure it finds 
its way to the right view method and that it does the right thing.

With the testing infrastructure from Flask, we can create a fake request as if we were actually running the web 
application. It isn't like we are really spinning up a server, but we can simulate a browser sending requests to it 
and make sure we are getting the right behavior there as well.

These are the three core types of tests that we will focus on in this chapter.

