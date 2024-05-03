/** @odoo-module **/

// Import the registry module from the @web/core/registry package
import { registry } from "@web/core/registry"

// Import some useful elements from Owl
const { Component, useState, onWillStart, useRef } = owl

// Import the useService hook from the @web/core/utils/hooks package
import { useService } from "@web/core/utils/hooks"

// Define the MyClientAction class, which extends Component
class MyClientAction extends Component {
    setup() {
        // Initialize the component's state using useState
        this.state = useState({
            task: {name:"", color:"#FF0000", completed:false},
            taskList: [],
            isEdit : false,
            activeId: false,
        })

        // Access the ORM service of Odoo
        this.orm = useService("orm")
        this.model = 'owl.todo.list'
        this.searchInput = useRef("search-input")

        // Perform an asynchronous operation before the component starts
        onWillStart(async () => {
            await this.getAllTasks()
        })

    }

    async getAllTasks() {
        // Perform a search-read operation on the owl.todo.list model
        // to get a list of tasks
        this.state.taskList = await this.orm.searchRead(this.model, [], ["name", "color", "completed"])
    }

    addTask(){
        // Method to add a new task
        this.resetForm()
        this.state.isEdit = false
        this.state.activeId = false
    }

    editTask(task){
        // Method to edit an existing task
        this.state.activeId = task.id
        this.state.isEdit = true
        this.state.task = {...task}
    }

    async saveTask(){
        // Method to save a task (either creating a new one or updating an existing one)
        if (!this.state.isEdit){
            await this.orm.create(this.model, [this.state.task])
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.task)
        }
        await this.getAllTasks()
    }

    resetForm(){
        // Method to reset the task form
        this.state.task = {name:"", color:"#FF0000", completed:false}
    }

    async deleteTask(task){
        // Method to delete a task
        await this.orm.unlink(this.model, [task.id])
        await this.getAllTasks()
    }

    async searchTask(){
        // Method to search for tasks based on user input
        const text = this.searchInput.el.value
        this.state.taskList = await this.orm.searchRead(this.model, [["name", "ilike", text]], ["name", "color", "completed"])
    }

    async toggleTask(event, task){
        // Method to toggle the completion status of a task
        await this.orm.write(this.model, [task.id], {completed: event.target.checked})
        await this.getAllTasks()
    }

    async updateColor(event, task){
        // Method to update the color of a task
        await this.orm.write(this.model, [task.id], {color: event.target.value})
        await this.getAllTasks()
    }

}

// Assign the template attribute to the MyClientAction class
// to specify the template it will use
MyClientAction.template = "owl_youtube.test1"

// Register the MyClientAction component in the registry
// using the tag "owl_youtube.MyClientAction"
registry.category("actions").add("owl_youtube.MyClientAction", MyClientAction)
