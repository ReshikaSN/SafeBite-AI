from src.state_engine import ToolStateEngine

engine = ToolStateEngine()

# Knife enters the system
engine.register_tool("Knife-01")

print("Initial:")
print(engine.get_state("Knife-01"))

# Knife touches peanut
engine.allergen_contact("Knife-01", "peanut")

print("\nAfter peanut contact:")
print(engine.get_state("Knife-01"))

# Knife enters allergen-free zone
result = engine.check_zone_entry(
    "Knife-01",
    "ALLERGEN_FREE"
)

print("\nZone check:")
print(result)

# Knife gets cleaned
engine.cleaning_event("Knife-01")

print("\nAfter cleaning:")
print(engine.get_state("Knife-01"))