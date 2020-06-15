import { Pizza } from "./pizza.class";
import { PizzaToppings } from "./pizza-toppings.enum";

export class PizzaCatalog {
    list: Pizza[] = [];

    constructor(list: Pizza[]) {
        this.list = list;
    }

    filterPizzaByVegan(vegan: boolean): Pizza[] {
        return this.list.filter((pizza: Pizza) => pizza.vegan === vegan);
    }

    filterPizzaByTopping(topping: PizzaToppings) {
        return this.list.filter((pizza: Pizza) => pizza.toppings.indexOf(topping));
    }

}