#pip install py-notifier

from pynotifier import Notification

#pip install psutil

import psutil

battery = psutil.sensors_battery()

percent = battery.percent

Notification("Battery Percentage ", str(percent) + " %Percent Remaining",duration=10).send()