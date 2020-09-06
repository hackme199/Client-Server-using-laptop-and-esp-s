#! /usr/bin/python3
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('If you can so please', 'tutuniam')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def ap():
    import network
    ssid = 'Micropython-Server'
    password = 'MicropythoN'
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid = ssid, password = password)
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(False)

    while ap.active() == False:
        pass
    print('####################Configured as AP successfully####################')
    print('credentials : ',ap.ifconfig())

import esp
esp.osdebug(None)

import gc
gc.collect()

do_connect()
