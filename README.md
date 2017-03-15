# ophanim

![](https://raw.githubusercontent.com/wdbm/ophanim/master/media/ophanim.png)

monitoring and notifications for measurements such as Bitcoin value and internet connection security

# introduction

Ophanim is a monitoring program that is designed to be run in the background. It monitors measurements like Bitcoin price fluctuations and internet connection security and sends alerts and messages about these things in the form of desktop notifications and Telegram messages.

![](https://raw.githubusercontent.com/wdbm/ophanim/master/media/notifications.gif) ![](https://raw.githubusercontent.com/wdbm/ophanim/master/media/messages.gif)

# setup

```Bash
sudo pip install ophanim
wget https://raw.githubusercontent.com/wdbm/denarius/master/database_LocalBitcoins.db
```

# usage

```Bash
ophanim.py --help
```

```Bash
ophanim.py --recipientstelegram="@username"
```

# links

- <https://github.com/wdbm/ucomsys>
