import socket

def is_ip_valid(ip, ports=[80, 443], timeout=5):
    for port in ports:
        try:
            with socket.create_connection((ip, port), timeout=timeout):
                return True
        except:
            continue
    return False

def remove_invalid_ips(filename="usable_ips.txt"):
    try:
        with open(filename, "r") as f:
            ips = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("文件未找到")
        return

    print(f"原始 IP 数量: {len(ips)}")

    valid_ips = []
    for ip in ips:
        print(f"测试 IP: {ip}")
        if is_ip_valid(ip):
            valid_ips.append(ip)

    print(f"有效 IP 数量: {len(valid_ips)}")

    with open(filename, "w") as f:
        f.write("\n".join(valid_ips))

if __name__ == "__main__":
    remove_invalid_ips()
