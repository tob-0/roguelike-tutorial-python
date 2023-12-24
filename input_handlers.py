from typing import Optional

import tcod.event

from actions import Action, MovementAction, EscapeAction


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        match key:
            case tcod.event.KeySym.UP:
                action = MovementAction(0, -1)
            case tcod.event.KeySym.DOWN:
                action = MovementAction(0, 1)
            case tcod.event.KeySym.LEFT:
                action = MovementAction(-1, 0)
            case tcod.event.KeySym.RIGHT:
                action = MovementAction(1,0)
            case tcod.event.KeySym.ESCAPE:
                action = EscapeAction()
            case _:
                pass

        return action
