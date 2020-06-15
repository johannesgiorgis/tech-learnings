export enum PizzaSizes {
    S,
    M,
    L,
    XL,
    XXL
}

export interface IPizzaPrice {
    size: string;
    percentage: number;
}

export const PizzaSizeNames: string[] = Object.keys(PizzaSizes)
    .map(x => {
        if (new RegExp(/[0-9]/g).test(x)) {
            return PizzaSizes[x].toLowerCase();
        }
    })
    .filter(x => x !== undefined);