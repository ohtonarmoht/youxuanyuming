import socket

# 读取当前的 IP 列表
with open('ip.txt', 'r') as file:
    ip_list = file.read().splitlines()

# 去重 IP 地址
ip_list = list(set(ip_list))

valid_ips = []

# 检查每个 IP 是否可用
for ip in ip_list:
    try:
        # 尝试连接 443 端口
        socket.create_connection((ip, 443), timeout=5)
        valid_ips.append(ip)
        print(f"{ip} is valid.")
    except Exception as e:
        print(f"Error for IP {ip}: {e}")

# 将有效的 IP 写回文件
with open('ip.txt', 'w') as file:
    file.write("\n".join(valid_ips))

print("Invalid IPs have been removed.")
