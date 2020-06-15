# Chapter 13 - Client & Server-Side Validation

## View Models

The view model pattern takes the data exchange, the data normalization, and the data validation and it pushes it somewhere else that can be tested separately, maintained separately.

Our view method only has to process the essence - it gets the data, maybe it creates the user and it doesn't redirect, or something to that effect.

This avoids us having 200 line functions for our view methods.

An action method is broken up into a Action method and a View Model.

## Value of view models

The value of view models is that they allow us to write simpler view methods.

```python
@app.route(...)
def register_get():
    vm = RegistrationView(request)
    return vm.to_dict()

@app.route(...)
def register_post():
    vm = RegistrationView(request)
    vm.validate()
    if vm.error:
        return vm.to_dict()

    if not register_user(vm.email_address, vm.password):
        vm.error = 'Registration failed'
        return vm.to_dict()

    return flask.redirect('/')
```

## View models: to / from dictionary

They provide two basic services:

- Data exchange and normalization
- Validation

```python
class ViewModelBase:
    def __init__(self):
        self.request = flask.request
        self.error: str = None
        self.user_id: int = None
    
    def to_dict(self) -> dict:
        return self.__dict__

# Model Classes derived from ViewModelBase
class RegistrationViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()

        self.first_name = self.request.form.get('first_name', '').strip()
        self.last_name = self.request.form.get('last_name', '').strip()
        self.email = self.request.form.get('last_name', '').strip().lower()
        self.password = self.request.form.get('password')
        self.full_name = self.first_name + ' ' + self.last_name

       # ..
```

## Server-side validation with Viewmodels

```python
class RegistrationViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()

        self.first_name = self.request.form.get('first_name', '').strip()
        self.last_name = self.request.form.get('last_name', '').strip()
        self.email = self.request.form.get('last_name', '').strip().lower()
        self.password = self.request.form.get('password')
        self.full_name = self.first_name + ' ' + self.last_name

       # ..
    def validate(self):
        if not self.first_name or not self.last_name:
            self.error = "You must specify a name."

        elif not self.email:
            self.error = "you must specify an email."

        elif not self.password:
            self.error = "you must specify a password."
        
        if user_service.find_user_by_email(self.email):
            self.error = 'The user with that email already exists.'


        # ...
```

## Client Side Validation

We can leverage HTML5 form values or attributes (e.g. `required`) and different types of input to make most of the validation happen before you ever see any form of submit for the form.

```html
<!DOCTYPE html>
<html lang="us-en">
<body>
    <form action="" method="POST">
        <input name="email" type="email" placeholder=" Your email address" class="form-control" value="{{ email }}" required>
        <input name="password" type="password" placeholder=" Password" class="form-control" value="{{ password }}" required>
        <button type="submit" class="btn btn-danger">Sign In</button>

    </form>
    {% if error %}
        <div class="error-msg">{{ error }}</div>
    {% endif %}
</body>
</html>
```


