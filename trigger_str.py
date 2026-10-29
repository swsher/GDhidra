import inspect
# handles strings for all triggers
# this module should never be exposed directly
# instead access it through trigger.py

def strUnfinished(verbose):
    funcName = inspect.currentframe().f_back.f_code.co_name
    return f"Unfinished Trigger String: {funcName}, Verbose: {verbose}\n"

# id 34
def strLevelEndTrigger1_0(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 899
def strColorTrigger(trigger, verbose=False):
    if verbose:
        return f"color() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"color() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 901
def strMoveTrigger(trigger, verbose=False):
    duration = trigger.get("10")
    x = trigger.get("28")
    y = trigger.get("29")
    targetGroup = trigger.get("51")
    
    if verbose:
        return strUnfinished(verbose)
    else:
        return f"move(group={targetGroup}, x={x}, y={y}, duration={duration})\n"

# id 1006
def strPulseTrigger(trigger, verbose=False):
    targetID = trigger.get("51")
    targetType = trigger.get("52")
    fadeIn = float(trigger.get("45")) if trigger.get("45") else 0.0
    hold = float(trigger.get("46")) if trigger.get("46") else 0.0
    fadeOut = float(trigger.get("47")) if trigger.get("47") else 0.0
    red = int(trigger.get("7")) if trigger.get("7") else 0
    blue = int(trigger.get("8")) if trigger.get("8") else 0
    green = int(trigger.get("9")) if trigger.get("9") else 0
    if verbose:
        return strUnfinished(verbose)
    else:
        duration = fadeIn + hold + fadeOut
        if targetType:
            return f"pulse(group={targetID}, rgb=({red}, {green}, {blue}), duration={duration})\n"
        else:
            return f"pulse(channel={targetID}, rgb=({red}, {green}, {blue}), duration={duration})\n"

# id 1007
# verbose and non verbose are the same
def strAlphaTrigger(trigger, verbose=False):
    duration = trigger.get("10")
    opacity = trigger.get("35")
    targetGroup = trigger.get("51")
    return f"set_opacity(group={targetGroup}, opacity={opacity}, duration={duration})\n"
    
# id 1049
# verbose and non verbose are the same
def strToggleTrigger(trigger, verbose=False):
    targetGroup = trigger.get("51")
    activate = trigger.get("56")
    if activate:
        return f"toggle_on(group={targetGroup})\n"
    else:
        return f"toggle_off(group={targetGroup})\n"

# id 1268
def strSpawnTrigger(trigger, verbose=False):
    raise Exception("Spawn Trigger is callable-like and cannot be returned as a string")

# id 1346
def strRotateTrigger(trigger, verbose=False):
    duration = trigger.get("10")
    targetGroup = trigger.get("51")
    degrees = float(trigger.get("68")) if trigger.get("68") else 0.0
    num360 = int(trigger.get("69")) if trigger.get("69") else 0
    if verbose:
        return strUnfinished(verbose)
    else:
        actualDegrees = degrees + num360*360
        return f"rotate(group={targetGroup}, degrees={actualDegrees}, duration={duration})\n"

# id 1347
# verbose and non-verbose are the same
def strFollowTrigger(trigger, verbose=False):
    duration = trigger.get("10")
    targetGroup = trigger.get("51")
    followGroup = trigger.get("71")
    xMod = trigger.get("72")
    yMod = trigger.get("73")
    return f"follow(group={targetGroup}, follow_group={followGroup}, duration={duration}, x_mod={xMod}, y_mod={yMod}))\n"

# id 1520
def strShakeTrigger(trigger, verbose=False):
    if verbose:
        return f"shake() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"shake() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 1585
# verbose and non-verbose are the same
def strAnimateTrigger(trigger, verbose=False):
    targetGroup = trigger.get("51")
    animID = trigger.get("76")
    return f"animate(group={targetGroup}, animation={animID})\n"

# id 1595
def strTouchTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 1611
def strCountTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 1612
def strHidePlayerTrigger(trigger, verbose=False):
    if verbose:
        return f"hide_player() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"hide_player() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 1613
def strShowPlayerTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 1616
# this is in an extremely weird place
# semi callable-like trigger, im just treat as function like for now
def strStopTrigger(trigger, verbose=False):
    raise Exception("Stop Trigger is callable-like and cannot be returned as a string")

# id 1811
def strInstantCountTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 1812
def strOnDeathTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 1814
def strFollowPlayerYTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 1815
def strCollisionTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 1817
def strPickupTrigger(trigger, verbose=False):
    if verbose:
        return f"pickup() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"pickup() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 1818
def strBackgroundEffectOnTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 1819
def strBackgroundEffectOffTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 1912
def strRandomTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 1913
# verbose and non verbose are the same
def strZoomCameraTrigger(trigger, verbose=False):
    duration = trigger.get("10")
    zoom = trigger.get("371")
    return f"set_camera_zoom(zoom={zoom}, duration={duration})\n"

# id 1914
def strStaticCameraTrigger(trigger, verbose=False):
    duration = trigger.get("10")
    targetGroup = trigger.get("51")
    exitStatic = trigger.get("110")
    exitInstant = trigger.get("465")
    if verbose:
        return strUnfinished(verbose)
    else:
        if exitStatic or exitInstant:
            return f"exit_static_camera(duration={duration})\n"
        else:
            return f"set_static_camera(group={targetGroup}, duration={duration})\n"

# id 1915
# verbose and non verbose are the same
def strEnterEffectTrigger(trigger, verbose=False):
    modes = ["unset", "enter", "exit"]
    mode = modes[int(trigger.get("217") if trigger.get("217") else 0)]
    targetChannel = trigger.get("344")
    return f"{mode}_effect(channel={targetChannel}) # unsure of what this trigger does\n"

# id 1916
def strOffsetCameraTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 1917
def strReverseTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 1931
def strOldEndTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 1932
def strPlayerControlTrigger(trigger, verbose=False):
    if verbose:
        return f"player_control() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"player_control() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 1934
def strSongTrigger(trigger, verbose=False):
    if verbose:
        return f"song() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"song() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 1935
def strTimeWarpTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2015
def strRotateCameraTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2062
# verbose and non verbose are the same
def strEdgeCameraTrigger(trigger, verbose=False):
    targetGroup = trigger.get("51")
    cameraEdges = ["unset", "left", "right", "top", "bottom"]
    edge = cameraEdges[int(trigger.get("164") if trigger.get("164") else 0)]

    if targetGroup is not None:
        return f"set_camera_{edge}_edge(group={targetGroup})\n"
    else:
        return f"unset_camera_{edge}_edge()\n"

# id 2066
def strGravityTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2067
def strScaleTrigger(trigger, verbose=False):
    duration = trigger.get("10")
    targetGroup = trigger.get("51")
    scaleX = trigger.get("150")
    scaleY = trigger.get("151")
    if verbose:
        return strUnfinished(verbose)
    else:
        return f"scale(target_group={targetGroup}, scale_x={scaleX}, scale_y={scaleY}, duration={duration})\n"

# id 2068
def strAdvancedRandomTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2899
# non verbose and verbose are the same
# it looks like a lot but I am breaking up into smaller functions
def strOptionsTrigger(trigger, verbose=False):
    streakAdditive = trigger.get("159")
    hideGround = trigger.get("161")
    hideMg = trigger.get("195")
    hideP1 = trigger.get("162")
    hideP2 = trigger.get("163")
    disableP1Controls = trigger.get("165")
    disableP2Controls = trigger.get("199")
    unlinkDualGravity = trigger.get("160")
    hideAttempts = trigger.get("532")
    deathAudio = trigger.get("575")
    noDeathSFX = trigger.get("576")
    editRespawnTime = trigger.get("573")
    boostSlide = trigger.get("593")
    respawnTime = trigger.get("574")

    string = ""
    if streakAdditive:
        string += f"enable_streak_additive()\n" if streakAdditive == "1" else f"disable_streak_additive()\n"
    if hideGround:
        string += f"hide_ground()\n" if hideGround == "1" else f"show_ground()\n"
    if hideMg:
        string += f"hide_middleground()\n" if hideMg == "1" else f"show_middleground()\n"        
    if hideP1:
        string += f"hide_player_1()\n" if hideP1 == "1" else f"show_player_1()\n"
    if hideP2:
        string += f"hide_player_2()\n" if hideP2 == "1" else f"show_player_2()\n"
    if disableP1Controls:
        string += f"disable_player_1_controls()\n" if disableP1Controls == "1" else f"enable_player_1_controls()\n"
    if disableP2Controls:
        string += f"disable_player_2_controls()\n" if disableP2Controls == "1" else f"enable_player_2_controls()\n"
    if unlinkDualGravity:
        string += f"unlink_dual_gravity()\n" if unlinkDualGravity == "1" else f"link_dual_gravity()\n"
    if hideAttempts:
        string += f"hide_attempt_counter()\n" if hideAttempts == "1" else f"show_attempt_counter()\n"
    if deathAudio:
        string += f"disable_audio_on_death()\n" if deathAudio == "1" else f"enable_audio_on_death()\n"
    if noDeathSFX:
        string += f"disable_death_sfx()\n" if noDeathSFX == "1" else f"enable_death_sfx()\n"
    if boostSlide:
        string += f"enable_boost_slide()\n" if boostSlide == "1" else f"disable_boost_slide()\n"
    if editRespawnTime:
        string += f"set_respawn_duration(duration={respawnTime})\n"

    return string


# id 2900
def strGameplayRotationTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2901
def strGameplayOffsetCameraTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2903
def strGradientTrigger(trigger, verbose=False):
    if verbose:
        return f"gradient() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"gradient() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 2904
def strShaderTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2905
def strShockWaveShaderTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2907
def strShockLineShaderTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2909
def strGlitchShaderTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2910
def strChromaticAberrationShaderTrigger(trigger, verbose=False):
    if verbose:
        return f"chromatic_aberration_shader() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"chromatic_aberration_shader() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 2911
def strChromaticGlitchShaderTrigger(trigger, verbose=False):
    if verbose:
        return f"chromatic_glitch_shader() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"chromatic_glitch_shader() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 2912
def strPixelateShaderTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2913
def strLensCircleShaderTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2914
def strRadialBlurShaderTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2915
def strMotionBlurShaderTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2916
def strBulgeShaderTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2917
def strPinchShaderTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2919
def strGrayscaleShaderTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2920
def strSepiaShaderTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2921
def strInvertColorTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2922
def strHueShaderTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2923
def strEditColorShaderTrigger(trigger, verbose=False):
    if verbose:
        return f"edit_color_shader() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"edit_color_shader() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 2924
def strSplitScreenShaderTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2925
def strModeCameraTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 2999
# verbose and non verbose are the same
def strEditMiddlegroundTrigger(trigger, verbose=False):
    duration = trigger.get("10")
    offset = trigger.get("29")
    return f"shift_middleground(offset={offset}, duration={duration})\n"

# id 3006
def strAreaMoveTrigger(trigger, verbose=False):
    if verbose:
        return f"area_move() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"area_move() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 3007
def strAreaRotateTrigger(trigger, verbose=False):
    if verbose:
        return f"area_rotate() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"area_rotate() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 3008
def strAreaScaleTrigger(trigger, verbose=False):
    if verbose:
        return f"area_scale() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"area_scale() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 3009
def strAreaFadeTrigger(trigger, verbose=False):
    if verbose:
        return f"area_fade() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"area_fade() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 3010
def strAreaTintTrigger(trigger, verbose=False):
    if verbose:
        return f"area_tint() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"area_tint() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 3011
def strEditAreaMoveTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3012
def strEditAreaRotateTrigger(trigger, verbose=False):
    if verbose:
        return f"edit_area_rotate() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"edit_area_rotate() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 3013
def strEditAreaScaleTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3014
def strEditAreaFadeTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3015
def strEditAreaTintTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3016
def strAdvancedFollowTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3017
def strEnterMoveTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3018
def strEnterRotateTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3019
def strEnterScaleTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3020
def strEnterFadeTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3021
def strEnterTintTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3022
def strTeleportTrigger(trigger, verbose=False):
    targetGroup = trigger.get("51")
    if verbose:
        return strUnfinished(verbose)
    else:
        return f"teleport(group={targetGroup})\n"

# id 3023
def strEnterStopTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3024
def strAreaStopTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3029
def strChangeBackgroundTrigger(trigger, verbose=False):
    if verbose:
        return f"change_background() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"change_background() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 3030
def strChangeGroundTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3031
def strChangeMiddlegroundTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3033
def strKeyframeAnimationTrigger(trigger, verbose=False):
    if verbose:
        return f"keyframe_animation() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"keyframe_animation() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 3600
def strEndTrigger(trigger, verbose=False):
    raise Exception("End Trigger is callable-like and cannot be returned as a string")

# id 3602
# extremely complicated trigger
def strSFXTrigger(trigger, verbose=False):
    sfxId = trigger.get("392")
    duration = trigger.get("490")
    if verbose:
        return strUnfinished(verbose)
    else:
        return f"play_sfx(id={sfxId}, duration={duration})\n"

# id 3603
def strEditSFXTrigger(trigger, verbose=False):
    if verbose:
        return f"edit_sfx() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"edit_sfx() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 3604
# verbose and non verbose are the same (this might be changed)
def strEventTrigger(trigger, verbose=False):
    raise Exception("Event Trigger is callable-like and cannot be returned as a string")

# id 3605
def strEditSongTrigger(trigger, verbose=False):
    if verbose:
        return f"edit_song() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"edit_song() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 3606
# verbose and non verbose are the same
def strBackgroundSpeedTrigger(trigger, verbose=False):
    modX = trigger.get("143")
    modY = trigger.get("144")
    return f"set_background_speed(x={modX}, y={modY})\n"

# id 3607
def strSequenceTrigger(trigger, verbose=False):
    raise Exception("Sequence Trigger is callable-like and cannot be returned as a string")

# id 3608
def strSpawnParticleTrigger(trigger, verbose=False):
    if verbose:
        f"spawn_particle() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        f"spawn_particle() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 3609
def strInstantCollisionTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3612
def strMiddlegroundSpeedTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3613
def strUITrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3614
# note if you are changing this avoid using the name time() to avoid namespace ambiguity
# thank you
def strTimeTrigger(trigger, verbose=False):
    if verbose:
        return f"time_trigger() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"time_trigger() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 3615
def strTimeEventTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3617
def strTimeControlTrigger(trigger, verbose=False):
    if verbose:
        return f"time_control() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"time_control() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 3618
def strResetTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3619
def strItemEditTrigger(trigger, verbose=False):
    if verbose:
        return f"item_edit() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"item_edit() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 3620
def strItemCompareTrigger(trigger, verbose=False):
    if verbose:
        return f"item_compare() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"
    else:
        return f"item_compare() # this function is unformatted, do it yourself with a pr to GDhidra on GitHub\n"

# id 3641
def strPersistentItemSetupTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3642
def strBPMTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3655
def strObjectControlTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3660
def strEditAdvancedFollowTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3661
def strRetargetAdvancedFollowTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

# id 3662
def strLinkVisibleTrigger(trigger, verbose=False):
    if verbose:
        return strUnfinished(verbose)
    else:
        return strUnfinished(verbose)

FUNC_TRIGGER_BY_ID = {
    1268: strSpawnTrigger,
    1616: strStopTrigger,
    3600: strEndTrigger,
    3604: strEventTrigger,
    3607: strSequenceTrigger
}

STR_TRIGGER_BY_ID = {
    34: strLevelEndTrigger1_0,
    899: strColorTrigger,
    901: strMoveTrigger,
    1006: strPulseTrigger,
    1007: strAlphaTrigger,
    1049: strToggleTrigger,
    1346: strRotateTrigger,
    1347: strFollowTrigger,
    1520: strShakeTrigger,
    1585: strAnimateTrigger,
    1595: strTouchTrigger,
    1611: strCountTrigger,
    1612: strHidePlayerTrigger,
    1613: strShowPlayerTrigger,
    1811: strInstantCountTrigger,
    1812: strOnDeathTrigger,
    1814: strFollowPlayerYTrigger,
    1815: strCollisionTrigger,
    1817: strPickupTrigger,
    1818: strBackgroundEffectOnTrigger,
    1819: strBackgroundEffectOffTrigger,
    1912: strRandomTrigger,
    1913: strZoomCameraTrigger,
    1914: strStaticCameraTrigger,
    1915: strEnterEffectTrigger,
    1916: strOffsetCameraTrigger,
    1917: strReverseTrigger,
    1931: strOldEndTrigger,
    1932: strPlayerControlTrigger,
    1934: strSongTrigger,
    1935: strTimeWarpTrigger,
    2015: strRotateCameraTrigger,
    2062: strEdgeCameraTrigger,
    2066: strGravityTrigger,
    2067: strScaleTrigger,
    2068: strAdvancedRandomTrigger,
    2899: strOptionsTrigger,
    2900: strGameplayRotationTrigger,
    2901: strGameplayOffsetCameraTrigger,
    2903: strGradientTrigger,
    2904: strShaderTrigger,
    2905: strShockWaveShaderTrigger,
    2907: strShockLineShaderTrigger,
    2909: strGlitchShaderTrigger,
    2910: strChromaticAberrationShaderTrigger,
    2911: strChromaticGlitchShaderTrigger,
    2912: strPixelateShaderTrigger,
    2913: strLensCircleShaderTrigger,
    2914: strRadialBlurShaderTrigger,
    2915: strMotionBlurShaderTrigger,
    2916: strBulgeShaderTrigger,
    2917: strPinchShaderTrigger,
    2919: strGrayscaleShaderTrigger,
    2920: strSepiaShaderTrigger,
    2921: strInvertColorTrigger,
    2922: strHueShaderTrigger,
    2923: strEditColorShaderTrigger,
    2924: strSplitScreenShaderTrigger,
    2925: strModeCameraTrigger,
    2999: strEditMiddlegroundTrigger,
    3006: strAreaMoveTrigger,
    3007: strAreaRotateTrigger,
    3008: strAreaScaleTrigger,
    3009: strAreaFadeTrigger,
    3010: strAreaTintTrigger,
    3011: strEditAreaMoveTrigger,
    3012: strEditAreaRotateTrigger,
    3013: strEditAreaScaleTrigger,
    3014: strEditAreaFadeTrigger,
    3015: strEditAreaTintTrigger,
    3016: strAdvancedFollowTrigger,
    3017: strEnterMoveTrigger,
    3018: strEnterRotateTrigger,
    3019: strEnterScaleTrigger,
    3020: strEnterFadeTrigger,
    3021: strEnterTintTrigger,
    3022: strTeleportTrigger,
    3023: strEnterStopTrigger,
    3024: strAreaStopTrigger,
    3029: strChangeBackgroundTrigger,
    3030: strChangeGroundTrigger,
    3031: strChangeMiddlegroundTrigger,
    3033: strKeyframeAnimationTrigger,
    3602: strSFXTrigger,
    3603: strEditSFXTrigger,
    3605: strEditSongTrigger,
    3606: strBackgroundSpeedTrigger,
    3608: strSpawnParticleTrigger,
    3609: strInstantCollisionTrigger,
    3612: strMiddlegroundSpeedTrigger,
    3613: strUITrigger,
    3614: strTimeTrigger,
    3615: strTimeEventTrigger,
    3617: strTimeControlTrigger,
    3618: strResetTrigger,
    3619: strItemEditTrigger,
    3620: strItemCompareTrigger,
    3641: strPersistentItemSetupTrigger,
    3642: strBPMTrigger,
    3655: strObjectControlTrigger,
    3660: strEditAdvancedFollowTrigger,
    3661: strRetargetAdvancedFollowTrigger,
    3662: strLinkVisibleTrigger
}