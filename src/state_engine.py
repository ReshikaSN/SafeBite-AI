from datetime import datetime


class ToolStateEngine:

    def __init__(self):
        self.tools = {}

    def register_tool(self, tool_id):
        if tool_id not in self.tools:
            self.tools[tool_id] = {
                "state": "CLEAN",
                "last_allergen": None,
                "last_contact_time": None,
                "cleaning_events": 0,
            }

    def allergen_contact(self, tool_id, allergen):
        self.register_tool(tool_id)

        self.tools[tool_id]["state"] = "POTENTIAL_ALLERGEN_CARRYOVER"
        self.tools[tool_id]["last_allergen"] = allergen
        self.tools[tool_id]["last_contact_time"] = datetime.now().isoformat()

    def cleaning_event(self, tool_id):
        self.register_tool(tool_id)

        self.tools[tool_id]["state"] = "CLEAN"
        self.tools[tool_id]["last_allergen"] = None
        self.tools[tool_id]["cleaning_events"] += 1

    def get_state(self, tool_id):
        self.register_tool(tool_id)
        return self.tools[tool_id]

    def check_zone_entry(self, tool_id, zone):
        self.register_tool(tool_id)

        state = self.tools[tool_id]["state"]

        if (
            state == "POTENTIAL_ALLERGEN_CARRYOVER"
            and zone == "ALLERGEN_FREE"
        ):
            return {
                "risk": "HIGH",
                "alert": True,
                "message": (
                    f"Tool {tool_id} may carry allergen "
                    f"{self.tools[tool_id]['last_allergen']} "
                    f"into allergen-free zone!"
                ),
            }

        return {
            "risk": "LOW",
            "alert": False,
            "message": "No cross-contact risk detected."
        }