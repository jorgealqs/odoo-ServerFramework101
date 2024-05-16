/** @odoo-module */

import { Component } from "@odoo/owl"

export class TodoItem extends Component {
    static template = "awesome_owl.TodoItem"
    static props = {
        todo: {
            type: Object,
            shape: { id: Number, description: String, isCompleted: Boolean }
        },
        toggleState: Function,
        removeTodo: Function
    }

    onChangeTodo() {
        // console.log("onChange ->", this.props.todo.id)
        this.props.toggleState(this.props.todo.id)
    }

    onClickRemoveTodo() {
        console.log("onClickRemoveTodo", this.props.todo.id)
        this.props.removeTodo(this.props.todo.id)
    }
}