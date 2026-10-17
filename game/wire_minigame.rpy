init python:
    import pygame
    import math

    class WireMinigame(renpy.Displayable):
        def __init__(self, **kwargs):
            super(WireMinigame, self).__init__(**kwargs)
            
            # Left Terminals (Source wires)
            self.left_terminals = [
                {"id": "red",    "color": "#cb3129", "pos": (786, 404)},
                {"id": "yellow", "color": "#ffc34a", "pos": (786, 509)},
                {"id": "blue",   "color": "#4d6dc5", "pos": (786, 618)},
                {"id": "orange", "color": "#ec793b", "pos": (786, 731)},
            ]
            
            # Right Terminals (Destination sockets)
            self.right_terminals = [
                {"id": "red",    "color": "#cb3129", "pos": (1153, 405)},
                {"id": "blue",   "color": "#4d6dc5", "pos": (1151, 517)},
                {"id": "orange", "color": "#ec793b", "pos": (1151, 619)},
                {"id": "yellow", "color": "#ffc34a", "pos": (1152, 729)},
            ]
            
            # Mapping: left_terminal_index -> right_terminal_index
            self.connections = {}
            self.dragging_idx = None
            self.mouse_pos = (0, 0)
            self.hit_radius = 40  # Pixel tolerance for clicking/releasing near terminals
            self.feedback_message = "Connect each wire to the WRONG socket to cause a short circuit!"

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            canvas = render.canvas()

            # 1. Draw already completed connections
            for l_idx, r_idx in self.connections.items():
                p_start = self.left_terminals[l_idx]["pos"]
                p_end = self.right_terminals[r_idx]["pos"]
                wire_color = self.left_terminals[l_idx]["color"]

                # Dark border outline underneath
                canvas.line("#1c1b1b", p_start, p_end, 14)
                # Colored core line
                canvas.line(wire_color, p_start, p_end, 8)

            # 2. Draw active dragging wire following the cursor
            if self.dragging_idx is not None:
                p_start = self.left_terminals[self.dragging_idx]["pos"]
                p_end = self.mouse_pos
                wire_color = self.left_terminals[self.dragging_idx]["color"]

                canvas.line("#1c1b1b", p_start, p_end, 14)
                canvas.line(wire_color, p_start, p_end, 8)

            return render

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                # Check if clicking on any Left Terminal
                for idx, terminal in enumerate(self.left_terminals):
                    tx, ty = terminal["pos"]
                    if math.hypot(x - tx, y - ty) <= self.hit_radius:
                        # Disconnect if previously connected, then start dragging
                        self.connections.pop(idx, None)
                        self.dragging_idx = idx
                        self.mouse_pos = (x, y)
                        renpy.redraw(self, 0)
                        return None

            elif ev.type == pygame.MOUSEMOTION:
                if self.dragging_idx is not None:
                    self.mouse_pos = (x, y)
                    renpy.redraw(self, 0)

            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                if self.dragging_idx is not None:
                    src_wire = self.left_terminals[self.dragging_idx]
                    connected = False

                    # Check if released over a Right Terminal
                    for r_idx, target in enumerate(self.right_terminals):
                        rx, ry = target["pos"]
                        if math.hypot(x - rx, y - ry) <= self.hit_radius:
                            # Sabotage Check: Must NOT connect matching colors
                            if src_wire["id"] == target["id"]:
                                self.feedback_message = "Matching the correct color won't blow the fuse! Cross them!"
                            else:
                                # Remove any wire currently connected to this target socket
                                for l_idx, current_r in list(self.connections.items()):
                                    if current_r == r_idx:
                                        del self.connections[l_idx]

                                self.connections[self.dragging_idx] = r_idx
                                remaining = 4 - len(self.connections)
                                if remaining > 0:
                                    self.feedback_message = f"Crossed! {remaining} more wire(s) needed to overload."
                                else:
                                    self.feedback_message = "Circuit overloaded!"
                                    renpy.redraw(self, 0)
                                    return "win"

                            connected = True
                            break

                    self.dragging_idx = None
                    renpy.redraw(self, 0)

            return None

# Replace the previous placeholder screen with this:
screen day3_wire_minigame_screen():
    # 1. Background box image
    add "gui/day3_casino/casino_playroom/wire_minigame/bg_wire_box.jpg" align (0.5, 0.5)

    # 2. Interactive Wire Displayable
    default minigame = WireMinigame()
    add minigame

    # 3. Objective & Guidance Text
    text "[minigame.feedback_message]":
        xalign 0.5
        ypos 100
        size 26
        color "#ffffff"
        outlines [(2, "#000000", 0, 0)]

    # 4. Control buttons
    textbutton "Cancel / Back":
        action Return("back")
        align (0.05, 0.95)
        text_size 24

    key "K_ESCAPE" action Return("back")