_state = None

class _State:
    def __init__(self) -> None:
        global _state
        _state = {} if not _state else _state

    def __getattr__(self, __attr):
        return _state[__attr]
    
    def __getitem__(self, __item):
        return _state[__item]
    
    def __setattr__(self, __name: str, __value):
        _state[__name] = __value

    def __setitem__(self, __name, __value):
        _state[__name] = __value

    def __delattr__(self, __name: str) -> None:
        _state.pop(__name)
            
    def __repr__(self) -> str:
        return str(_state)


class Sstate(_State):
    def __init__(self) -> None:
        super().__init__()
        
    def pop(self, key: str):
        super().__delattr__(key)
