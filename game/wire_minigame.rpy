init python:
    import pygame
    import math

    class WireMinigame(renpy.Displayable):
        def __init__(self, **kwargs):
            super(WireMinigame, self).__init__(**kwargs)
            self.left_terminals = [
                {"id": "red",    "color": "#cb3129", "pos": (786, 404)},
                {"id": "yellow", "color": "#ffc34a", "pos": (786, 509)},
                {"id": "blue",   "color": "#4d6dc5", "pos": (786, 618)},
                {"id": "orange", "color": "#ec793b", "pos": (786, 731)},
            ]
            self.right_terminals = [
                {"id": "red",    "color": "#cb3129", "pos": (1153, 405)},
                {"id": "blue",   "color": "#4d6dc5", "pos": (1151, 517)},
                {"id": "orange", "color": "#ec793b", "pos": (1151, 619)},
                {"id": "yellow", "color": "#ffc34a", "pos": (1152, 729)},
            ]
            self.connections = {}
            self.dragging_idx = None
            self.mouse_pos = (0, 0)
            self.hit_radius = 40
            self.feedback_message = "Connect each wire to the WRONG socket to cause a short circuit!"

        def _draw_wire(self, canvas, p_start, p_end, color):
            canvas.line("#1c1b1b", p_start, p_end, 14)
            canvas.line(color, p_start, p_end, 8)

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            canvas = render.canvas()

            for l_idx, r_idx in self.connections.items():
                self._draw_wire(
                    canvas,
                    self.left_terminals[l_idx]["pos"],
                    self.right_terminals[r_idx]["pos"],
                    self.left_terminals[l_idx]["color"]
                )

            if self.dragging_idx is not None:
                self._draw_wire(
                    canvas,
                    self.left_terminals[self.dragging_idx]["pos"],
                    self.mouse_pos,
                    self.left_terminals[self.dragging_idx]["color"]
                )

            return render

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                for idx, terminal in enumerate(self.left_terminals):
                    tx, ty = terminal["pos"]
                    if math.hypot(x - tx, y - ty) <= self.hit_radius:
                        self.connections.pop(idx, None)
                        self.dragging_idx = idx
                        self.mouse_pos = (x, y)
                        renpy.play("audio/sfx_wire_grab.ogg", channel="sound")
                        renpy.redraw(self, 0)
                        return None

            elif ev.type == pygame.MOUSEMOTION and self.dragging_idx is not None:
                self.mouse_pos = (x, y)
                renpy.redraw(self, 0)

            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1 and self.dragging_idx is not None:
                src_wire = self.left_terminals[self.dragging_idx]
                connected = False

                for r_idx, target in enumerate(self.right_terminals):
                    rx, ry = target["pos"]
                    if math.hypot(x - rx, y - ry) <= self.hit_radius:
                        if src_wire["id"] == target["id"]:
                            renpy.play("audio/sfx_wire_wrong.ogg", channel="sound")
                            self.feedback_message = "Matching the correct color won't blow the fuse! Cross them!"
                        else:
                            for l_idx, current_r in list(self.connections.items()):
                                if current_r == r_idx:
                                    del self.connections[l_idx]
                            self.connections[self.dragging_idx] = r_idx
                            remaining = 4 - len(self.connections)
                            renpy.play("audio/sfx_wire_connect.ogg", channel="sound")
                            if remaining > 0:
                                self.feedback_message = f"Crossed! {remaining} more wire(s) needed to overload."
                            else:
                                self.feedback_message = "Circuit overloaded!"
                                self.dragging_idx = None
                                renpy.redraw(self, 0)
                                return "win"
                        connected = True
                        break

                if not connected:
                    renpy.play("audio/ui_cancel.ogg", channel="sound")
                self.dragging_idx = None
                renpy.redraw(self, 0)

            return None

screen day3_wire_minigame_screen():
    on "show" action Show("global_hud")
    add "gui/day3_casino/casino_playroom/wire_minigame/bg_wire_box.jpg" align (0.5, 0.5)
    default minigame = WireMinigame()
    add minigame
    text "[minigame.feedback_message]":
        xalign 0.5
        ypos 100
        size 26
        color "#ffffff"
        outlines [(2, "#000000", 0, 0)]
    textbutton "Cancel / Back":
        hover_sound "audio/ui_hover.ogg"
        activate_sound "audio/ui_cancel.ogg"
        action Return("back")
        align (0.05, 0.95)
        text_size 24
    if not renpy.get_screen("global_hud"):
        use global_hud
    key "K_ESCAPE" action [Play("sound", "audio/ui_cancel.ogg"), Return("back")]