gpio -g mode 6 out
sleep 0.5
gpio -g write 6 1
sleep 0.5
gpio -g mode 21 out
sleep 0.5
gpio -g write 21 1
sleep 0.5
gpio -g write 21 0
