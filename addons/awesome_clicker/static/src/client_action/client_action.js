/** @odoo-module */

import { Component, useState } from "@odoo/owl"
import { registry } from "@web/core/registry"
import { useService } from "@web/core/utils/hooks"
import { useClicker } from "../clicker_hook"
import { ClickerValue } from "../clicker_value/clicker_value"

class ClickerClientAction extends Component {
    static template = "awesome_clicker.ClickerClientAction"
    static props = ['*']
    static components = { ClickerValue }

    setup() {
        // this.clickService = useState(useService("awesome_clicker.clicker"))
        this.clicker = useClicker();
    }

}

registry.category("actions").add("awesome_clicker.client_action", ClickerClientAction)