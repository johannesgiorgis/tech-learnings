"use strict";
class TodoItem {
    constructor(_description, identifier) {
        this._description = _description;
        this._creationTimestamp = new Date().getTime();
        if (identifier) {
            this._identifier = identifier;
        }
        else {
            this._identifier = Math.random().toString(36).substring(2, 9);
        }
    }
    get creationTimestamp() {
        return this._creationTimestamp;
    }
    get identifier() {
        return this._identifier;
    }
    get description() {
        return this._description;
    }
}
class TodoList {
    constructor(todoList) {
        this._todoList = [];
        if (Array.isArray(todoList) && todoList.length) {
            this._todoList = this._todoList.concat(todoList);
        }
    }
    get todoList() {
        return this._todoList;
    }
    addTodo(todoItem) {
        if (todoItem) {
            this._todoList = this._todoList.concat(todoItem);
        }
    }
    removeTodo(itemId) {
        if (itemId) {
            this._todoList = this._todoList.filter((item) => {
                if (item.identifier === itemId) {
                    return false; // drop
                }
                else {
                    return true; // keep
                }
            });
        }
    }
}
class HTMLTodoListView {
    constructor() {
        this.todoInput = document.getElementById("todoInput");
        this.todoListDiv = document.getElementById("todoListContainer");
        this.todoListFilter = document.getElementById("todoFilter");
        // defensive checks
        if (!this.todoInput) {
            throw new Error("Could not find the todoInput HTML input element. Is the HTML correct?");
        }
        if (!this.todoListDiv) {
            throw new Error("Could not find the todoListContainer HTML div. Is the HTML correct?");
        }
        if (!this.todoListFilter) {
            throw new Error("Could not find the todoFilter HTML input. Is the HTML correct?");
        }
    }
    clearInput() {
        this.todoInput.value = "";
    }
    getFilter() {
        return this.todoListFilter.value.toUpperCase();
    }
    getInput() {
        const todoInputValue = this.todoInput.value.trim();
        const retValue = new TodoItem(todoInputValue);
        return retValue;
    }
    render(todoList) {
        console.log("Updating the rendered todo list");
        this.todoListDiv.innerHTML = "";
        this.todoListDiv.textContent = ""; // Edge, ...
        const ul = document.createElement("ul");
        ul.setAttribute("id", "todoList");
        this.todoListDiv.appendChild(ul);
        todoList.forEach((item) => {
            const li = document.createElement("li");
            li.setAttribute("class", "todo-list-item");
            li.innerHTML = `<a href='#' onclick='todoIt.removeTodo("${item.identifier}")
        '>${item.description}</a>`;
            ul.appendChild(li);
        });
    }
    filter() {
        console.log("Filtering the rendered todo list");
        const todoListHtml = document.getElementById("todoList");
        if (todoListHtml === null) {
            console.log("Nothing to filter");
            return;
        }
        const todoListFilterText = this.getFilter();
        todoListHtml.childNodes.forEach((item) => {
            let itemText = item.textContent;
            if (itemText !== null) {
                itemText = itemText.toUpperCase();
                if (itemText.startsWith(todoListFilterText)) {
                    item.style.display = "list-item";
                }
                else {
                    item.style.display = "none";
                }
            }
        });
    }
}
class TodoIt {
    constructor(_todoListView) {
        this._todoListView = _todoListView;
        this._todoList = new TodoList();
        console.log("TodoIt");
        if (!_todoListView) {
            throw new Error("The todo list view implemenetation is required to properly initialize TodoIt!");
        }
    }
    addTodo() {
        // get the value from the view
        const newTodo = this._todoListView.getInput();
        if (newTodo.description !== "") {
            console.log("Adding todo: ", newTodo);
            this._todoList.addTodo(newTodo);
            console.log("New todo list: ", this._todoList.todoList);
            this._todoListView.clearInput();
            this._todoListView.render(this._todoList.todoList);
            this.filterTodoList();
        }
    }
    filterTodoList() {
        this._todoListView.filter();
    }
    removeTodo(identifier) {
        if (identifier) {
            console.log("item to remove: ", identifier);
            this._todoList.removeTodo(identifier);
            this._todoListView.render(this._todoList.todoList);
            this.filterTodoList();
        }
    }
}
class EventUtils {
    static isEnter(event) {
        let isEnterResult = false;
        if (event !== undefined && event.defaultPrevented) {
            return false;
        }
        if (event == undefined) {
            isEnterResult = false;
        }
        else if (event.key !== undefined) {
            isEnterResult = event.key === "Enter";
        }
        else if (event.keyCode !== undefined) {
            isEnterResult = event.keyCode === 3;
        }
        return isEnterResult;
    }
}
const view = new HTMLTodoListView();
const todoIt = new TodoIt(view);
//# sourceMappingURL=todo-it.js.map