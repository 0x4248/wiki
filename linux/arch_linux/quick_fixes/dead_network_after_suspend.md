# Dead network after suspend quick fix

If you are experiencing a dead network after suspending your laptop, you can try the following:

reloading the kernel module:

```bash
WIRELESS_CARD=$(ip link | grep wlp | cut -d: -f2 | tr -d ' ')
SSID=$(iwctl station $WIRELESS_CARD show | grep SSID | cut -d: -f2 | tr -d ' ')
sudo modprobe -r iwlmvm iwlwifi 
sudo modprobe iwlmvm iwlwifi
sudo systemctl restart NetworkManager
iwctl station $WIRELESS_CARD connect $SSID
```

This will reload the kernel modules for the Intel wireless card.

If this does not work, you can try disabling and re-enabling the wireless card:

```bash
sudo ip link set wlp61s0 down
sudo ip link set wlp61s0 up
```

Often the DNS resolver is not working after a suspend