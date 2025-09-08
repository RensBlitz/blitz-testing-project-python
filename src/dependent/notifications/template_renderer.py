from typing import Any, Dict


class TemplateRenderer:
    def render(self, template_name: str, data: Dict[str, Any]) -> str:
        parts = [f"TEMPLATE[{template_name}]:"]
        for key, value in data.items():
            parts.append(f"{key}={value};")
        return "".join(parts)
