# ==============================================================================
# 1. GLOBAL AUDIO CONTROLLER (0.5x Stings, BGM Ducking, 2x Ambience) & HUD/SAVE
# ==============================================================================
default scoop_current_location = "Investigation"

init -5 python:
    # Register independent Ambient mixer and Sting channel
    renpy.music.register_channel("ambient", mixer="ambient", loop=True, tight=True)
    renpy.music.register_channel("sting", mixer="sfx", loop=False)

    _scoop_orig_music_play = renpy.music.play
    _scoop_sting_active = False

    def _scoop_prepend_volume(filenames, factor=2.0):
        """Applies a sample gain multiplier to audio filenames."""
        if isinstance(filenames, str):
            if not filenames.startswith("<"):
                return f"<volume {factor}>{filenames}"
            return filenames
        elif isinstance(filenames, (list, tuple)):
            return [
                (f"<volume {factor}>{f}" if isinstance(f, str) and not f.startswith("<") else f)
                for f in filenames
            ]
        return filenames

    def _scoop_custom_music_play(filenames, channel="music", loop=None, fadeout=None, synchro_start=False, fadein=0, tight=None, if_changed=False, relative_volume=1.0, **kwargs):
        global _scoop_sting_active

        # 2x Louder Ambience
        if channel == "ambient":
            base_vol = 1.0 if relative_volume is None else relative_volume
            relative_volume = min(1.0, base_vol * 2.0)
            filenames = _scoop_prepend_volume(filenames, 2.0)

        # 0.5x (Half) Volume for Stings
        elif channel == "sting":
            base_vol = 1.0 if relative_volume is None else relative_volume
            relative_volume = max(0.0, min(1.0, base_vol * 0.5))
            filenames = _scoop_prepend_volume(filenames, 0.5)

        rv = _scoop_orig_music_play(
            filenames,
            channel=channel,
            loop=loop,
            fadeout=fadeout,
            synchro_start=synchro_start,
            fadein=fadein,
            tight=tight,
            if_changed=if_changed,
            relative_volume=relative_volume,
            **kwargs
        )

        # Pause and mute BGM ("music") whenever a sting is playing
        if channel == "sting":
            _scoop_sting_active = True
            renpy.music.set_volume(0.0, delay=0.0, channel="music")
            renpy.music.set_pause(True, channel="music")
        elif channel == "music":
            if _scoop_sting_active or renpy.music.get_playing(channel="sting"):
                _scoop_sting_active = True
                renpy.music.set_volume(0.0, delay=0.0, channel="music")
                renpy.music.set_pause(True, channel="music")

        return rv

    renpy.music.play = _scoop_custom_music_play

    def _scoop_sting_periodic_monitor():
        """Keeps BGM paused while a sting plays and resumes BGM once the sting ends."""
        global _scoop_sting_active
        if renpy.music.get_playing(channel="sting"):
            _scoop_sting_active = True
            renpy.music.set_volume(0.0, delay=0.0, channel="music")
            if not renpy.music.get_pause(channel="music"):
                renpy.music.set_pause(True, channel="music")
        else:
            if _scoop_sting_active:
                _scoop_sting_active = False
                renpy.music.set_pause(False, channel="music")
                renpy.music.set_volume(1.0, delay=0.4, channel="music")

    if _scoop_sting_periodic_monitor not in config.periodic_callbacks:
        config.periodic_callbacks.append(_scoop_sting_periodic_monitor)

    # Retain exact event state for Save/Load and guarantee global_hud stays visible
    def _scoop_retain_event_state():
        if not renpy.get_screen("main_menu") and not renpy.context()._menu:
            store._rollback = True
            renpy.retain_after_load()
            if not renpy.get_screen("global_hud"):
                renpy.show_screen("global_hud")

    if _scoop_retain_event_state not in config.start_interact_callbacks:
        config.start_interact_callbacks.append(_scoop_retain_event_state)

    def _scoop_after_load_cleanup():
        global _scoop_sting_active
        _scoop_sting_active = False
        renpy.music.stop(channel="sting")
        renpy.music.set_pause(False, channel="music")
        renpy.music.set_volume(1.0, delay=0.2, channel="music")
        if not renpy.get_screen("main_menu") and not renpy.get_screen("global_hud"):
            renpy.show_screen("global_hud")

    if _scoop_after_load_cleanup not in config.after_load_callbacks:
        config.after_load_callbacks.append(_scoop_after_load_cleanup)

    def _scoop_track_label(label_name, abnormal):
        if not label_name.startswith("_"):
            clean_label = label_name.replace("_", " ").title()
            store.scoop_current_location = clean_label
            day_num = getattr(store, "current_day", 1)
            store.save_name = f"Day {day_num} - {clean_label}"

    config.label_callback = _scoop_track_label

    def scoop_mixer_pct(mixer_name):
        try:
            return int(round(preferences.get_mixer(mixer_name) * 100))
        except Exception:
            try:
                return int(round(preferences.get_volume(mixer_name) * 100))
            except Exception:
                return 100

    def scoop_icon_idle(image_path, zoom_val=0.1):
        return Transform(image_path, zoom=zoom_val)

    def scoop_icon_hover(image_path, zoom_val=0.1, amount=0.2):
        return Transform(image_path, zoom=zoom_val, matrixcolor=BrightnessMatrix(amount))

init 999 python:
    if "global_hud" not in config.overlay_screens:
        config.overlay_screens.append("global_hud")

# ==============================================================================
# 2. PERSISTENT GLOBAL HUD (Settings Top-Left, Bag & News Van Top-Right)
# ==============================================================================
screen global_hud():
    zorder 200

    if not renpy.get_screen("main_menu"):
        # Top-Left Settings Button (1080x1080 scaled to ~81x81px; hides while News Van is open)
        if not renpy.get_screen("news_van_screen"):
            if renpy.loadable("gui/icons/settings.png"):
                imagebutton:
                    xpos 25
                    ypos 25
                    idle scoop_icon_idle("gui/icons/settings.png", 0.075)
                    hover scoop_icon_hover("gui/icons/settings.png", 0.075)
                    hover_sound "audio/ui_hover.ogg"
                    activate_sound "audio/ui_click.ogg"
                    action [
                        FileTakeScreenshot(),
                        SetVariable("save_name", "Day " + str(current_day) + " - " + str(scoop_current_location)),
                        ShowMenu("scoop_settings_menu")
                    ]
            else:
                textbutton "SETTINGS":
                    xpos 25
                    ypos 25
                    hover_sound "audio/ui_hover.ogg"
                    activate_sound "audio/ui_click.ogg"
                    background Solid("#141414DD")
                    hover_background Solid("#c99838")
                    padding (16, 10)
                    text_size 22
                    text_bold True
                    text_color "#ffffff"
                    text_hover_color "#111111"
                    action [
                        FileTakeScreenshot(),
                        SetVariable("save_name", "Day " + str(current_day) + " - " + str(scoop_current_location)),
                        ShowMenu("scoop_settings_menu")
                    ]

        # Top-Right Bag & News Van Icons (Visible on Days 1, 2, 3, and 5 outside of Tutorial)
        if current_day != 4 and not renpy.get_screen("tutorial_spotlight") and not renpy.get_screen("tutorial_office_environment"):
            # Persistent Bag Icon
            imagebutton:
                xalign 0.88
                yalign 0.05
                idle scoop_icon_idle("gui/warehouse/ui_icon_bag_idle.png", 0.1)
                hover scoop_icon_hover("gui/warehouse/ui_icon_bag_idle.png", 0.1)
                hover_sound "audio/ui_hover.ogg"
                action [
                    If(renpy.get_screen("inventory_bag"), Play("sound", "audio/ui_bag_close.ogg"), Play("sound", "audio/ui_bag_open.ogg")),
                    ToggleScreen("inventory_bag")
                ]

            # News Van Icon
            imagebutton:
                xalign 0.95
                yalign 0.05
                idle scoop_icon_idle("gui/warehouse/ui_icon_van_idle.png", 0.1)
                hover scoop_icon_hover("gui/warehouse/ui_icon_van_idle.png", 0.1)
                hover_sound "audio/ui_hover.ogg"
                activate_sound "audio/sfx_van_door.ogg"
                action Show("news_van_screen")

# ==============================================================================
# 3. CUSTOM NOIR STYLES FOR SLIDERS & MENU BUTTONS
# ==============================================================================
style scoop_volume_slider is bar:
    xsize 500
    ysize 22
    left_bar Frame(Solid("#c99838"), 0, 0)   # Gold filled track
    right_bar Frame(Solid("#2b2b2b"), 0, 0)  # Dark unfilled track
    thumb Solid("#ffffff", xsize=14, ysize=30)
    thumb_offset 7
    hover_sound "audio/ui_hover.ogg"

style scoop_menu_btn is button:
    xsize 420
    ysize 64
    xalign 0.5
    background Solid("#242424")
    hover_background Solid("#c99838")
    insensitive_background Solid("#1a1a1a")
    hover_sound "audio/ui_hover.ogg"
    activate_sound "audio/ui_click.ogg"

style scoop_menu_btn_text is text:
    align (0.5, 0.5)
    size 26
    bold True
    color "#ffffff"
    hover_color "#111111"
    insensitive_color "#555555"

# ==============================================================================
# 4. MAIN SETTINGS HUB (Opened by Top-Left Settings Icon)
# ==============================================================================
screen scoop_settings_menu():
    tag menu
    modal True
    zorder 250

    add Solid("#000000B8")

    frame:
        align (0.5, 0.5)
        xsize 580
        ysize 650
        background Solid("#141414F5")
        padding (50, 40)

        vbox:
            spacing 18
            xfill True
            yalign 0.5

            text "SETTINGS" xalign 0.5 size 38 bold True color "#f0c75e" outlines [(2, "#000000", 0, 0)]
            null height 8

            button:
                style "scoop_menu_btn"
                action ShowMenu("scoop_audio_screen")
                text "Audio" style "scoop_menu_btn_text"

            button:
                style "scoop_menu_btn"
                sensitive (not renpy.get_screen("main_menu"))
                action [FilePage(1), ShowMenu("scoop_save_screen")]
                text "Save" style "scoop_menu_btn_text"

            button:
                style "scoop_menu_btn"
                action ShowMenu("scoop_load_screen")
                text "Load" style "scoop_menu_btn_text"

            button:
                style "scoop_menu_btn"
                action ShowMenu("scoop_credits_screen")
                text "Credits" style "scoop_menu_btn_text"

            button:
                style "scoop_menu_btn"
                action Confirm(
                    "Return to the Main Menu?\nUnsaved progress will be lost.",
                    yes=[Stop("ambient"), Stop("sting"), MainMenu(confirm=False)]
                )
                text "Main Menu" style "scoop_menu_btn_text"

            null height 8

            textbutton "Resume Game":
                xalign 0.5
                hover_sound "audio/ui_hover.ogg"
                activate_sound "audio/ui_cancel.ogg"
                action Return()
                text_size 24
                text_color "#bbbbbb"
                text_hover_color "#f0c75e"

    key "K_ESCAPE" action [Play("sound", "audio/ui_cancel.ogg"), Return()]

# ==============================================================================
# 5. AUDIO SUB-SCREEN (Music, SFX & Ambience Sliders)
# ==============================================================================
screen scoop_audio_screen():
    tag menu
    modal True
    zorder 250

    add Solid("#000000B8")

    frame:
        align (0.5, 0.5)
        xsize 720
        ysize 560
        background Solid("#141414F5")
        padding (50, 40)

        vbox:
            spacing 26
            xfill True

            text "AUDIO SETTINGS" xalign 0.5 size 36 bold True color "#f0c75e" outlines [(2, "#000000", 0, 0)]

            # Slider 1: Background Music (BGM)
            vbox:
                spacing 8
                hbox:
                    xfill True
                    text "Background Music (BGM)" size 24 color "#ffffff"
                    $ bgm_pct = scoop_mixer_pct("music")
                    text "[bgm_pct]%" xalign 1.0 size 24 bold True color "#f0c75e"
                bar:
                    value Preference("music volume")
                    style "scoop_volume_slider"
                    xalign 0.5

            # Slider 2: Sound Effects (SFX & Stings)
            vbox:
                spacing 8
                hbox:
                    xfill True
                    text "Sound Effects (SFX)" size 24 color "#ffffff"
                    $ sfx_pct = scoop_mixer_pct("sfx")
                    text "[sfx_pct]%" xalign 1.0 size 24 bold True color "#f0c75e"
                bar:
                    value Preference("sound volume")
                    style "scoop_volume_slider"
                    released Play("sound", "audio/ui_notify.ogg")
                    xalign 0.5

            # Slider 3: Ambience (Environmental Audio - 2x Boosted)
            vbox:
                spacing 8
                hbox:
                    xfill True
                    text "Ambience & Environment" size 24 color "#ffffff"
                    $ amb_pct = scoop_mixer_pct("ambient")
                    text "[amb_pct]%" xalign 1.0 size 24 bold True color "#f0c75e"
                bar:
                    value Preference("mixer ambient volume")
                    style "scoop_volume_slider"
                    xalign 0.5

            null height 6

            # Utility & Back Buttons
            hbox:
                xalign 0.5
                spacing 30

                textbutton "Test SFX":
                    hover_sound "audio/ui_hover.ogg"
                    action Play("sound", "audio/sfx_camera_shutter.ogg")
                    background Solid("#2b2b2b")
                    hover_background Solid("#444444")
                    padding (20, 10)
                    text_size 22
                    text_color "#ffffff"
                    text_hover_color "#f0c75e"

                textbutton "Mute All":
                    hover_sound "audio/ui_hover.ogg"
                    activate_sound "audio/ui_click.ogg"
                    action Preference("all mute", "toggle")
                    background Solid("#2b2b2b")
                    hover_background Solid("#591c1c")
                    selected_background Solid("#8a1c1c")
                    padding (20, 10)
                    text_size 22
                    text_color "#ffffff"
                    text_selected_color "#ffaaaa"

                textbutton "Back to Settings":
                    hover_sound "audio/ui_hover.ogg"
                    activate_sound "audio/ui_cancel.ogg"
                    action ShowMenu("scoop_settings_menu")
                    background Solid("#c99838")
                    hover_background Solid("#e3b34c")
                    padding (24, 10)
                    text_size 22
                    text_bold True
                    text_color "#111111"

    key "K_ESCAPE" action [Play("sound", "audio/ui_cancel.ogg"), ShowMenu("scoop_settings_menu")]

# ==============================================================================
# 6. FUNCTIONAL SAVE SCREEN (Saves Exact Event State)
# ==============================================================================
screen scoop_save_screen():
    tag menu
    modal True
    zorder 250

    on "show" action If(FileCurrentPage() in ("auto", "quick"), FilePage(1))
    on "replace" action If(FileCurrentPage() in ("auto", "quick"), FilePage(1))

    add Solid("#000000B8")

    frame:
        align (0.5, 0.5)
        xsize 1360
        ysize 840
        background Solid("#141414F5")
        padding (45, 35)

        vbox:
            spacing 20
            xfill True
            yfill True

            text "SAVE INVESTIGATION EVENT" xalign 0.5 size 36 bold True color "#f0c75e" outlines [(2, "#000000", 0, 0)]

            # Page Selector (Pages 1 - 5)
            hbox:
                xalign 0.5
                spacing 16
                for page_num in range(1, 6):
                    textbutton "Page [page_num]":
                        hover_sound "audio/ui_hover.ogg"
                        activate_sound "audio/ui_click.ogg"
                        action FilePage(page_num)
                        background Solid("#262626")
                        selected_background Solid("#c99838")
                        hover_background Solid("#444444")
                        padding (18, 8)
                        text_size 20
                        text_color "#ffffff"
                        text_selected_color "#111111"

            # 3x2 Save Slot Grid
            grid 3 2:
                xalign 0.5
                spacing 26

                for slot in range(1, 7):
                    frame:
                        xsize 390
                        ysize 265
                        background Solid("#222222")
                        padding (12, 12)

                        button:
                            xfill True
                            yfill True
                            background None
                            hover_background Solid("#ffffff18")
                            hover_sound "audio/ui_hover.ogg"
                            activate_sound "audio/ui_click.ogg"
                            action [
                                SetVariable("save_name", "Day " + str(current_day) + " - " + str(scoop_current_location)),
                                FileSave(slot)
                            ]

                            vbox:
                                spacing 6
                                xalign 0.5

                                fixed:
                                    xsize 300
                                    ysize 169
                                    xalign 0.5
                                    add Solid("#111111")
                                    text "EMPTY SLOT" align (0.5, 0.5) size 18 color "#555555"
                                    add FileScreenshot(slot) align (0.5, 0.5) at Transform(maxsize=(300, 169))

                                text FileSaveName(slot) xalign 0.5 size 18 bold True color "#f0c75e"
                                text FileTime(slot, format="%b %d, %Y - %I:%M %p", empty="Click to Save Event") xalign 0.5 size 16 color "#cccccc"

                        if FileLoadable(slot):
                            textbutton "Delete":
                                align (1.0, 0.0)
                                hover_sound "audio/ui_hover.ogg"
                                activate_sound "audio/ui_cancel.ogg"
                                action FileDelete(slot)
                                background Solid("#6e1919CC")
                                hover_background Solid("#a62424")
                                padding (8, 4)
                                text_size 14
                                text_color "#ffffff"

            # Navigation Footer
            hbox:
                xalign 0.5
                spacing 35
                yalign 1.0

                textbutton "Back to Settings":
                    hover_sound "audio/ui_hover.ogg"
                    activate_sound "audio/ui_cancel.ogg"
                    action ShowMenu("scoop_settings_menu")
                    background Solid("#c99838")
                    hover_background Solid("#e3b34c")
                    padding (26, 10)
                    text_size 22
                    text_bold True
                    text_color "#111111"

                textbutton "Resume Game":
                    hover_sound "audio/ui_hover.ogg"
                    activate_sound "audio/ui_cancel.ogg"
                    action Return()
                    background Solid("#2b2b2b")
                    hover_background Solid("#444444")
                    padding (26, 10)
                    text_size 22
                    text_color "#ffffff"

    key "K_ESCAPE" action [Play("sound", "audio/ui_cancel.ogg"), ShowMenu("scoop_settings_menu")]

# ==============================================================================
# 7. FUNCTIONAL LOAD SCREEN (Restores Exact Saved Event)
# ==============================================================================
screen scoop_load_screen():
    tag menu
    modal True
    zorder 250

    on "show" action If(FileCurrentPage() == "quick", FilePage(1))
    on "replace" action If(FileCurrentPage() == "quick", FilePage(1))

    add Solid("#000000B8")

    frame:
        align (0.5, 0.5)
        xsize 1360
        ysize 840
        background Solid("#141414F5")
        padding (45, 35)

        vbox:
            spacing 20
            xfill True
            yfill True

            text "LOAD INVESTIGATION EVENT" xalign 0.5 size 36 bold True color "#f0c75e" outlines [(2, "#000000", 0, 0)]

            # Page Selector (Auto + Pages 1 - 5)
            hbox:
                xalign 0.5
                spacing 16
                textbutton "Auto Saves":
                    hover_sound "audio/ui_hover.ogg"
                    activate_sound "audio/ui_click.ogg"
                    action FilePage("auto")
                    background Solid("#262626")
                    selected_background Solid("#c99838")
                    hover_background Solid("#444444")
                    padding (18, 8)
                    text_size 20
                    text_color "#ffffff"
                    text_selected_color "#111111"

                for page_num in range(1, 6):
                    textbutton "Page [page_num]":
                        hover_sound "audio/ui_hover.ogg"
                        activate_sound "audio/ui_click.ogg"
                        action FilePage(page_num)
                        background Solid("#262626")
                        selected_background Solid("#c99838")
                        hover_background Solid("#444444")
                        padding (18, 8)
                        text_size 20
                        text_color "#ffffff"
                        text_selected_color "#111111"

            # 3x2 Load Slot Grid
            grid 3 2:
                xalign 0.5
                spacing 26

                for slot in range(1, 7):
                    frame:
                        xsize 390
                        ysize 265
                        background Solid("#222222")
                        padding (12, 12)

                        button:
                            xfill True
                            yfill True
                            background None
                            hover_background Solid("#ffffff18")
                            hover_sound "audio/ui_hover.ogg"
                            activate_sound "audio/ui_click.ogg"
                            action FileLoad(slot)

                            vbox:
                                spacing 6
                                xalign 0.5

                                fixed:
                                    xsize 300
                                    ysize 169
                                    xalign 0.5
                                    add Solid("#111111")
                                    text "EMPTY SLOT" align (0.5, 0.5) size 18 color "#555555"
                                    add FileScreenshot(slot) align (0.5, 0.5) at Transform(maxsize=(300, 169))

                                text FileSaveName(slot) xalign 0.5 size 18 bold True color "#f0c75e"
                                text FileTime(slot, format="%b %d, %Y - %I:%M %p", empty="No Save Data") xalign 0.5 size 16 color "#cccccc"

                        if FileLoadable(slot):
                            textbutton "Delete":
                                align (1.0, 0.0)
                                hover_sound "audio/ui_hover.ogg"
                                activate_sound "audio/ui_cancel.ogg"
                                action FileDelete(slot)
                                background Solid("#6e1919CC")
                                hover_background Solid("#a62424")
                                padding (8, 4)
                                text_size 14
                                text_color "#ffffff"

            # Navigation Footer
            hbox:
                xalign 0.5
                spacing 35
                yalign 1.0

                textbutton "Back to Settings":
                    hover_sound "audio/ui_hover.ogg"
                    activate_sound "audio/ui_cancel.ogg"
                    action ShowMenu("scoop_settings_menu")
                    background Solid("#c99838")
                    hover_background Solid("#e3b34c")
                    padding (26, 10)
                    text_size 22
                    text_bold True
                    text_color "#111111"

                textbutton "Resume Game":
                    hover_sound "audio/ui_hover.ogg"
                    activate_sound "audio/ui_cancel.ogg"
                    action Return()
                    background Solid("#2b2b2b")
                    hover_background Solid("#444444")
                    padding (26, 10)
                    text_size 22
                    text_color "#ffffff"

    key "K_ESCAPE" action [Play("sound", "audio/ui_cancel.ogg"), ShowMenu("scoop_settings_menu")]

# ==============================================================================
# 8. CREDITS SCREEN
# ==============================================================================
screen scoop_credits_screen():
    tag menu
    modal True
    zorder 250

    add Solid("#000000B8")

    frame:
        align (0.5, 0.5)
        xsize 820
        ysize 640
        background Solid("#141414F5")
        padding (50, 45)

        vbox:
            spacing 20
            xfill True
            yfill True

            text "THE CREATORS" xalign 0.5 size 40 bold True color "#f0c75e" outlines [(2, "#000000", 0, 0)]
            text "The Local Scoop — Development Team" xalign 0.5 size 22 italic True color "#aaaaaa"

            null height 10

            viewport:
                xfill True
                ysize 360
                scrollbars "vertical"
                mousewheel True

                vbox:
                    xfill True
                    spacing 16

                    text "Project Lead & Programming" xalign 0.5 size 22 bold True color "#f0c75e"
                    text "Creator Name 1\nCreator Name 2" xalign 0.5 text_align 0.5 size 20 color "#ffffff"

                    null height 6

                    text "Story, Script & Investigation Design" xalign 0.5 size 22 bold True color "#f0c75e"
                    text "Creator Name 3\nCreator Name 4" xalign 0.5 text_align 0.5 size 20 color "#ffffff"

                    null height 6

                    text "Backgrounds, Sprites & UI Art" xalign 0.5 size 22 bold True color "#f0c75e"
                    text "Creator Name 5\nCreator Name 6" xalign 0.5 text_align 0.5 size 20 color "#ffffff"

                    null height 6

                    text "Music & Sound Design" xalign 0.5 size 22 bold True color "#f0c75e"
                    text "The Creators" xalign 0.5 text_align 0.5 size 20 color "#ffffff"

            textbutton "Back to Settings":
                xalign 0.5
                yalign 1.0
                hover_sound "audio/ui_hover.ogg"
                activate_sound "audio/ui_cancel.ogg"
                action ShowMenu("scoop_settings_menu")
                background Solid("#c99838")
                hover_background Solid("#e3b34c")
                padding (30, 12)
                text_size 22
                text_bold True
                text_color "#111111"

    key "K_ESCAPE" action [Play("sound", "audio/ui_cancel.ogg"), ShowMenu("scoop_settings_menu")]