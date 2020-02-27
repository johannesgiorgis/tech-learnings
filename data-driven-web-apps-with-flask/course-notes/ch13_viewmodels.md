# Chapter 13 - Client & Server-Side Validation

## View Models

The view model pattern takes the data exchange, the data normalization, and the data validation and it pushes it somewhere else that can be tested separately, maintained separately.

Our view method only has to process the essence - it gets the data, maybe it creates the user and it doesn't redirect, or something to that effect.

This avoids us having 200 line functions for our view methods.

An action method is broken up into a Action method and a View Model.
