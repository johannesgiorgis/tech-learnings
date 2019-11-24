/* Alter code below this line */
class Thermostat {
    constructor(temperature) {
        this._ftemperature = temperature;
        this._ctemperature = (5/9) * (this._ftemperature - 32);
    }
    // getter
    get temperature() {
        return this._ctemperature;
    }
    // setter
    set temperature(temperature) {
        this._ctemperature = temperature;
        this._ftemperature = this._ctemperature * (9.0/5) + 32;
    }
}
/* Alter code above this line */

const thermos = new Thermostat(76); // setting in Fahrenheit scale
let temp = thermos.temperature; // 24.44 in C
thermos.temperature = 26;
temp = thermos.temperature; // 26 in C
