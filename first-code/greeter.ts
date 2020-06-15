function greeter(person: string) {
    return "Hello, " + person;
}

let user = "Johannes";

document.body.textContent = greeter(user);