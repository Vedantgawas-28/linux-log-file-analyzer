error_count = 0
warning_count = 0
ip_count = {}

with open("logs/server.log") as f:
    for line in f:
        if "ERROR" in line:
            error_count += 1
        if "WARNING" in line:
            warning_count += 1

        ip = line.split()[0]
        ip_count[ip] = ip_count.get(ip, 0) + 1

print("ERROR logs:", error_count)
print("WARNING logs:", warning_count)
print("Requests per IP:", ip_count)
