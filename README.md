[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/twB3Mrb7)
# Menu Flattener — Kitchen Display System

## Story
Your café’s POS has a nested menu: categories, subcategories, and items. The kitchen display needs a **flat list** of item names in the same left-to-right, top-to-bottom order.

## Technical Description
Write:

```py
flatten_menu(menu) -> list[str]
```

Where `menu` is a nested dictionary structure like:
Input shape:

```py
{
  "type": "category",
  "name": "Menu",
  "children": [
    {"type":"item","name":"Americano"},
    {"type":"category","name":"Sandwiches","children":[
        {"type":"item","name":"BLT"},
        {"type":"item","name":"Club"}
    ]},
    ...
  ]
}
```
Return a flat list of item names in traversal order.

## Hints
- Base cases: item → [name]; empty category → [].

- Recursive case: category → concat results of children.

- Ignore unknown nodes safely.

## Run Tests Locally
```bash
python -m pytest -q
```
##Common Problems
- Returning nested lists (forgetting to extend/concat).

- Treating categories as items.

- Changing the order (must be left-to-right).