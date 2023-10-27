radio.onReceivedString(function (receivedString) {
    signal = radio.receivedPacket(RadioPacketProperty.SignalStrength)
    signal_step = Math.map(signal, -95, -42, 0, 9)
    led.plotBarGraph(
    signal_step,
    9
    )
    volume = Math.map(signal_step, 0, 9, 128, 255)
    music.play(music.createSoundExpression(
    WaveShape.Square,
    500,
    500,
    volume,
    volume,
    500,
    SoundExpressionEffect.None,
    InterpolationCurve.Linear
    ), music.PlaybackMode.InBackground)
})
let volume = 0
let signal_step = 0
let signal = 0
radio.setGroup(1)
basic.showString("R")
