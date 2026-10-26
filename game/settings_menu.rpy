# ==============================================================================
# INDEPENDENT AMBIENT MIXER & VOLUME HELPER
# ==============================================================================
init -5 python:
    # Overrides the ambient channel to use its own dedicated "ambient" mixer
    renpy.music.register_channel("ambient", mixer="ambient", loop=True, tight=True)

    def scoop_mixer_pct(mixer_name):
        try:
            return int(round(preferences.get_mixer(mixer_name) * 100))
        except Exception:
            try:
                return int(round(preferences.get_volume(mixer_name) * 100))
            except Exception:
                return 100

# ==============================================================================
# CUSTOM NOIR STYLES FOR SLIDERS & MENU BUTTONS
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
    hover_sound "audio/ui_hover.ogg"
    activate_sound "audio/ui_click.ogg"

style scoop_menu_btn_text is text:
    align (0.5, 0.5)
    size 26
    bold True
    color "#ffffff"
    hover_color "#111111"

# ==============================================================================
# 1. MAIN SETTINGS HUB (Opened by Top-Left Settings Icon)
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
                sensitive (not main_menu)
                action ShowMenu("scoop_save_screen")
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
# 2. AUDIO SUB-SCREEN (Music, SFX & Ambience Sliders)
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

            # Slider 3: Ambience (Environmental Audio)
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
# 3. FUNCTIONAL SAVE SCREEN
# ==============================================================================
screen scoop_save_screen():
    tag menu
    modal True
    zorder 250

    # Ensure player isn't stuck on the read-only Auto page when trying to save
    on "show" action If(FileCurrentPage() == "auto", FilePage(1))

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

            text "SAVE INVESTIGATION" xalign 0.5 size 36 bold True color "#f0c75e" outlines [(2, "#000000", 0, 0)]

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

                        # Main Clickable Save Area
                        button:
                            xfill True
                            yfill True
                            background None
                            hover_background Solid("#ffffff12")
                            hover_sound "audio/ui_hover.ogg"
                            activate_sound "audio/ui_click.ogg"
                            action FileSave(slot)

                            vbox:
                                spacing 6
                                xalign 0.5

                                # Thumbnail Box
                                fixed:
                                    xsize 300
                                    ysize 169
                                    xalign 0.5
                                    add Solid("#111111")
                                    text "EMPTY SLOT" align (0.5, 0.5) size 18 color "#555555"
                                    add FileScreenshot(slot) align (0.5, 0.5) at Transform(maxsize=(300, 169))

                                # Day Label & Timestamp
                                text FileSaveName(slot) xalign 0.5 size 19 bold True color "#f0c75e"
                                text FileTime(slot, format="%b %d, %Y - %I:%M %p", empty="Click to Save") xalign 0.5 size 16 color "#cccccc"

                        # Delete Slot Button (Top-right of occupied slots)
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
# 4. FUNCTIONAL LOAD SCREEN
# ==============================================================================
screen scoop_load_screen():
    tag menu
    modal True
    zorder 250

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

            text "LOAD INVESTIGATION" xalign 0.5 size 36 bold True color "#f0c75e" outlines [(2, "#000000", 0, 0)]

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
                            hover_background Solid("#ffffff12")
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

                                text FileSaveName(slot) xalign 0.5 size 19 bold True color "#f0c75e"
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
# 5. CREDITS SCREEN (Sample Text Ready to Edit)
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

            # Scrollable Credits Body — Replace sample names below with your team!
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

            # Back Button
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