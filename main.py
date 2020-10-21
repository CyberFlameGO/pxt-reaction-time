playerA = 0
playerB = 0

def on_forever():
    global playerA, playerB
    basic.pause(1000)
    basic.pause(randint(0, 4000))
    basic.show_leds("""
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        """)
    while not (input.button_is_pressed(Button.A)) and not (input.button_is_pressed(Button.B)):
        basic.pause(20)
    if input.button_is_pressed(Button.A):
        basic.show_leds("""
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            """)
        playerA += 1
    if input.button_is_pressed(Button.B):
        basic.show_leds("""
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            """)
        playerB += 1
    basic.pause(1000)
    basic.clear_screen()
    basic.pause(1000)
    basic.show_leds("""
        . . # . .
        . # . . .
        # # # # #
        . # . . .
        . . # . .
        """)
    basic.pause(1000)
    basic.show_number(playerA)
    basic.pause(1000)
    basic.show_leds("""
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        """)
    basic.pause(1000)
    basic.show_number(playerB)
    basic.pause(1000)
    basic.clear_screen()
basic.forever(on_forever)
