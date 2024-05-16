/** @odoo-module **/

// Import the registry module from the @web/core/registry package
import { registry } from "@web/core/registry"

// Import some useful elements from Owl
const { useState, Component, xml } = owl

class Template extends Component {
    static template = "awesome_owl.counter"

    increment(value, index) {
        // Call the increment function of the parent component (Counter)
        this.props.parent.increment(value, index)
    }

    decrement(value, index) {
        // Call the decrement function of the parent component (Counter)
        this.props.parent.decrement(value, index)
    }
}

class Counter extends Component {
    setup() {
        this.state = useState
        ({
            name: " Counter: ",
            value1: 0,
            value2: 1,
            value3: 2
        })
    }

    getTotal() {
        return this.state.value1 + this.state.value2 + this.state.value3;
    }

    increment(option, index) {
        this.state[`value${index}`]++
    }

    decrement(option, index) {
        this.state[`value${index}`]--
    }

    static template = xml`
        <Template parent="this" value="state.value1" index="1" title="state.name"/>
        <Template parent="this" value="state.value2" index="2" title="state.name" />
        <Template parent="this" value="state.value3" index="3" title="state.name" />
        <div>
            Total: <t t-esc="getTotal()" />
        </div>
    `

    static components = { Template }
}

// Register the Counter component in the registry
// using the tag "awesome_owl.Counter"
registry.category("actions").add("awesome_owl.Counter", Counter)
