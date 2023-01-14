## Homework on "Decorators"

The folder contains code with executable examples, abstract and homework examples, and a Jupyter-Notebook with function examples.
You need to install one additional package (requirements.txt ) for the demonstration.
The functions themselves do not require third party packages to work.

The following decorators are provided:
- time_this
- function_logging
- russian_roulette_decorator

#### *time_this* :
Decorator replaces the return value of the function being decorated for the duration of its execution.

#### *function_logging* :
Decorator allows you to log function launches by printing out the input data and return type.

#### *russian_roulette_decorator* :
Decorator - Russian roulette; it decorates the function by replacing the return value with the value passed to the decorator with a given probability.