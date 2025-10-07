
# src/menu.py

def flatten_menu(node):
    """
    Return a flat list of item names from a nested menu.
    Node has "type": "category" or "item".
    Robust to missing fields and unknown node types: unknown/malformed nodes are ignored.
    """
    # Ignore non-dict nodes
    if not isinstance(node, dict):
        return []

    node_type = node.get("type")
    if node_type == "item":
        # Return the name if present and a string, else ignore
        name = node.get("name")
        return [name] if isinstance(name, str) else []
    elif node_type == "category":
        items = []
        for child in node.get("children", []):
            items.extend(flatten_menu(child))
        return items
    # Missing or unknown types are ignored (treated as empty)
    return []
