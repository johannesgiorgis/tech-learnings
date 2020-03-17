# Chapter 14 - Testing Web Apps

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

## Testing View Models

They are the simplest of the web framework integrated pieces we have to test.

We need to provide some kind of request data, set up the flask request and other flask features for the view model.

Next, we simply call the functions of the view model.

Let's take the example of testing for the scenario where no email is provided:

```python
from pypi_org import app as flask_app

def test_register_validation_no_email():
    # 3 A's of test: Arrange, Act, then Assert

    # Arrange - set up form data
    from pypi_org.viewmodels.account.register_viewmodel import  import RegisterViewModel
    form_data = {
        "email": "",
        "password": "a",
    }
    
    # allows us to work the form data above
    with flask_app.test_request_context(path="/account/register", data=form_data):
        vm = RegisterViewModel()

        # Act
        vm.validate()

    # Assert
    assert vm.error is not None
    assert 'email' in vm.error
```

## Testing View Methods

As we are using view models, we can assume that all the validation is working just fine, the data exchange is working 
fine as long as we have already tested that.

We do need to test is that the view method is working with the view model's response correctly. If an error comes back, 
it actually shows the page with an error rather than just ignores it or that if it uses that data to try to create 
our user if that user can't be created it still shows the error instead of just redirecting you.

```python
def test_home_page(self):
    # Arrange
    from pypi_org.views.home_views import index
    with flask_app.app.test_request_context(path='/'):
        
        # Act
        r: Response = index()
    
    # Assert
    assert r.status_code == 200
    assert len(r.model.get('packages')) > 0
```

Realistic test that needs to mock the database interaction:

```python
def test_package_details_no_db(self):

    # Arrange
    from pypi_org.views.package_views import project
    from pypi_org.data.package import Package

    test_package = Package()
    test_package.id = 'sqlalchemy'
    test_package.releases = [
        Release(created_date=datetime.datetime.now(), major_ver=1, minor_ver=2, build_ver=200),
        Release(created_date=datetime.datetime.now() - datetime.timedelta(days=10)),
    ]
    with mock.patch('pypi_org.services.package_service.package_by_id', return_value=test_package):
        with mock.patch('pypi_org.services.package_service.releases_for_package', return_value=test_package.releases):
            with flask_app.app.test_request_context(path='/project/sqlalchemy'):
            
                # Act
                r = project(test_package.id) # calls package_servic.package_by_id() ...

    # Assert
    web_package: Package = r.model['package']
    self.assertEqual(web_package.id, 'sqlalchemy')
    self.assertEqual(len(web_package.releases), 2)
```
