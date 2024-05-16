/** @odoo-module */

import { Component, useState, useRef, onMounted } from "@odoo/owl"
import { TodoItem } from "./todo_item"
// Import the registry module from the @web/core/registry package
import { registry } from "@web/core/registry"
import { useAutofocus } from "../utils"

class TodoList extends Component {
    static template = "awesome_owl.TodoList"
    static components = { TodoItem }

    setup() {
        this.todos = useState([])
        this.inputRef = useAutofocus("input")
    }

    addTodo(e){
        let value = e.target.value
        if (e.keyCode === 13 && value !== '') {
            const newTodo = { id: this.getNextId(), description: value, isCompleted: false }
            this.todos.push(newTodo)
            e.target.value = ''
        }
    }

    getNextId() {
        if (!this._nextId) {
            this._nextId = 0 // Inicializar el contador si es la primera vez que se llama
        }
        return this._nextId++
    }

    toggleTodo(todoId) {
        // console.log("todoId ->", todoId)
        const todo = this.todos.find((todo) => todo.id === todoId)
        if (todo) {
            todo.isCompleted = !todo.isCompleted
        }
    }

    removeTodoList(todoId){
        console.log("removeTodo", todoId, this.todos)
        const index = this.todos.findIndex((elem) => elem.id === todoId)
        if (index >= 0) {
            // remove the element at index from list
            this.todos.splice(index, 1)
        }
    }

}

registry.category("actions").add("awesome_owl.TodoList", TodoList)
