# Global keybind so players can press 'V' anytime (even during Day 4) to adjust volume
init python:
    config.underlay.append(
        renpy.Keymap(v= renpy.curry(renpy.run)(ToggleScreen("audio_settings_modal")))
    )

# Styles for the custom Noir Volume Sliders (no external PNGs required)
style scoop_volume_slider is bar:
    xsize 460
    ysize 22
    left_bar Frame(Solid("#c99838"), 0, 0)   # Warm amber/gold filled bar
    right_bar Frame(Solid("#2b2b2b"), 0, 0)  # Dark unfilled track
    thumb Solid("#ffffff", xsize=14, ysize=30)
    thumb_offset 7
    hover_sound "audio/ui_hover.ogg"

screen audio_settings_modal():
    modal True
    zorder 250

    # Dimmed backdrop
    add Solid("#000000AA")

    # Main Settings Box
    frame:
        align (0.5, 0.5)
        xsize 680
        ysize 430
        background Solid("#161616F2")
        padding (45, 35)

        vbox:
            spacing 26
            xfill True

            # Header
            text "AUDIO SETTINGS" xalign 0.5 size 34 bold True color "#f0c75e" outlines [(2, "#000000", 0, 0)]

            null height 4

            # 1. Background Music Slider
            vbox:
                spacing 10
                hbox:
                    xfill True
                    text "Background Music (BGM)" size 24 color "#ffffff"
                    $ bgm_pct = int(preferences.get_volume("music") * 100)
                    text "[bgm_pct]%" xalign 1.0 size 24 bold True color "#f0c75e"

                bar:
                    value Preference("music volume")
                    style "scoop_volume_slider"
                    xalign 0.5

            # 2. Sound Effects & Ambience Slider
            vbox:
                spacing 10
                hbox:
                    xfill True
                    text "Sound Effects & Ambience (SFX)" size 24 color "#ffffff"
                    $ sfx_pct = int(preferences.get_volume("sfx") * 100)
                    text "[sfx_pct]%" xalign 1.0 size 24 bold True color "#f0c75e"

                bar:
                    value Preference("sound volume")
                    style "scoop_volume_slider"
                    released Play("sound", "audio/ui_notify.ogg") # Plays a sample sound when you release the slider!
                    xalign 0.5

            null height 10

            # Bottom Action Buttons (Test SFX, Mute All, Close)
            hbox:
                xalign 0.5
                spacing 40

                textbutton "Test SFX":
                    hover_sound "audio/ui_hover.ogg"
                    action Play("sound", "audio/sfx_camera_shutter.ogg")
                    background Solid("#2c2c2c")
                    hover_background Solid("#444444")
                    padding (20, 10)
                    text_size 22
                    text_color "#ffffff"
                    text_hover_color "#f0c75e"

                textbutton "Mute All":
                    hover_sound "audio/ui_hover.ogg"
                    activate_sound "audio/ui_click.ogg"
                    action Preference("all mute", "toggle")
                    background Solid("#2c2c2c")
                    hover_background Solid("#591c1c")
                    selected_background Solid("#8a1c1c")
                    padding (20, 10)
                    text_size 22
                    text_color "#ffffff"
                    text_selected_color "#ffaaaa"

                textbutton "Done":
                    hover_sound "audio/ui_hover.ogg"
                    activate_sound "audio/ui_cancel.ogg"
                    action Hide("audio_settings_modal")
                    background Solid("#c99838")
                    hover_background Solid("#e3b34c")
                    padding (26, 10)
                    text_size 22
                    text_bold True
                    text_color "#111111"

    key "K_ESCAPE" action [Play("sound", "audio/ui_cancel.ogg"), Hide("audio_settings_modal")]