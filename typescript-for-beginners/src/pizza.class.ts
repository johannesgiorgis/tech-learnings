import { PizzaToppings } from "./pizza-toppings.enum";
import { PizzaSizes } from "./pizza-sizes.enum";

// IPizza with required and optional properties
interface IPizza {
    name: string;
    slices: number;
    toppings: PizzaToppings[]; //string;
    price: number;
    cheesecrust: boolean;
    sizes: PizzaSizes[];
    vegan?: boolean;
    vegetarian?: boolean;
}

interface IPizzaPrice {
    size: string;
    price: number;
}

export class Pizza {
    name: string = '';
    slices: number = 8;
    toppings: PizzaToppings[] = [];
    price: number = 0;
    cheesecrust: boolean = false;
    sizes: PizzaSizes[] = [];
    vegan?: boolean = false;
    vegetaran?: boolean = false;
    prices: IPizzaPrice[] = null;

    constructor(data: IPizza) {
        this.name = data.name;
        this.slices = data.slices;
        this.toppings = data.toppings;
        this.price = data.price;
        this.cheesecrust = data.cheesecrust;
        this.sizes = data.sizes;
        this.prices = this.getPizzaPrices();

        if (data.vegan) {
            this.vegan = data.vegan;
        }
        if (data.vegetarian) {
            this.vegetaran = data.vegetarian;
        }
        return this;
    }

    private getPizzaPrices(): IPizzaPrice[] {
        return this.sizes.map((item, index) => {
            const addition = (this.price / 100) * 15 * index;
            console.log(this.price + addition);
            return {
                size: PizzaSizes[item],
                price: this.price + addition
            };
        });
    }
}