"use strict";
console.log("TodoIt");
let todoList = [];
console.log("Current todo list: ", todoList);
const todoInput = document.getElementById("todoInput");
const todoListDiv = document.getElementById("todoListContainer");
function isEnter(event) {
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
function addTodo() {
    // if we don't have the todo input
    if (todoInput == null) {
        console.error("The todo input is missing from the page!");
        return;
    }
    // get the value from the input
    const newTodo = todoInput.value;
    // verify that there is text
    if ("" !== newTodo.trim()) {
        console.log("Adding todo: ", newTodo);
        // add the new item to the list
        todoList.push(newTodo);
        console.log("New todo list: ", todoList);
        // clear the input
        todoInput.value = "";
        // keep the list sorted
        todoList.sort();
        // update the todo list
        updateTodoList();
        // apply the todo list filter
        filterTodoList();
    }
}
function updateTodoList() {
    console.log("Updating the rendered todo list");
    todoListDiv.innerHTML = "";
    todoListDiv.textContent = ""; // Edge, ...
    const ul = document.createElement("ul");
    ul.setAttribute("id", "todoList");
    todoListDiv.appendChild(ul);
    todoList.forEach((item) => {
        const li = document.createElement("li");
        li.setAttribute("class", "todo-list-item");
        // li.innerText = item;
        li.innerHTML = `<a href='#' onclick='removeTodoListItem("${item}")'>${item}</a>`;
        ul.appendChild(li);
    });
}
function filterTodoList() {
    console.log("Filtering the rendered todo list");
    const todoListHtml = document.getElementById("todoList");
    if (todoList === null) {
        console.log("Nothing to filter");
        return;
    }
    const todoListFilter = document.getElementById("todoFilter");
    const todoListFilterText = todoListFilter.value.toUpperCase();
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
function removeTodoListItem(itemToRemove) {
    console.log("item to remove: ", itemToRemove);
    todoList = todoList.filter((value, _index, _array) => {
        if (value === itemToRemove) {
            return false;
        }
        return true;
    });
    // unsafe alternative: todoList.splice(...)
    // update the todo list
    updateTodoList();
    // apply the todo list filter
    filterTodoList();
}
//# sourceMappingURL=todo-it.js.map