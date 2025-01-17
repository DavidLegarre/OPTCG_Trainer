def effect_factory(effect_data):
    effect_type = effect_data.get("type")
    if effect_type == "draw_card":
        return DrawCardEffect(
            name=effect_data["name"],
            description=effect_data["description"],
            trigger=effect_data["trigger"],
            cost=effect_data.get("cost"),
            draw_amount=effect_data.get("draw_amount", 1),
        )
    # Add more effect types as needed
    else:
        raise ValueError(f"Unknown effect type: {effect_type}")
