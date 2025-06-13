from typing import Protocol, Any, Dict

class ModelContextProtocol(Protocol):
    """
    Protocol for model context prompt.
    Implement this protocol to define how your model context should behave.
    """
    def get_context(self) -> Dict[str, Any]:
        ...

    def update_context(self, data: Dict[str, Any]) -> None:
        ...

class ModelContext(ModelContextProtocol):
    """
    Example implementation of ModelContextProtocol.
    Stores context as a dictionary.
    """
    def __init__(self):
        self._context: Dict[str, Any] = {}

    def get_context(self) -> Dict[str, Any]:
        return self._context

    def update_context(self, data: Dict[str, Any]) -> None:
        self._context.update(data)

# Usage example:
# context = ModelContext()
# context.update_context({'user': 'Alice', 'session': 123})
# print(context.get_context())