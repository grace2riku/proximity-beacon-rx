def on_received_string(receivedString):
    global signal, signal_step, volume
    signal = radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH)
    signal_step = Math.map(signal, -95, -42, 0, 9)
    led.plot_bar_graph(signal_step, 9)
    volume = Math.map(signal_step, 0, 9, 128, 255)
    music.play(music.create_sound_expression(WaveShape.SQUARE,
            500,
            500,
            volume,
            volume,
            100,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.IN_BACKGROUND)
radio.on_received_string(on_received_string)

volume = 0
signal_step = 0
signal = 0
radio.set_group(1)
basic.show_string("R")