# OMEGA FEDERATION: MIKROTIK STATION SETUP
# Target: RB951Ui-2HnD
# SSID: Derick_Wifi

/interface wireless security-profiles
add name=Derick_Profile mode=dynamic-keys authentication-types=wpa2-psk unicast-ciphers=aes-ccm group-ciphers=aes-ccm wpa2-pre-shared-key="D86S80@MAQ"

/interface wireless
set [ find default-name=wlan1 ] mode=station ssid="Derick_Wifi" security-profile=Derick_Profile disabled=no

/ip dhcp-client
add interface=wlan1 disabled=no

/ip dns
set allow-remote-requests=yes servers=8.8.8.8,8.8.4.4

/ip firewall nat
add chain=srcnat out-interface=wlan1 action=masquerade comment="Masquerade for Derick_Wifi"
