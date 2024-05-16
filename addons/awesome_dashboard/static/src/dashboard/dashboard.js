/** @odoo-module */

/**
 * This module defines the AwesomeDashboard component, which is a custom dashboard
 * implemented using Odoo's Owl framework.
 */

import { Component, onWillStart, useState } from "@odoo/owl" // Importing the Component class from the Owl framework
import { registry } from "@web/core/registry" // Importing the registry module from the web core package
import { Layout } from "@web/search/layout" // Importing the Layout component from the web search package
import { useService } from "@web/core/utils/hooks" // Importing the useService function from the web core utils package
import { DashboardItem } from "./dashboard_item/dashboard_item"
// import { PieChart } from "./pie_chart/pie_chart"
// import { items } from "./dashboard_items"
import { Dialog } from "@web/core/dialog/dialog";
import { CheckBox } from "@web/core/checkbox/checkbox";
import { browser } from "@web/core/browser/browser";

class AwesomeDashboard extends Component {
    /**
     * The template for the AwesomeDashboard component.
     */
    static template = "awesome_dashboard.AwesomeDashboard"

    /**
     * The components used in the AwesomeDashboard component.
     */
    // static components = { Layout, DashboardItem, PieChart }
    static components = { Layout, DashboardItem }

    /**
     * Setup function to initialize the component.
     * It sets up the action service and initializes the display object.
     */
    setup() {
        this.action = useService("action") // Using the action service
        this.statistics = useState(useService("awesome_dashboard.statistics"))
        this.dialog = useService("dialog")
        this.display = {
            controlPanel: {},
        }
        // this.items = items
        this.items = registry.category("awesome_dashboard").getAll()
        // onWillStart(async () => {
        //     this.statistics = await this.statistics.loadStatistics()
        // })
        this.state = useState({
            disabledItems: browser.localStorage.getItem("disabledDashboardItems")?.split(",") || []
        });
    }

    openConfiguration() {
        this.dialog.add(ConfigurationDialog, {
            items: this.items,
            disabledItems: this.state.disabledItems,
            onUpdateConfiguration: this.updateConfiguration.bind(this),
        })
    }

    updateConfiguration(newDisabledItems) {
        this.state.disabledItems = newDisabledItems;
    }

    /**
     * Opens the customer view by triggering the base.action_partner_form action.
     */
    openCustomerView() {
        this.action.doAction("base.action_partner_form")
    }

    /**
     * Opens the leads view by triggering the ir.actions.act_window action.
     */
    openLeads() {
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "All leads",
            res_model: "crm.lead",
            views: [
                [false, "list"],
                [false, "form"],
            ],
        })
    }
}

class ConfigurationDialog extends Component {
    static template = "awesome_dashboard.ConfigurationDialog";
    static components = { Dialog, CheckBox };
    static props = ["close", "items", "disabledItems", "onUpdateConfiguration"];

    setup() {
        this.items = useState(this.props.items.map((item) => {
            return {
                ...item,
                enabled: !this.props.disabledItems.includes(item.id),
            }
        }));
    }

    done() {
        this.props.close();
    }

    onChange(checked, changedItem) {
        changedItem.enabled = checked;
        const newDisabledItems = Object.values(this.items).filter(
            (item) => !item.enabled
        ).map((item) => item.id)

        browser.localStorage.setItem(
            "disabledDashboardItems",
            newDisabledItems,
        );

        this.props.onUpdateConfiguration(newDisabledItems);
    }

}

// Registering the AwesomeDashboard component in the actions category of the registry
// registry.category("actions").add("awesome_dashboard.dashboard", AwesomeDashboard)
registry.category("lazy_components").add("AwesomeDashboard", AwesomeDashboard);
